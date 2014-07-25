#! /usr/bin/env python
import sys, string, datetime, time, socket, struct, re, os
from pysqlite2 import dbapi2 as sqlite
import pcapy as pcap
import curses
import MySQLdb
from curses import panel
from optparse import OptionParser
#import sqlite3 as sqlite #the module is called sqlite3 on the python doc site, might be for python2.5


class Sniffer:
   
    def __init__(self, check_seconds=10, pcap_filter='tcp and port 80 and not (dst port 80 and dst net 128.193)', sqlitedbname='test.db'):
        self.start_time = self.last_checked = datetime.datetime.now()
        self.check_seconds = check_seconds #how frequently to check for outdated requests, as well as how old a request has to be in order to be considered outdated (in seconds)
        self.pcap_filter = pcap_filter
        self.request_dict = {}
        self.domain_re = re.compile('.*domain=(?P<domain>.*?)((;.*$)|$)', re.IGNORECASE)
        self.expiry_re = re.compile('.*expires=(?P<expiry>.*?)((;.*$)|$)', re.IGNORECASE)
        self.get_re = re.compile('GET (?P<get>.*?) HTTP')
        self.status_re = re.compile('HTTP/[0-9]\.[0-9] (?P<status>[0-9]{3})')
        self.protocols = {socket.IPPROTO_TCP:'tcp', socket.IPPROTO_UDP:'udp', socket.IPPROTO_ICMP:'icmp'}
        self.sqlitedbname = sqlitedbname
        self.connections = {}
        self.con_size = 0
        self.time_update = time.time()
        #Determine the correct interface; the first two should be mututally exclusive, an k9 can be considered a special case that overrides 'linux2'
        if(sys.platform == "linux2"):#linux2?  well, that's what skoll says and its why i'm adding this part
            self.dev = 'eth0'#should be eth0 but this lets wifi work
        if(sys.platform == "darwin"):
            self.dev = 'en1'
        if(socket.gethostname() == "k9"):
            self.dev = 'eth3'

        self.db_setup()
   
    def start(self):
        
        # note:    to_ms does nothing on linux
        self.p = pcap.open_live(self.dev, 1600, 1, 100)#opens a connection descriptor
       
        self.p.setfilter(self.pcap_filter)#sets our packet filter we set in init
        print "Listening on %s: net=%s, mask=%s\n" % (self.dev, self.p.getnet(), self.p.getmask())
        # try-except block to catch keyboard interrupt.    Failure to shut
        # down cleanly can result in the interface not being taken out of promisc.
        # mode
        self.p.setnonblock(1)#goes into nonblcoking mode so we dont wait for packets that have timed out
        
        try:
            while 1:#can't use self.p.loop in nonblock
                self.p.dispatch(1, self.print_packet)#read 1 packet and parse it, then repeat ad nauseam
       
        except KeyboardInterrupt:#if we get a ctrl-c abort
            print '%s' % sys.exc_type
            print 'shutting down'
            self.cursor.close()
            self.connection.close()#notice we dont close down the descriptor, only the database, dont know why that is
   

    #mysql db
    def db_setup(self):
        #if(options.debug == True):
            self.connection =  MySQLdb.connect(host="mysql.cs.orst.edu", user="team33", passwd="team33", db="team33")#connect to our mysql database
            self.cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)#create a cursor to interact with it, throw the dictionary flag so we can mess with the output
