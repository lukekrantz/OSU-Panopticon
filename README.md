Installation
==============

* http_sniff.py:

	http_sniff needs python 2.5. This is because the packet sniffing library it uses is a little outdated, and hasn't been compiled for python 2.6. 
	It wouldn't be too complicated to recompile the library for a newer python, if it is needed.


Non Standard Libraries needed:



* pcapy:

python frontend to libpcap. Can be found at: http://oss.coresecurity.com/projects/pcapy.html  Ubuntu
 has a apt package at python-pcapy. it has some complicated documentation, but the functions are similiar 
to the libpcap library so those documents work the same.


* MySQLdb:

the standard (but not included for some reason) python mysql library. http://sourceforge.net/projects/mysql-python/ 
Ubuntu has an apt package for this as well, python-mysqldb


Execution:
==========
http_sniff needs root privelages on a linux machine, administrator on windows if it gets ported. 
To run it type: sudo python http_sniff.py or chmod it to have execution privelages and drop the 
python part. p3p.py doesn't need to be ran as root as it doesnt use the packet sniffing library.


Program Overview:
==================

* http_sniff:

	http_sniff.py is the sniffing application.  It sniffs on the device defined on lines 29-34.  Change these to meet your needs.  It grabs the packets that pass through the packet filter and checks to see if they are in the dictionary of connections.  If they are the dictionary then they are part of an ongoing connection and get parsed through and added to the database.  If they are not in the dictionary we check to see how large it is.  If it is less than 500 (an arbitrary number at this point) then it is added to the dictionary and parsed as usual.  If the dictionary is full then we reject the packet, effectively saving a bunch of cpu time so we dont slow down the system too much.  If the packet is rejected, and it has been over a minute since the last packet was rejected, we clear out the connection database.  This means that if a connection has timed out, a number that is based on the browser that is being used, then it gets erased from the database to save room for new connections. The actual parsing is commented in the code if it is not intuitive.


* p3p:

	This is a helper function that goes through the rawpkt table of the database and if the p3p section is null, it checks the standard place for it, we could only find host/w3c/p3p.xml in the w3c p3p specification, and parses through the xml for the actual document location, and adds it to the database.
	makeDB
	This file contains the php fucntions to make the databases.


