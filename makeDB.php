<?php
$createrwpkt = "CREATE TABLE rawpkt
(
id INTEGER NOT NULL AUTO_INCREMENT,
PRIMARY KEY(id),
host VARCHAR(128),
get VARCHAR(1024),
referer VARCHAR(1024),
contenttype VARCHAR(32),
pkt_date VARCHAR(32),
insert_date DATETIME,
status INTEGER,
server VARCHAR(100),
useragent VARCHAR(100),
p3p VARCHAR(256),
etag VARCHAR(32),
contentlength INTEGER,
seq INTEGER,
ack INTEGER,
residential BOOLEAN NOT NULL DEFAULT 0,
grp_id INTEGER
)";
$createcookie = "CREATE TABLE cookie_has
(
id INTEGER NOT NULL AUTO_INCREMENT,
PRIMARY KEY(id),
domain_id INTEGER NOT NULL,
pkt_id INTEGER NOT NULL,
set_by VARCHAR(24),
expiry VARCHAR(32),
session BOOLEAN
)";
$createdomains = "CREATE TABLE domains
(
id INTEGER NOT NULL AUTO_INCREMENT,
PRIMARY KEY(id),
domain VARCHAR(128) NOT NULL,
has_bug INT(1)
)";


$con = mysql_connect("mysql.cs.orst.edu","team33","team33");
mysql_select_db("team33") or die("Unable to select database\n");
mysql_query($createrwpkt,$con) or die("Unable to create rwpkt table\n");
mysql_query($createcookie,$con) or die("Unable to create cookie table\n");
mysql_query($createdomains,$con) or die("Unable to create domains table\n");



mysql_close($con);
?>