#        else:
#            if(os.path.exists(self.sqlitedbname)):
#                os.remove(self.sqlitedbname)
#            self.connection = sqlite.connect(self.sqlitedbname)
#            self.connection.row_factory = sqlite.Row
#            self.cursor = self.connection.cursor()
#       
#            ##To create the DB
#            self.cursor.execute("""
#            CREATE TABLE rawpkt (
#            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#            host VARCHAR(128),
#            get VARCHAR(1024),
#            referer VARCHAR(1024),
#            contenttype VARCHAR(32),
#            pkt_date DATE,
#            insert_date DATE,
#            status INTEGER,
#            server VARCHAR(50),
#            useragent VARCHAR(50),
#            p3p VARCHAR(256),
#            etag VARCHAR(32),
#            contentlength INTEGER,
#            seq INTEGER,
#            ack INTEGER,
#            residential BOOLEAN NOT NULL DEFAULT 0
#            )
#            """)
#           
#            self.cursor.execute("""
#            CREATE TABLE cookie_has (
#            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#            domain_id INTEGER NOT NULL,
#            pkt_id INTEGER NOT NULL,
#            set_by VARCHAT(24),
#            expiry DATE,
#            session BOOLEAN
#            )
#           
#            """)
#           
#            self.cursor.execute("""
#            CREATE TABLE domains (
#            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#            domain VARCHAR(128) NOT NULL)
#            """)
#            self.connection.commit()
            #cursor.close()
            #connection.close()
   
    def decode_ip_packet(self,s):#takes in the packet info after the ethertype from spot 14 on
        d={}
        d['version']=(ord(s[0]) & 0xf0) >> 4#gets the first byte, takes the first half of it then shifts it??? anyways its the version number   Maybe it shifts it right because it was the left half of the number
        d['header_len']=ord(s[0]) & 0x0f#second half of the first byte, header length, straight from wireshark ip section
        d['tos']=ord(s[1])#the "Differentiated Services Field" still no clue as to what this does
        d['total_len']=socket.ntohs(struct.unpack('H',s[2:4])[0])#gets the struct that is at 2 and 3, unpacks it to an int ('H' means unsingned short in c, converts it to an int, then converts network byte order to host byte order
        d['id']=socket.ntohs(struct.unpack('H',s[4:6])[0])#and get the first part of the tuple that it returns, this line does the same for next 2 spots
        d['flags']=(ord(s[6]) & 0xe0) >> 5#gets flags shifting again
        d['fragment_offset']=socket.ntohs(struct.unpack('H',s[6:8])[0] & 0x1f)
        d['ttl']=ord(s[8])
        d['protocol']=ord(s[9])
        d['checksum']=socket.ntohs(struct.unpack('H',s[10:12])[0])
        d['source_address']=socket.inet_ntoa(s[12:16])#converts network address in a struct to a string
      
        d['destination_address']=socket.inet_ntoa(s[16:20])
      
        if d['header_len']>5:#think 5 is normal, so if its a bad packet?
            d['options']=s[20:4*(d['header_len']-5)]#?????
        else:
            d['options']=None
        d['data']=s[4*d['header_len']:]#shove from header length on (20 bytes in)
        return d#return our new dictonary with the ip stuff parsed out
        #it seems this entire function is pretty useless to us, all we need is headerlen to figure out where the datastarts
       
   
    def dumphex(self,s):
        bytes = map(lambda x: '%.2x' % x, map(ord, s))
        for i in xrange(0,len(bytes)/16):
            print '        %s' % string.join(bytes[i*16:(i+1)*16],' ')
        print '        %s' % string.join(bytes[(i+1)*16:],' ')

    def _connadd(self,data,dict_name):
        self.con_size = self.con_size + 1;
       # user_agent = #different timeouts for different browsers, will use a lookup table for the common ones, use some false one for the rest
       #14 + 4 * (ord(data[14]) & 0x0f) port ie tcp:0 
       #s[tcp['tcphdr_len']/4:]
       #  
        if re.search(('Firefox'),str(data)) != None:#doesnt work
            self.connections[dict_name] = 300 + time.time()
        elif re.search('Opera',str(data)) != None:
            self.connections[dict_name] = 300 + time.time()#bald faced lie, cant find the real number
        elif re.search('MSIE',str(data)) != None:
            self.connections[dict_name] = 60 + time.time()
        elif re.search('Chrome',str(data)) != None:
            self.connections[dict_name] = 300 + time.time()
        else:
            self.connections[dict_name] = 300 + time.time()
        print self.con_size
        print "\n\n"
    def _connupdate(self,data,dict_name):
       
       
        if re.search(('Firefox'),str(data)) != None:#search the entire packet for the string Firefox, so we know its timeout time
            self.connections[dict_name] = 300 + time.time()
        elif re.search('Opera',str(data)) != None:
            self.connections[dict_name] = 300 + time.time()#bald faced lie, cant find the real number
        elif re.search('MSIE',str(data)) != None:
            self.connections[dict_name] = 60 + time.time()
        elif re.search('Chrome',str(data)) != None:
            self.connections[dict_name] = 300 + time.time()#assuming since its from mozilla its the same
        else:
            self.connections[dict_name] = 300 + time.time()
    def _cleanconnections(self):
        for member in self.connections:
            if member > time.time():
                del member
                self.con_size = self.con_size - 1
            else:
                pass
    def print_packet(self, pkthdr, data):
        if not data:#if the packet is blank we look for a new one
            return
        if data[12:14]=='\x08\x00':#if spots 12 and 13 are 0800 then its ethertype is ipv4 and we are good
            
            src_addr = socket.inet_ntoa(data[26:30])
            dst_addr = socket.inet_ntoa(data[30:34])
            
            
            port = socket.ntohs(struct.unpack('H',data[14 + 4 * (ord(data[14]) & 0x0f):2 + 14 + 4 * (ord(data[14]) & 0x0f)])[0])  if  socket.ntohs(struct.unpack('H',data[14 + 4 * (ord(data[14]) & 0x0f):2 + 14 + 4 * (ord(data[14]) & 0x0f)])[0]) != 80 else socket.ntohs(struct.unpack('H',data[2 + 14 + 4 * (ord(data[14]) & 0x0f):4 + 14 + 4 * (ord(data[14]) & 0x0f)])[0])
            
            if str(src_addr) + str(port) in self.connections or str(dst_addr) + str(port) in self.connections:
                if str(src_addr) + str(port) in self.connections:#update the timeout value
                    self._connupdate(data,str(src_addr) + str(port))
                    grp_id = str(src_addr) + str(port)
                    self.tcp_decode(self.decode_ip_packet(data[14:]),grp_id)#send output from ip_decode to tcp_decode, only send from 14 on (so not the frame and ethernet stuff
                else:
                    self._connupdate(data,str(dst_addr) + str(port))
                    grp_id = str(dst_addr) + str(port)
                    self.tcp_decode(self.decode_ip_packet(data[14:]),grp_id)
            elif self.con_size < 500:#add to the connections if its small
                self._connadd(data,str(src_addr) + str(port))
                grp_id = str(src_addr) + str(port)
                self.tcp_decode(self.decode_ip_packet(data[14:]),grp_id)
            else:
                if (time.time() - self.time_update) > 60:#clean the connections table every minutes, could go longer or shorter if needed
                    self.time_update = time.time()
                    self._cleanconnections()
         
                
    def tcp_decode(self, d, grp_id):
        s = d['data']#s holds the tcp and beyond data
        tcp = {}
        tcp['ip_header'] = d#ip_header holds the header and the data
        tcp['bytes'] = map(lambda x: '%.2x' % x, map(ord, s))#for each number in the entire string of numbers, store the two bit hex of the unicode of the number into bytes 
        tcp['src_port'] = socket.ntohs(struct.unpack('H',s[0:2])[0])
       
        tcp['dst_port'] = socket.ntohs(struct.unpack('H',s[2:4])[0])
    
        tcp['seq'] = socket.ntohs(struct.unpack('HH',s[4:8])[0])
        tcp['ack'] = socket.ntohs(struct.unpack('HH',s[8:12])[0])
        tcp['tcphdr_len'] = int(str(tcp['bytes'][12:13][0]), 16)
        tcp['flags'] = ord(s[13:14])
        tcp['window_size'] = socket.ntohs(struct.unpack('H',s[14:16])[0])
        tcp['checksum'] = socket.ntohs(struct.unpack('H',s[16:18])[0])
        #options somewhere in here
        tcp['data'] = s[tcp['tcphdr_len']/4:]
        #if (flags == 16 or flags == 24): #10 and 18 in hex
        if(str(tcp['data']).lower().find('http') !=-1):
            #print "\n\nstarting tcp data\n\n\n"
            #print str(tcp['data']).lower()
           # print "\n\nending tcp data\n\n\n"
            self.http_decode(tcp, grp_id)
   
    def parse_setcookie(self, cookie_list):
        cookiejar = []
        for cookie in cookie_list:
            #take apart the cookie and make into a dictionary.  There is a cookie module for python, but i'm not sure if it would be easier
            cookie = str(cookie).lower()
            cookie_dict = {}
           
            domain_result = self.domain_re.match(str(cookie))
            if (domain_result):
                cookie_dict['domain'] = domain_result.group('domain')
                print "\t:-) Cookie domain: " + cookie_dict['domain']
            else:
                print "\t:-( Cookie: " + cookie
                continue # skip to next cookie

           
            query = "SELECT id, domain FROM domains WHERE domain ='" + cookie_dict['domain'] + "'"
            try:
                self.cursor.execute(query)
            except:
                continue #go to next cookie
            for row in self.cursor:
                if(row['domain']== cookie_dict['domain']):#if the domains in this cookie have already been seen
                    cookie_dict['id'] = row['id']
            if( not cookie_dict.has_key('id')): #this domain wasn't already in the db
                value = (cookie_dict['domain'],)
                host_list = str(cookie_dict['domain']).split('.')
                host_str = host_list[len(host_list)-2] + "." + host_list[len(host_list)-1]
                self.cursor.execute("SELECT id FROM domains WHERE domain = %s AND has_bug = 0",host_str)
                row = self.cursor.fetchone()
                if(row == None):
                    cookie_dict['id'] = self.cursor.execute("INSERT INTO domains(domain,has_bug) VALUES (%s,0)", host_str)#add it to the table
                else:
                    cookie_dict['id'] = row['id']
           
            expiry_result = self.expiry_re.match(str(cookie))
            if (expiry_result):
                cookie_dict['session'] = 0
                try:
                    cookie_dict['expiry'] = str(datetime.datetime(*time.strptime(expiry_result.group('expiry'), '%a, %d-%b-%Y %H:%M:%S %Z')[0:6]))
                    print "\t:-) Expires: " + cookie_dict['expiry']
                except ValueError:
                    break #ignore incorrectly formatted cookies
                    print ":-( Value Error: " + expiry_result.group('expiry')
            else:
                cookie_dict['session'] = 1
                cookie_dict['expiry'] = ""
                print "No Expires: " + cookie

           
            print "\tCookie from domain " + cookie_dict['domain']
            cookiejar.append(cookie_dict)
        return cookiejar
   
    def parse_cookie(self, raw_cookie, host):
        cookie = str(raw_cookie).lower()
        cookie_dict = {}
       
        if(raw_cookie.find('domain=') == -1):
            cookie_dict['domain'] = host
        else:
            print "##### Cookie to be parsed: " + raw_cookie
            return cookie_dict
       
        query = "SELECT id, domain FROM domains WHERE domain='" + cookie_dict['domain'] + "'"
        self.cursor.execute(query)
        for row in self.cursor:
            if(row['domain'] == cookie_dict['domain']):#if any of the domains in this cookie have already been seen, remove from the list and put their ID on the id_list
                cookie_dict['id'] = row['id']
       
        if( not cookie_dict.has_key('id')): #this domain wasn't already in the db
            value = (cookie_dict['domain'],)
            print "\n\n\n\n\n\n"
            print cookie_dict['domain']
            print "\n\n\n\n\n\n"
            host_list = str(cookie_dict['domain']).split('.')
            host_str = host_list[len(host_list)-2] + "." + host_list[len(host_list)-1]
            
            
            
            
            self.cursor.execute("SELECT id FROM domains WHERE domain = %s AND has_bug = 0",host_str)
            row = self.cursor.fetchone()
            if(row == None):
                cookie_dict['id'] = self.cursor.execute("INSERT INTO domains(domain,has_bug) VALUES (%s,0)", host_str)#add it to the table
            else:
                cookie_dict['id'] = row['id']
            
            
            
        cookie_dict['session'] = ""
        cookie_dict['expiry'] = ""
        print "\tCookie for domain " + cookie_dict['domain']
        return cookie_dict
   
    def is_resnet(self,ip):
        #resnet =  2160192768 - 2160197631 (128.193.237.0 - 128.193.255.255)
        int_ip = struct.unpack('i',socket.inet_aton(ip))[0]
        if(int_ip > 2160192768 and int_ip < 2160197631):
            return True
        return False
   
    def http_decode(self,tcp,grp_id):
        data = tcp['data']
        seq = tcp['seq']
        ack = tcp['ack']
        http_parameters={}
        start = 0
        end = str(data).find('\r\n\r\n')
        bug = 0
        bugsize = 0
       
        try:
            #Get Request
            get_result = self.get_re.match(str(data))
            if (get_result):
                get = get_result.group('get')
                qmark = str(get).lower().find('?')
                if(qmark != -1):
                    http_parameters['get'] = get[0:qmark]
                else:
                    http_parameters['get'] = get
                start = str(data).find('HTTP')+ 10 # http/1.1\r\n
           
            #Responce and its status
            status_result = self.status_re.match(str(data))
            if (status_result):
                http_parameters['status'] = status_result.group('status')
                start = str(data).find('\r\n')+2 # http/x.x xxx text\r\n
           
            data_list = re.split("\r\n", str(data)[start:end])
            if(start > end):
                return
         
            for line in data_list:
                #print str(line)
                if(line != ''):
                    key,value = re.split(": ", line)
                    if(key.lower() == "set-cookie" or key.lower() == "set-cookie2"):
                        if(not http_parameters.has_key(key.lower())):
                            http_parameters[key.lower()] = []
                        http_parameters[key.lower()].append(value)
                    else:
                        http_parameters[key.lower()] = value
               
        except KeyError: #magic fairy dust to prevent crashing; ignores packets that aren't properly parsed
            return
        except ValueError:
            return

       
        if(http_parameters.has_key('get')):#This is a request
            self.request_dict[seq] = http_parameters
            self.request_dict[seq]['request_time'] = datetime.datetime.now()
           
            #resnet =  2160192768 - 2160197631 (128.193.237.0 - 128.193.255.255)
            if( self.is_resnet(tcp['ip_header']['source_address']) or self.is_resnet(tcp['ip_header']['destination_address'])):
                self.request_dict[seq]['residential'] = 1
            else:
                self.request_dict[seq]['residential'] = 0
            print "(" + str(self.request_dict[seq]['residential'])  + ") Request #" + str(seq)  + " for " + self.request_dict[seq]['host']
            return # don't log request packets
        elif (self.request_dict.has_key(ack)):
            print "Matched request #" + str(ack)
            for para in self.request_dict[ack]:
                if(not http_parameters.has_key(para)): #add any fields not in the request to the entry
                    http_parameters[para] = self.request_dict[ack][para]
            del self.request_dict[ack]
        else:
            print "Unmatched response packet"
            return #a non request packet (a response) that doesn't match timething we have, drop it.

       
        if(datetime.datetime.now() - self.last_checked > datetime.timedelta(0,self.check_seconds)):
            self.last_checked = datetime.datetime.now()
            for key in self.request_dict.keys(): #remove requests that haven't been found.  key = seq number
                if(datetime.datetime.now() - self.request_dict[key]['request_time'] > datetime.timedelta(0,self.check_seconds)):
                    del self.request_dict[key]
            print "Current request dictionary size: " + str(len(self.request_dict))
            #if(len(self.request_dict) > 500):
                #print "Request Dictionary is over 500 elements, if this is not a high load time, this is a problem"
            print "Running for " + str (datetime.datetime.now() - self.start_time)
       
        query = 'INSERT INTO rawpkt ('
        values = []
        cookie_domains = {} #the return list of parse_cookie
        setcooke_domains = [] #the return list of parse_setcookie
       
        if(http_parameters.has_key('host')):
            query += "host, "
            values.append(str(http_parameters['host']))
       
        if(http_parameters.has_key('get')):
            query += "get, "
            q_mark = str(http_parameters['get']).lower().find('?')
            if(q_mark != -1):
                values.append(http_parameters['get'][0:q_mark])
            else:
                values.append(http_parameters['get'])
       
        if(http_parameters.has_key('referer')):
            query += "referer, "
            values.append(str(http_parameters['referer']))
       
        if(http_parameters.has_key('user-agent')):
            query += "useragent, "
            values.append(str(http_parameters['user-agent']))
       
        if(http_parameters.has_key('content-type')):
            query += "contenttype, "
            values.append(str(http_parameters['content-type']))
           # print "\n\n\n"+str(http_parameters['content-type']).lower()+"\n\n\n"
           # print re.search(('gif'),http_parameters['content-type'])
           # print "\n\n\n\n"
            if(re.search(('gif'),http_parameters['content-type']) != None or re.search(('png'),http_parameters['content-type']) != None):
                #its a gif set something to 1
                bug = 1
                
       
        if(http_parameters.has_key('content-length')):
            query += "contentlength, "
            values.append(int(http_parameters['content-length']))
            print str(http_parameters['content-length'])+"\n\n\n"
            if( int(str(http_parameters['content-length'])) <= 50):
                bugsize = 1
           
       
        if(http_parameters.has_key('date')):
            query += "pkt_date, "
            values.append(str(http_parameters['date']))
       
        query += "insert_date, "
        values.append(datetime.datetime.now())
       
        if(http_parameters.has_key('status')):
            query += "status, "
            values.append(str(http_parameters['status']))
       
        if(http_parameters.has_key('server')):
            query += "server, "
            values.append(str(http_parameters['server']))
       
        if(http_parameters.has_key('p3p')):
            query += "p3p, "
            values.append(str(http_parameters['p3p']))
       
        if(http_parameters.has_key('etag')):
            query += "etag, "
            values.append(str(http_parameters['etag']).replace('"', ''))
       
        if(http_parameters.has_key('cookie')):
            if(http_parameters.has_key('host')):
                cookie_domains = self.parse_cookie(http_parameters['cookie'],http_parameters['host'])
       
        if(http_parameters.has_key('set-cookie')):
            setcookie_domains = self.parse_setcookie(http_parameters['set-cookie'])
       
        if(http_parameters.has_key('set-cookie2')):
            setcookie_domains = self.parse_setcookie(http_parameters['set-cookie2'])
       
        query += "seq, "
        values.append(seq)
       
        query += "ack, "
        values.append(ack)
        
        query += "grp_id) "
        grp_id = re.sub(r'(\d*)\.',r'\1',str(grp_id))
        values.append(str(grp_id))
        
        query += 'VALUES ( ' + ', '.join(["%s" for i in range(0,len(values))]) +  ")"
        pkt_id = self.cursor.execute(query, values)
        if(pkt_id % 100 == 0):
            print "Last Row ID: " + str(pkt_id)
            print "Records per second: " + str (pkt_id / (datetime.datetime.now() - self.start_time).seconds )
        self.connection.commit()

       
        if(http_parameters.has_key('cookie') and cookie_domains != {}):
            values = (cookie_domains['id'], pkt_id, "client", cookie_domains['expiry'], cookie_domains['session'])
            self.cursor.execute("INSERT INTO cookie_has(domain_id, pkt_id, set_by, expiry, session) VALUES (%s, %s, %s, %s, %s)", values)
            self.connection.commit()

       
        if((http_parameters.has_key('set-cookie') or http_parameters.has_key('set-cookie2')) and setcookie_domains != []):
            values = []
            for cookie in setcookie_domains:
                values.append((cookie['id'], pkt_id, "server", cookie['expiry'], cookie['session']))
            self.cursor.executemany("INSERT INTO cookie_has(domain_id, pkt_id, set_by, expiry, session) VALUES (%s, %s, %s, %s, %s)", values)
            self.connection.commit()
        if(bug == 1 and bugsize == 1):
            host_list = str(http_parameters['host']).split('.')
            host_str = host_list[len(host_list)-2] + "." + host_list[len(host_list)-1]
           
            
            #self.cursor.execute("INSERT INTO domains(domain,has_bug) VALUES (%s,1)",host_str)#get the last part of host....
            
            self.cursor.execute("SELECT id FROM domains WHERE domain = %s AND has_bug = 1",host_str)
            row = self.cursor.fetchone()
            if(row == None):
                self.cursor.execute("INSERT INTO domains(domain,has_bug) VALUES (%s,1)", host_str)#add it to the table
            else:
                pass
            
            
            
            self.connection.commit()


class SniffUI:
    def __init__(self):
        pass
    def start(self):
        curses.wrapper(self.RunUI)
    def RunUI(self, stdscr):
        win = curses.newwin(8,8,1,1)
        pan = panel.new_panel(win)
        pan.show()
        while 1:
            stdscr.addstr(0, 0, "Current mode: Typing mode", curses.A_REVERSE)
            panel.update_panels()
            curses.doupdate()
            stdscr.refresh()



if __name__=='__main__':
    debug = ""
    #n = SniffUI()
    s = Sniffer()
    #option parser      Edit       Delete      1     en.wikipedia.org     /wiki/P3P     http://www.google.com/url?sa=t&source=web&ct=res&c...     text/html; charset=UTF-8     Fri, 12 Mar 2010 22:06:03 GMT     2010-03-13 14:05:37     304      NULL     Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.8...      NULL      NULL      NULL     29717     34900     0

    parser = OptionParser()
    parser.set_defaults(debug=False)
    parser.add_option('--debug', dest=debug, action='store_true', help="Run with debug to use the local sqlitedb")
    (options, argv) = parser.parse_args(sys.argv)
   
    #n.start()
    s.start()