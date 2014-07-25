#!/usr/bin/env python
import sys, os, re, urllib2
from pysqlite2 import dbapi2 as sqlite

if len(sys.argv) < 3:
    print "Usage: ./" + sys.argv[0] + " <dbname> (webbugs|cookies) [--consolidate]"
    sys.exit()
if(len(sys.argv) > 3 and (sys.argv[3] == '--consolidate')):
    consolidate = True
else:
    consolidate = False

domain_re = re.compile('.*http:\/\/(?P<domain>.*?)\/')
sqlitedbname = sys.argv[1]
datatype = sys.argv[2]
connection = sqlite.connect(sqlitedbname)
connection.row_factory = sqlite.Row
cursor = connection.cursor()
if(datatype == "webbugs"):
    f = open("webbugs.graphml", 'w')
elif(datatype == "cookies"):
    f = open("cookies.graphml", 'w')
else:
    print "unknown data type: " + str(datatype)
    sys.exit(1)
    
header = """<?xml version="1.0" encoding="UTF-8"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns/graphml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:y="http://www.yworks.com/xml/graphml" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns/graphml http://www.yworks.com/xml/schema/graphml/1.0/ygraphml.xsd">
  <key for="node" id="d0" yfiles.type="nodegraphics"/>
  <key attr.name="description" attr.type="string" for="node" id="d1"/>
  <key for="edge" id="d2" yfiles.type="edgegraphics"/>
  <key attr.name="description" attr.type="string" for="edge" id="d3"/>
  <key for="graphml" id="d4" yfiles.type="resources"/>
  <graph edgedefault="directed" id="G" parse.order="free">"""

footer = """\n</graph>\n<data key="d4">\n<y:Resources/>\n</data>\n</graphml>"""

if(datatype == "webbugs"):
    query = 'select host,referer from rawpkt where status="200" and contenttype like "image/gif%" and contentlength < 44 and referer like "http://%"'
elif(datatype == "cookies"):
    query = 'select p.host,d.domain from cookie_has c,domains d, rawpkt p where (c.domain_id=d.id and c.pkt_id=p.id) and (d.domain != p.host and d.domain != "(null)" and p.host !="(null)")'
else:
    print "error in determining the SQL query to use"
    sys.exit(1)
    
cursor.execute(query)


print "Stage 1: Parse the data into a set of nodes and a set of edge tuples"
edges = set() #built-in set type
nodes = set()
for row in cursor:
    try:
        if(datatype == 'webbugs'):
            if(row['referer'] != None):
                domain_result = domain_re.match(str(row['referer']))
                if (domain_result):
                    domain = domain_result.group('domain')
                    if(domain != row['host']):
                        edges.add((domain.replace('&',''),row['host'].replace('&','')))
                        nodes.add(domain.replace('&',''))
                        nodes.add(row['host'].replace('&',''))
        elif(datatype == 'cookies'):
            if(row['host'].find(row['domain']) == -1): #cookie isn't for the same domain
                if(row['host'].count('&') > 0 or row['domain'].count('&') > 0) or (row['host'].count(',') > 0 or row['domain'].count(',') > 0) or (row['host'].count('"') > 0 or row['domain'].count('"') > 0):
                    print row
                else:
                    edges.add((row['host'],row['domain']))
                    nodes.add(row['domain'])
                    nodes.add(row['host'])
        else:
            print "error in determining how to process the query results"
            sys.exit(1)
    except:
        print row


cursor.close()
connection.close()


####IMCOMPLETE
if(consolidate):
    print "Stage 2: Remove subdomains and consolidate into a single domain"
    consolidated_edges = set()
    consolidated_nodes = set()
    #http://data.iana.org/TLD/tlds-alpha-by-domain.txt
    tlds = urllib2.urlopen('http://data.iana.org/TLD/tlds-alpha-by-domain.txt')
    for tld in tlds:
        tld = tld.lower().strip()
        if(tld.isalpha()): #ignore first line which is a comment
            for n in nodes:
                if(n[-(len(tld)+1):] == '.' + tld): #end of domain string is the tld?
                    idx = n.rfind('.', 0, -(len(tld)+1)) # find the last '.' before the tld
                    if(idx != -1): #if this contains a dot besides between the domain and tld
                        print n + " -> " + n[idx+1:]
                        if(n[idx+1:] not in nodes):
                            consolidated_nodes.add(n[idx+1:])
                        for host,domain in edges:
                            if(host == n):
                                host = n[idx+1:]
                            if(domain == n):
                                domain = n[idx+1:]
                            consolidated_edges.add((host,domain))
    nodes = consolidated_nodes
    edges = consolidated_edges



#write to a graphml file

f.write(header)
    
for id in nodes:
    node_string = '<node id="' + id + '">\n'
    node_string += '<data key="d0">\n'
    node_string += '<y:ShapeNode>\n'
    node_string += '<y:NodeLabel>' + id + '</y:NodeLabel>\n'
    node_string += '</y:ShapeNode>\n'
    node_string += '</data>\n</node>\n'
    f.write(node_string)

i = 0
for host,domain in edges:
    i += 1 
    edge_string = '<edge id="' +  str(i) + '" source="' + host + '" target="' + domain + '">\n'
    edge_string += '<data key="d2">\n'
    edge_string += '<y:PolyLineEdge>\n'
    edge_string += '<y:Path sx="0.0" sy="0.0" tx="0.0" ty="0.0"/>\n'
    edge_string += '<y:LineStyle type="line" width="1.0" color="#000000" />\n'
    edge_string += '<y:Arrows source="none" target="standard"/>\n'
    edge_string += '<y:BendStyle smoothed="false"/>\n'
    edge_string += '</y:PolyLineEdge>\n'
    edge_string += '</data>\n<data key="d3"/>\n</edge>\n'
    f.write(edge_string)
    
f.write(footer)
f.close()
