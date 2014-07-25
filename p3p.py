#! /usr/bin/env python

import curses
import MySQLdb
from urllib2 import Request, urlopen, URLError, HTTPError
from xml.dom import minidom

#
# P3P helper program
# we go through each of the hosts in the rawpkt table
# if the p3p policy is null and we haven't looked at it before we search host/w3c/p3p.xml and if it exists put policyref in the table
#

class p3p:
    def __init__(self):
        self.db_setup()
        self.hosts = self.get_targets()
        self.hosts_fixed = {}
        print "done intiing\n"
        
    def db_setup(self):
        self.connection =  MySQLdb.connect(host="mysql.cs.orst.edu", user="team33", passwd="team33", db="team33")
        self.cursor = self.connection.cursor()
        
    def get_targets(self):
        #get host from rawpkt if p3p policy == null
        self.cursor.execute('SELECT host FROM `rawpkt` WHERE p3p is NULL')
        return self.cursor.fetchall()
    
    def run(self):
        for tmp in self.hosts:
            # search str(tmp).split("'")[1] + "/w3c/p3p.xml"
            host =  str(tmp).split("'")[1]
            if host in self.hosts_fixed:
                print "host in dict\n"
            else:
                self.hosts_fixed[host] = host
                print "host added to dict\n"
                try:
                    print "http://" + str(tmp).split("'")[1] + "/w3c/p3p.xml"
                    response = urlopen("http://" + str(tmp).split("'")[1] + "/w3c/p3p.xml")
                    xml = response.read()
                    try:
                        xmldoc = minidom.parseString(xml)
                        policyref = xmldoc.getElementsByTagName('POLICY-REF')
                        if policyref != []:#minimal error checking
                            try:
                                about = policyref[0].attributes["about"]
                                values = []
                                values.append("policyref = " + str(about.value))
                                values.append(str(host))
                                self.cursor.execute("UPDATE rawpkt SET p3p=%s WHERE host=%s", values)
        
                            except KeyError, ke:
                                print "no about attribute"
                        else:
                            print "no policy ref tag" 
                    except:
                        print "malformed xml probably gmail or another site that forwards bad url's\n"
                    
                except HTTPError, e:
                    print "404\n"
            
if __name__=='__main__':
    p3p = p3p()
    p3p.run()