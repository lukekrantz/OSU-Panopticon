



<!DOCTYPE html>
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
 <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" >
 
 <meta name="ROBOTS" content="NOARCHIVE">
 
 <link rel="icon" type="image/vnd.microsoft.icon" href="https://ssl.gstatic.com/codesite/ph/images/phosting.ico">
 
 
 <script type="text/javascript">
 
 
 
 
 var codesite_token = "ABZ6GAcyt1dMU9RFW3eWmwpjxglIUw4cqw:1406256704307";
 
 
 var CS_env = {"projectName": "panopticon-osu", "projectHomeUrl": "/p/panopticon-osu", "profileUrl": "/u/115368015194065129388/", "token": "ABZ6GAcyt1dMU9RFW3eWmwpjxglIUw4cqw:1406256704307", "relativeBaseUrl": "", "domainName": null, "assetVersionPath": "https://ssl.gstatic.com/codesite/ph/13997016681179179006", "assetHostPath": "https://ssl.gstatic.com/codesite/ph", "loggedInUserEmail": "lukeKrantz@gmail.com"};
 var _gaq = _gaq || [];
 _gaq.push(
 ['siteTracker._setAccount', 'UA-18071-1'],
 ['siteTracker._trackPageview']);
 
 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
 })();
 
 </script>
 
 
 <title>http_sniff.py - 
 panopticon-osu -
 
 
 packet sniffer specialized for anyalizing privacy concerns - Google Project Hosting
 </title>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/13997016681179179006/css/core.css">
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/13997016681179179006/css/ph_detail.css" >
 
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/13997016681179179006/css/d_sb.css" >
 
 
 
<!--[if IE]>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/13997016681179179006/css/d_ie.css" >
<![endif]-->
 <style type="text/css">
 .menuIcon.off { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -42px }
 .menuIcon.on { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -28px }
 .menuIcon.down { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 0; }
 
 
 
  tr.inline_comment {
 background: #fff;
 vertical-align: top;
 }
 div.draft, div.published {
 padding: .3em;
 border: 1px solid #999; 
 margin-bottom: .1em;
 font-family: arial, sans-serif;
 max-width: 60em;
 }
 div.draft {
 background: #ffa;
 } 
 div.published {
 background: #e5ecf9;
 }
 div.published .body, div.draft .body {
 padding: .5em .1em .1em .1em;
 max-width: 60em;
 white-space: pre-wrap;
 white-space: -moz-pre-wrap;
 white-space: -pre-wrap;
 white-space: -o-pre-wrap;
 word-wrap: break-word;
 font-size: 1em;
 }
 div.draft .actions {
 margin-left: 1em;
 font-size: 90%;
 }
 div.draft form {
 padding: .5em .5em .5em 0;
 }
 div.draft textarea, div.published textarea {
 width: 95%;
 height: 10em;
 font-family: arial, sans-serif;
 margin-bottom: .5em;
 }

 
 .nocursor, .nocursor td, .cursor_hidden, .cursor_hidden td {
 background-color: white;
 height: 2px;
 }
 .cursor, .cursor td {
 background-color: darkblue;
 height: 2px;
 display: '';
 }
 
 
.list {
 border: 1px solid white;
 border-bottom: 0;
}

 
 </style>
</head>
<body class="t4">
<script type="text/javascript">
 window.___gcfg = {lang: 'en'};
 (function() 
 {var po = document.createElement("script");
 po.type = "text/javascript"; po.async = true;po.src = "https://apis.google.com/js/plusone.js";
 var s = document.getElementsByTagName("script")[0];
 s.parentNode.insertBefore(po, s);
 })();
</script>
<div class="headbg">

 <div id="gaia">
 

 <span>
 
 
 
 <a href="#" id="multilogin-dropdown" onclick="return false;"
 ><u><b>lukeKrantz@gmail.com</b></u> <small>&#9660;</small></a>
 
 
 | <a href="/u/115368015194065129388/" id="projects-dropdown" onclick="return false;"
 ><u>My favorites</u> <small>&#9660;</small></a>
 | <a href="/u/115368015194065129388/" onclick="_CS_click('/gb/ph/profile');"
 title="Profile, Updates, and Settings"
 ><u>Profile</u></a>
 | <a href="https://www.google.com/accounts/Logout?continue=https%3A%2F%2Fcode.google.com%2Fp%2Fpanopticon-osu%2Fsource%2Fbrowse%2Ftrunk%2Fsrc%2Fhttp_sniff.py" 
 onclick="_CS_click('/gb/ph/signout');"
 ><u>Sign out</u></a>
 
 </span>

 </div>

 <div class="gbh" style="left: 0pt;"></div>
 <div class="gbh" style="right: 0pt;"></div>
 
 
 <div style="height: 1px"></div>
<!--[if lte IE 7]>
<div style="text-align:center;">
Your version of Internet Explorer is not supported. Try a browser that
contributes to open source, such as <a href="http://www.firefox.com">Firefox</a>,
<a href="http://www.google.com/chrome">Google Chrome</a>, or
<a href="http://code.google.com/chrome/chromeframe/">Google Chrome Frame</a>.
</div>
<![endif]-->



 <table style="padding:0px; margin: 0px 0px 10px 0px; width:100%" cellpadding="0" cellspacing="0"
 itemscope itemtype="http://schema.org/CreativeWork">
 <tr style="height: 58px;">
 
 
 
 <td id="plogo">
 <link itemprop="url" href="/p/panopticon-osu">
 <a href="/p/panopticon-osu/">
 
 <img src="https://ssl.gstatic.com/codesite/ph/images/defaultlogo.png" alt="Logo" itemprop="image">
 
 </a>
 </td>
 
 <td style="padding-left: 0.5em">
 
 <div id="pname">
 <a href="/p/panopticon-osu/"><span itemprop="name">panopticon-osu</span></a>
 </div>
 
 <div id="psum">
 <a id="project_summary_link"
 href="/p/panopticon-osu/"><span itemprop="description">packet sniffer specialized for anyalizing privacy concerns</span></a>
 
 </div>
 
 
 </td>
 <td style="white-space:nowrap;text-align:right; vertical-align:bottom;">
 
 <form action="/hosting/search">
 <input size="30" name="q" value="" type="text">
 
 <input type="submit" name="projectsearch" value="Search projects" >
 </form>
 
 </tr>
 </table>

</div>

 
<div id="mt" class="gtb"> 
 <a href="/p/panopticon-osu/" class="tab ">Project&nbsp;Home</a>
 
 
 
 
 
 
 <a href="/p/panopticon-osu/w/list" class="tab ">Wiki</a>
 
 
 
 
 
 <a href="/p/panopticon-osu/issues/list"
 class="tab ">Issues</a>
 
 
 
 
 
 <a href="/p/panopticon-osu/source/checkout"
 class="tab active">Source</a>
 
 
 
 
 
 <a href="/p/panopticon-osu/admin"
 class="tab inactive">Administer</a>
 
 
 
 
 <div class=gtbc></div>
</div>
<table cellspacing="0" cellpadding="0" width="100%" align="center" border="0" class="st">
 <tr>
 
 
 
 
 
 
 <td class="subt">
 <div class="st2">
 <div class="isf">
 
 


 <span class="inst1"><a href="/p/panopticon-osu/source/checkout">Checkout</a></span> &nbsp;
 <span class="inst2"><a href="/p/panopticon-osu/source/browse/">Browse</a></span> &nbsp;
 <span class="inst3"><a href="/p/panopticon-osu/source/list">Changes</a></span> &nbsp;
 
 
 
 
 
 <a href="/p/panopticon-osu/issues/entry?show=review&former=sourcelist">Request code review</a>
 
 
 
 </form>
 <script type="text/javascript">
 
 function codesearchQuery(form) {
 var query = document.getElementById('q').value;
 if (query) { form.action += '%20' + query; }
 }
 </script>
 </div>
</div>

 </td>
 
 
 
 <td align="right" valign="top" class="bevel-right"></td>
 </tr>
</table>


<script type="text/javascript">
 var cancelBubble = false;
 function _go(url) { document.location = url; }
</script>
<div id="maincol"
 
>

 




<div class="collapse">
<div id="colcontrol">
<style type="text/css">
 #file_flipper { white-space: nowrap; padding-right: 2em; }
 #file_flipper.hidden { display: none; }
 #file_flipper .pagelink { color: #0000CC; text-decoration: underline; }
 #file_flipper #visiblefiles { padding-left: 0.5em; padding-right: 0.5em; }
</style>
<table id="nav_and_rev" class="list"
 cellpadding="0" cellspacing="0" width="100%">
 <tr>
 
 <td nowrap="nowrap" class="src_crumbs src_nav" width="33%">
 <strong class="src_nav">Source path:&nbsp;</strong>
 <span id="crumb_root">
 
 <a href="/p/panopticon-osu/source/browse/">svn</a>/&nbsp;</span>
 <span id="crumb_links" class="ifClosed"><a href="/p/panopticon-osu/source/browse/trunk/">trunk</a><span class="sp">/&nbsp;</span><a href="/p/panopticon-osu/source/browse/trunk/src/">src</a><span class="sp">/&nbsp;</span>http_sniff.py</span>
 
 


 </td>
 
 
 <td nowrap="nowrap" width="33%" align="center">
 <a href="/p/panopticon-osu/source/browse/trunk/src/http_sniff.py?edit=1"
 ><img src="https://ssl.gstatic.com/codesite/ph/images/pencil-y14.png"
 class="edit_icon">Edit file</a>
 </td>
 
 
 <td nowrap="nowrap" width="33%" align="right">
 <table cellpadding="0" cellspacing="0" style="font-size: 100%"><tr>
 
 
 <td class="flipper">
 <ul class="leftside">
 
 <li><a href="/p/panopticon-osu/source/browse/trunk/src/http_sniff.py?r=24" title="Previous">&lsaquo;r24</a></li>
 
 </ul>
 </td>
 
 <td class="flipper"><b>r27</b></td>
 
 </tr></table>
 </td> 
 </tr>
</table>

<div class="fc">
 
 
 
<style type="text/css">
.undermouse span {
 background-image: url(https://ssl.gstatic.com/codesite/ph/images/comments.gif); }
</style>
<table class="opened" id="review_comment_area"
onmouseout="gutterOut()"><tr>
<td id="nums">
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
<pre><table width="100%" id="nums_table_0"><tr id="gr_svn27_1"

 onmouseover="gutterOver(1)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',1);">&nbsp;</span
></td><td id="1"><a href="#1">1</a></td></tr
><tr id="gr_svn27_2"

 onmouseover="gutterOver(2)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',2);">&nbsp;</span
></td><td id="2"><a href="#2">2</a></td></tr
><tr id="gr_svn27_3"

 onmouseover="gutterOver(3)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',3);">&nbsp;</span
></td><td id="3"><a href="#3">3</a></td></tr
><tr id="gr_svn27_4"

 onmouseover="gutterOver(4)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',4);">&nbsp;</span
></td><td id="4"><a href="#4">4</a></td></tr
><tr id="gr_svn27_5"

 onmouseover="gutterOver(5)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',5);">&nbsp;</span
></td><td id="5"><a href="#5">5</a></td></tr
><tr id="gr_svn27_6"

 onmouseover="gutterOver(6)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',6);">&nbsp;</span
></td><td id="6"><a href="#6">6</a></td></tr
><tr id="gr_svn27_7"

 onmouseover="gutterOver(7)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',7);">&nbsp;</span
></td><td id="7"><a href="#7">7</a></td></tr
><tr id="gr_svn27_8"

 onmouseover="gutterOver(8)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',8);">&nbsp;</span
></td><td id="8"><a href="#8">8</a></td></tr
><tr id="gr_svn27_9"

 onmouseover="gutterOver(9)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',9);">&nbsp;</span
></td><td id="9"><a href="#9">9</a></td></tr
><tr id="gr_svn27_10"

 onmouseover="gutterOver(10)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',10);">&nbsp;</span
></td><td id="10"><a href="#10">10</a></td></tr
><tr id="gr_svn27_11"

 onmouseover="gutterOver(11)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',11);">&nbsp;</span
></td><td id="11"><a href="#11">11</a></td></tr
><tr id="gr_svn27_12"

 onmouseover="gutterOver(12)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',12);">&nbsp;</span
></td><td id="12"><a href="#12">12</a></td></tr
><tr id="gr_svn27_13"

 onmouseover="gutterOver(13)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',13);">&nbsp;</span
></td><td id="13"><a href="#13">13</a></td></tr
><tr id="gr_svn27_14"

 onmouseover="gutterOver(14)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',14);">&nbsp;</span
></td><td id="14"><a href="#14">14</a></td></tr
><tr id="gr_svn27_15"

 onmouseover="gutterOver(15)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',15);">&nbsp;</span
></td><td id="15"><a href="#15">15</a></td></tr
><tr id="gr_svn27_16"

 onmouseover="gutterOver(16)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',16);">&nbsp;</span
></td><td id="16"><a href="#16">16</a></td></tr
><tr id="gr_svn27_17"

 onmouseover="gutterOver(17)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',17);">&nbsp;</span
></td><td id="17"><a href="#17">17</a></td></tr
><tr id="gr_svn27_18"

 onmouseover="gutterOver(18)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',18);">&nbsp;</span
></td><td id="18"><a href="#18">18</a></td></tr
><tr id="gr_svn27_19"

 onmouseover="gutterOver(19)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',19);">&nbsp;</span
></td><td id="19"><a href="#19">19</a></td></tr
><tr id="gr_svn27_20"

 onmouseover="gutterOver(20)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',20);">&nbsp;</span
></td><td id="20"><a href="#20">20</a></td></tr
><tr id="gr_svn27_21"

 onmouseover="gutterOver(21)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',21);">&nbsp;</span
></td><td id="21"><a href="#21">21</a></td></tr
><tr id="gr_svn27_22"

 onmouseover="gutterOver(22)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',22);">&nbsp;</span
></td><td id="22"><a href="#22">22</a></td></tr
><tr id="gr_svn27_23"

 onmouseover="gutterOver(23)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',23);">&nbsp;</span
></td><td id="23"><a href="#23">23</a></td></tr
><tr id="gr_svn27_24"

 onmouseover="gutterOver(24)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',24);">&nbsp;</span
></td><td id="24"><a href="#24">24</a></td></tr
><tr id="gr_svn27_25"

 onmouseover="gutterOver(25)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',25);">&nbsp;</span
></td><td id="25"><a href="#25">25</a></td></tr
><tr id="gr_svn27_26"

 onmouseover="gutterOver(26)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',26);">&nbsp;</span
></td><td id="26"><a href="#26">26</a></td></tr
><tr id="gr_svn27_27"

 onmouseover="gutterOver(27)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',27);">&nbsp;</span
></td><td id="27"><a href="#27">27</a></td></tr
><tr id="gr_svn27_28"

 onmouseover="gutterOver(28)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',28);">&nbsp;</span
></td><td id="28"><a href="#28">28</a></td></tr
><tr id="gr_svn27_29"

 onmouseover="gutterOver(29)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',29);">&nbsp;</span
></td><td id="29"><a href="#29">29</a></td></tr
><tr id="gr_svn27_30"

 onmouseover="gutterOver(30)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',30);">&nbsp;</span
></td><td id="30"><a href="#30">30</a></td></tr
><tr id="gr_svn27_31"

 onmouseover="gutterOver(31)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',31);">&nbsp;</span
></td><td id="31"><a href="#31">31</a></td></tr
><tr id="gr_svn27_32"

 onmouseover="gutterOver(32)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',32);">&nbsp;</span
></td><td id="32"><a href="#32">32</a></td></tr
><tr id="gr_svn27_33"

 onmouseover="gutterOver(33)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',33);">&nbsp;</span
></td><td id="33"><a href="#33">33</a></td></tr
><tr id="gr_svn27_34"

 onmouseover="gutterOver(34)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',34);">&nbsp;</span
></td><td id="34"><a href="#34">34</a></td></tr
><tr id="gr_svn27_35"

 onmouseover="gutterOver(35)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',35);">&nbsp;</span
></td><td id="35"><a href="#35">35</a></td></tr
><tr id="gr_svn27_36"

 onmouseover="gutterOver(36)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',36);">&nbsp;</span
></td><td id="36"><a href="#36">36</a></td></tr
><tr id="gr_svn27_37"

 onmouseover="gutterOver(37)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',37);">&nbsp;</span
></td><td id="37"><a href="#37">37</a></td></tr
><tr id="gr_svn27_38"

 onmouseover="gutterOver(38)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',38);">&nbsp;</span
></td><td id="38"><a href="#38">38</a></td></tr
><tr id="gr_svn27_39"

 onmouseover="gutterOver(39)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',39);">&nbsp;</span
></td><td id="39"><a href="#39">39</a></td></tr
><tr id="gr_svn27_40"

 onmouseover="gutterOver(40)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',40);">&nbsp;</span
></td><td id="40"><a href="#40">40</a></td></tr
><tr id="gr_svn27_41"

 onmouseover="gutterOver(41)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',41);">&nbsp;</span
></td><td id="41"><a href="#41">41</a></td></tr
><tr id="gr_svn27_42"

 onmouseover="gutterOver(42)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',42);">&nbsp;</span
></td><td id="42"><a href="#42">42</a></td></tr
><tr id="gr_svn27_43"

 onmouseover="gutterOver(43)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',43);">&nbsp;</span
></td><td id="43"><a href="#43">43</a></td></tr
><tr id="gr_svn27_44"

 onmouseover="gutterOver(44)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',44);">&nbsp;</span
></td><td id="44"><a href="#44">44</a></td></tr
><tr id="gr_svn27_45"

 onmouseover="gutterOver(45)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',45);">&nbsp;</span
></td><td id="45"><a href="#45">45</a></td></tr
><tr id="gr_svn27_46"

 onmouseover="gutterOver(46)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',46);">&nbsp;</span
></td><td id="46"><a href="#46">46</a></td></tr
><tr id="gr_svn27_47"

 onmouseover="gutterOver(47)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',47);">&nbsp;</span
></td><td id="47"><a href="#47">47</a></td></tr
><tr id="gr_svn27_48"

 onmouseover="gutterOver(48)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',48);">&nbsp;</span
></td><td id="48"><a href="#48">48</a></td></tr
><tr id="gr_svn27_49"

 onmouseover="gutterOver(49)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',49);">&nbsp;</span
></td><td id="49"><a href="#49">49</a></td></tr
><tr id="gr_svn27_50"

 onmouseover="gutterOver(50)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',50);">&nbsp;</span
></td><td id="50"><a href="#50">50</a></td></tr
><tr id="gr_svn27_51"

 onmouseover="gutterOver(51)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',51);">&nbsp;</span
></td><td id="51"><a href="#51">51</a></td></tr
><tr id="gr_svn27_52"

 onmouseover="gutterOver(52)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',52);">&nbsp;</span
></td><td id="52"><a href="#52">52</a></td></tr
><tr id="gr_svn27_53"

 onmouseover="gutterOver(53)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',53);">&nbsp;</span
></td><td id="53"><a href="#53">53</a></td></tr
><tr id="gr_svn27_54"

 onmouseover="gutterOver(54)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',54);">&nbsp;</span
></td><td id="54"><a href="#54">54</a></td></tr
><tr id="gr_svn27_55"

 onmouseover="gutterOver(55)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',55);">&nbsp;</span
></td><td id="55"><a href="#55">55</a></td></tr
><tr id="gr_svn27_56"

 onmouseover="gutterOver(56)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',56);">&nbsp;</span
></td><td id="56"><a href="#56">56</a></td></tr
><tr id="gr_svn27_57"

 onmouseover="gutterOver(57)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',57);">&nbsp;</span
></td><td id="57"><a href="#57">57</a></td></tr
><tr id="gr_svn27_58"

 onmouseover="gutterOver(58)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',58);">&nbsp;</span
></td><td id="58"><a href="#58">58</a></td></tr
><tr id="gr_svn27_59"

 onmouseover="gutterOver(59)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',59);">&nbsp;</span
></td><td id="59"><a href="#59">59</a></td></tr
><tr id="gr_svn27_60"

 onmouseover="gutterOver(60)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',60);">&nbsp;</span
></td><td id="60"><a href="#60">60</a></td></tr
><tr id="gr_svn27_61"

 onmouseover="gutterOver(61)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',61);">&nbsp;</span
></td><td id="61"><a href="#61">61</a></td></tr
><tr id="gr_svn27_62"

 onmouseover="gutterOver(62)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',62);">&nbsp;</span
></td><td id="62"><a href="#62">62</a></td></tr
><tr id="gr_svn27_63"

 onmouseover="gutterOver(63)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',63);">&nbsp;</span
></td><td id="63"><a href="#63">63</a></td></tr
><tr id="gr_svn27_64"

 onmouseover="gutterOver(64)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',64);">&nbsp;</span
></td><td id="64"><a href="#64">64</a></td></tr
><tr id="gr_svn27_65"

 onmouseover="gutterOver(65)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',65);">&nbsp;</span
></td><td id="65"><a href="#65">65</a></td></tr
><tr id="gr_svn27_66"

 onmouseover="gutterOver(66)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',66);">&nbsp;</span
></td><td id="66"><a href="#66">66</a></td></tr
><tr id="gr_svn27_67"

 onmouseover="gutterOver(67)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',67);">&nbsp;</span
></td><td id="67"><a href="#67">67</a></td></tr
><tr id="gr_svn27_68"

 onmouseover="gutterOver(68)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',68);">&nbsp;</span
></td><td id="68"><a href="#68">68</a></td></tr
><tr id="gr_svn27_69"

 onmouseover="gutterOver(69)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',69);">&nbsp;</span
></td><td id="69"><a href="#69">69</a></td></tr
><tr id="gr_svn27_70"

 onmouseover="gutterOver(70)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',70);">&nbsp;</span
></td><td id="70"><a href="#70">70</a></td></tr
><tr id="gr_svn27_71"

 onmouseover="gutterOver(71)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',71);">&nbsp;</span
></td><td id="71"><a href="#71">71</a></td></tr
><tr id="gr_svn27_72"

 onmouseover="gutterOver(72)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',72);">&nbsp;</span
></td><td id="72"><a href="#72">72</a></td></tr
><tr id="gr_svn27_73"

 onmouseover="gutterOver(73)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',73);">&nbsp;</span
></td><td id="73"><a href="#73">73</a></td></tr
><tr id="gr_svn27_74"

 onmouseover="gutterOver(74)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',74);">&nbsp;</span
></td><td id="74"><a href="#74">74</a></td></tr
><tr id="gr_svn27_75"

 onmouseover="gutterOver(75)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',75);">&nbsp;</span
></td><td id="75"><a href="#75">75</a></td></tr
><tr id="gr_svn27_76"

 onmouseover="gutterOver(76)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',76);">&nbsp;</span
></td><td id="76"><a href="#76">76</a></td></tr
><tr id="gr_svn27_77"

 onmouseover="gutterOver(77)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',77);">&nbsp;</span
></td><td id="77"><a href="#77">77</a></td></tr
><tr id="gr_svn27_78"

 onmouseover="gutterOver(78)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',78);">&nbsp;</span
></td><td id="78"><a href="#78">78</a></td></tr
><tr id="gr_svn27_79"

 onmouseover="gutterOver(79)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',79);">&nbsp;</span
></td><td id="79"><a href="#79">79</a></td></tr
><tr id="gr_svn27_80"

 onmouseover="gutterOver(80)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',80);">&nbsp;</span
></td><td id="80"><a href="#80">80</a></td></tr
><tr id="gr_svn27_81"

 onmouseover="gutterOver(81)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',81);">&nbsp;</span
></td><td id="81"><a href="#81">81</a></td></tr
><tr id="gr_svn27_82"

 onmouseover="gutterOver(82)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',82);">&nbsp;</span
></td><td id="82"><a href="#82">82</a></td></tr
><tr id="gr_svn27_83"

 onmouseover="gutterOver(83)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',83);">&nbsp;</span
></td><td id="83"><a href="#83">83</a></td></tr
><tr id="gr_svn27_84"

 onmouseover="gutterOver(84)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',84);">&nbsp;</span
></td><td id="84"><a href="#84">84</a></td></tr
><tr id="gr_svn27_85"

 onmouseover="gutterOver(85)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',85);">&nbsp;</span
></td><td id="85"><a href="#85">85</a></td></tr
><tr id="gr_svn27_86"

 onmouseover="gutterOver(86)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',86);">&nbsp;</span
></td><td id="86"><a href="#86">86</a></td></tr
><tr id="gr_svn27_87"

 onmouseover="gutterOver(87)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',87);">&nbsp;</span
></td><td id="87"><a href="#87">87</a></td></tr
><tr id="gr_svn27_88"

 onmouseover="gutterOver(88)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',88);">&nbsp;</span
></td><td id="88"><a href="#88">88</a></td></tr
><tr id="gr_svn27_89"

 onmouseover="gutterOver(89)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',89);">&nbsp;</span
></td><td id="89"><a href="#89">89</a></td></tr
><tr id="gr_svn27_90"

 onmouseover="gutterOver(90)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',90);">&nbsp;</span
></td><td id="90"><a href="#90">90</a></td></tr
><tr id="gr_svn27_91"

 onmouseover="gutterOver(91)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',91);">&nbsp;</span
></td><td id="91"><a href="#91">91</a></td></tr
><tr id="gr_svn27_92"

 onmouseover="gutterOver(92)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',92);">&nbsp;</span
></td><td id="92"><a href="#92">92</a></td></tr
><tr id="gr_svn27_93"

 onmouseover="gutterOver(93)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',93);">&nbsp;</span
></td><td id="93"><a href="#93">93</a></td></tr
><tr id="gr_svn27_94"

 onmouseover="gutterOver(94)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',94);">&nbsp;</span
></td><td id="94"><a href="#94">94</a></td></tr
><tr id="gr_svn27_95"

 onmouseover="gutterOver(95)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',95);">&nbsp;</span
></td><td id="95"><a href="#95">95</a></td></tr
><tr id="gr_svn27_96"

 onmouseover="gutterOver(96)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',96);">&nbsp;</span
></td><td id="96"><a href="#96">96</a></td></tr
><tr id="gr_svn27_97"

 onmouseover="gutterOver(97)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',97);">&nbsp;</span
></td><td id="97"><a href="#97">97</a></td></tr
><tr id="gr_svn27_98"

 onmouseover="gutterOver(98)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',98);">&nbsp;</span
></td><td id="98"><a href="#98">98</a></td></tr
><tr id="gr_svn27_99"

 onmouseover="gutterOver(99)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',99);">&nbsp;</span
></td><td id="99"><a href="#99">99</a></td></tr
><tr id="gr_svn27_100"

 onmouseover="gutterOver(100)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',100);">&nbsp;</span
></td><td id="100"><a href="#100">100</a></td></tr
><tr id="gr_svn27_101"

 onmouseover="gutterOver(101)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',101);">&nbsp;</span
></td><td id="101"><a href="#101">101</a></td></tr
><tr id="gr_svn27_102"

 onmouseover="gutterOver(102)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',102);">&nbsp;</span
></td><td id="102"><a href="#102">102</a></td></tr
><tr id="gr_svn27_103"

 onmouseover="gutterOver(103)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',103);">&nbsp;</span
></td><td id="103"><a href="#103">103</a></td></tr
><tr id="gr_svn27_104"

 onmouseover="gutterOver(104)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',104);">&nbsp;</span
></td><td id="104"><a href="#104">104</a></td></tr
><tr id="gr_svn27_105"

 onmouseover="gutterOver(105)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',105);">&nbsp;</span
></td><td id="105"><a href="#105">105</a></td></tr
><tr id="gr_svn27_106"

 onmouseover="gutterOver(106)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',106);">&nbsp;</span
></td><td id="106"><a href="#106">106</a></td></tr
><tr id="gr_svn27_107"

 onmouseover="gutterOver(107)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',107);">&nbsp;</span
></td><td id="107"><a href="#107">107</a></td></tr
><tr id="gr_svn27_108"

 onmouseover="gutterOver(108)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',108);">&nbsp;</span
></td><td id="108"><a href="#108">108</a></td></tr
><tr id="gr_svn27_109"

 onmouseover="gutterOver(109)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',109);">&nbsp;</span
></td><td id="109"><a href="#109">109</a></td></tr
><tr id="gr_svn27_110"

 onmouseover="gutterOver(110)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',110);">&nbsp;</span
></td><td id="110"><a href="#110">110</a></td></tr
><tr id="gr_svn27_111"

 onmouseover="gutterOver(111)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',111);">&nbsp;</span
></td><td id="111"><a href="#111">111</a></td></tr
><tr id="gr_svn27_112"

 onmouseover="gutterOver(112)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',112);">&nbsp;</span
></td><td id="112"><a href="#112">112</a></td></tr
><tr id="gr_svn27_113"

 onmouseover="gutterOver(113)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',113);">&nbsp;</span
></td><td id="113"><a href="#113">113</a></td></tr
><tr id="gr_svn27_114"

 onmouseover="gutterOver(114)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',114);">&nbsp;</span
></td><td id="114"><a href="#114">114</a></td></tr
><tr id="gr_svn27_115"

 onmouseover="gutterOver(115)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',115);">&nbsp;</span
></td><td id="115"><a href="#115">115</a></td></tr
><tr id="gr_svn27_116"

 onmouseover="gutterOver(116)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',116);">&nbsp;</span
></td><td id="116"><a href="#116">116</a></td></tr
><tr id="gr_svn27_117"

 onmouseover="gutterOver(117)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',117);">&nbsp;</span
></td><td id="117"><a href="#117">117</a></td></tr
><tr id="gr_svn27_118"

 onmouseover="gutterOver(118)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',118);">&nbsp;</span
></td><td id="118"><a href="#118">118</a></td></tr
><tr id="gr_svn27_119"

 onmouseover="gutterOver(119)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',119);">&nbsp;</span
></td><td id="119"><a href="#119">119</a></td></tr
><tr id="gr_svn27_120"

 onmouseover="gutterOver(120)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',120);">&nbsp;</span
></td><td id="120"><a href="#120">120</a></td></tr
><tr id="gr_svn27_121"

 onmouseover="gutterOver(121)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',121);">&nbsp;</span
></td><td id="121"><a href="#121">121</a></td></tr
><tr id="gr_svn27_122"

 onmouseover="gutterOver(122)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',122);">&nbsp;</span
></td><td id="122"><a href="#122">122</a></td></tr
><tr id="gr_svn27_123"

 onmouseover="gutterOver(123)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',123);">&nbsp;</span
></td><td id="123"><a href="#123">123</a></td></tr
><tr id="gr_svn27_124"

 onmouseover="gutterOver(124)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',124);">&nbsp;</span
></td><td id="124"><a href="#124">124</a></td></tr
><tr id="gr_svn27_125"

 onmouseover="gutterOver(125)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',125);">&nbsp;</span
></td><td id="125"><a href="#125">125</a></td></tr
><tr id="gr_svn27_126"

 onmouseover="gutterOver(126)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',126);">&nbsp;</span
></td><td id="126"><a href="#126">126</a></td></tr
><tr id="gr_svn27_127"

 onmouseover="gutterOver(127)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',127);">&nbsp;</span
></td><td id="127"><a href="#127">127</a></td></tr
><tr id="gr_svn27_128"

 onmouseover="gutterOver(128)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',128);">&nbsp;</span
></td><td id="128"><a href="#128">128</a></td></tr
><tr id="gr_svn27_129"

 onmouseover="gutterOver(129)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',129);">&nbsp;</span
></td><td id="129"><a href="#129">129</a></td></tr
><tr id="gr_svn27_130"

 onmouseover="gutterOver(130)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',130);">&nbsp;</span
></td><td id="130"><a href="#130">130</a></td></tr
><tr id="gr_svn27_131"

 onmouseover="gutterOver(131)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',131);">&nbsp;</span
></td><td id="131"><a href="#131">131</a></td></tr
><tr id="gr_svn27_132"

 onmouseover="gutterOver(132)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',132);">&nbsp;</span
></td><td id="132"><a href="#132">132</a></td></tr
><tr id="gr_svn27_133"

 onmouseover="gutterOver(133)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',133);">&nbsp;</span
></td><td id="133"><a href="#133">133</a></td></tr
><tr id="gr_svn27_134"

 onmouseover="gutterOver(134)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',134);">&nbsp;</span
></td><td id="134"><a href="#134">134</a></td></tr
><tr id="gr_svn27_135"

 onmouseover="gutterOver(135)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',135);">&nbsp;</span
></td><td id="135"><a href="#135">135</a></td></tr
><tr id="gr_svn27_136"

 onmouseover="gutterOver(136)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',136);">&nbsp;</span
></td><td id="136"><a href="#136">136</a></td></tr
><tr id="gr_svn27_137"

 onmouseover="gutterOver(137)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',137);">&nbsp;</span
></td><td id="137"><a href="#137">137</a></td></tr
><tr id="gr_svn27_138"

 onmouseover="gutterOver(138)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',138);">&nbsp;</span
></td><td id="138"><a href="#138">138</a></td></tr
><tr id="gr_svn27_139"

 onmouseover="gutterOver(139)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',139);">&nbsp;</span
></td><td id="139"><a href="#139">139</a></td></tr
><tr id="gr_svn27_140"

 onmouseover="gutterOver(140)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',140);">&nbsp;</span
></td><td id="140"><a href="#140">140</a></td></tr
><tr id="gr_svn27_141"

 onmouseover="gutterOver(141)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',141);">&nbsp;</span
></td><td id="141"><a href="#141">141</a></td></tr
><tr id="gr_svn27_142"

 onmouseover="gutterOver(142)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',142);">&nbsp;</span
></td><td id="142"><a href="#142">142</a></td></tr
><tr id="gr_svn27_143"

 onmouseover="gutterOver(143)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',143);">&nbsp;</span
></td><td id="143"><a href="#143">143</a></td></tr
><tr id="gr_svn27_144"

 onmouseover="gutterOver(144)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',144);">&nbsp;</span
></td><td id="144"><a href="#144">144</a></td></tr
><tr id="gr_svn27_145"

 onmouseover="gutterOver(145)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',145);">&nbsp;</span
></td><td id="145"><a href="#145">145</a></td></tr
><tr id="gr_svn27_146"

 onmouseover="gutterOver(146)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',146);">&nbsp;</span
></td><td id="146"><a href="#146">146</a></td></tr
><tr id="gr_svn27_147"

 onmouseover="gutterOver(147)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',147);">&nbsp;</span
></td><td id="147"><a href="#147">147</a></td></tr
><tr id="gr_svn27_148"

 onmouseover="gutterOver(148)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',148);">&nbsp;</span
></td><td id="148"><a href="#148">148</a></td></tr
><tr id="gr_svn27_149"

 onmouseover="gutterOver(149)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',149);">&nbsp;</span
></td><td id="149"><a href="#149">149</a></td></tr
><tr id="gr_svn27_150"

 onmouseover="gutterOver(150)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',150);">&nbsp;</span
></td><td id="150"><a href="#150">150</a></td></tr
><tr id="gr_svn27_151"

 onmouseover="gutterOver(151)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',151);">&nbsp;</span
></td><td id="151"><a href="#151">151</a></td></tr
><tr id="gr_svn27_152"

 onmouseover="gutterOver(152)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',152);">&nbsp;</span
></td><td id="152"><a href="#152">152</a></td></tr
><tr id="gr_svn27_153"

 onmouseover="gutterOver(153)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',153);">&nbsp;</span
></td><td id="153"><a href="#153">153</a></td></tr
><tr id="gr_svn27_154"

 onmouseover="gutterOver(154)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',154);">&nbsp;</span
></td><td id="154"><a href="#154">154</a></td></tr
><tr id="gr_svn27_155"

 onmouseover="gutterOver(155)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',155);">&nbsp;</span
></td><td id="155"><a href="#155">155</a></td></tr
><tr id="gr_svn27_156"

 onmouseover="gutterOver(156)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',156);">&nbsp;</span
></td><td id="156"><a href="#156">156</a></td></tr
><tr id="gr_svn27_157"

 onmouseover="gutterOver(157)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',157);">&nbsp;</span
></td><td id="157"><a href="#157">157</a></td></tr
><tr id="gr_svn27_158"

 onmouseover="gutterOver(158)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',158);">&nbsp;</span
></td><td id="158"><a href="#158">158</a></td></tr
><tr id="gr_svn27_159"

 onmouseover="gutterOver(159)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',159);">&nbsp;</span
></td><td id="159"><a href="#159">159</a></td></tr
><tr id="gr_svn27_160"

 onmouseover="gutterOver(160)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',160);">&nbsp;</span
></td><td id="160"><a href="#160">160</a></td></tr
><tr id="gr_svn27_161"

 onmouseover="gutterOver(161)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',161);">&nbsp;</span
></td><td id="161"><a href="#161">161</a></td></tr
><tr id="gr_svn27_162"

 onmouseover="gutterOver(162)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',162);">&nbsp;</span
></td><td id="162"><a href="#162">162</a></td></tr
><tr id="gr_svn27_163"

 onmouseover="gutterOver(163)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',163);">&nbsp;</span
></td><td id="163"><a href="#163">163</a></td></tr
><tr id="gr_svn27_164"

 onmouseover="gutterOver(164)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',164);">&nbsp;</span
></td><td id="164"><a href="#164">164</a></td></tr
><tr id="gr_svn27_165"

 onmouseover="gutterOver(165)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',165);">&nbsp;</span
></td><td id="165"><a href="#165">165</a></td></tr
><tr id="gr_svn27_166"

 onmouseover="gutterOver(166)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',166);">&nbsp;</span
></td><td id="166"><a href="#166">166</a></td></tr
><tr id="gr_svn27_167"

 onmouseover="gutterOver(167)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',167);">&nbsp;</span
></td><td id="167"><a href="#167">167</a></td></tr
><tr id="gr_svn27_168"

 onmouseover="gutterOver(168)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',168);">&nbsp;</span
></td><td id="168"><a href="#168">168</a></td></tr
><tr id="gr_svn27_169"

 onmouseover="gutterOver(169)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',169);">&nbsp;</span
></td><td id="169"><a href="#169">169</a></td></tr
><tr id="gr_svn27_170"

 onmouseover="gutterOver(170)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',170);">&nbsp;</span
></td><td id="170"><a href="#170">170</a></td></tr
><tr id="gr_svn27_171"

 onmouseover="gutterOver(171)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',171);">&nbsp;</span
></td><td id="171"><a href="#171">171</a></td></tr
><tr id="gr_svn27_172"

 onmouseover="gutterOver(172)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',172);">&nbsp;</span
></td><td id="172"><a href="#172">172</a></td></tr
><tr id="gr_svn27_173"

 onmouseover="gutterOver(173)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',173);">&nbsp;</span
></td><td id="173"><a href="#173">173</a></td></tr
><tr id="gr_svn27_174"

 onmouseover="gutterOver(174)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',174);">&nbsp;</span
></td><td id="174"><a href="#174">174</a></td></tr
><tr id="gr_svn27_175"

 onmouseover="gutterOver(175)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',175);">&nbsp;</span
></td><td id="175"><a href="#175">175</a></td></tr
><tr id="gr_svn27_176"

 onmouseover="gutterOver(176)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',176);">&nbsp;</span
></td><td id="176"><a href="#176">176</a></td></tr
><tr id="gr_svn27_177"

 onmouseover="gutterOver(177)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',177);">&nbsp;</span
></td><td id="177"><a href="#177">177</a></td></tr
><tr id="gr_svn27_178"

 onmouseover="gutterOver(178)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',178);">&nbsp;</span
></td><td id="178"><a href="#178">178</a></td></tr
><tr id="gr_svn27_179"

 onmouseover="gutterOver(179)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',179);">&nbsp;</span
></td><td id="179"><a href="#179">179</a></td></tr
><tr id="gr_svn27_180"

 onmouseover="gutterOver(180)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',180);">&nbsp;</span
></td><td id="180"><a href="#180">180</a></td></tr
><tr id="gr_svn27_181"

 onmouseover="gutterOver(181)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',181);">&nbsp;</span
></td><td id="181"><a href="#181">181</a></td></tr
><tr id="gr_svn27_182"

 onmouseover="gutterOver(182)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',182);">&nbsp;</span
></td><td id="182"><a href="#182">182</a></td></tr
><tr id="gr_svn27_183"

 onmouseover="gutterOver(183)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',183);">&nbsp;</span
></td><td id="183"><a href="#183">183</a></td></tr
><tr id="gr_svn27_184"

 onmouseover="gutterOver(184)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',184);">&nbsp;</span
></td><td id="184"><a href="#184">184</a></td></tr
><tr id="gr_svn27_185"

 onmouseover="gutterOver(185)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',185);">&nbsp;</span
></td><td id="185"><a href="#185">185</a></td></tr
><tr id="gr_svn27_186"

 onmouseover="gutterOver(186)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',186);">&nbsp;</span
></td><td id="186"><a href="#186">186</a></td></tr
><tr id="gr_svn27_187"

 onmouseover="gutterOver(187)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',187);">&nbsp;</span
></td><td id="187"><a href="#187">187</a></td></tr
><tr id="gr_svn27_188"

 onmouseover="gutterOver(188)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',188);">&nbsp;</span
></td><td id="188"><a href="#188">188</a></td></tr
><tr id="gr_svn27_189"

 onmouseover="gutterOver(189)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',189);">&nbsp;</span
></td><td id="189"><a href="#189">189</a></td></tr
><tr id="gr_svn27_190"

 onmouseover="gutterOver(190)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',190);">&nbsp;</span
></td><td id="190"><a href="#190">190</a></td></tr
><tr id="gr_svn27_191"

 onmouseover="gutterOver(191)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',191);">&nbsp;</span
></td><td id="191"><a href="#191">191</a></td></tr
><tr id="gr_svn27_192"

 onmouseover="gutterOver(192)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',192);">&nbsp;</span
></td><td id="192"><a href="#192">192</a></td></tr
><tr id="gr_svn27_193"

 onmouseover="gutterOver(193)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',193);">&nbsp;</span
></td><td id="193"><a href="#193">193</a></td></tr
><tr id="gr_svn27_194"

 onmouseover="gutterOver(194)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',194);">&nbsp;</span
></td><td id="194"><a href="#194">194</a></td></tr
><tr id="gr_svn27_195"

 onmouseover="gutterOver(195)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',195);">&nbsp;</span
></td><td id="195"><a href="#195">195</a></td></tr
><tr id="gr_svn27_196"

 onmouseover="gutterOver(196)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',196);">&nbsp;</span
></td><td id="196"><a href="#196">196</a></td></tr
><tr id="gr_svn27_197"

 onmouseover="gutterOver(197)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',197);">&nbsp;</span
></td><td id="197"><a href="#197">197</a></td></tr
><tr id="gr_svn27_198"

 onmouseover="gutterOver(198)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',198);">&nbsp;</span
></td><td id="198"><a href="#198">198</a></td></tr
><tr id="gr_svn27_199"

 onmouseover="gutterOver(199)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',199);">&nbsp;</span
></td><td id="199"><a href="#199">199</a></td></tr
><tr id="gr_svn27_200"

 onmouseover="gutterOver(200)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',200);">&nbsp;</span
></td><td id="200"><a href="#200">200</a></td></tr
><tr id="gr_svn27_201"

 onmouseover="gutterOver(201)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',201);">&nbsp;</span
></td><td id="201"><a href="#201">201</a></td></tr
><tr id="gr_svn27_202"

 onmouseover="gutterOver(202)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',202);">&nbsp;</span
></td><td id="202"><a href="#202">202</a></td></tr
><tr id="gr_svn27_203"

 onmouseover="gutterOver(203)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',203);">&nbsp;</span
></td><td id="203"><a href="#203">203</a></td></tr
><tr id="gr_svn27_204"

 onmouseover="gutterOver(204)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',204);">&nbsp;</span
></td><td id="204"><a href="#204">204</a></td></tr
><tr id="gr_svn27_205"

 onmouseover="gutterOver(205)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',205);">&nbsp;</span
></td><td id="205"><a href="#205">205</a></td></tr
><tr id="gr_svn27_206"

 onmouseover="gutterOver(206)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',206);">&nbsp;</span
></td><td id="206"><a href="#206">206</a></td></tr
><tr id="gr_svn27_207"

 onmouseover="gutterOver(207)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',207);">&nbsp;</span
></td><td id="207"><a href="#207">207</a></td></tr
><tr id="gr_svn27_208"

 onmouseover="gutterOver(208)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',208);">&nbsp;</span
></td><td id="208"><a href="#208">208</a></td></tr
><tr id="gr_svn27_209"

 onmouseover="gutterOver(209)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',209);">&nbsp;</span
></td><td id="209"><a href="#209">209</a></td></tr
><tr id="gr_svn27_210"

 onmouseover="gutterOver(210)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',210);">&nbsp;</span
></td><td id="210"><a href="#210">210</a></td></tr
><tr id="gr_svn27_211"

 onmouseover="gutterOver(211)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',211);">&nbsp;</span
></td><td id="211"><a href="#211">211</a></td></tr
><tr id="gr_svn27_212"

 onmouseover="gutterOver(212)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',212);">&nbsp;</span
></td><td id="212"><a href="#212">212</a></td></tr
><tr id="gr_svn27_213"

 onmouseover="gutterOver(213)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',213);">&nbsp;</span
></td><td id="213"><a href="#213">213</a></td></tr
><tr id="gr_svn27_214"

 onmouseover="gutterOver(214)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',214);">&nbsp;</span
></td><td id="214"><a href="#214">214</a></td></tr
><tr id="gr_svn27_215"

 onmouseover="gutterOver(215)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',215);">&nbsp;</span
></td><td id="215"><a href="#215">215</a></td></tr
><tr id="gr_svn27_216"

 onmouseover="gutterOver(216)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',216);">&nbsp;</span
></td><td id="216"><a href="#216">216</a></td></tr
><tr id="gr_svn27_217"

 onmouseover="gutterOver(217)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',217);">&nbsp;</span
></td><td id="217"><a href="#217">217</a></td></tr
><tr id="gr_svn27_218"

 onmouseover="gutterOver(218)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',218);">&nbsp;</span
></td><td id="218"><a href="#218">218</a></td></tr
><tr id="gr_svn27_219"

 onmouseover="gutterOver(219)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',219);">&nbsp;</span
></td><td id="219"><a href="#219">219</a></td></tr
><tr id="gr_svn27_220"

 onmouseover="gutterOver(220)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',220);">&nbsp;</span
></td><td id="220"><a href="#220">220</a></td></tr
><tr id="gr_svn27_221"

 onmouseover="gutterOver(221)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',221);">&nbsp;</span
></td><td id="221"><a href="#221">221</a></td></tr
><tr id="gr_svn27_222"

 onmouseover="gutterOver(222)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',222);">&nbsp;</span
></td><td id="222"><a href="#222">222</a></td></tr
><tr id="gr_svn27_223"

 onmouseover="gutterOver(223)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',223);">&nbsp;</span
></td><td id="223"><a href="#223">223</a></td></tr
><tr id="gr_svn27_224"

 onmouseover="gutterOver(224)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',224);">&nbsp;</span
></td><td id="224"><a href="#224">224</a></td></tr
><tr id="gr_svn27_225"

 onmouseover="gutterOver(225)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',225);">&nbsp;</span
></td><td id="225"><a href="#225">225</a></td></tr
><tr id="gr_svn27_226"

 onmouseover="gutterOver(226)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',226);">&nbsp;</span
></td><td id="226"><a href="#226">226</a></td></tr
><tr id="gr_svn27_227"

 onmouseover="gutterOver(227)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',227);">&nbsp;</span
></td><td id="227"><a href="#227">227</a></td></tr
><tr id="gr_svn27_228"

 onmouseover="gutterOver(228)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',228);">&nbsp;</span
></td><td id="228"><a href="#228">228</a></td></tr
><tr id="gr_svn27_229"

 onmouseover="gutterOver(229)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',229);">&nbsp;</span
></td><td id="229"><a href="#229">229</a></td></tr
><tr id="gr_svn27_230"

 onmouseover="gutterOver(230)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',230);">&nbsp;</span
></td><td id="230"><a href="#230">230</a></td></tr
><tr id="gr_svn27_231"

 onmouseover="gutterOver(231)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',231);">&nbsp;</span
></td><td id="231"><a href="#231">231</a></td></tr
><tr id="gr_svn27_232"

 onmouseover="gutterOver(232)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',232);">&nbsp;</span
></td><td id="232"><a href="#232">232</a></td></tr
><tr id="gr_svn27_233"

 onmouseover="gutterOver(233)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',233);">&nbsp;</span
></td><td id="233"><a href="#233">233</a></td></tr
><tr id="gr_svn27_234"

 onmouseover="gutterOver(234)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',234);">&nbsp;</span
></td><td id="234"><a href="#234">234</a></td></tr
><tr id="gr_svn27_235"

 onmouseover="gutterOver(235)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',235);">&nbsp;</span
></td><td id="235"><a href="#235">235</a></td></tr
><tr id="gr_svn27_236"

 onmouseover="gutterOver(236)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',236);">&nbsp;</span
></td><td id="236"><a href="#236">236</a></td></tr
><tr id="gr_svn27_237"

 onmouseover="gutterOver(237)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',237);">&nbsp;</span
></td><td id="237"><a href="#237">237</a></td></tr
><tr id="gr_svn27_238"

 onmouseover="gutterOver(238)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',238);">&nbsp;</span
></td><td id="238"><a href="#238">238</a></td></tr
><tr id="gr_svn27_239"

 onmouseover="gutterOver(239)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',239);">&nbsp;</span
></td><td id="239"><a href="#239">239</a></td></tr
><tr id="gr_svn27_240"

 onmouseover="gutterOver(240)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',240);">&nbsp;</span
></td><td id="240"><a href="#240">240</a></td></tr
><tr id="gr_svn27_241"

 onmouseover="gutterOver(241)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',241);">&nbsp;</span
></td><td id="241"><a href="#241">241</a></td></tr
><tr id="gr_svn27_242"

 onmouseover="gutterOver(242)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',242);">&nbsp;</span
></td><td id="242"><a href="#242">242</a></td></tr
><tr id="gr_svn27_243"

 onmouseover="gutterOver(243)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',243);">&nbsp;</span
></td><td id="243"><a href="#243">243</a></td></tr
><tr id="gr_svn27_244"

 onmouseover="gutterOver(244)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',244);">&nbsp;</span
></td><td id="244"><a href="#244">244</a></td></tr
><tr id="gr_svn27_245"

 onmouseover="gutterOver(245)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',245);">&nbsp;</span
></td><td id="245"><a href="#245">245</a></td></tr
><tr id="gr_svn27_246"

 onmouseover="gutterOver(246)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',246);">&nbsp;</span
></td><td id="246"><a href="#246">246</a></td></tr
><tr id="gr_svn27_247"

 onmouseover="gutterOver(247)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',247);">&nbsp;</span
></td><td id="247"><a href="#247">247</a></td></tr
><tr id="gr_svn27_248"

 onmouseover="gutterOver(248)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',248);">&nbsp;</span
></td><td id="248"><a href="#248">248</a></td></tr
><tr id="gr_svn27_249"

 onmouseover="gutterOver(249)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',249);">&nbsp;</span
></td><td id="249"><a href="#249">249</a></td></tr
><tr id="gr_svn27_250"

 onmouseover="gutterOver(250)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',250);">&nbsp;</span
></td><td id="250"><a href="#250">250</a></td></tr
><tr id="gr_svn27_251"

 onmouseover="gutterOver(251)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',251);">&nbsp;</span
></td><td id="251"><a href="#251">251</a></td></tr
><tr id="gr_svn27_252"

 onmouseover="gutterOver(252)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',252);">&nbsp;</span
></td><td id="252"><a href="#252">252</a></td></tr
><tr id="gr_svn27_253"

 onmouseover="gutterOver(253)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',253);">&nbsp;</span
></td><td id="253"><a href="#253">253</a></td></tr
><tr id="gr_svn27_254"

 onmouseover="gutterOver(254)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',254);">&nbsp;</span
></td><td id="254"><a href="#254">254</a></td></tr
><tr id="gr_svn27_255"

 onmouseover="gutterOver(255)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',255);">&nbsp;</span
></td><td id="255"><a href="#255">255</a></td></tr
><tr id="gr_svn27_256"

 onmouseover="gutterOver(256)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',256);">&nbsp;</span
></td><td id="256"><a href="#256">256</a></td></tr
><tr id="gr_svn27_257"

 onmouseover="gutterOver(257)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',257);">&nbsp;</span
></td><td id="257"><a href="#257">257</a></td></tr
><tr id="gr_svn27_258"

 onmouseover="gutterOver(258)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',258);">&nbsp;</span
></td><td id="258"><a href="#258">258</a></td></tr
><tr id="gr_svn27_259"

 onmouseover="gutterOver(259)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',259);">&nbsp;</span
></td><td id="259"><a href="#259">259</a></td></tr
><tr id="gr_svn27_260"

 onmouseover="gutterOver(260)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',260);">&nbsp;</span
></td><td id="260"><a href="#260">260</a></td></tr
><tr id="gr_svn27_261"

 onmouseover="gutterOver(261)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',261);">&nbsp;</span
></td><td id="261"><a href="#261">261</a></td></tr
><tr id="gr_svn27_262"

 onmouseover="gutterOver(262)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',262);">&nbsp;</span
></td><td id="262"><a href="#262">262</a></td></tr
><tr id="gr_svn27_263"

 onmouseover="gutterOver(263)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',263);">&nbsp;</span
></td><td id="263"><a href="#263">263</a></td></tr
><tr id="gr_svn27_264"

 onmouseover="gutterOver(264)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',264);">&nbsp;</span
></td><td id="264"><a href="#264">264</a></td></tr
><tr id="gr_svn27_265"

 onmouseover="gutterOver(265)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',265);">&nbsp;</span
></td><td id="265"><a href="#265">265</a></td></tr
><tr id="gr_svn27_266"

 onmouseover="gutterOver(266)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',266);">&nbsp;</span
></td><td id="266"><a href="#266">266</a></td></tr
><tr id="gr_svn27_267"

 onmouseover="gutterOver(267)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',267);">&nbsp;</span
></td><td id="267"><a href="#267">267</a></td></tr
><tr id="gr_svn27_268"

 onmouseover="gutterOver(268)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',268);">&nbsp;</span
></td><td id="268"><a href="#268">268</a></td></tr
><tr id="gr_svn27_269"

 onmouseover="gutterOver(269)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',269);">&nbsp;</span
></td><td id="269"><a href="#269">269</a></td></tr
><tr id="gr_svn27_270"

 onmouseover="gutterOver(270)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',270);">&nbsp;</span
></td><td id="270"><a href="#270">270</a></td></tr
><tr id="gr_svn27_271"

 onmouseover="gutterOver(271)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',271);">&nbsp;</span
></td><td id="271"><a href="#271">271</a></td></tr
><tr id="gr_svn27_272"

 onmouseover="gutterOver(272)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',272);">&nbsp;</span
></td><td id="272"><a href="#272">272</a></td></tr
><tr id="gr_svn27_273"

 onmouseover="gutterOver(273)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',273);">&nbsp;</span
></td><td id="273"><a href="#273">273</a></td></tr
><tr id="gr_svn27_274"

 onmouseover="gutterOver(274)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',274);">&nbsp;</span
></td><td id="274"><a href="#274">274</a></td></tr
><tr id="gr_svn27_275"

 onmouseover="gutterOver(275)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',275);">&nbsp;</span
></td><td id="275"><a href="#275">275</a></td></tr
><tr id="gr_svn27_276"

 onmouseover="gutterOver(276)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',276);">&nbsp;</span
></td><td id="276"><a href="#276">276</a></td></tr
><tr id="gr_svn27_277"

 onmouseover="gutterOver(277)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',277);">&nbsp;</span
></td><td id="277"><a href="#277">277</a></td></tr
><tr id="gr_svn27_278"

 onmouseover="gutterOver(278)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',278);">&nbsp;</span
></td><td id="278"><a href="#278">278</a></td></tr
><tr id="gr_svn27_279"

 onmouseover="gutterOver(279)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',279);">&nbsp;</span
></td><td id="279"><a href="#279">279</a></td></tr
><tr id="gr_svn27_280"

 onmouseover="gutterOver(280)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',280);">&nbsp;</span
></td><td id="280"><a href="#280">280</a></td></tr
><tr id="gr_svn27_281"

 onmouseover="gutterOver(281)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',281);">&nbsp;</span
></td><td id="281"><a href="#281">281</a></td></tr
><tr id="gr_svn27_282"

 onmouseover="gutterOver(282)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',282);">&nbsp;</span
></td><td id="282"><a href="#282">282</a></td></tr
><tr id="gr_svn27_283"

 onmouseover="gutterOver(283)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',283);">&nbsp;</span
></td><td id="283"><a href="#283">283</a></td></tr
><tr id="gr_svn27_284"

 onmouseover="gutterOver(284)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',284);">&nbsp;</span
></td><td id="284"><a href="#284">284</a></td></tr
><tr id="gr_svn27_285"

 onmouseover="gutterOver(285)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',285);">&nbsp;</span
></td><td id="285"><a href="#285">285</a></td></tr
><tr id="gr_svn27_286"

 onmouseover="gutterOver(286)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',286);">&nbsp;</span
></td><td id="286"><a href="#286">286</a></td></tr
><tr id="gr_svn27_287"

 onmouseover="gutterOver(287)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',287);">&nbsp;</span
></td><td id="287"><a href="#287">287</a></td></tr
><tr id="gr_svn27_288"

 onmouseover="gutterOver(288)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',288);">&nbsp;</span
></td><td id="288"><a href="#288">288</a></td></tr
><tr id="gr_svn27_289"

 onmouseover="gutterOver(289)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',289);">&nbsp;</span
></td><td id="289"><a href="#289">289</a></td></tr
><tr id="gr_svn27_290"

 onmouseover="gutterOver(290)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',290);">&nbsp;</span
></td><td id="290"><a href="#290">290</a></td></tr
><tr id="gr_svn27_291"

 onmouseover="gutterOver(291)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',291);">&nbsp;</span
></td><td id="291"><a href="#291">291</a></td></tr
><tr id="gr_svn27_292"

 onmouseover="gutterOver(292)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',292);">&nbsp;</span
></td><td id="292"><a href="#292">292</a></td></tr
><tr id="gr_svn27_293"

 onmouseover="gutterOver(293)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',293);">&nbsp;</span
></td><td id="293"><a href="#293">293</a></td></tr
><tr id="gr_svn27_294"

 onmouseover="gutterOver(294)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',294);">&nbsp;</span
></td><td id="294"><a href="#294">294</a></td></tr
><tr id="gr_svn27_295"

 onmouseover="gutterOver(295)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',295);">&nbsp;</span
></td><td id="295"><a href="#295">295</a></td></tr
><tr id="gr_svn27_296"

 onmouseover="gutterOver(296)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',296);">&nbsp;</span
></td><td id="296"><a href="#296">296</a></td></tr
><tr id="gr_svn27_297"

 onmouseover="gutterOver(297)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',297);">&nbsp;</span
></td><td id="297"><a href="#297">297</a></td></tr
><tr id="gr_svn27_298"

 onmouseover="gutterOver(298)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',298);">&nbsp;</span
></td><td id="298"><a href="#298">298</a></td></tr
><tr id="gr_svn27_299"

 onmouseover="gutterOver(299)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',299);">&nbsp;</span
></td><td id="299"><a href="#299">299</a></td></tr
><tr id="gr_svn27_300"

 onmouseover="gutterOver(300)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',300);">&nbsp;</span
></td><td id="300"><a href="#300">300</a></td></tr
><tr id="gr_svn27_301"

 onmouseover="gutterOver(301)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',301);">&nbsp;</span
></td><td id="301"><a href="#301">301</a></td></tr
><tr id="gr_svn27_302"

 onmouseover="gutterOver(302)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',302);">&nbsp;</span
></td><td id="302"><a href="#302">302</a></td></tr
><tr id="gr_svn27_303"

 onmouseover="gutterOver(303)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',303);">&nbsp;</span
></td><td id="303"><a href="#303">303</a></td></tr
><tr id="gr_svn27_304"

 onmouseover="gutterOver(304)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',304);">&nbsp;</span
></td><td id="304"><a href="#304">304</a></td></tr
><tr id="gr_svn27_305"

 onmouseover="gutterOver(305)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',305);">&nbsp;</span
></td><td id="305"><a href="#305">305</a></td></tr
><tr id="gr_svn27_306"

 onmouseover="gutterOver(306)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',306);">&nbsp;</span
></td><td id="306"><a href="#306">306</a></td></tr
><tr id="gr_svn27_307"

 onmouseover="gutterOver(307)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',307);">&nbsp;</span
></td><td id="307"><a href="#307">307</a></td></tr
><tr id="gr_svn27_308"

 onmouseover="gutterOver(308)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',308);">&nbsp;</span
></td><td id="308"><a href="#308">308</a></td></tr
><tr id="gr_svn27_309"

 onmouseover="gutterOver(309)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',309);">&nbsp;</span
></td><td id="309"><a href="#309">309</a></td></tr
><tr id="gr_svn27_310"

 onmouseover="gutterOver(310)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',310);">&nbsp;</span
></td><td id="310"><a href="#310">310</a></td></tr
><tr id="gr_svn27_311"

 onmouseover="gutterOver(311)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',311);">&nbsp;</span
></td><td id="311"><a href="#311">311</a></td></tr
><tr id="gr_svn27_312"

 onmouseover="gutterOver(312)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',312);">&nbsp;</span
></td><td id="312"><a href="#312">312</a></td></tr
><tr id="gr_svn27_313"

 onmouseover="gutterOver(313)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',313);">&nbsp;</span
></td><td id="313"><a href="#313">313</a></td></tr
><tr id="gr_svn27_314"

 onmouseover="gutterOver(314)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',314);">&nbsp;</span
></td><td id="314"><a href="#314">314</a></td></tr
><tr id="gr_svn27_315"

 onmouseover="gutterOver(315)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',315);">&nbsp;</span
></td><td id="315"><a href="#315">315</a></td></tr
><tr id="gr_svn27_316"

 onmouseover="gutterOver(316)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',316);">&nbsp;</span
></td><td id="316"><a href="#316">316</a></td></tr
><tr id="gr_svn27_317"

 onmouseover="gutterOver(317)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',317);">&nbsp;</span
></td><td id="317"><a href="#317">317</a></td></tr
><tr id="gr_svn27_318"

 onmouseover="gutterOver(318)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',318);">&nbsp;</span
></td><td id="318"><a href="#318">318</a></td></tr
><tr id="gr_svn27_319"

 onmouseover="gutterOver(319)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',319);">&nbsp;</span
></td><td id="319"><a href="#319">319</a></td></tr
><tr id="gr_svn27_320"

 onmouseover="gutterOver(320)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',320);">&nbsp;</span
></td><td id="320"><a href="#320">320</a></td></tr
><tr id="gr_svn27_321"

 onmouseover="gutterOver(321)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',321);">&nbsp;</span
></td><td id="321"><a href="#321">321</a></td></tr
><tr id="gr_svn27_322"

 onmouseover="gutterOver(322)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',322);">&nbsp;</span
></td><td id="322"><a href="#322">322</a></td></tr
><tr id="gr_svn27_323"

 onmouseover="gutterOver(323)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',323);">&nbsp;</span
></td><td id="323"><a href="#323">323</a></td></tr
><tr id="gr_svn27_324"

 onmouseover="gutterOver(324)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',324);">&nbsp;</span
></td><td id="324"><a href="#324">324</a></td></tr
><tr id="gr_svn27_325"

 onmouseover="gutterOver(325)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',325);">&nbsp;</span
></td><td id="325"><a href="#325">325</a></td></tr
><tr id="gr_svn27_326"

 onmouseover="gutterOver(326)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',326);">&nbsp;</span
></td><td id="326"><a href="#326">326</a></td></tr
><tr id="gr_svn27_327"

 onmouseover="gutterOver(327)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',327);">&nbsp;</span
></td><td id="327"><a href="#327">327</a></td></tr
><tr id="gr_svn27_328"

 onmouseover="gutterOver(328)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',328);">&nbsp;</span
></td><td id="328"><a href="#328">328</a></td></tr
><tr id="gr_svn27_329"

 onmouseover="gutterOver(329)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',329);">&nbsp;</span
></td><td id="329"><a href="#329">329</a></td></tr
><tr id="gr_svn27_330"

 onmouseover="gutterOver(330)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',330);">&nbsp;</span
></td><td id="330"><a href="#330">330</a></td></tr
><tr id="gr_svn27_331"

 onmouseover="gutterOver(331)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',331);">&nbsp;</span
></td><td id="331"><a href="#331">331</a></td></tr
><tr id="gr_svn27_332"

 onmouseover="gutterOver(332)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',332);">&nbsp;</span
></td><td id="332"><a href="#332">332</a></td></tr
><tr id="gr_svn27_333"

 onmouseover="gutterOver(333)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',333);">&nbsp;</span
></td><td id="333"><a href="#333">333</a></td></tr
><tr id="gr_svn27_334"

 onmouseover="gutterOver(334)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',334);">&nbsp;</span
></td><td id="334"><a href="#334">334</a></td></tr
><tr id="gr_svn27_335"

 onmouseover="gutterOver(335)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',335);">&nbsp;</span
></td><td id="335"><a href="#335">335</a></td></tr
><tr id="gr_svn27_336"

 onmouseover="gutterOver(336)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',336);">&nbsp;</span
></td><td id="336"><a href="#336">336</a></td></tr
><tr id="gr_svn27_337"

 onmouseover="gutterOver(337)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',337);">&nbsp;</span
></td><td id="337"><a href="#337">337</a></td></tr
><tr id="gr_svn27_338"

 onmouseover="gutterOver(338)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',338);">&nbsp;</span
></td><td id="338"><a href="#338">338</a></td></tr
><tr id="gr_svn27_339"

 onmouseover="gutterOver(339)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',339);">&nbsp;</span
></td><td id="339"><a href="#339">339</a></td></tr
><tr id="gr_svn27_340"

 onmouseover="gutterOver(340)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',340);">&nbsp;</span
></td><td id="340"><a href="#340">340</a></td></tr
><tr id="gr_svn27_341"

 onmouseover="gutterOver(341)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',341);">&nbsp;</span
></td><td id="341"><a href="#341">341</a></td></tr
><tr id="gr_svn27_342"

 onmouseover="gutterOver(342)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',342);">&nbsp;</span
></td><td id="342"><a href="#342">342</a></td></tr
><tr id="gr_svn27_343"

 onmouseover="gutterOver(343)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',343);">&nbsp;</span
></td><td id="343"><a href="#343">343</a></td></tr
><tr id="gr_svn27_344"

 onmouseover="gutterOver(344)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',344);">&nbsp;</span
></td><td id="344"><a href="#344">344</a></td></tr
><tr id="gr_svn27_345"

 onmouseover="gutterOver(345)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',345);">&nbsp;</span
></td><td id="345"><a href="#345">345</a></td></tr
><tr id="gr_svn27_346"

 onmouseover="gutterOver(346)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',346);">&nbsp;</span
></td><td id="346"><a href="#346">346</a></td></tr
><tr id="gr_svn27_347"

 onmouseover="gutterOver(347)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',347);">&nbsp;</span
></td><td id="347"><a href="#347">347</a></td></tr
><tr id="gr_svn27_348"

 onmouseover="gutterOver(348)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',348);">&nbsp;</span
></td><td id="348"><a href="#348">348</a></td></tr
><tr id="gr_svn27_349"

 onmouseover="gutterOver(349)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',349);">&nbsp;</span
></td><td id="349"><a href="#349">349</a></td></tr
><tr id="gr_svn27_350"

 onmouseover="gutterOver(350)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',350);">&nbsp;</span
></td><td id="350"><a href="#350">350</a></td></tr
><tr id="gr_svn27_351"

 onmouseover="gutterOver(351)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',351);">&nbsp;</span
></td><td id="351"><a href="#351">351</a></td></tr
><tr id="gr_svn27_352"

 onmouseover="gutterOver(352)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',352);">&nbsp;</span
></td><td id="352"><a href="#352">352</a></td></tr
><tr id="gr_svn27_353"

 onmouseover="gutterOver(353)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',353);">&nbsp;</span
></td><td id="353"><a href="#353">353</a></td></tr
><tr id="gr_svn27_354"

 onmouseover="gutterOver(354)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',354);">&nbsp;</span
></td><td id="354"><a href="#354">354</a></td></tr
><tr id="gr_svn27_355"

 onmouseover="gutterOver(355)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',355);">&nbsp;</span
></td><td id="355"><a href="#355">355</a></td></tr
><tr id="gr_svn27_356"

 onmouseover="gutterOver(356)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',356);">&nbsp;</span
></td><td id="356"><a href="#356">356</a></td></tr
><tr id="gr_svn27_357"

 onmouseover="gutterOver(357)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',357);">&nbsp;</span
></td><td id="357"><a href="#357">357</a></td></tr
><tr id="gr_svn27_358"

 onmouseover="gutterOver(358)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',358);">&nbsp;</span
></td><td id="358"><a href="#358">358</a></td></tr
><tr id="gr_svn27_359"

 onmouseover="gutterOver(359)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',359);">&nbsp;</span
></td><td id="359"><a href="#359">359</a></td></tr
><tr id="gr_svn27_360"

 onmouseover="gutterOver(360)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',360);">&nbsp;</span
></td><td id="360"><a href="#360">360</a></td></tr
><tr id="gr_svn27_361"

 onmouseover="gutterOver(361)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',361);">&nbsp;</span
></td><td id="361"><a href="#361">361</a></td></tr
><tr id="gr_svn27_362"

 onmouseover="gutterOver(362)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',362);">&nbsp;</span
></td><td id="362"><a href="#362">362</a></td></tr
><tr id="gr_svn27_363"

 onmouseover="gutterOver(363)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',363);">&nbsp;</span
></td><td id="363"><a href="#363">363</a></td></tr
><tr id="gr_svn27_364"

 onmouseover="gutterOver(364)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',364);">&nbsp;</span
></td><td id="364"><a href="#364">364</a></td></tr
><tr id="gr_svn27_365"

 onmouseover="gutterOver(365)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',365);">&nbsp;</span
></td><td id="365"><a href="#365">365</a></td></tr
><tr id="gr_svn27_366"

 onmouseover="gutterOver(366)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',366);">&nbsp;</span
></td><td id="366"><a href="#366">366</a></td></tr
><tr id="gr_svn27_367"

 onmouseover="gutterOver(367)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',367);">&nbsp;</span
></td><td id="367"><a href="#367">367</a></td></tr
><tr id="gr_svn27_368"

 onmouseover="gutterOver(368)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',368);">&nbsp;</span
></td><td id="368"><a href="#368">368</a></td></tr
><tr id="gr_svn27_369"

 onmouseover="gutterOver(369)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',369);">&nbsp;</span
></td><td id="369"><a href="#369">369</a></td></tr
><tr id="gr_svn27_370"

 onmouseover="gutterOver(370)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',370);">&nbsp;</span
></td><td id="370"><a href="#370">370</a></td></tr
><tr id="gr_svn27_371"

 onmouseover="gutterOver(371)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',371);">&nbsp;</span
></td><td id="371"><a href="#371">371</a></td></tr
><tr id="gr_svn27_372"

 onmouseover="gutterOver(372)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',372);">&nbsp;</span
></td><td id="372"><a href="#372">372</a></td></tr
><tr id="gr_svn27_373"

 onmouseover="gutterOver(373)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',373);">&nbsp;</span
></td><td id="373"><a href="#373">373</a></td></tr
><tr id="gr_svn27_374"

 onmouseover="gutterOver(374)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',374);">&nbsp;</span
></td><td id="374"><a href="#374">374</a></td></tr
><tr id="gr_svn27_375"

 onmouseover="gutterOver(375)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',375);">&nbsp;</span
></td><td id="375"><a href="#375">375</a></td></tr
><tr id="gr_svn27_376"

 onmouseover="gutterOver(376)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',376);">&nbsp;</span
></td><td id="376"><a href="#376">376</a></td></tr
><tr id="gr_svn27_377"

 onmouseover="gutterOver(377)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',377);">&nbsp;</span
></td><td id="377"><a href="#377">377</a></td></tr
><tr id="gr_svn27_378"

 onmouseover="gutterOver(378)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',378);">&nbsp;</span
></td><td id="378"><a href="#378">378</a></td></tr
><tr id="gr_svn27_379"

 onmouseover="gutterOver(379)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',379);">&nbsp;</span
></td><td id="379"><a href="#379">379</a></td></tr
><tr id="gr_svn27_380"

 onmouseover="gutterOver(380)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',380);">&nbsp;</span
></td><td id="380"><a href="#380">380</a></td></tr
><tr id="gr_svn27_381"

 onmouseover="gutterOver(381)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',381);">&nbsp;</span
></td><td id="381"><a href="#381">381</a></td></tr
><tr id="gr_svn27_382"

 onmouseover="gutterOver(382)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',382);">&nbsp;</span
></td><td id="382"><a href="#382">382</a></td></tr
><tr id="gr_svn27_383"

 onmouseover="gutterOver(383)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',383);">&nbsp;</span
></td><td id="383"><a href="#383">383</a></td></tr
><tr id="gr_svn27_384"

 onmouseover="gutterOver(384)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',384);">&nbsp;</span
></td><td id="384"><a href="#384">384</a></td></tr
><tr id="gr_svn27_385"

 onmouseover="gutterOver(385)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',385);">&nbsp;</span
></td><td id="385"><a href="#385">385</a></td></tr
><tr id="gr_svn27_386"

 onmouseover="gutterOver(386)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',386);">&nbsp;</span
></td><td id="386"><a href="#386">386</a></td></tr
><tr id="gr_svn27_387"

 onmouseover="gutterOver(387)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',387);">&nbsp;</span
></td><td id="387"><a href="#387">387</a></td></tr
><tr id="gr_svn27_388"

 onmouseover="gutterOver(388)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',388);">&nbsp;</span
></td><td id="388"><a href="#388">388</a></td></tr
><tr id="gr_svn27_389"

 onmouseover="gutterOver(389)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',389);">&nbsp;</span
></td><td id="389"><a href="#389">389</a></td></tr
><tr id="gr_svn27_390"

 onmouseover="gutterOver(390)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',390);">&nbsp;</span
></td><td id="390"><a href="#390">390</a></td></tr
><tr id="gr_svn27_391"

 onmouseover="gutterOver(391)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',391);">&nbsp;</span
></td><td id="391"><a href="#391">391</a></td></tr
><tr id="gr_svn27_392"

 onmouseover="gutterOver(392)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',392);">&nbsp;</span
></td><td id="392"><a href="#392">392</a></td></tr
><tr id="gr_svn27_393"

 onmouseover="gutterOver(393)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',393);">&nbsp;</span
></td><td id="393"><a href="#393">393</a></td></tr
><tr id="gr_svn27_394"

 onmouseover="gutterOver(394)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',394);">&nbsp;</span
></td><td id="394"><a href="#394">394</a></td></tr
><tr id="gr_svn27_395"

 onmouseover="gutterOver(395)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',395);">&nbsp;</span
></td><td id="395"><a href="#395">395</a></td></tr
><tr id="gr_svn27_396"

 onmouseover="gutterOver(396)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',396);">&nbsp;</span
></td><td id="396"><a href="#396">396</a></td></tr
><tr id="gr_svn27_397"

 onmouseover="gutterOver(397)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',397);">&nbsp;</span
></td><td id="397"><a href="#397">397</a></td></tr
><tr id="gr_svn27_398"

 onmouseover="gutterOver(398)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',398);">&nbsp;</span
></td><td id="398"><a href="#398">398</a></td></tr
><tr id="gr_svn27_399"

 onmouseover="gutterOver(399)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',399);">&nbsp;</span
></td><td id="399"><a href="#399">399</a></td></tr
><tr id="gr_svn27_400"

 onmouseover="gutterOver(400)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',400);">&nbsp;</span
></td><td id="400"><a href="#400">400</a></td></tr
><tr id="gr_svn27_401"

 onmouseover="gutterOver(401)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',401);">&nbsp;</span
></td><td id="401"><a href="#401">401</a></td></tr
><tr id="gr_svn27_402"

 onmouseover="gutterOver(402)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',402);">&nbsp;</span
></td><td id="402"><a href="#402">402</a></td></tr
><tr id="gr_svn27_403"

 onmouseover="gutterOver(403)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',403);">&nbsp;</span
></td><td id="403"><a href="#403">403</a></td></tr
><tr id="gr_svn27_404"

 onmouseover="gutterOver(404)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',404);">&nbsp;</span
></td><td id="404"><a href="#404">404</a></td></tr
><tr id="gr_svn27_405"

 onmouseover="gutterOver(405)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',405);">&nbsp;</span
></td><td id="405"><a href="#405">405</a></td></tr
><tr id="gr_svn27_406"

 onmouseover="gutterOver(406)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',406);">&nbsp;</span
></td><td id="406"><a href="#406">406</a></td></tr
><tr id="gr_svn27_407"

 onmouseover="gutterOver(407)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',407);">&nbsp;</span
></td><td id="407"><a href="#407">407</a></td></tr
><tr id="gr_svn27_408"

 onmouseover="gutterOver(408)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',408);">&nbsp;</span
></td><td id="408"><a href="#408">408</a></td></tr
><tr id="gr_svn27_409"

 onmouseover="gutterOver(409)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',409);">&nbsp;</span
></td><td id="409"><a href="#409">409</a></td></tr
><tr id="gr_svn27_410"

 onmouseover="gutterOver(410)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',410);">&nbsp;</span
></td><td id="410"><a href="#410">410</a></td></tr
><tr id="gr_svn27_411"

 onmouseover="gutterOver(411)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',411);">&nbsp;</span
></td><td id="411"><a href="#411">411</a></td></tr
><tr id="gr_svn27_412"

 onmouseover="gutterOver(412)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',412);">&nbsp;</span
></td><td id="412"><a href="#412">412</a></td></tr
><tr id="gr_svn27_413"

 onmouseover="gutterOver(413)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',413);">&nbsp;</span
></td><td id="413"><a href="#413">413</a></td></tr
><tr id="gr_svn27_414"

 onmouseover="gutterOver(414)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',414);">&nbsp;</span
></td><td id="414"><a href="#414">414</a></td></tr
><tr id="gr_svn27_415"

 onmouseover="gutterOver(415)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',415);">&nbsp;</span
></td><td id="415"><a href="#415">415</a></td></tr
><tr id="gr_svn27_416"

 onmouseover="gutterOver(416)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',416);">&nbsp;</span
></td><td id="416"><a href="#416">416</a></td></tr
><tr id="gr_svn27_417"

 onmouseover="gutterOver(417)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',417);">&nbsp;</span
></td><td id="417"><a href="#417">417</a></td></tr
><tr id="gr_svn27_418"

 onmouseover="gutterOver(418)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',418);">&nbsp;</span
></td><td id="418"><a href="#418">418</a></td></tr
><tr id="gr_svn27_419"

 onmouseover="gutterOver(419)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',419);">&nbsp;</span
></td><td id="419"><a href="#419">419</a></td></tr
><tr id="gr_svn27_420"

 onmouseover="gutterOver(420)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',420);">&nbsp;</span
></td><td id="420"><a href="#420">420</a></td></tr
><tr id="gr_svn27_421"

 onmouseover="gutterOver(421)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',421);">&nbsp;</span
></td><td id="421"><a href="#421">421</a></td></tr
><tr id="gr_svn27_422"

 onmouseover="gutterOver(422)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',422);">&nbsp;</span
></td><td id="422"><a href="#422">422</a></td></tr
><tr id="gr_svn27_423"

 onmouseover="gutterOver(423)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',423);">&nbsp;</span
></td><td id="423"><a href="#423">423</a></td></tr
><tr id="gr_svn27_424"

 onmouseover="gutterOver(424)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',424);">&nbsp;</span
></td><td id="424"><a href="#424">424</a></td></tr
><tr id="gr_svn27_425"

 onmouseover="gutterOver(425)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',425);">&nbsp;</span
></td><td id="425"><a href="#425">425</a></td></tr
><tr id="gr_svn27_426"

 onmouseover="gutterOver(426)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',426);">&nbsp;</span
></td><td id="426"><a href="#426">426</a></td></tr
><tr id="gr_svn27_427"

 onmouseover="gutterOver(427)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',427);">&nbsp;</span
></td><td id="427"><a href="#427">427</a></td></tr
><tr id="gr_svn27_428"

 onmouseover="gutterOver(428)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',428);">&nbsp;</span
></td><td id="428"><a href="#428">428</a></td></tr
><tr id="gr_svn27_429"

 onmouseover="gutterOver(429)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',429);">&nbsp;</span
></td><td id="429"><a href="#429">429</a></td></tr
><tr id="gr_svn27_430"

 onmouseover="gutterOver(430)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',430);">&nbsp;</span
></td><td id="430"><a href="#430">430</a></td></tr
><tr id="gr_svn27_431"

 onmouseover="gutterOver(431)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',431);">&nbsp;</span
></td><td id="431"><a href="#431">431</a></td></tr
><tr id="gr_svn27_432"

 onmouseover="gutterOver(432)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',432);">&nbsp;</span
></td><td id="432"><a href="#432">432</a></td></tr
><tr id="gr_svn27_433"

 onmouseover="gutterOver(433)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',433);">&nbsp;</span
></td><td id="433"><a href="#433">433</a></td></tr
><tr id="gr_svn27_434"

 onmouseover="gutterOver(434)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',434);">&nbsp;</span
></td><td id="434"><a href="#434">434</a></td></tr
><tr id="gr_svn27_435"

 onmouseover="gutterOver(435)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',435);">&nbsp;</span
></td><td id="435"><a href="#435">435</a></td></tr
><tr id="gr_svn27_436"

 onmouseover="gutterOver(436)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',436);">&nbsp;</span
></td><td id="436"><a href="#436">436</a></td></tr
><tr id="gr_svn27_437"

 onmouseover="gutterOver(437)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',437);">&nbsp;</span
></td><td id="437"><a href="#437">437</a></td></tr
><tr id="gr_svn27_438"

 onmouseover="gutterOver(438)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',438);">&nbsp;</span
></td><td id="438"><a href="#438">438</a></td></tr
><tr id="gr_svn27_439"

 onmouseover="gutterOver(439)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',439);">&nbsp;</span
></td><td id="439"><a href="#439">439</a></td></tr
><tr id="gr_svn27_440"

 onmouseover="gutterOver(440)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',440);">&nbsp;</span
></td><td id="440"><a href="#440">440</a></td></tr
><tr id="gr_svn27_441"

 onmouseover="gutterOver(441)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',441);">&nbsp;</span
></td><td id="441"><a href="#441">441</a></td></tr
><tr id="gr_svn27_442"

 onmouseover="gutterOver(442)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',442);">&nbsp;</span
></td><td id="442"><a href="#442">442</a></td></tr
><tr id="gr_svn27_443"

 onmouseover="gutterOver(443)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',443);">&nbsp;</span
></td><td id="443"><a href="#443">443</a></td></tr
><tr id="gr_svn27_444"

 onmouseover="gutterOver(444)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',444);">&nbsp;</span
></td><td id="444"><a href="#444">444</a></td></tr
><tr id="gr_svn27_445"

 onmouseover="gutterOver(445)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',445);">&nbsp;</span
></td><td id="445"><a href="#445">445</a></td></tr
><tr id="gr_svn27_446"

 onmouseover="gutterOver(446)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',446);">&nbsp;</span
></td><td id="446"><a href="#446">446</a></td></tr
><tr id="gr_svn27_447"

 onmouseover="gutterOver(447)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',447);">&nbsp;</span
></td><td id="447"><a href="#447">447</a></td></tr
><tr id="gr_svn27_448"

 onmouseover="gutterOver(448)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',448);">&nbsp;</span
></td><td id="448"><a href="#448">448</a></td></tr
><tr id="gr_svn27_449"

 onmouseover="gutterOver(449)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',449);">&nbsp;</span
></td><td id="449"><a href="#449">449</a></td></tr
><tr id="gr_svn27_450"

 onmouseover="gutterOver(450)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',450);">&nbsp;</span
></td><td id="450"><a href="#450">450</a></td></tr
><tr id="gr_svn27_451"

 onmouseover="gutterOver(451)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',451);">&nbsp;</span
></td><td id="451"><a href="#451">451</a></td></tr
><tr id="gr_svn27_452"

 onmouseover="gutterOver(452)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',452);">&nbsp;</span
></td><td id="452"><a href="#452">452</a></td></tr
><tr id="gr_svn27_453"

 onmouseover="gutterOver(453)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',453);">&nbsp;</span
></td><td id="453"><a href="#453">453</a></td></tr
><tr id="gr_svn27_454"

 onmouseover="gutterOver(454)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',454);">&nbsp;</span
></td><td id="454"><a href="#454">454</a></td></tr
><tr id="gr_svn27_455"

 onmouseover="gutterOver(455)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',455);">&nbsp;</span
></td><td id="455"><a href="#455">455</a></td></tr
><tr id="gr_svn27_456"

 onmouseover="gutterOver(456)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',456);">&nbsp;</span
></td><td id="456"><a href="#456">456</a></td></tr
><tr id="gr_svn27_457"

 onmouseover="gutterOver(457)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',457);">&nbsp;</span
></td><td id="457"><a href="#457">457</a></td></tr
><tr id="gr_svn27_458"

 onmouseover="gutterOver(458)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',458);">&nbsp;</span
></td><td id="458"><a href="#458">458</a></td></tr
><tr id="gr_svn27_459"

 onmouseover="gutterOver(459)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',459);">&nbsp;</span
></td><td id="459"><a href="#459">459</a></td></tr
><tr id="gr_svn27_460"

 onmouseover="gutterOver(460)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',460);">&nbsp;</span
></td><td id="460"><a href="#460">460</a></td></tr
><tr id="gr_svn27_461"

 onmouseover="gutterOver(461)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',461);">&nbsp;</span
></td><td id="461"><a href="#461">461</a></td></tr
><tr id="gr_svn27_462"

 onmouseover="gutterOver(462)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',462);">&nbsp;</span
></td><td id="462"><a href="#462">462</a></td></tr
><tr id="gr_svn27_463"

 onmouseover="gutterOver(463)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',463);">&nbsp;</span
></td><td id="463"><a href="#463">463</a></td></tr
><tr id="gr_svn27_464"

 onmouseover="gutterOver(464)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',464);">&nbsp;</span
></td><td id="464"><a href="#464">464</a></td></tr
><tr id="gr_svn27_465"

 onmouseover="gutterOver(465)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',465);">&nbsp;</span
></td><td id="465"><a href="#465">465</a></td></tr
><tr id="gr_svn27_466"

 onmouseover="gutterOver(466)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',466);">&nbsp;</span
></td><td id="466"><a href="#466">466</a></td></tr
><tr id="gr_svn27_467"

 onmouseover="gutterOver(467)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',467);">&nbsp;</span
></td><td id="467"><a href="#467">467</a></td></tr
><tr id="gr_svn27_468"

 onmouseover="gutterOver(468)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',468);">&nbsp;</span
></td><td id="468"><a href="#468">468</a></td></tr
><tr id="gr_svn27_469"

 onmouseover="gutterOver(469)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',469);">&nbsp;</span
></td><td id="469"><a href="#469">469</a></td></tr
><tr id="gr_svn27_470"

 onmouseover="gutterOver(470)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',470);">&nbsp;</span
></td><td id="470"><a href="#470">470</a></td></tr
><tr id="gr_svn27_471"

 onmouseover="gutterOver(471)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',471);">&nbsp;</span
></td><td id="471"><a href="#471">471</a></td></tr
><tr id="gr_svn27_472"

 onmouseover="gutterOver(472)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',472);">&nbsp;</span
></td><td id="472"><a href="#472">472</a></td></tr
><tr id="gr_svn27_473"

 onmouseover="gutterOver(473)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',473);">&nbsp;</span
></td><td id="473"><a href="#473">473</a></td></tr
><tr id="gr_svn27_474"

 onmouseover="gutterOver(474)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',474);">&nbsp;</span
></td><td id="474"><a href="#474">474</a></td></tr
><tr id="gr_svn27_475"

 onmouseover="gutterOver(475)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',475);">&nbsp;</span
></td><td id="475"><a href="#475">475</a></td></tr
><tr id="gr_svn27_476"

 onmouseover="gutterOver(476)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',476);">&nbsp;</span
></td><td id="476"><a href="#476">476</a></td></tr
><tr id="gr_svn27_477"

 onmouseover="gutterOver(477)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',477);">&nbsp;</span
></td><td id="477"><a href="#477">477</a></td></tr
><tr id="gr_svn27_478"

 onmouseover="gutterOver(478)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',478);">&nbsp;</span
></td><td id="478"><a href="#478">478</a></td></tr
><tr id="gr_svn27_479"

 onmouseover="gutterOver(479)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',479);">&nbsp;</span
></td><td id="479"><a href="#479">479</a></td></tr
><tr id="gr_svn27_480"

 onmouseover="gutterOver(480)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',480);">&nbsp;</span
></td><td id="480"><a href="#480">480</a></td></tr
><tr id="gr_svn27_481"

 onmouseover="gutterOver(481)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',481);">&nbsp;</span
></td><td id="481"><a href="#481">481</a></td></tr
><tr id="gr_svn27_482"

 onmouseover="gutterOver(482)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',482);">&nbsp;</span
></td><td id="482"><a href="#482">482</a></td></tr
><tr id="gr_svn27_483"

 onmouseover="gutterOver(483)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',483);">&nbsp;</span
></td><td id="483"><a href="#483">483</a></td></tr
><tr id="gr_svn27_484"

 onmouseover="gutterOver(484)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',484);">&nbsp;</span
></td><td id="484"><a href="#484">484</a></td></tr
><tr id="gr_svn27_485"

 onmouseover="gutterOver(485)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',485);">&nbsp;</span
></td><td id="485"><a href="#485">485</a></td></tr
><tr id="gr_svn27_486"

 onmouseover="gutterOver(486)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',486);">&nbsp;</span
></td><td id="486"><a href="#486">486</a></td></tr
><tr id="gr_svn27_487"

 onmouseover="gutterOver(487)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',487);">&nbsp;</span
></td><td id="487"><a href="#487">487</a></td></tr
><tr id="gr_svn27_488"

 onmouseover="gutterOver(488)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',488);">&nbsp;</span
></td><td id="488"><a href="#488">488</a></td></tr
><tr id="gr_svn27_489"

 onmouseover="gutterOver(489)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',489);">&nbsp;</span
></td><td id="489"><a href="#489">489</a></td></tr
><tr id="gr_svn27_490"

 onmouseover="gutterOver(490)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',490);">&nbsp;</span
></td><td id="490"><a href="#490">490</a></td></tr
><tr id="gr_svn27_491"

 onmouseover="gutterOver(491)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',491);">&nbsp;</span
></td><td id="491"><a href="#491">491</a></td></tr
><tr id="gr_svn27_492"

 onmouseover="gutterOver(492)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',492);">&nbsp;</span
></td><td id="492"><a href="#492">492</a></td></tr
><tr id="gr_svn27_493"

 onmouseover="gutterOver(493)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',493);">&nbsp;</span
></td><td id="493"><a href="#493">493</a></td></tr
><tr id="gr_svn27_494"

 onmouseover="gutterOver(494)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',494);">&nbsp;</span
></td><td id="494"><a href="#494">494</a></td></tr
><tr id="gr_svn27_495"

 onmouseover="gutterOver(495)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',495);">&nbsp;</span
></td><td id="495"><a href="#495">495</a></td></tr
><tr id="gr_svn27_496"

 onmouseover="gutterOver(496)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',496);">&nbsp;</span
></td><td id="496"><a href="#496">496</a></td></tr
><tr id="gr_svn27_497"

 onmouseover="gutterOver(497)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',497);">&nbsp;</span
></td><td id="497"><a href="#497">497</a></td></tr
><tr id="gr_svn27_498"

 onmouseover="gutterOver(498)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',498);">&nbsp;</span
></td><td id="498"><a href="#498">498</a></td></tr
><tr id="gr_svn27_499"

 onmouseover="gutterOver(499)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',499);">&nbsp;</span
></td><td id="499"><a href="#499">499</a></td></tr
><tr id="gr_svn27_500"

 onmouseover="gutterOver(500)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',500);">&nbsp;</span
></td><td id="500"><a href="#500">500</a></td></tr
><tr id="gr_svn27_501"

 onmouseover="gutterOver(501)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',501);">&nbsp;</span
></td><td id="501"><a href="#501">501</a></td></tr
><tr id="gr_svn27_502"

 onmouseover="gutterOver(502)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',502);">&nbsp;</span
></td><td id="502"><a href="#502">502</a></td></tr
><tr id="gr_svn27_503"

 onmouseover="gutterOver(503)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',503);">&nbsp;</span
></td><td id="503"><a href="#503">503</a></td></tr
><tr id="gr_svn27_504"

 onmouseover="gutterOver(504)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',504);">&nbsp;</span
></td><td id="504"><a href="#504">504</a></td></tr
><tr id="gr_svn27_505"

 onmouseover="gutterOver(505)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',505);">&nbsp;</span
></td><td id="505"><a href="#505">505</a></td></tr
><tr id="gr_svn27_506"

 onmouseover="gutterOver(506)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',506);">&nbsp;</span
></td><td id="506"><a href="#506">506</a></td></tr
><tr id="gr_svn27_507"

 onmouseover="gutterOver(507)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',507);">&nbsp;</span
></td><td id="507"><a href="#507">507</a></td></tr
><tr id="gr_svn27_508"

 onmouseover="gutterOver(508)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',508);">&nbsp;</span
></td><td id="508"><a href="#508">508</a></td></tr
><tr id="gr_svn27_509"

 onmouseover="gutterOver(509)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',509);">&nbsp;</span
></td><td id="509"><a href="#509">509</a></td></tr
><tr id="gr_svn27_510"

 onmouseover="gutterOver(510)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',510);">&nbsp;</span
></td><td id="510"><a href="#510">510</a></td></tr
><tr id="gr_svn27_511"

 onmouseover="gutterOver(511)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',511);">&nbsp;</span
></td><td id="511"><a href="#511">511</a></td></tr
><tr id="gr_svn27_512"

 onmouseover="gutterOver(512)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',512);">&nbsp;</span
></td><td id="512"><a href="#512">512</a></td></tr
><tr id="gr_svn27_513"

 onmouseover="gutterOver(513)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',513);">&nbsp;</span
></td><td id="513"><a href="#513">513</a></td></tr
><tr id="gr_svn27_514"

 onmouseover="gutterOver(514)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',514);">&nbsp;</span
></td><td id="514"><a href="#514">514</a></td></tr
><tr id="gr_svn27_515"

 onmouseover="gutterOver(515)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',515);">&nbsp;</span
></td><td id="515"><a href="#515">515</a></td></tr
><tr id="gr_svn27_516"

 onmouseover="gutterOver(516)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',516);">&nbsp;</span
></td><td id="516"><a href="#516">516</a></td></tr
><tr id="gr_svn27_517"

 onmouseover="gutterOver(517)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',517);">&nbsp;</span
></td><td id="517"><a href="#517">517</a></td></tr
><tr id="gr_svn27_518"

 onmouseover="gutterOver(518)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',518);">&nbsp;</span
></td><td id="518"><a href="#518">518</a></td></tr
><tr id="gr_svn27_519"

 onmouseover="gutterOver(519)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',519);">&nbsp;</span
></td><td id="519"><a href="#519">519</a></td></tr
><tr id="gr_svn27_520"

 onmouseover="gutterOver(520)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',520);">&nbsp;</span
></td><td id="520"><a href="#520">520</a></td></tr
><tr id="gr_svn27_521"

 onmouseover="gutterOver(521)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',521);">&nbsp;</span
></td><td id="521"><a href="#521">521</a></td></tr
><tr id="gr_svn27_522"

 onmouseover="gutterOver(522)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',522);">&nbsp;</span
></td><td id="522"><a href="#522">522</a></td></tr
><tr id="gr_svn27_523"

 onmouseover="gutterOver(523)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',523);">&nbsp;</span
></td><td id="523"><a href="#523">523</a></td></tr
><tr id="gr_svn27_524"

 onmouseover="gutterOver(524)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',524);">&nbsp;</span
></td><td id="524"><a href="#524">524</a></td></tr
><tr id="gr_svn27_525"

 onmouseover="gutterOver(525)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',525);">&nbsp;</span
></td><td id="525"><a href="#525">525</a></td></tr
><tr id="gr_svn27_526"

 onmouseover="gutterOver(526)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',526);">&nbsp;</span
></td><td id="526"><a href="#526">526</a></td></tr
><tr id="gr_svn27_527"

 onmouseover="gutterOver(527)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',527);">&nbsp;</span
></td><td id="527"><a href="#527">527</a></td></tr
><tr id="gr_svn27_528"

 onmouseover="gutterOver(528)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',528);">&nbsp;</span
></td><td id="528"><a href="#528">528</a></td></tr
><tr id="gr_svn27_529"

 onmouseover="gutterOver(529)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',529);">&nbsp;</span
></td><td id="529"><a href="#529">529</a></td></tr
><tr id="gr_svn27_530"

 onmouseover="gutterOver(530)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',530);">&nbsp;</span
></td><td id="530"><a href="#530">530</a></td></tr
><tr id="gr_svn27_531"

 onmouseover="gutterOver(531)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',531);">&nbsp;</span
></td><td id="531"><a href="#531">531</a></td></tr
><tr id="gr_svn27_532"

 onmouseover="gutterOver(532)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',532);">&nbsp;</span
></td><td id="532"><a href="#532">532</a></td></tr
><tr id="gr_svn27_533"

 onmouseover="gutterOver(533)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',533);">&nbsp;</span
></td><td id="533"><a href="#533">533</a></td></tr
><tr id="gr_svn27_534"

 onmouseover="gutterOver(534)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',534);">&nbsp;</span
></td><td id="534"><a href="#534">534</a></td></tr
><tr id="gr_svn27_535"

 onmouseover="gutterOver(535)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',535);">&nbsp;</span
></td><td id="535"><a href="#535">535</a></td></tr
><tr id="gr_svn27_536"

 onmouseover="gutterOver(536)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',536);">&nbsp;</span
></td><td id="536"><a href="#536">536</a></td></tr
><tr id="gr_svn27_537"

 onmouseover="gutterOver(537)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',537);">&nbsp;</span
></td><td id="537"><a href="#537">537</a></td></tr
><tr id="gr_svn27_538"

 onmouseover="gutterOver(538)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',538);">&nbsp;</span
></td><td id="538"><a href="#538">538</a></td></tr
><tr id="gr_svn27_539"

 onmouseover="gutterOver(539)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',539);">&nbsp;</span
></td><td id="539"><a href="#539">539</a></td></tr
><tr id="gr_svn27_540"

 onmouseover="gutterOver(540)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',540);">&nbsp;</span
></td><td id="540"><a href="#540">540</a></td></tr
><tr id="gr_svn27_541"

 onmouseover="gutterOver(541)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',541);">&nbsp;</span
></td><td id="541"><a href="#541">541</a></td></tr
><tr id="gr_svn27_542"

 onmouseover="gutterOver(542)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',542);">&nbsp;</span
></td><td id="542"><a href="#542">542</a></td></tr
><tr id="gr_svn27_543"

 onmouseover="gutterOver(543)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',543);">&nbsp;</span
></td><td id="543"><a href="#543">543</a></td></tr
><tr id="gr_svn27_544"

 onmouseover="gutterOver(544)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',544);">&nbsp;</span
></td><td id="544"><a href="#544">544</a></td></tr
><tr id="gr_svn27_545"

 onmouseover="gutterOver(545)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',545);">&nbsp;</span
></td><td id="545"><a href="#545">545</a></td></tr
><tr id="gr_svn27_546"

 onmouseover="gutterOver(546)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',546);">&nbsp;</span
></td><td id="546"><a href="#546">546</a></td></tr
><tr id="gr_svn27_547"

 onmouseover="gutterOver(547)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',547);">&nbsp;</span
></td><td id="547"><a href="#547">547</a></td></tr
><tr id="gr_svn27_548"

 onmouseover="gutterOver(548)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',548);">&nbsp;</span
></td><td id="548"><a href="#548">548</a></td></tr
><tr id="gr_svn27_549"

 onmouseover="gutterOver(549)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',549);">&nbsp;</span
></td><td id="549"><a href="#549">549</a></td></tr
><tr id="gr_svn27_550"

 onmouseover="gutterOver(550)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',550);">&nbsp;</span
></td><td id="550"><a href="#550">550</a></td></tr
><tr id="gr_svn27_551"

 onmouseover="gutterOver(551)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',551);">&nbsp;</span
></td><td id="551"><a href="#551">551</a></td></tr
><tr id="gr_svn27_552"

 onmouseover="gutterOver(552)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',552);">&nbsp;</span
></td><td id="552"><a href="#552">552</a></td></tr
><tr id="gr_svn27_553"

 onmouseover="gutterOver(553)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',553);">&nbsp;</span
></td><td id="553"><a href="#553">553</a></td></tr
><tr id="gr_svn27_554"

 onmouseover="gutterOver(554)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',554);">&nbsp;</span
></td><td id="554"><a href="#554">554</a></td></tr
><tr id="gr_svn27_555"

 onmouseover="gutterOver(555)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',555);">&nbsp;</span
></td><td id="555"><a href="#555">555</a></td></tr
><tr id="gr_svn27_556"

 onmouseover="gutterOver(556)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',556);">&nbsp;</span
></td><td id="556"><a href="#556">556</a></td></tr
><tr id="gr_svn27_557"

 onmouseover="gutterOver(557)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',557);">&nbsp;</span
></td><td id="557"><a href="#557">557</a></td></tr
><tr id="gr_svn27_558"

 onmouseover="gutterOver(558)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',558);">&nbsp;</span
></td><td id="558"><a href="#558">558</a></td></tr
><tr id="gr_svn27_559"

 onmouseover="gutterOver(559)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',559);">&nbsp;</span
></td><td id="559"><a href="#559">559</a></td></tr
><tr id="gr_svn27_560"

 onmouseover="gutterOver(560)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',560);">&nbsp;</span
></td><td id="560"><a href="#560">560</a></td></tr
><tr id="gr_svn27_561"

 onmouseover="gutterOver(561)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',561);">&nbsp;</span
></td><td id="561"><a href="#561">561</a></td></tr
><tr id="gr_svn27_562"

 onmouseover="gutterOver(562)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',562);">&nbsp;</span
></td><td id="562"><a href="#562">562</a></td></tr
><tr id="gr_svn27_563"

 onmouseover="gutterOver(563)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',563);">&nbsp;</span
></td><td id="563"><a href="#563">563</a></td></tr
><tr id="gr_svn27_564"

 onmouseover="gutterOver(564)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',564);">&nbsp;</span
></td><td id="564"><a href="#564">564</a></td></tr
><tr id="gr_svn27_565"

 onmouseover="gutterOver(565)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',565);">&nbsp;</span
></td><td id="565"><a href="#565">565</a></td></tr
><tr id="gr_svn27_566"

 onmouseover="gutterOver(566)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',566);">&nbsp;</span
></td><td id="566"><a href="#566">566</a></td></tr
><tr id="gr_svn27_567"

 onmouseover="gutterOver(567)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',567);">&nbsp;</span
></td><td id="567"><a href="#567">567</a></td></tr
><tr id="gr_svn27_568"

 onmouseover="gutterOver(568)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',568);">&nbsp;</span
></td><td id="568"><a href="#568">568</a></td></tr
><tr id="gr_svn27_569"

 onmouseover="gutterOver(569)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',569);">&nbsp;</span
></td><td id="569"><a href="#569">569</a></td></tr
><tr id="gr_svn27_570"

 onmouseover="gutterOver(570)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',570);">&nbsp;</span
></td><td id="570"><a href="#570">570</a></td></tr
><tr id="gr_svn27_571"

 onmouseover="gutterOver(571)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',571);">&nbsp;</span
></td><td id="571"><a href="#571">571</a></td></tr
><tr id="gr_svn27_572"

 onmouseover="gutterOver(572)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',572);">&nbsp;</span
></td><td id="572"><a href="#572">572</a></td></tr
><tr id="gr_svn27_573"

 onmouseover="gutterOver(573)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',573);">&nbsp;</span
></td><td id="573"><a href="#573">573</a></td></tr
><tr id="gr_svn27_574"

 onmouseover="gutterOver(574)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',574);">&nbsp;</span
></td><td id="574"><a href="#574">574</a></td></tr
><tr id="gr_svn27_575"

 onmouseover="gutterOver(575)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',575);">&nbsp;</span
></td><td id="575"><a href="#575">575</a></td></tr
><tr id="gr_svn27_576"

 onmouseover="gutterOver(576)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',576);">&nbsp;</span
></td><td id="576"><a href="#576">576</a></td></tr
><tr id="gr_svn27_577"

 onmouseover="gutterOver(577)"

><td><span title="Add comment" onclick="codereviews.startEdit('svn27',577);">&nbsp;</span
></td><td id="577"><a href="#577">577</a></td></tr
></table></pre>
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
</td>
<td id="lines">
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
<pre class="prettyprint lang-py"><table id="src_table_0"><tr
id=sl_svn27_1

 onmouseover="gutterOver(1)"

><td class="source">#! /usr/bin/env python<br></td></tr
><tr
id=sl_svn27_2

 onmouseover="gutterOver(2)"

><td class="source">import sys, string, datetime, time, socket, struct, re, os<br></td></tr
><tr
id=sl_svn27_3

 onmouseover="gutterOver(3)"

><td class="source">from pysqlite2 import dbapi2 as sqlite<br></td></tr
><tr
id=sl_svn27_4

 onmouseover="gutterOver(4)"

><td class="source">import pcapy as pcap<br></td></tr
><tr
id=sl_svn27_5

 onmouseover="gutterOver(5)"

><td class="source">import curses<br></td></tr
><tr
id=sl_svn27_6

 onmouseover="gutterOver(6)"

><td class="source">import MySQLdb<br></td></tr
><tr
id=sl_svn27_7

 onmouseover="gutterOver(7)"

><td class="source">from curses import panel<br></td></tr
><tr
id=sl_svn27_8

 onmouseover="gutterOver(8)"

><td class="source">from optparse import OptionParser<br></td></tr
><tr
id=sl_svn27_9

 onmouseover="gutterOver(9)"

><td class="source">#import sqlite3 as sqlite #the module is called sqlite3 on the python doc site, might be for python2.5<br></td></tr
><tr
id=sl_svn27_10

 onmouseover="gutterOver(10)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_11

 onmouseover="gutterOver(11)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_12

 onmouseover="gutterOver(12)"

><td class="source">class Sniffer:<br></td></tr
><tr
id=sl_svn27_13

 onmouseover="gutterOver(13)"

><td class="source">   <br></td></tr
><tr
id=sl_svn27_14

 onmouseover="gutterOver(14)"

><td class="source">    def __init__(self, check_seconds=10, pcap_filter=&#39;tcp and port 80 and not (dst port 80 and dst net 128.193)&#39;, sqlitedbname=&#39;test.db&#39;):<br></td></tr
><tr
id=sl_svn27_15

 onmouseover="gutterOver(15)"

><td class="source">        self.start_time = self.last_checked = datetime.datetime.now()<br></td></tr
><tr
id=sl_svn27_16

 onmouseover="gutterOver(16)"

><td class="source">        self.check_seconds = check_seconds #how frequently to check for outdated requests, as well as how old a request has to be in order to be considered outdated (in seconds)<br></td></tr
><tr
id=sl_svn27_17

 onmouseover="gutterOver(17)"

><td class="source">        self.pcap_filter = pcap_filter<br></td></tr
><tr
id=sl_svn27_18

 onmouseover="gutterOver(18)"

><td class="source">        self.request_dict = {}<br></td></tr
><tr
id=sl_svn27_19

 onmouseover="gutterOver(19)"

><td class="source">        self.domain_re = re.compile(&#39;.*domain=(?P&lt;domain&gt;.*?)((;.*$)|$)&#39;, re.IGNORECASE)<br></td></tr
><tr
id=sl_svn27_20

 onmouseover="gutterOver(20)"

><td class="source">        self.expiry_re = re.compile(&#39;.*expires=(?P&lt;expiry&gt;.*?)((;.*$)|$)&#39;, re.IGNORECASE)<br></td></tr
><tr
id=sl_svn27_21

 onmouseover="gutterOver(21)"

><td class="source">        self.get_re = re.compile(&#39;GET (?P&lt;get&gt;.*?) HTTP&#39;)<br></td></tr
><tr
id=sl_svn27_22

 onmouseover="gutterOver(22)"

><td class="source">        self.status_re = re.compile(&#39;HTTP/[0-9]\.[0-9] (?P&lt;status&gt;[0-9]{3})&#39;)<br></td></tr
><tr
id=sl_svn27_23

 onmouseover="gutterOver(23)"

><td class="source">        self.protocols = {socket.IPPROTO_TCP:&#39;tcp&#39;, socket.IPPROTO_UDP:&#39;udp&#39;, socket.IPPROTO_ICMP:&#39;icmp&#39;}<br></td></tr
><tr
id=sl_svn27_24

 onmouseover="gutterOver(24)"

><td class="source">        self.sqlitedbname = sqlitedbname<br></td></tr
><tr
id=sl_svn27_25

 onmouseover="gutterOver(25)"

><td class="source">        self.connections = {}<br></td></tr
><tr
id=sl_svn27_26

 onmouseover="gutterOver(26)"

><td class="source">        self.con_size = 0<br></td></tr
><tr
id=sl_svn27_27

 onmouseover="gutterOver(27)"

><td class="source">        self.time_update = time.time()<br></td></tr
><tr
id=sl_svn27_28

 onmouseover="gutterOver(28)"

><td class="source">        #Determine the correct interface; the first two should be mututally exclusive, an k9 can be considered a special case that overrides &#39;linux2&#39;<br></td></tr
><tr
id=sl_svn27_29

 onmouseover="gutterOver(29)"

><td class="source">        if(sys.platform == &quot;linux2&quot;):#linux2?  well, that&#39;s what skoll says and its why i&#39;m adding this part<br></td></tr
><tr
id=sl_svn27_30

 onmouseover="gutterOver(30)"

><td class="source">            self.dev = &#39;eth0&#39;#should be eth0 but this lets wifi work<br></td></tr
><tr
id=sl_svn27_31

 onmouseover="gutterOver(31)"

><td class="source">        if(sys.platform == &quot;darwin&quot;):<br></td></tr
><tr
id=sl_svn27_32

 onmouseover="gutterOver(32)"

><td class="source">            self.dev = &#39;en1&#39;<br></td></tr
><tr
id=sl_svn27_33

 onmouseover="gutterOver(33)"

><td class="source">        if(socket.gethostname() == &quot;k9&quot;):<br></td></tr
><tr
id=sl_svn27_34

 onmouseover="gutterOver(34)"

><td class="source">            self.dev = &#39;eth3&#39;<br></td></tr
><tr
id=sl_svn27_35

 onmouseover="gutterOver(35)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_36

 onmouseover="gutterOver(36)"

><td class="source">        self.db_setup()<br></td></tr
><tr
id=sl_svn27_37

 onmouseover="gutterOver(37)"

><td class="source">   <br></td></tr
><tr
id=sl_svn27_38

 onmouseover="gutterOver(38)"

><td class="source">    def start(self):<br></td></tr
><tr
id=sl_svn27_39

 onmouseover="gutterOver(39)"

><td class="source">        <br></td></tr
><tr
id=sl_svn27_40

 onmouseover="gutterOver(40)"

><td class="source">        # note:    to_ms does nothing on linux<br></td></tr
><tr
id=sl_svn27_41

 onmouseover="gutterOver(41)"

><td class="source">        self.p = pcap.open_live(self.dev, 1600, 1, 100)#opens a connection descriptor<br></td></tr
><tr
id=sl_svn27_42

 onmouseover="gutterOver(42)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_43

 onmouseover="gutterOver(43)"

><td class="source">        self.p.setfilter(self.pcap_filter)#sets our packet filter we set in init<br></td></tr
><tr
id=sl_svn27_44

 onmouseover="gutterOver(44)"

><td class="source">        print &quot;Listening on %s: net=%s, mask=%s\n&quot; % (self.dev, self.p.getnet(), self.p.getmask())<br></td></tr
><tr
id=sl_svn27_45

 onmouseover="gutterOver(45)"

><td class="source">        # try-except block to catch keyboard interrupt.    Failure to shut<br></td></tr
><tr
id=sl_svn27_46

 onmouseover="gutterOver(46)"

><td class="source">        # down cleanly can result in the interface not being taken out of promisc.<br></td></tr
><tr
id=sl_svn27_47

 onmouseover="gutterOver(47)"

><td class="source">        # mode<br></td></tr
><tr
id=sl_svn27_48

 onmouseover="gutterOver(48)"

><td class="source">        self.p.setnonblock(1)#goes into nonblcoking mode so we dont wait for packets that have timed out<br></td></tr
><tr
id=sl_svn27_49

 onmouseover="gutterOver(49)"

><td class="source">        <br></td></tr
><tr
id=sl_svn27_50

 onmouseover="gutterOver(50)"

><td class="source">        try:<br></td></tr
><tr
id=sl_svn27_51

 onmouseover="gutterOver(51)"

><td class="source">            while 1:#can&#39;t use self.p.loop in nonblock<br></td></tr
><tr
id=sl_svn27_52

 onmouseover="gutterOver(52)"

><td class="source">                self.p.dispatch(1, self.print_packet)#read 1 packet and parse it, then repeat ad nauseam<br></td></tr
><tr
id=sl_svn27_53

 onmouseover="gutterOver(53)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_54

 onmouseover="gutterOver(54)"

><td class="source">        except KeyboardInterrupt:#if we get a ctrl-c abort<br></td></tr
><tr
id=sl_svn27_55

 onmouseover="gutterOver(55)"

><td class="source">            print &#39;%s&#39; % sys.exc_type<br></td></tr
><tr
id=sl_svn27_56

 onmouseover="gutterOver(56)"

><td class="source">            print &#39;shutting down&#39;<br></td></tr
><tr
id=sl_svn27_57

 onmouseover="gutterOver(57)"

><td class="source">            self.cursor.close()<br></td></tr
><tr
id=sl_svn27_58

 onmouseover="gutterOver(58)"

><td class="source">            self.connection.close()#notice we dont close down the descriptor, only the database, dont know why that is<br></td></tr
><tr
id=sl_svn27_59

 onmouseover="gutterOver(59)"

><td class="source">   <br></td></tr
><tr
id=sl_svn27_60

 onmouseover="gutterOver(60)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_61

 onmouseover="gutterOver(61)"

><td class="source">    #mysql db<br></td></tr
><tr
id=sl_svn27_62

 onmouseover="gutterOver(62)"

><td class="source">    def db_setup(self):<br></td></tr
><tr
id=sl_svn27_63

 onmouseover="gutterOver(63)"

><td class="source">        #if(options.debug == True):<br></td></tr
><tr
id=sl_svn27_64

 onmouseover="gutterOver(64)"

><td class="source">            self.connection =  MySQLdb.connect(host=&quot;mysql.cs.orst.edu&quot;, user=&quot;team33&quot;, passwd=&quot;team33&quot;, db=&quot;team33&quot;)#connect to our mysql database<br></td></tr
><tr
id=sl_svn27_65

 onmouseover="gutterOver(65)"

><td class="source">            self.cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)#create a cursor to interact with it, throw the dictionary flag so we can mess with the output<br></td></tr
><tr
id=sl_svn27_66

 onmouseover="gutterOver(66)"

><td class="source">#        else:<br></td></tr
><tr
id=sl_svn27_67

 onmouseover="gutterOver(67)"

><td class="source">#            if(os.path.exists(self.sqlitedbname)):<br></td></tr
><tr
id=sl_svn27_68

 onmouseover="gutterOver(68)"

><td class="source">#                os.remove(self.sqlitedbname)<br></td></tr
><tr
id=sl_svn27_69

 onmouseover="gutterOver(69)"

><td class="source">#            self.connection = sqlite.connect(self.sqlitedbname)<br></td></tr
><tr
id=sl_svn27_70

 onmouseover="gutterOver(70)"

><td class="source">#            self.connection.row_factory = sqlite.Row<br></td></tr
><tr
id=sl_svn27_71

 onmouseover="gutterOver(71)"

><td class="source">#            self.cursor = self.connection.cursor()<br></td></tr
><tr
id=sl_svn27_72

 onmouseover="gutterOver(72)"

><td class="source">#       <br></td></tr
><tr
id=sl_svn27_73

 onmouseover="gutterOver(73)"

><td class="source">#            ##To create the DB<br></td></tr
><tr
id=sl_svn27_74

 onmouseover="gutterOver(74)"

><td class="source">#            self.cursor.execute(&quot;&quot;&quot;<br></td></tr
><tr
id=sl_svn27_75

 onmouseover="gutterOver(75)"

><td class="source">#            CREATE TABLE rawpkt (<br></td></tr
><tr
id=sl_svn27_76

 onmouseover="gutterOver(76)"

><td class="source">#            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,<br></td></tr
><tr
id=sl_svn27_77

 onmouseover="gutterOver(77)"

><td class="source">#            host VARCHAR(128),<br></td></tr
><tr
id=sl_svn27_78

 onmouseover="gutterOver(78)"

><td class="source">#            get VARCHAR(1024),<br></td></tr
><tr
id=sl_svn27_79

 onmouseover="gutterOver(79)"

><td class="source">#            referer VARCHAR(1024),<br></td></tr
><tr
id=sl_svn27_80

 onmouseover="gutterOver(80)"

><td class="source">#            contenttype VARCHAR(32),<br></td></tr
><tr
id=sl_svn27_81

 onmouseover="gutterOver(81)"

><td class="source">#            pkt_date DATE,<br></td></tr
><tr
id=sl_svn27_82

 onmouseover="gutterOver(82)"

><td class="source">#            insert_date DATE,<br></td></tr
><tr
id=sl_svn27_83

 onmouseover="gutterOver(83)"

><td class="source">#            status INTEGER,<br></td></tr
><tr
id=sl_svn27_84

 onmouseover="gutterOver(84)"

><td class="source">#            server VARCHAR(50),<br></td></tr
><tr
id=sl_svn27_85

 onmouseover="gutterOver(85)"

><td class="source">#            useragent VARCHAR(50),<br></td></tr
><tr
id=sl_svn27_86

 onmouseover="gutterOver(86)"

><td class="source">#            p3p VARCHAR(256),<br></td></tr
><tr
id=sl_svn27_87

 onmouseover="gutterOver(87)"

><td class="source">#            etag VARCHAR(32),<br></td></tr
><tr
id=sl_svn27_88

 onmouseover="gutterOver(88)"

><td class="source">#            contentlength INTEGER,<br></td></tr
><tr
id=sl_svn27_89

 onmouseover="gutterOver(89)"

><td class="source">#            seq INTEGER,<br></td></tr
><tr
id=sl_svn27_90

 onmouseover="gutterOver(90)"

><td class="source">#            ack INTEGER,<br></td></tr
><tr
id=sl_svn27_91

 onmouseover="gutterOver(91)"

><td class="source">#            residential BOOLEAN NOT NULL DEFAULT 0<br></td></tr
><tr
id=sl_svn27_92

 onmouseover="gutterOver(92)"

><td class="source">#            )<br></td></tr
><tr
id=sl_svn27_93

 onmouseover="gutterOver(93)"

><td class="source">#            &quot;&quot;&quot;)<br></td></tr
><tr
id=sl_svn27_94

 onmouseover="gutterOver(94)"

><td class="source">#           <br></td></tr
><tr
id=sl_svn27_95

 onmouseover="gutterOver(95)"

><td class="source">#            self.cursor.execute(&quot;&quot;&quot;<br></td></tr
><tr
id=sl_svn27_96

 onmouseover="gutterOver(96)"

><td class="source">#            CREATE TABLE cookie_has (<br></td></tr
><tr
id=sl_svn27_97

 onmouseover="gutterOver(97)"

><td class="source">#            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,<br></td></tr
><tr
id=sl_svn27_98

 onmouseover="gutterOver(98)"

><td class="source">#            domain_id INTEGER NOT NULL,<br></td></tr
><tr
id=sl_svn27_99

 onmouseover="gutterOver(99)"

><td class="source">#            pkt_id INTEGER NOT NULL,<br></td></tr
><tr
id=sl_svn27_100

 onmouseover="gutterOver(100)"

><td class="source">#            set_by VARCHAT(24),<br></td></tr
><tr
id=sl_svn27_101

 onmouseover="gutterOver(101)"

><td class="source">#            expiry DATE,<br></td></tr
><tr
id=sl_svn27_102

 onmouseover="gutterOver(102)"

><td class="source">#            session BOOLEAN<br></td></tr
><tr
id=sl_svn27_103

 onmouseover="gutterOver(103)"

><td class="source">#            )<br></td></tr
><tr
id=sl_svn27_104

 onmouseover="gutterOver(104)"

><td class="source">#           <br></td></tr
><tr
id=sl_svn27_105

 onmouseover="gutterOver(105)"

><td class="source">#            &quot;&quot;&quot;)<br></td></tr
><tr
id=sl_svn27_106

 onmouseover="gutterOver(106)"

><td class="source">#           <br></td></tr
><tr
id=sl_svn27_107

 onmouseover="gutterOver(107)"

><td class="source">#            self.cursor.execute(&quot;&quot;&quot;<br></td></tr
><tr
id=sl_svn27_108

 onmouseover="gutterOver(108)"

><td class="source">#            CREATE TABLE domains (<br></td></tr
><tr
id=sl_svn27_109

 onmouseover="gutterOver(109)"

><td class="source">#            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,<br></td></tr
><tr
id=sl_svn27_110

 onmouseover="gutterOver(110)"

><td class="source">#            domain VARCHAR(128) NOT NULL)<br></td></tr
><tr
id=sl_svn27_111

 onmouseover="gutterOver(111)"

><td class="source">#            &quot;&quot;&quot;)<br></td></tr
><tr
id=sl_svn27_112

 onmouseover="gutterOver(112)"

><td class="source">#            self.connection.commit()<br></td></tr
><tr
id=sl_svn27_113

 onmouseover="gutterOver(113)"

><td class="source">            #cursor.close()<br></td></tr
><tr
id=sl_svn27_114

 onmouseover="gutterOver(114)"

><td class="source">            #connection.close()<br></td></tr
><tr
id=sl_svn27_115

 onmouseover="gutterOver(115)"

><td class="source">   <br></td></tr
><tr
id=sl_svn27_116

 onmouseover="gutterOver(116)"

><td class="source">    def decode_ip_packet(self,s):#takes in the packet info after the ethertype from spot 14 on<br></td></tr
><tr
id=sl_svn27_117

 onmouseover="gutterOver(117)"

><td class="source">        d={}<br></td></tr
><tr
id=sl_svn27_118

 onmouseover="gutterOver(118)"

><td class="source">        d[&#39;version&#39;]=(ord(s[0]) &amp; 0xf0) &gt;&gt; 4#gets the first byte, takes the first half of it then shifts it??? anyways its the version number   Maybe it shifts it right because it was the left half of the number<br></td></tr
><tr
id=sl_svn27_119

 onmouseover="gutterOver(119)"

><td class="source">        d[&#39;header_len&#39;]=ord(s[0]) &amp; 0x0f#second half of the first byte, header length, straight from wireshark ip section<br></td></tr
><tr
id=sl_svn27_120

 onmouseover="gutterOver(120)"

><td class="source">        d[&#39;tos&#39;]=ord(s[1])#the &quot;Differentiated Services Field&quot; still no clue as to what this does<br></td></tr
><tr
id=sl_svn27_121

 onmouseover="gutterOver(121)"

><td class="source">        d[&#39;total_len&#39;]=socket.ntohs(struct.unpack(&#39;H&#39;,s[2:4])[0])#gets the struct that is at 2 and 3, unpacks it to an int (&#39;H&#39; means unsingned short in c, converts it to an int, then converts network byte order to host byte order<br></td></tr
><tr
id=sl_svn27_122

 onmouseover="gutterOver(122)"

><td class="source">        d[&#39;id&#39;]=socket.ntohs(struct.unpack(&#39;H&#39;,s[4:6])[0])#and get the first part of the tuple that it returns, this line does the same for next 2 spots<br></td></tr
><tr
id=sl_svn27_123

 onmouseover="gutterOver(123)"

><td class="source">        d[&#39;flags&#39;]=(ord(s[6]) &amp; 0xe0) &gt;&gt; 5#gets flags shifting again<br></td></tr
><tr
id=sl_svn27_124

 onmouseover="gutterOver(124)"

><td class="source">        d[&#39;fragment_offset&#39;]=socket.ntohs(struct.unpack(&#39;H&#39;,s[6:8])[0] &amp; 0x1f)<br></td></tr
><tr
id=sl_svn27_125

 onmouseover="gutterOver(125)"

><td class="source">        d[&#39;ttl&#39;]=ord(s[8])<br></td></tr
><tr
id=sl_svn27_126

 onmouseover="gutterOver(126)"

><td class="source">        d[&#39;protocol&#39;]=ord(s[9])<br></td></tr
><tr
id=sl_svn27_127

 onmouseover="gutterOver(127)"

><td class="source">        d[&#39;checksum&#39;]=socket.ntohs(struct.unpack(&#39;H&#39;,s[10:12])[0])<br></td></tr
><tr
id=sl_svn27_128

 onmouseover="gutterOver(128)"

><td class="source">        d[&#39;source_address&#39;]=socket.inet_ntoa(s[12:16])#converts network address in a struct to a string<br></td></tr
><tr
id=sl_svn27_129

 onmouseover="gutterOver(129)"

><td class="source">      <br></td></tr
><tr
id=sl_svn27_130

 onmouseover="gutterOver(130)"

><td class="source">        d[&#39;destination_address&#39;]=socket.inet_ntoa(s[16:20])<br></td></tr
><tr
id=sl_svn27_131

 onmouseover="gutterOver(131)"

><td class="source">      <br></td></tr
><tr
id=sl_svn27_132

 onmouseover="gutterOver(132)"

><td class="source">        if d[&#39;header_len&#39;]&gt;5:#think 5 is normal, so if its a bad packet?<br></td></tr
><tr
id=sl_svn27_133

 onmouseover="gutterOver(133)"

><td class="source">            d[&#39;options&#39;]=s[20:4*(d[&#39;header_len&#39;]-5)]#?????<br></td></tr
><tr
id=sl_svn27_134

 onmouseover="gutterOver(134)"

><td class="source">        else:<br></td></tr
><tr
id=sl_svn27_135

 onmouseover="gutterOver(135)"

><td class="source">            d[&#39;options&#39;]=None<br></td></tr
><tr
id=sl_svn27_136

 onmouseover="gutterOver(136)"

><td class="source">        d[&#39;data&#39;]=s[4*d[&#39;header_len&#39;]:]#shove from header length on (20 bytes in)<br></td></tr
><tr
id=sl_svn27_137

 onmouseover="gutterOver(137)"

><td class="source">        return d#return our new dictonary with the ip stuff parsed out<br></td></tr
><tr
id=sl_svn27_138

 onmouseover="gutterOver(138)"

><td class="source">        #it seems this entire function is pretty useless to us, all we need is headerlen to figure out where the datastarts<br></td></tr
><tr
id=sl_svn27_139

 onmouseover="gutterOver(139)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_140

 onmouseover="gutterOver(140)"

><td class="source">   <br></td></tr
><tr
id=sl_svn27_141

 onmouseover="gutterOver(141)"

><td class="source">    def dumphex(self,s):<br></td></tr
><tr
id=sl_svn27_142

 onmouseover="gutterOver(142)"

><td class="source">        bytes = map(lambda x: &#39;%.2x&#39; % x, map(ord, s))<br></td></tr
><tr
id=sl_svn27_143

 onmouseover="gutterOver(143)"

><td class="source">        for i in xrange(0,len(bytes)/16):<br></td></tr
><tr
id=sl_svn27_144

 onmouseover="gutterOver(144)"

><td class="source">            print &#39;        %s&#39; % string.join(bytes[i*16:(i+1)*16],&#39; &#39;)<br></td></tr
><tr
id=sl_svn27_145

 onmouseover="gutterOver(145)"

><td class="source">        print &#39;        %s&#39; % string.join(bytes[(i+1)*16:],&#39; &#39;)<br></td></tr
><tr
id=sl_svn27_146

 onmouseover="gutterOver(146)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_147

 onmouseover="gutterOver(147)"

><td class="source">    def _connadd(self,data,dict_name):<br></td></tr
><tr
id=sl_svn27_148

 onmouseover="gutterOver(148)"

><td class="source">        self.con_size = self.con_size + 1;<br></td></tr
><tr
id=sl_svn27_149

 onmouseover="gutterOver(149)"

><td class="source">       # user_agent = #different timeouts for different browsers, will use a lookup table for the common ones, use some false one for the rest<br></td></tr
><tr
id=sl_svn27_150

 onmouseover="gutterOver(150)"

><td class="source">       #14 + 4 * (ord(data[14]) &amp; 0x0f) port ie tcp:0 <br></td></tr
><tr
id=sl_svn27_151

 onmouseover="gutterOver(151)"

><td class="source">       #s[tcp[&#39;tcphdr_len&#39;]/4:]<br></td></tr
><tr
id=sl_svn27_152

 onmouseover="gutterOver(152)"

><td class="source">       #  <br></td></tr
><tr
id=sl_svn27_153

 onmouseover="gutterOver(153)"

><td class="source">        if re.search((&#39;Firefox&#39;),str(data)) != None:#doesnt work<br></td></tr
><tr
id=sl_svn27_154

 onmouseover="gutterOver(154)"

><td class="source">            self.connections[dict_name] = 300 + time.time()<br></td></tr
><tr
id=sl_svn27_155

 onmouseover="gutterOver(155)"

><td class="source">        elif re.search(&#39;Opera&#39;,str(data)) != None:<br></td></tr
><tr
id=sl_svn27_156

 onmouseover="gutterOver(156)"

><td class="source">            self.connections[dict_name] = 300 + time.time()#bald faced lie, cant find the real number<br></td></tr
><tr
id=sl_svn27_157

 onmouseover="gutterOver(157)"

><td class="source">        elif re.search(&#39;MSIE&#39;,str(data)) != None:<br></td></tr
><tr
id=sl_svn27_158

 onmouseover="gutterOver(158)"

><td class="source">            self.connections[dict_name] = 60 + time.time()<br></td></tr
><tr
id=sl_svn27_159

 onmouseover="gutterOver(159)"

><td class="source">        elif re.search(&#39;Chrome&#39;,str(data)) != None:<br></td></tr
><tr
id=sl_svn27_160

 onmouseover="gutterOver(160)"

><td class="source">            self.connections[dict_name] = 300 + time.time()<br></td></tr
><tr
id=sl_svn27_161

 onmouseover="gutterOver(161)"

><td class="source">        else:<br></td></tr
><tr
id=sl_svn27_162

 onmouseover="gutterOver(162)"

><td class="source">            self.connections[dict_name] = 300 + time.time()<br></td></tr
><tr
id=sl_svn27_163

 onmouseover="gutterOver(163)"

><td class="source">        print self.con_size<br></td></tr
><tr
id=sl_svn27_164

 onmouseover="gutterOver(164)"

><td class="source">        print &quot;\n\n&quot;<br></td></tr
><tr
id=sl_svn27_165

 onmouseover="gutterOver(165)"

><td class="source">    def _connupdate(self,data,dict_name):<br></td></tr
><tr
id=sl_svn27_166

 onmouseover="gutterOver(166)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_167

 onmouseover="gutterOver(167)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_168

 onmouseover="gutterOver(168)"

><td class="source">        if re.search((&#39;Firefox&#39;),str(data)) != None:#search the entire packet for the string Firefox, so we know its timeout time<br></td></tr
><tr
id=sl_svn27_169

 onmouseover="gutterOver(169)"

><td class="source">            self.connections[dict_name] = 300 + time.time()<br></td></tr
><tr
id=sl_svn27_170

 onmouseover="gutterOver(170)"

><td class="source">        elif re.search(&#39;Opera&#39;,str(data)) != None:<br></td></tr
><tr
id=sl_svn27_171

 onmouseover="gutterOver(171)"

><td class="source">            self.connections[dict_name] = 300 + time.time()#bald faced lie, cant find the real number<br></td></tr
><tr
id=sl_svn27_172

 onmouseover="gutterOver(172)"

><td class="source">        elif re.search(&#39;MSIE&#39;,str(data)) != None:<br></td></tr
><tr
id=sl_svn27_173

 onmouseover="gutterOver(173)"

><td class="source">            self.connections[dict_name] = 60 + time.time()<br></td></tr
><tr
id=sl_svn27_174

 onmouseover="gutterOver(174)"

><td class="source">        elif re.search(&#39;Chrome&#39;,str(data)) != None:<br></td></tr
><tr
id=sl_svn27_175

 onmouseover="gutterOver(175)"

><td class="source">            self.connections[dict_name] = 300 + time.time()#assuming since its from mozilla its the same<br></td></tr
><tr
id=sl_svn27_176

 onmouseover="gutterOver(176)"

><td class="source">        else:<br></td></tr
><tr
id=sl_svn27_177

 onmouseover="gutterOver(177)"

><td class="source">            self.connections[dict_name] = 300 + time.time()<br></td></tr
><tr
id=sl_svn27_178

 onmouseover="gutterOver(178)"

><td class="source">    def _cleanconnections(self):<br></td></tr
><tr
id=sl_svn27_179

 onmouseover="gutterOver(179)"

><td class="source">        for member in self.connections:<br></td></tr
><tr
id=sl_svn27_180

 onmouseover="gutterOver(180)"

><td class="source">            if member &gt; time.time():<br></td></tr
><tr
id=sl_svn27_181

 onmouseover="gutterOver(181)"

><td class="source">                del member<br></td></tr
><tr
id=sl_svn27_182

 onmouseover="gutterOver(182)"

><td class="source">                self.con_size = self.con_size - 1<br></td></tr
><tr
id=sl_svn27_183

 onmouseover="gutterOver(183)"

><td class="source">            else:<br></td></tr
><tr
id=sl_svn27_184

 onmouseover="gutterOver(184)"

><td class="source">                pass<br></td></tr
><tr
id=sl_svn27_185

 onmouseover="gutterOver(185)"

><td class="source">    def print_packet(self, pkthdr, data):<br></td></tr
><tr
id=sl_svn27_186

 onmouseover="gutterOver(186)"

><td class="source">        if not data:#if the packet is blank we look for a new one<br></td></tr
><tr
id=sl_svn27_187

 onmouseover="gutterOver(187)"

><td class="source">            return<br></td></tr
><tr
id=sl_svn27_188

 onmouseover="gutterOver(188)"

><td class="source">        if data[12:14]==&#39;\x08\x00&#39;:#if spots 12 and 13 are 0800 then its ethertype is ipv4 and we are good<br></td></tr
><tr
id=sl_svn27_189

 onmouseover="gutterOver(189)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_190

 onmouseover="gutterOver(190)"

><td class="source">            src_addr = socket.inet_ntoa(data[26:30])<br></td></tr
><tr
id=sl_svn27_191

 onmouseover="gutterOver(191)"

><td class="source">            dst_addr = socket.inet_ntoa(data[30:34])<br></td></tr
><tr
id=sl_svn27_192

 onmouseover="gutterOver(192)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_193

 onmouseover="gutterOver(193)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_194

 onmouseover="gutterOver(194)"

><td class="source">            port = socket.ntohs(struct.unpack(&#39;H&#39;,data[14 + 4 * (ord(data[14]) &amp; 0x0f):2 + 14 + 4 * (ord(data[14]) &amp; 0x0f)])[0])  if  socket.ntohs(struct.unpack(&#39;H&#39;,data[14 + 4 * (ord(data[14]) &amp; 0x0f):2 + 14 + 4 * (ord(data[14]) &amp; 0x0f)])[0]) != 80 else socket.ntohs(struct.unpack(&#39;H&#39;,data[2 + 14 + 4 * (ord(data[14]) &amp; 0x0f):4 + 14 + 4 * (ord(data[14]) &amp; 0x0f)])[0])<br></td></tr
><tr
id=sl_svn27_195

 onmouseover="gutterOver(195)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_196

 onmouseover="gutterOver(196)"

><td class="source">            if str(src_addr) + str(port) in self.connections or str(dst_addr) + str(port) in self.connections:<br></td></tr
><tr
id=sl_svn27_197

 onmouseover="gutterOver(197)"

><td class="source">                if str(src_addr) + str(port) in self.connections:#update the timeout value<br></td></tr
><tr
id=sl_svn27_198

 onmouseover="gutterOver(198)"

><td class="source">                    self._connupdate(data,str(src_addr) + str(port))<br></td></tr
><tr
id=sl_svn27_199

 onmouseover="gutterOver(199)"

><td class="source">                    grp_id = str(src_addr) + str(port)<br></td></tr
><tr
id=sl_svn27_200

 onmouseover="gutterOver(200)"

><td class="source">                    self.tcp_decode(self.decode_ip_packet(data[14:]),grp_id)#send output from ip_decode to tcp_decode, only send from 14 on (so not the frame and ethernet stuff<br></td></tr
><tr
id=sl_svn27_201

 onmouseover="gutterOver(201)"

><td class="source">                else:<br></td></tr
><tr
id=sl_svn27_202

 onmouseover="gutterOver(202)"

><td class="source">                    self._connupdate(data,str(dst_addr) + str(port))<br></td></tr
><tr
id=sl_svn27_203

 onmouseover="gutterOver(203)"

><td class="source">                    grp_id = str(dst_addr) + str(port)<br></td></tr
><tr
id=sl_svn27_204

 onmouseover="gutterOver(204)"

><td class="source">                    self.tcp_decode(self.decode_ip_packet(data[14:]),grp_id)<br></td></tr
><tr
id=sl_svn27_205

 onmouseover="gutterOver(205)"

><td class="source">            elif self.con_size &lt; 500:#add to the connections if its small<br></td></tr
><tr
id=sl_svn27_206

 onmouseover="gutterOver(206)"

><td class="source">                self._connadd(data,str(src_addr) + str(port))<br></td></tr
><tr
id=sl_svn27_207

 onmouseover="gutterOver(207)"

><td class="source">                grp_id = str(src_addr) + str(port)<br></td></tr
><tr
id=sl_svn27_208

 onmouseover="gutterOver(208)"

><td class="source">                self.tcp_decode(self.decode_ip_packet(data[14:]),grp_id)<br></td></tr
><tr
id=sl_svn27_209

 onmouseover="gutterOver(209)"

><td class="source">            else:<br></td></tr
><tr
id=sl_svn27_210

 onmouseover="gutterOver(210)"

><td class="source">                if (time.time() - self.time_update) &gt; 60:#clean the connections table every minutes, could go longer or shorter if needed<br></td></tr
><tr
id=sl_svn27_211

 onmouseover="gutterOver(211)"

><td class="source">                    self.time_update = time.time()<br></td></tr
><tr
id=sl_svn27_212

 onmouseover="gutterOver(212)"

><td class="source">                    self._cleanconnections()<br></td></tr
><tr
id=sl_svn27_213

 onmouseover="gutterOver(213)"

><td class="source">         <br></td></tr
><tr
id=sl_svn27_214

 onmouseover="gutterOver(214)"

><td class="source">                <br></td></tr
><tr
id=sl_svn27_215

 onmouseover="gutterOver(215)"

><td class="source">    def tcp_decode(self, d, grp_id):<br></td></tr
><tr
id=sl_svn27_216

 onmouseover="gutterOver(216)"

><td class="source">        s = d[&#39;data&#39;]#s holds the tcp and beyond data<br></td></tr
><tr
id=sl_svn27_217

 onmouseover="gutterOver(217)"

><td class="source">        tcp = {}<br></td></tr
><tr
id=sl_svn27_218

 onmouseover="gutterOver(218)"

><td class="source">        tcp[&#39;ip_header&#39;] = d#ip_header holds the header and the data<br></td></tr
><tr
id=sl_svn27_219

 onmouseover="gutterOver(219)"

><td class="source">        tcp[&#39;bytes&#39;] = map(lambda x: &#39;%.2x&#39; % x, map(ord, s))#for each number in the entire string of numbers, store the two bit hex of the unicode of the number into bytes <br></td></tr
><tr
id=sl_svn27_220

 onmouseover="gutterOver(220)"

><td class="source">        tcp[&#39;src_port&#39;] = socket.ntohs(struct.unpack(&#39;H&#39;,s[0:2])[0])<br></td></tr
><tr
id=sl_svn27_221

 onmouseover="gutterOver(221)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_222

 onmouseover="gutterOver(222)"

><td class="source">        tcp[&#39;dst_port&#39;] = socket.ntohs(struct.unpack(&#39;H&#39;,s[2:4])[0])<br></td></tr
><tr
id=sl_svn27_223

 onmouseover="gutterOver(223)"

><td class="source">    <br></td></tr
><tr
id=sl_svn27_224

 onmouseover="gutterOver(224)"

><td class="source">        tcp[&#39;seq&#39;] = socket.ntohs(struct.unpack(&#39;HH&#39;,s[4:8])[0])<br></td></tr
><tr
id=sl_svn27_225

 onmouseover="gutterOver(225)"

><td class="source">        tcp[&#39;ack&#39;] = socket.ntohs(struct.unpack(&#39;HH&#39;,s[8:12])[0])<br></td></tr
><tr
id=sl_svn27_226

 onmouseover="gutterOver(226)"

><td class="source">        tcp[&#39;tcphdr_len&#39;] = int(str(tcp[&#39;bytes&#39;][12:13][0]), 16)<br></td></tr
><tr
id=sl_svn27_227

 onmouseover="gutterOver(227)"

><td class="source">        tcp[&#39;flags&#39;] = ord(s[13:14])<br></td></tr
><tr
id=sl_svn27_228

 onmouseover="gutterOver(228)"

><td class="source">        tcp[&#39;window_size&#39;] = socket.ntohs(struct.unpack(&#39;H&#39;,s[14:16])[0])<br></td></tr
><tr
id=sl_svn27_229

 onmouseover="gutterOver(229)"

><td class="source">        tcp[&#39;checksum&#39;] = socket.ntohs(struct.unpack(&#39;H&#39;,s[16:18])[0])<br></td></tr
><tr
id=sl_svn27_230

 onmouseover="gutterOver(230)"

><td class="source">        #options somewhere in here<br></td></tr
><tr
id=sl_svn27_231

 onmouseover="gutterOver(231)"

><td class="source">        tcp[&#39;data&#39;] = s[tcp[&#39;tcphdr_len&#39;]/4:]<br></td></tr
><tr
id=sl_svn27_232

 onmouseover="gutterOver(232)"

><td class="source">        #if (flags == 16 or flags == 24): #10 and 18 in hex<br></td></tr
><tr
id=sl_svn27_233

 onmouseover="gutterOver(233)"

><td class="source">        if(str(tcp[&#39;data&#39;]).lower().find(&#39;http&#39;) !=-1):<br></td></tr
><tr
id=sl_svn27_234

 onmouseover="gutterOver(234)"

><td class="source">            #print &quot;\n\nstarting tcp data\n\n\n&quot;<br></td></tr
><tr
id=sl_svn27_235

 onmouseover="gutterOver(235)"

><td class="source">            #print str(tcp[&#39;data&#39;]).lower()<br></td></tr
><tr
id=sl_svn27_236

 onmouseover="gutterOver(236)"

><td class="source">           # print &quot;\n\nending tcp data\n\n\n&quot;<br></td></tr
><tr
id=sl_svn27_237

 onmouseover="gutterOver(237)"

><td class="source">            self.http_decode(tcp, grp_id)<br></td></tr
><tr
id=sl_svn27_238

 onmouseover="gutterOver(238)"

><td class="source">   <br></td></tr
><tr
id=sl_svn27_239

 onmouseover="gutterOver(239)"

><td class="source">    def parse_setcookie(self, cookie_list):<br></td></tr
><tr
id=sl_svn27_240

 onmouseover="gutterOver(240)"

><td class="source">        cookiejar = []<br></td></tr
><tr
id=sl_svn27_241

 onmouseover="gutterOver(241)"

><td class="source">        for cookie in cookie_list:<br></td></tr
><tr
id=sl_svn27_242

 onmouseover="gutterOver(242)"

><td class="source">            #take apart the cookie and make into a dictionary.  There is a cookie module for python, but i&#39;m not sure if it would be easier<br></td></tr
><tr
id=sl_svn27_243

 onmouseover="gutterOver(243)"

><td class="source">            cookie = str(cookie).lower()<br></td></tr
><tr
id=sl_svn27_244

 onmouseover="gutterOver(244)"

><td class="source">            cookie_dict = {}<br></td></tr
><tr
id=sl_svn27_245

 onmouseover="gutterOver(245)"

><td class="source">           <br></td></tr
><tr
id=sl_svn27_246

 onmouseover="gutterOver(246)"

><td class="source">            domain_result = self.domain_re.match(str(cookie))<br></td></tr
><tr
id=sl_svn27_247

 onmouseover="gutterOver(247)"

><td class="source">            if (domain_result):<br></td></tr
><tr
id=sl_svn27_248

 onmouseover="gutterOver(248)"

><td class="source">                cookie_dict[&#39;domain&#39;] = domain_result.group(&#39;domain&#39;)<br></td></tr
><tr
id=sl_svn27_249

 onmouseover="gutterOver(249)"

><td class="source">                print &quot;\t:-) Cookie domain: &quot; + cookie_dict[&#39;domain&#39;]<br></td></tr
><tr
id=sl_svn27_250

 onmouseover="gutterOver(250)"

><td class="source">            else:<br></td></tr
><tr
id=sl_svn27_251

 onmouseover="gutterOver(251)"

><td class="source">                print &quot;\t:-( Cookie: &quot; + cookie<br></td></tr
><tr
id=sl_svn27_252

 onmouseover="gutterOver(252)"

><td class="source">                continue # skip to next cookie<br></td></tr
><tr
id=sl_svn27_253

 onmouseover="gutterOver(253)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_254

 onmouseover="gutterOver(254)"

><td class="source">           <br></td></tr
><tr
id=sl_svn27_255

 onmouseover="gutterOver(255)"

><td class="source">            query = &quot;SELECT id, domain FROM domains WHERE domain =&#39;&quot; + cookie_dict[&#39;domain&#39;] + &quot;&#39;&quot;<br></td></tr
><tr
id=sl_svn27_256

 onmouseover="gutterOver(256)"

><td class="source">            try:<br></td></tr
><tr
id=sl_svn27_257

 onmouseover="gutterOver(257)"

><td class="source">                self.cursor.execute(query)<br></td></tr
><tr
id=sl_svn27_258

 onmouseover="gutterOver(258)"

><td class="source">            except:<br></td></tr
><tr
id=sl_svn27_259

 onmouseover="gutterOver(259)"

><td class="source">                continue #go to next cookie<br></td></tr
><tr
id=sl_svn27_260

 onmouseover="gutterOver(260)"

><td class="source">            for row in self.cursor:<br></td></tr
><tr
id=sl_svn27_261

 onmouseover="gutterOver(261)"

><td class="source">                if(row[&#39;domain&#39;]== cookie_dict[&#39;domain&#39;]):#if the domains in this cookie have already been seen<br></td></tr
><tr
id=sl_svn27_262

 onmouseover="gutterOver(262)"

><td class="source">                    cookie_dict[&#39;id&#39;] = row[&#39;id&#39;]<br></td></tr
><tr
id=sl_svn27_263

 onmouseover="gutterOver(263)"

><td class="source">            if( not cookie_dict.has_key(&#39;id&#39;)): #this domain wasn&#39;t already in the db<br></td></tr
><tr
id=sl_svn27_264

 onmouseover="gutterOver(264)"

><td class="source">                value = (cookie_dict[&#39;domain&#39;],)<br></td></tr
><tr
id=sl_svn27_265

 onmouseover="gutterOver(265)"

><td class="source">                host_list = str(cookie_dict[&#39;domain&#39;]).split(&#39;.&#39;)<br></td></tr
><tr
id=sl_svn27_266

 onmouseover="gutterOver(266)"

><td class="source">                host_str = host_list[len(host_list)-2] + &quot;.&quot; + host_list[len(host_list)-1]<br></td></tr
><tr
id=sl_svn27_267

 onmouseover="gutterOver(267)"

><td class="source">                self.cursor.execute(&quot;SELECT id FROM domains WHERE domain = %s AND has_bug = 0&quot;,host_str)<br></td></tr
><tr
id=sl_svn27_268

 onmouseover="gutterOver(268)"

><td class="source">                row = self.cursor.fetchone()<br></td></tr
><tr
id=sl_svn27_269

 onmouseover="gutterOver(269)"

><td class="source">                if(row == None):<br></td></tr
><tr
id=sl_svn27_270

 onmouseover="gutterOver(270)"

><td class="source">                    cookie_dict[&#39;id&#39;] = self.cursor.execute(&quot;INSERT INTO domains(domain,has_bug) VALUES (%s,0)&quot;, host_str)#add it to the table<br></td></tr
><tr
id=sl_svn27_271

 onmouseover="gutterOver(271)"

><td class="source">                else:<br></td></tr
><tr
id=sl_svn27_272

 onmouseover="gutterOver(272)"

><td class="source">                    cookie_dict[&#39;id&#39;] = row[&#39;id&#39;]<br></td></tr
><tr
id=sl_svn27_273

 onmouseover="gutterOver(273)"

><td class="source">           <br></td></tr
><tr
id=sl_svn27_274

 onmouseover="gutterOver(274)"

><td class="source">            expiry_result = self.expiry_re.match(str(cookie))<br></td></tr
><tr
id=sl_svn27_275

 onmouseover="gutterOver(275)"

><td class="source">            if (expiry_result):<br></td></tr
><tr
id=sl_svn27_276

 onmouseover="gutterOver(276)"

><td class="source">                cookie_dict[&#39;session&#39;] = 0<br></td></tr
><tr
id=sl_svn27_277

 onmouseover="gutterOver(277)"

><td class="source">                try:<br></td></tr
><tr
id=sl_svn27_278

 onmouseover="gutterOver(278)"

><td class="source">                    cookie_dict[&#39;expiry&#39;] = str(datetime.datetime(*time.strptime(expiry_result.group(&#39;expiry&#39;), &#39;%a, %d-%b-%Y %H:%M:%S %Z&#39;)[0:6]))<br></td></tr
><tr
id=sl_svn27_279

 onmouseover="gutterOver(279)"

><td class="source">                    print &quot;\t:-) Expires: &quot; + cookie_dict[&#39;expiry&#39;]<br></td></tr
><tr
id=sl_svn27_280

 onmouseover="gutterOver(280)"

><td class="source">                except ValueError:<br></td></tr
><tr
id=sl_svn27_281

 onmouseover="gutterOver(281)"

><td class="source">                    break #ignore incorrectly formatted cookies<br></td></tr
><tr
id=sl_svn27_282

 onmouseover="gutterOver(282)"

><td class="source">                    print &quot;:-( Value Error: &quot; + expiry_result.group(&#39;expiry&#39;)<br></td></tr
><tr
id=sl_svn27_283

 onmouseover="gutterOver(283)"

><td class="source">            else:<br></td></tr
><tr
id=sl_svn27_284

 onmouseover="gutterOver(284)"

><td class="source">                cookie_dict[&#39;session&#39;] = 1<br></td></tr
><tr
id=sl_svn27_285

 onmouseover="gutterOver(285)"

><td class="source">                cookie_dict[&#39;expiry&#39;] = &quot;&quot;<br></td></tr
><tr
id=sl_svn27_286

 onmouseover="gutterOver(286)"

><td class="source">                print &quot;No Expires: &quot; + cookie<br></td></tr
><tr
id=sl_svn27_287

 onmouseover="gutterOver(287)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_288

 onmouseover="gutterOver(288)"

><td class="source">           <br></td></tr
><tr
id=sl_svn27_289

 onmouseover="gutterOver(289)"

><td class="source">            print &quot;\tCookie from domain &quot; + cookie_dict[&#39;domain&#39;]<br></td></tr
><tr
id=sl_svn27_290

 onmouseover="gutterOver(290)"

><td class="source">            cookiejar.append(cookie_dict)<br></td></tr
><tr
id=sl_svn27_291

 onmouseover="gutterOver(291)"

><td class="source">        return cookiejar<br></td></tr
><tr
id=sl_svn27_292

 onmouseover="gutterOver(292)"

><td class="source">   <br></td></tr
><tr
id=sl_svn27_293

 onmouseover="gutterOver(293)"

><td class="source">    def parse_cookie(self, raw_cookie, host):<br></td></tr
><tr
id=sl_svn27_294

 onmouseover="gutterOver(294)"

><td class="source">        cookie = str(raw_cookie).lower()<br></td></tr
><tr
id=sl_svn27_295

 onmouseover="gutterOver(295)"

><td class="source">        cookie_dict = {}<br></td></tr
><tr
id=sl_svn27_296

 onmouseover="gutterOver(296)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_297

 onmouseover="gutterOver(297)"

><td class="source">        if(raw_cookie.find(&#39;domain=&#39;) == -1):<br></td></tr
><tr
id=sl_svn27_298

 onmouseover="gutterOver(298)"

><td class="source">            cookie_dict[&#39;domain&#39;] = host<br></td></tr
><tr
id=sl_svn27_299

 onmouseover="gutterOver(299)"

><td class="source">        else:<br></td></tr
><tr
id=sl_svn27_300

 onmouseover="gutterOver(300)"

><td class="source">            print &quot;##### Cookie to be parsed: &quot; + raw_cookie<br></td></tr
><tr
id=sl_svn27_301

 onmouseover="gutterOver(301)"

><td class="source">            return cookie_dict<br></td></tr
><tr
id=sl_svn27_302

 onmouseover="gutterOver(302)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_303

 onmouseover="gutterOver(303)"

><td class="source">        query = &quot;SELECT id, domain FROM domains WHERE domain=&#39;&quot; + cookie_dict[&#39;domain&#39;] + &quot;&#39;&quot;<br></td></tr
><tr
id=sl_svn27_304

 onmouseover="gutterOver(304)"

><td class="source">        self.cursor.execute(query)<br></td></tr
><tr
id=sl_svn27_305

 onmouseover="gutterOver(305)"

><td class="source">        for row in self.cursor:<br></td></tr
><tr
id=sl_svn27_306

 onmouseover="gutterOver(306)"

><td class="source">            if(row[&#39;domain&#39;] == cookie_dict[&#39;domain&#39;]):#if any of the domains in this cookie have already been seen, remove from the list and put their ID on the id_list<br></td></tr
><tr
id=sl_svn27_307

 onmouseover="gutterOver(307)"

><td class="source">                cookie_dict[&#39;id&#39;] = row[&#39;id&#39;]<br></td></tr
><tr
id=sl_svn27_308

 onmouseover="gutterOver(308)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_309

 onmouseover="gutterOver(309)"

><td class="source">        if( not cookie_dict.has_key(&#39;id&#39;)): #this domain wasn&#39;t already in the db<br></td></tr
><tr
id=sl_svn27_310

 onmouseover="gutterOver(310)"

><td class="source">            value = (cookie_dict[&#39;domain&#39;],)<br></td></tr
><tr
id=sl_svn27_311

 onmouseover="gutterOver(311)"

><td class="source">            print &quot;\n\n\n\n\n\n&quot;<br></td></tr
><tr
id=sl_svn27_312

 onmouseover="gutterOver(312)"

><td class="source">            print cookie_dict[&#39;domain&#39;]<br></td></tr
><tr
id=sl_svn27_313

 onmouseover="gutterOver(313)"

><td class="source">            print &quot;\n\n\n\n\n\n&quot;<br></td></tr
><tr
id=sl_svn27_314

 onmouseover="gutterOver(314)"

><td class="source">            host_list = str(cookie_dict[&#39;domain&#39;]).split(&#39;.&#39;)<br></td></tr
><tr
id=sl_svn27_315

 onmouseover="gutterOver(315)"

><td class="source">            host_str = host_list[len(host_list)-2] + &quot;.&quot; + host_list[len(host_list)-1]<br></td></tr
><tr
id=sl_svn27_316

 onmouseover="gutterOver(316)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_317

 onmouseover="gutterOver(317)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_318

 onmouseover="gutterOver(318)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_319

 onmouseover="gutterOver(319)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_320

 onmouseover="gutterOver(320)"

><td class="source">            self.cursor.execute(&quot;SELECT id FROM domains WHERE domain = %s AND has_bug = 0&quot;,host_str)<br></td></tr
><tr
id=sl_svn27_321

 onmouseover="gutterOver(321)"

><td class="source">            row = self.cursor.fetchone()<br></td></tr
><tr
id=sl_svn27_322

 onmouseover="gutterOver(322)"

><td class="source">            if(row == None):<br></td></tr
><tr
id=sl_svn27_323

 onmouseover="gutterOver(323)"

><td class="source">                cookie_dict[&#39;id&#39;] = self.cursor.execute(&quot;INSERT INTO domains(domain,has_bug) VALUES (%s,0)&quot;, host_str)#add it to the table<br></td></tr
><tr
id=sl_svn27_324

 onmouseover="gutterOver(324)"

><td class="source">            else:<br></td></tr
><tr
id=sl_svn27_325

 onmouseover="gutterOver(325)"

><td class="source">                cookie_dict[&#39;id&#39;] = row[&#39;id&#39;]<br></td></tr
><tr
id=sl_svn27_326

 onmouseover="gutterOver(326)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_327

 onmouseover="gutterOver(327)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_328

 onmouseover="gutterOver(328)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_329

 onmouseover="gutterOver(329)"

><td class="source">        cookie_dict[&#39;session&#39;] = &quot;&quot;<br></td></tr
><tr
id=sl_svn27_330

 onmouseover="gutterOver(330)"

><td class="source">        cookie_dict[&#39;expiry&#39;] = &quot;&quot;<br></td></tr
><tr
id=sl_svn27_331

 onmouseover="gutterOver(331)"

><td class="source">        print &quot;\tCookie for domain &quot; + cookie_dict[&#39;domain&#39;]<br></td></tr
><tr
id=sl_svn27_332

 onmouseover="gutterOver(332)"

><td class="source">        return cookie_dict<br></td></tr
><tr
id=sl_svn27_333

 onmouseover="gutterOver(333)"

><td class="source">   <br></td></tr
><tr
id=sl_svn27_334

 onmouseover="gutterOver(334)"

><td class="source">    def is_resnet(self,ip):<br></td></tr
><tr
id=sl_svn27_335

 onmouseover="gutterOver(335)"

><td class="source">        #resnet =  2160192768 - 2160197631 (128.193.237.0 - 128.193.255.255)<br></td></tr
><tr
id=sl_svn27_336

 onmouseover="gutterOver(336)"

><td class="source">        int_ip = struct.unpack(&#39;i&#39;,socket.inet_aton(ip))[0]<br></td></tr
><tr
id=sl_svn27_337

 onmouseover="gutterOver(337)"

><td class="source">        if(int_ip &gt; 2160192768 and int_ip &lt; 2160197631):<br></td></tr
><tr
id=sl_svn27_338

 onmouseover="gutterOver(338)"

><td class="source">            return True<br></td></tr
><tr
id=sl_svn27_339

 onmouseover="gutterOver(339)"

><td class="source">        return False<br></td></tr
><tr
id=sl_svn27_340

 onmouseover="gutterOver(340)"

><td class="source">   <br></td></tr
><tr
id=sl_svn27_341

 onmouseover="gutterOver(341)"

><td class="source">    def http_decode(self,tcp,grp_id):<br></td></tr
><tr
id=sl_svn27_342

 onmouseover="gutterOver(342)"

><td class="source">        data = tcp[&#39;data&#39;]<br></td></tr
><tr
id=sl_svn27_343

 onmouseover="gutterOver(343)"

><td class="source">        seq = tcp[&#39;seq&#39;]<br></td></tr
><tr
id=sl_svn27_344

 onmouseover="gutterOver(344)"

><td class="source">        ack = tcp[&#39;ack&#39;]<br></td></tr
><tr
id=sl_svn27_345

 onmouseover="gutterOver(345)"

><td class="source">        http_parameters={}<br></td></tr
><tr
id=sl_svn27_346

 onmouseover="gutterOver(346)"

><td class="source">        start = 0<br></td></tr
><tr
id=sl_svn27_347

 onmouseover="gutterOver(347)"

><td class="source">        end = str(data).find(&#39;\r\n\r\n&#39;)<br></td></tr
><tr
id=sl_svn27_348

 onmouseover="gutterOver(348)"

><td class="source">        bug = 0<br></td></tr
><tr
id=sl_svn27_349

 onmouseover="gutterOver(349)"

><td class="source">        bugsize = 0<br></td></tr
><tr
id=sl_svn27_350

 onmouseover="gutterOver(350)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_351

 onmouseover="gutterOver(351)"

><td class="source">        try:<br></td></tr
><tr
id=sl_svn27_352

 onmouseover="gutterOver(352)"

><td class="source">            #Get Request<br></td></tr
><tr
id=sl_svn27_353

 onmouseover="gutterOver(353)"

><td class="source">            get_result = self.get_re.match(str(data))<br></td></tr
><tr
id=sl_svn27_354

 onmouseover="gutterOver(354)"

><td class="source">            if (get_result):<br></td></tr
><tr
id=sl_svn27_355

 onmouseover="gutterOver(355)"

><td class="source">                get = get_result.group(&#39;get&#39;)<br></td></tr
><tr
id=sl_svn27_356

 onmouseover="gutterOver(356)"

><td class="source">                qmark = str(get).lower().find(&#39;?&#39;)<br></td></tr
><tr
id=sl_svn27_357

 onmouseover="gutterOver(357)"

><td class="source">                if(qmark != -1):<br></td></tr
><tr
id=sl_svn27_358

 onmouseover="gutterOver(358)"

><td class="source">                    http_parameters[&#39;get&#39;] = get[0:qmark]<br></td></tr
><tr
id=sl_svn27_359

 onmouseover="gutterOver(359)"

><td class="source">                else:<br></td></tr
><tr
id=sl_svn27_360

 onmouseover="gutterOver(360)"

><td class="source">                    http_parameters[&#39;get&#39;] = get<br></td></tr
><tr
id=sl_svn27_361

 onmouseover="gutterOver(361)"

><td class="source">                start = str(data).find(&#39;HTTP&#39;)+ 10 # http/1.1\r\n<br></td></tr
><tr
id=sl_svn27_362

 onmouseover="gutterOver(362)"

><td class="source">           <br></td></tr
><tr
id=sl_svn27_363

 onmouseover="gutterOver(363)"

><td class="source">            #Responce and its status<br></td></tr
><tr
id=sl_svn27_364

 onmouseover="gutterOver(364)"

><td class="source">            status_result = self.status_re.match(str(data))<br></td></tr
><tr
id=sl_svn27_365

 onmouseover="gutterOver(365)"

><td class="source">            if (status_result):<br></td></tr
><tr
id=sl_svn27_366

 onmouseover="gutterOver(366)"

><td class="source">                http_parameters[&#39;status&#39;] = status_result.group(&#39;status&#39;)<br></td></tr
><tr
id=sl_svn27_367

 onmouseover="gutterOver(367)"

><td class="source">                start = str(data).find(&#39;\r\n&#39;)+2 # http/x.x xxx text\r\n<br></td></tr
><tr
id=sl_svn27_368

 onmouseover="gutterOver(368)"

><td class="source">           <br></td></tr
><tr
id=sl_svn27_369

 onmouseover="gutterOver(369)"

><td class="source">            data_list = re.split(&quot;\r\n&quot;, str(data)[start:end])<br></td></tr
><tr
id=sl_svn27_370

 onmouseover="gutterOver(370)"

><td class="source">            if(start &gt; end):<br></td></tr
><tr
id=sl_svn27_371

 onmouseover="gutterOver(371)"

><td class="source">                return<br></td></tr
><tr
id=sl_svn27_372

 onmouseover="gutterOver(372)"

><td class="source">         <br></td></tr
><tr
id=sl_svn27_373

 onmouseover="gutterOver(373)"

><td class="source">            for line in data_list:<br></td></tr
><tr
id=sl_svn27_374

 onmouseover="gutterOver(374)"

><td class="source">                #print str(line)<br></td></tr
><tr
id=sl_svn27_375

 onmouseover="gutterOver(375)"

><td class="source">                if(line != &#39;&#39;):<br></td></tr
><tr
id=sl_svn27_376

 onmouseover="gutterOver(376)"

><td class="source">                    key,value = re.split(&quot;: &quot;, line)<br></td></tr
><tr
id=sl_svn27_377

 onmouseover="gutterOver(377)"

><td class="source">                    if(key.lower() == &quot;set-cookie&quot; or key.lower() == &quot;set-cookie2&quot;):<br></td></tr
><tr
id=sl_svn27_378

 onmouseover="gutterOver(378)"

><td class="source">                        if(not http_parameters.has_key(key.lower())):<br></td></tr
><tr
id=sl_svn27_379

 onmouseover="gutterOver(379)"

><td class="source">                            http_parameters[key.lower()] = []<br></td></tr
><tr
id=sl_svn27_380

 onmouseover="gutterOver(380)"

><td class="source">                        http_parameters[key.lower()].append(value)<br></td></tr
><tr
id=sl_svn27_381

 onmouseover="gutterOver(381)"

><td class="source">                    else:<br></td></tr
><tr
id=sl_svn27_382

 onmouseover="gutterOver(382)"

><td class="source">                        http_parameters[key.lower()] = value<br></td></tr
><tr
id=sl_svn27_383

 onmouseover="gutterOver(383)"

><td class="source">               <br></td></tr
><tr
id=sl_svn27_384

 onmouseover="gutterOver(384)"

><td class="source">        except KeyError: #magic fairy dust to prevent crashing; ignores packets that aren&#39;t properly parsed<br></td></tr
><tr
id=sl_svn27_385

 onmouseover="gutterOver(385)"

><td class="source">            return<br></td></tr
><tr
id=sl_svn27_386

 onmouseover="gutterOver(386)"

><td class="source">        except ValueError:<br></td></tr
><tr
id=sl_svn27_387

 onmouseover="gutterOver(387)"

><td class="source">            return<br></td></tr
><tr
id=sl_svn27_388

 onmouseover="gutterOver(388)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_389

 onmouseover="gutterOver(389)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_390

 onmouseover="gutterOver(390)"

><td class="source">        if(http_parameters.has_key(&#39;get&#39;)):#This is a request<br></td></tr
><tr
id=sl_svn27_391

 onmouseover="gutterOver(391)"

><td class="source">            self.request_dict[seq] = http_parameters<br></td></tr
><tr
id=sl_svn27_392

 onmouseover="gutterOver(392)"

><td class="source">            self.request_dict[seq][&#39;request_time&#39;] = datetime.datetime.now()<br></td></tr
><tr
id=sl_svn27_393

 onmouseover="gutterOver(393)"

><td class="source">           <br></td></tr
><tr
id=sl_svn27_394

 onmouseover="gutterOver(394)"

><td class="source">            #resnet =  2160192768 - 2160197631 (128.193.237.0 - 128.193.255.255)<br></td></tr
><tr
id=sl_svn27_395

 onmouseover="gutterOver(395)"

><td class="source">            if( self.is_resnet(tcp[&#39;ip_header&#39;][&#39;source_address&#39;]) or self.is_resnet(tcp[&#39;ip_header&#39;][&#39;destination_address&#39;])):<br></td></tr
><tr
id=sl_svn27_396

 onmouseover="gutterOver(396)"

><td class="source">                self.request_dict[seq][&#39;residential&#39;] = 1<br></td></tr
><tr
id=sl_svn27_397

 onmouseover="gutterOver(397)"

><td class="source">            else:<br></td></tr
><tr
id=sl_svn27_398

 onmouseover="gutterOver(398)"

><td class="source">                self.request_dict[seq][&#39;residential&#39;] = 0<br></td></tr
><tr
id=sl_svn27_399

 onmouseover="gutterOver(399)"

><td class="source">            print &quot;(&quot; + str(self.request_dict[seq][&#39;residential&#39;])  + &quot;) Request #&quot; + str(seq)  + &quot; for &quot; + self.request_dict[seq][&#39;host&#39;]<br></td></tr
><tr
id=sl_svn27_400

 onmouseover="gutterOver(400)"

><td class="source">            return # don&#39;t log request packets<br></td></tr
><tr
id=sl_svn27_401

 onmouseover="gutterOver(401)"

><td class="source">        elif (self.request_dict.has_key(ack)):<br></td></tr
><tr
id=sl_svn27_402

 onmouseover="gutterOver(402)"

><td class="source">            print &quot;Matched request #&quot; + str(ack)<br></td></tr
><tr
id=sl_svn27_403

 onmouseover="gutterOver(403)"

><td class="source">            for para in self.request_dict[ack]:<br></td></tr
><tr
id=sl_svn27_404

 onmouseover="gutterOver(404)"

><td class="source">                if(not http_parameters.has_key(para)): #add any fields not in the request to the entry<br></td></tr
><tr
id=sl_svn27_405

 onmouseover="gutterOver(405)"

><td class="source">                    http_parameters[para] = self.request_dict[ack][para]<br></td></tr
><tr
id=sl_svn27_406

 onmouseover="gutterOver(406)"

><td class="source">            del self.request_dict[ack]<br></td></tr
><tr
id=sl_svn27_407

 onmouseover="gutterOver(407)"

><td class="source">        else:<br></td></tr
><tr
id=sl_svn27_408

 onmouseover="gutterOver(408)"

><td class="source">            print &quot;Unmatched response packet&quot;<br></td></tr
><tr
id=sl_svn27_409

 onmouseover="gutterOver(409)"

><td class="source">            return #a non request packet (a response) that doesn&#39;t match timething we have, drop it.<br></td></tr
><tr
id=sl_svn27_410

 onmouseover="gutterOver(410)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_411

 onmouseover="gutterOver(411)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_412

 onmouseover="gutterOver(412)"

><td class="source">        if(datetime.datetime.now() - self.last_checked &gt; datetime.timedelta(0,self.check_seconds)):<br></td></tr
><tr
id=sl_svn27_413

 onmouseover="gutterOver(413)"

><td class="source">            self.last_checked = datetime.datetime.now()<br></td></tr
><tr
id=sl_svn27_414

 onmouseover="gutterOver(414)"

><td class="source">            for key in self.request_dict.keys(): #remove requests that haven&#39;t been found.  key = seq number<br></td></tr
><tr
id=sl_svn27_415

 onmouseover="gutterOver(415)"

><td class="source">                if(datetime.datetime.now() - self.request_dict[key][&#39;request_time&#39;] &gt; datetime.timedelta(0,self.check_seconds)):<br></td></tr
><tr
id=sl_svn27_416

 onmouseover="gutterOver(416)"

><td class="source">                    del self.request_dict[key]<br></td></tr
><tr
id=sl_svn27_417

 onmouseover="gutterOver(417)"

><td class="source">            print &quot;Current request dictionary size: &quot; + str(len(self.request_dict))<br></td></tr
><tr
id=sl_svn27_418

 onmouseover="gutterOver(418)"

><td class="source">            #if(len(self.request_dict) &gt; 500):<br></td></tr
><tr
id=sl_svn27_419

 onmouseover="gutterOver(419)"

><td class="source">                #print &quot;Request Dictionary is over 500 elements, if this is not a high load time, this is a problem&quot;<br></td></tr
><tr
id=sl_svn27_420

 onmouseover="gutterOver(420)"

><td class="source">            print &quot;Running for &quot; + str (datetime.datetime.now() - self.start_time)<br></td></tr
><tr
id=sl_svn27_421

 onmouseover="gutterOver(421)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_422

 onmouseover="gutterOver(422)"

><td class="source">        query = &#39;INSERT INTO rawpkt (&#39;<br></td></tr
><tr
id=sl_svn27_423

 onmouseover="gutterOver(423)"

><td class="source">        values = []<br></td></tr
><tr
id=sl_svn27_424

 onmouseover="gutterOver(424)"

><td class="source">        cookie_domains = {} #the return list of parse_cookie<br></td></tr
><tr
id=sl_svn27_425

 onmouseover="gutterOver(425)"

><td class="source">        setcooke_domains = [] #the return list of parse_setcookie<br></td></tr
><tr
id=sl_svn27_426

 onmouseover="gutterOver(426)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_427

 onmouseover="gutterOver(427)"

><td class="source">        if(http_parameters.has_key(&#39;host&#39;)):<br></td></tr
><tr
id=sl_svn27_428

 onmouseover="gutterOver(428)"

><td class="source">            query += &quot;host, &quot;<br></td></tr
><tr
id=sl_svn27_429

 onmouseover="gutterOver(429)"

><td class="source">            values.append(str(http_parameters[&#39;host&#39;]))<br></td></tr
><tr
id=sl_svn27_430

 onmouseover="gutterOver(430)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_431

 onmouseover="gutterOver(431)"

><td class="source">        if(http_parameters.has_key(&#39;get&#39;)):<br></td></tr
><tr
id=sl_svn27_432

 onmouseover="gutterOver(432)"

><td class="source">            query += &quot;get, &quot;<br></td></tr
><tr
id=sl_svn27_433

 onmouseover="gutterOver(433)"

><td class="source">            q_mark = str(http_parameters[&#39;get&#39;]).lower().find(&#39;?&#39;)<br></td></tr
><tr
id=sl_svn27_434

 onmouseover="gutterOver(434)"

><td class="source">            if(q_mark != -1):<br></td></tr
><tr
id=sl_svn27_435

 onmouseover="gutterOver(435)"

><td class="source">                values.append(http_parameters[&#39;get&#39;][0:q_mark])<br></td></tr
><tr
id=sl_svn27_436

 onmouseover="gutterOver(436)"

><td class="source">            else:<br></td></tr
><tr
id=sl_svn27_437

 onmouseover="gutterOver(437)"

><td class="source">                values.append(http_parameters[&#39;get&#39;])<br></td></tr
><tr
id=sl_svn27_438

 onmouseover="gutterOver(438)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_439

 onmouseover="gutterOver(439)"

><td class="source">        if(http_parameters.has_key(&#39;referer&#39;)):<br></td></tr
><tr
id=sl_svn27_440

 onmouseover="gutterOver(440)"

><td class="source">            query += &quot;referer, &quot;<br></td></tr
><tr
id=sl_svn27_441

 onmouseover="gutterOver(441)"

><td class="source">            values.append(str(http_parameters[&#39;referer&#39;]))<br></td></tr
><tr
id=sl_svn27_442

 onmouseover="gutterOver(442)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_443

 onmouseover="gutterOver(443)"

><td class="source">        if(http_parameters.has_key(&#39;user-agent&#39;)):<br></td></tr
><tr
id=sl_svn27_444

 onmouseover="gutterOver(444)"

><td class="source">            query += &quot;useragent, &quot;<br></td></tr
><tr
id=sl_svn27_445

 onmouseover="gutterOver(445)"

><td class="source">            values.append(str(http_parameters[&#39;user-agent&#39;]))<br></td></tr
><tr
id=sl_svn27_446

 onmouseover="gutterOver(446)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_447

 onmouseover="gutterOver(447)"

><td class="source">        if(http_parameters.has_key(&#39;content-type&#39;)):<br></td></tr
><tr
id=sl_svn27_448

 onmouseover="gutterOver(448)"

><td class="source">            query += &quot;contenttype, &quot;<br></td></tr
><tr
id=sl_svn27_449

 onmouseover="gutterOver(449)"

><td class="source">            values.append(str(http_parameters[&#39;content-type&#39;]))<br></td></tr
><tr
id=sl_svn27_450

 onmouseover="gutterOver(450)"

><td class="source">           # print &quot;\n\n\n&quot;+str(http_parameters[&#39;content-type&#39;]).lower()+&quot;\n\n\n&quot;<br></td></tr
><tr
id=sl_svn27_451

 onmouseover="gutterOver(451)"

><td class="source">           # print re.search((&#39;gif&#39;),http_parameters[&#39;content-type&#39;])<br></td></tr
><tr
id=sl_svn27_452

 onmouseover="gutterOver(452)"

><td class="source">           # print &quot;\n\n\n\n&quot;<br></td></tr
><tr
id=sl_svn27_453

 onmouseover="gutterOver(453)"

><td class="source">            if(re.search((&#39;gif&#39;),http_parameters[&#39;content-type&#39;]) != None or re.search((&#39;png&#39;),http_parameters[&#39;content-type&#39;]) != None):<br></td></tr
><tr
id=sl_svn27_454

 onmouseover="gutterOver(454)"

><td class="source">                #its a gif set something to 1<br></td></tr
><tr
id=sl_svn27_455

 onmouseover="gutterOver(455)"

><td class="source">                bug = 1<br></td></tr
><tr
id=sl_svn27_456

 onmouseover="gutterOver(456)"

><td class="source">                <br></td></tr
><tr
id=sl_svn27_457

 onmouseover="gutterOver(457)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_458

 onmouseover="gutterOver(458)"

><td class="source">        if(http_parameters.has_key(&#39;content-length&#39;)):<br></td></tr
><tr
id=sl_svn27_459

 onmouseover="gutterOver(459)"

><td class="source">            query += &quot;contentlength, &quot;<br></td></tr
><tr
id=sl_svn27_460

 onmouseover="gutterOver(460)"

><td class="source">            values.append(int(http_parameters[&#39;content-length&#39;]))<br></td></tr
><tr
id=sl_svn27_461

 onmouseover="gutterOver(461)"

><td class="source">            print str(http_parameters[&#39;content-length&#39;])+&quot;\n\n\n&quot;<br></td></tr
><tr
id=sl_svn27_462

 onmouseover="gutterOver(462)"

><td class="source">            if( int(str(http_parameters[&#39;content-length&#39;])) &lt;= 50):<br></td></tr
><tr
id=sl_svn27_463

 onmouseover="gutterOver(463)"

><td class="source">                bugsize = 1<br></td></tr
><tr
id=sl_svn27_464

 onmouseover="gutterOver(464)"

><td class="source">           <br></td></tr
><tr
id=sl_svn27_465

 onmouseover="gutterOver(465)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_466

 onmouseover="gutterOver(466)"

><td class="source">        if(http_parameters.has_key(&#39;date&#39;)):<br></td></tr
><tr
id=sl_svn27_467

 onmouseover="gutterOver(467)"

><td class="source">            query += &quot;pkt_date, &quot;<br></td></tr
><tr
id=sl_svn27_468

 onmouseover="gutterOver(468)"

><td class="source">            values.append(str(http_parameters[&#39;date&#39;]))<br></td></tr
><tr
id=sl_svn27_469

 onmouseover="gutterOver(469)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_470

 onmouseover="gutterOver(470)"

><td class="source">        query += &quot;insert_date, &quot;<br></td></tr
><tr
id=sl_svn27_471

 onmouseover="gutterOver(471)"

><td class="source">        values.append(datetime.datetime.now())<br></td></tr
><tr
id=sl_svn27_472

 onmouseover="gutterOver(472)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_473

 onmouseover="gutterOver(473)"

><td class="source">        if(http_parameters.has_key(&#39;status&#39;)):<br></td></tr
><tr
id=sl_svn27_474

 onmouseover="gutterOver(474)"

><td class="source">            query += &quot;status, &quot;<br></td></tr
><tr
id=sl_svn27_475

 onmouseover="gutterOver(475)"

><td class="source">            values.append(str(http_parameters[&#39;status&#39;]))<br></td></tr
><tr
id=sl_svn27_476

 onmouseover="gutterOver(476)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_477

 onmouseover="gutterOver(477)"

><td class="source">        if(http_parameters.has_key(&#39;server&#39;)):<br></td></tr
><tr
id=sl_svn27_478

 onmouseover="gutterOver(478)"

><td class="source">            query += &quot;server, &quot;<br></td></tr
><tr
id=sl_svn27_479

 onmouseover="gutterOver(479)"

><td class="source">            values.append(str(http_parameters[&#39;server&#39;]))<br></td></tr
><tr
id=sl_svn27_480

 onmouseover="gutterOver(480)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_481

 onmouseover="gutterOver(481)"

><td class="source">        if(http_parameters.has_key(&#39;p3p&#39;)):<br></td></tr
><tr
id=sl_svn27_482

 onmouseover="gutterOver(482)"

><td class="source">            query += &quot;p3p, &quot;<br></td></tr
><tr
id=sl_svn27_483

 onmouseover="gutterOver(483)"

><td class="source">            values.append(str(http_parameters[&#39;p3p&#39;]))<br></td></tr
><tr
id=sl_svn27_484

 onmouseover="gutterOver(484)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_485

 onmouseover="gutterOver(485)"

><td class="source">        if(http_parameters.has_key(&#39;etag&#39;)):<br></td></tr
><tr
id=sl_svn27_486

 onmouseover="gutterOver(486)"

><td class="source">            query += &quot;etag, &quot;<br></td></tr
><tr
id=sl_svn27_487

 onmouseover="gutterOver(487)"

><td class="source">            values.append(str(http_parameters[&#39;etag&#39;]).replace(&#39;&quot;&#39;, &#39;&#39;))<br></td></tr
><tr
id=sl_svn27_488

 onmouseover="gutterOver(488)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_489

 onmouseover="gutterOver(489)"

><td class="source">        if(http_parameters.has_key(&#39;cookie&#39;)):<br></td></tr
><tr
id=sl_svn27_490

 onmouseover="gutterOver(490)"

><td class="source">            if(http_parameters.has_key(&#39;host&#39;)):<br></td></tr
><tr
id=sl_svn27_491

 onmouseover="gutterOver(491)"

><td class="source">                cookie_domains = self.parse_cookie(http_parameters[&#39;cookie&#39;],http_parameters[&#39;host&#39;])<br></td></tr
><tr
id=sl_svn27_492

 onmouseover="gutterOver(492)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_493

 onmouseover="gutterOver(493)"

><td class="source">        if(http_parameters.has_key(&#39;set-cookie&#39;)):<br></td></tr
><tr
id=sl_svn27_494

 onmouseover="gutterOver(494)"

><td class="source">            setcookie_domains = self.parse_setcookie(http_parameters[&#39;set-cookie&#39;])<br></td></tr
><tr
id=sl_svn27_495

 onmouseover="gutterOver(495)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_496

 onmouseover="gutterOver(496)"

><td class="source">        if(http_parameters.has_key(&#39;set-cookie2&#39;)):<br></td></tr
><tr
id=sl_svn27_497

 onmouseover="gutterOver(497)"

><td class="source">            setcookie_domains = self.parse_setcookie(http_parameters[&#39;set-cookie2&#39;])<br></td></tr
><tr
id=sl_svn27_498

 onmouseover="gutterOver(498)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_499

 onmouseover="gutterOver(499)"

><td class="source">        query += &quot;seq, &quot;<br></td></tr
><tr
id=sl_svn27_500

 onmouseover="gutterOver(500)"

><td class="source">        values.append(seq)<br></td></tr
><tr
id=sl_svn27_501

 onmouseover="gutterOver(501)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_502

 onmouseover="gutterOver(502)"

><td class="source">        query += &quot;ack, &quot;<br></td></tr
><tr
id=sl_svn27_503

 onmouseover="gutterOver(503)"

><td class="source">        values.append(ack)<br></td></tr
><tr
id=sl_svn27_504

 onmouseover="gutterOver(504)"

><td class="source">        <br></td></tr
><tr
id=sl_svn27_505

 onmouseover="gutterOver(505)"

><td class="source">        query += &quot;grp_id) &quot;<br></td></tr
><tr
id=sl_svn27_506

 onmouseover="gutterOver(506)"

><td class="source">        grp_id = re.sub(r&#39;(\d*)\.&#39;,r&#39;\1&#39;,str(grp_id))<br></td></tr
><tr
id=sl_svn27_507

 onmouseover="gutterOver(507)"

><td class="source">        values.append(str(grp_id))<br></td></tr
><tr
id=sl_svn27_508

 onmouseover="gutterOver(508)"

><td class="source">        <br></td></tr
><tr
id=sl_svn27_509

 onmouseover="gutterOver(509)"

><td class="source">        query += &#39;VALUES ( &#39; + &#39;, &#39;.join([&quot;%s&quot; for i in range(0,len(values))]) +  &quot;)&quot;<br></td></tr
><tr
id=sl_svn27_510

 onmouseover="gutterOver(510)"

><td class="source">        pkt_id = self.cursor.execute(query, values)<br></td></tr
><tr
id=sl_svn27_511

 onmouseover="gutterOver(511)"

><td class="source">        if(pkt_id % 100 == 0):<br></td></tr
><tr
id=sl_svn27_512

 onmouseover="gutterOver(512)"

><td class="source">            print &quot;Last Row ID: &quot; + str(pkt_id)<br></td></tr
><tr
id=sl_svn27_513

 onmouseover="gutterOver(513)"

><td class="source">            print &quot;Records per second: &quot; + str (pkt_id / (datetime.datetime.now() - self.start_time).seconds )<br></td></tr
><tr
id=sl_svn27_514

 onmouseover="gutterOver(514)"

><td class="source">        self.connection.commit()<br></td></tr
><tr
id=sl_svn27_515

 onmouseover="gutterOver(515)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_516

 onmouseover="gutterOver(516)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_517

 onmouseover="gutterOver(517)"

><td class="source">        if(http_parameters.has_key(&#39;cookie&#39;) and cookie_domains != {}):<br></td></tr
><tr
id=sl_svn27_518

 onmouseover="gutterOver(518)"

><td class="source">            values = (cookie_domains[&#39;id&#39;], pkt_id, &quot;client&quot;, cookie_domains[&#39;expiry&#39;], cookie_domains[&#39;session&#39;])<br></td></tr
><tr
id=sl_svn27_519

 onmouseover="gutterOver(519)"

><td class="source">            self.cursor.execute(&quot;INSERT INTO cookie_has(domain_id, pkt_id, set_by, expiry, session) VALUES (%s, %s, %s, %s, %s)&quot;, values)<br></td></tr
><tr
id=sl_svn27_520

 onmouseover="gutterOver(520)"

><td class="source">            self.connection.commit()<br></td></tr
><tr
id=sl_svn27_521

 onmouseover="gutterOver(521)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_522

 onmouseover="gutterOver(522)"

><td class="source">       <br></td></tr
><tr
id=sl_svn27_523

 onmouseover="gutterOver(523)"

><td class="source">        if((http_parameters.has_key(&#39;set-cookie&#39;) or http_parameters.has_key(&#39;set-cookie2&#39;)) and setcookie_domains != []):<br></td></tr
><tr
id=sl_svn27_524

 onmouseover="gutterOver(524)"

><td class="source">            values = []<br></td></tr
><tr
id=sl_svn27_525

 onmouseover="gutterOver(525)"

><td class="source">            for cookie in setcookie_domains:<br></td></tr
><tr
id=sl_svn27_526

 onmouseover="gutterOver(526)"

><td class="source">                values.append((cookie[&#39;id&#39;], pkt_id, &quot;server&quot;, cookie[&#39;expiry&#39;], cookie[&#39;session&#39;]))<br></td></tr
><tr
id=sl_svn27_527

 onmouseover="gutterOver(527)"

><td class="source">            self.cursor.executemany(&quot;INSERT INTO cookie_has(domain_id, pkt_id, set_by, expiry, session) VALUES (%s, %s, %s, %s, %s)&quot;, values)<br></td></tr
><tr
id=sl_svn27_528

 onmouseover="gutterOver(528)"

><td class="source">            self.connection.commit()<br></td></tr
><tr
id=sl_svn27_529

 onmouseover="gutterOver(529)"

><td class="source">        if(bug == 1 and bugsize == 1):<br></td></tr
><tr
id=sl_svn27_530

 onmouseover="gutterOver(530)"

><td class="source">            host_list = str(http_parameters[&#39;host&#39;]).split(&#39;.&#39;)<br></td></tr
><tr
id=sl_svn27_531

 onmouseover="gutterOver(531)"

><td class="source">            host_str = host_list[len(host_list)-2] + &quot;.&quot; + host_list[len(host_list)-1]<br></td></tr
><tr
id=sl_svn27_532

 onmouseover="gutterOver(532)"

><td class="source">           <br></td></tr
><tr
id=sl_svn27_533

 onmouseover="gutterOver(533)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_534

 onmouseover="gutterOver(534)"

><td class="source">            #self.cursor.execute(&quot;INSERT INTO domains(domain,has_bug) VALUES (%s,1)&quot;,host_str)#get the last part of host....<br></td></tr
><tr
id=sl_svn27_535

 onmouseover="gutterOver(535)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_536

 onmouseover="gutterOver(536)"

><td class="source">            self.cursor.execute(&quot;SELECT id FROM domains WHERE domain = %s AND has_bug = 1&quot;,host_str)<br></td></tr
><tr
id=sl_svn27_537

 onmouseover="gutterOver(537)"

><td class="source">            row = self.cursor.fetchone()<br></td></tr
><tr
id=sl_svn27_538

 onmouseover="gutterOver(538)"

><td class="source">            if(row == None):<br></td></tr
><tr
id=sl_svn27_539

 onmouseover="gutterOver(539)"

><td class="source">                self.cursor.execute(&quot;INSERT INTO domains(domain,has_bug) VALUES (%s,1)&quot;, host_str)#add it to the table<br></td></tr
><tr
id=sl_svn27_540

 onmouseover="gutterOver(540)"

><td class="source">            else:<br></td></tr
><tr
id=sl_svn27_541

 onmouseover="gutterOver(541)"

><td class="source">                pass<br></td></tr
><tr
id=sl_svn27_542

 onmouseover="gutterOver(542)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_543

 onmouseover="gutterOver(543)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_544

 onmouseover="gutterOver(544)"

><td class="source">            <br></td></tr
><tr
id=sl_svn27_545

 onmouseover="gutterOver(545)"

><td class="source">            self.connection.commit()<br></td></tr
><tr
id=sl_svn27_546

 onmouseover="gutterOver(546)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_547

 onmouseover="gutterOver(547)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_548

 onmouseover="gutterOver(548)"

><td class="source">class SniffUI:<br></td></tr
><tr
id=sl_svn27_549

 onmouseover="gutterOver(549)"

><td class="source">    def __init__(self):<br></td></tr
><tr
id=sl_svn27_550

 onmouseover="gutterOver(550)"

><td class="source">        pass<br></td></tr
><tr
id=sl_svn27_551

 onmouseover="gutterOver(551)"

><td class="source">    def start(self):<br></td></tr
><tr
id=sl_svn27_552

 onmouseover="gutterOver(552)"

><td class="source">        curses.wrapper(self.RunUI)<br></td></tr
><tr
id=sl_svn27_553

 onmouseover="gutterOver(553)"

><td class="source">    def RunUI(self, stdscr):<br></td></tr
><tr
id=sl_svn27_554

 onmouseover="gutterOver(554)"

><td class="source">        win = curses.newwin(8,8,1,1)<br></td></tr
><tr
id=sl_svn27_555

 onmouseover="gutterOver(555)"

><td class="source">        pan = panel.new_panel(win)<br></td></tr
><tr
id=sl_svn27_556

 onmouseover="gutterOver(556)"

><td class="source">        pan.show()<br></td></tr
><tr
id=sl_svn27_557

 onmouseover="gutterOver(557)"

><td class="source">        while 1:<br></td></tr
><tr
id=sl_svn27_558

 onmouseover="gutterOver(558)"

><td class="source">            stdscr.addstr(0, 0, &quot;Current mode: Typing mode&quot;, curses.A_REVERSE)<br></td></tr
><tr
id=sl_svn27_559

 onmouseover="gutterOver(559)"

><td class="source">            panel.update_panels()<br></td></tr
><tr
id=sl_svn27_560

 onmouseover="gutterOver(560)"

><td class="source">            curses.doupdate()<br></td></tr
><tr
id=sl_svn27_561

 onmouseover="gutterOver(561)"

><td class="source">            stdscr.refresh()<br></td></tr
><tr
id=sl_svn27_562

 onmouseover="gutterOver(562)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_563

 onmouseover="gutterOver(563)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_564

 onmouseover="gutterOver(564)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_565

 onmouseover="gutterOver(565)"

><td class="source">if __name__==&#39;__main__&#39;:<br></td></tr
><tr
id=sl_svn27_566

 onmouseover="gutterOver(566)"

><td class="source">    debug = &quot;&quot;<br></td></tr
><tr
id=sl_svn27_567

 onmouseover="gutterOver(567)"

><td class="source">    #n = SniffUI()<br></td></tr
><tr
id=sl_svn27_568

 onmouseover="gutterOver(568)"

><td class="source">    s = Sniffer()<br></td></tr
><tr
id=sl_svn27_569

 onmouseover="gutterOver(569)"

><td class="source">    #option parser      Edit       Delete      1     en.wikipedia.org     /wiki/P3P     http://www.google.com/url?sa=t&amp;source=web&amp;ct=res&amp;c...     text/html; charset=UTF-8     Fri, 12 Mar 2010 22:06:03 GMT     2010-03-13 14:05:37     304      NULL     Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.8...      NULL      NULL      NULL     29717     34900     0<br></td></tr
><tr
id=sl_svn27_570

 onmouseover="gutterOver(570)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_571

 onmouseover="gutterOver(571)"

><td class="source">    parser = OptionParser()<br></td></tr
><tr
id=sl_svn27_572

 onmouseover="gutterOver(572)"

><td class="source">    parser.set_defaults(debug=False)<br></td></tr
><tr
id=sl_svn27_573

 onmouseover="gutterOver(573)"

><td class="source">    parser.add_option(&#39;--debug&#39;, dest=debug, action=&#39;store_true&#39;, help=&quot;Run with debug to use the local sqlitedb&quot;)<br></td></tr
><tr
id=sl_svn27_574

 onmouseover="gutterOver(574)"

><td class="source">    (options, argv) = parser.parse_args(sys.argv)<br></td></tr
><tr
id=sl_svn27_575

 onmouseover="gutterOver(575)"

><td class="source">   <br></td></tr
><tr
id=sl_svn27_576

 onmouseover="gutterOver(576)"

><td class="source">    #n.start()<br></td></tr
><tr
id=sl_svn27_577

 onmouseover="gutterOver(577)"

><td class="source">    s.start()<br></td></tr
></table></pre>
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
</td>
</tr></table>

 
<script type="text/javascript">
 var lineNumUnderMouse = -1;
 
 function gutterOver(num) {
 gutterOut();
 var newTR = document.getElementById('gr_svn27_' + num);
 if (newTR) {
 newTR.className = 'undermouse';
 }
 lineNumUnderMouse = num;
 }
 function gutterOut() {
 if (lineNumUnderMouse != -1) {
 var oldTR = document.getElementById(
 'gr_svn27_' + lineNumUnderMouse);
 if (oldTR) {
 oldTR.className = '';
 }
 lineNumUnderMouse = -1;
 }
 }
 var numsGenState = {table_base_id: 'nums_table_'};
 var srcGenState = {table_base_id: 'src_table_'};
 var alignerRunning = false;
 var startOver = false;
 function setLineNumberHeights() {
 if (alignerRunning) {
 startOver = true;
 return;
 }
 numsGenState.chunk_id = 0;
 numsGenState.table = document.getElementById('nums_table_0');
 numsGenState.row_num = 0;
 if (!numsGenState.table) {
 return; // Silently exit if no file is present.
 }
 srcGenState.chunk_id = 0;
 srcGenState.table = document.getElementById('src_table_0');
 srcGenState.row_num = 0;
 alignerRunning = true;
 continueToSetLineNumberHeights();
 }
 function rowGenerator(genState) {
 if (genState.row_num < genState.table.rows.length) {
 var currentRow = genState.table.rows[genState.row_num];
 genState.row_num++;
 return currentRow;
 }
 var newTable = document.getElementById(
 genState.table_base_id + (genState.chunk_id + 1));
 if (newTable) {
 genState.chunk_id++;
 genState.row_num = 0;
 genState.table = newTable;
 return genState.table.rows[0];
 }
 return null;
 }
 var MAX_ROWS_PER_PASS = 1000;
 function continueToSetLineNumberHeights() {
 var rowsInThisPass = 0;
 var numRow = 1;
 var srcRow = 1;
 while (numRow && srcRow && rowsInThisPass < MAX_ROWS_PER_PASS) {
 numRow = rowGenerator(numsGenState);
 srcRow = rowGenerator(srcGenState);
 rowsInThisPass++;
 if (numRow && srcRow) {
 if (numRow.offsetHeight != srcRow.offsetHeight) {
 numRow.firstChild.style.height = srcRow.offsetHeight + 'px';
 }
 }
 }
 if (rowsInThisPass >= MAX_ROWS_PER_PASS) {
 setTimeout(continueToSetLineNumberHeights, 10);
 } else {
 alignerRunning = false;
 if (startOver) {
 startOver = false;
 setTimeout(setLineNumberHeights, 500);
 }
 }
 }
 function initLineNumberHeights() {
 // Do 2 complete passes, because there can be races
 // between this code and prettify.
 startOver = true;
 setTimeout(setLineNumberHeights, 250);
 window.onresize = setLineNumberHeights;
 }
 initLineNumberHeights();
</script>

 
 
 <div id="log">
 <div style="text-align:right">
 <a class="ifCollapse" href="#" onclick="_toggleMeta(this); return false">Show details</a>
 <a class="ifExpand" href="#" onclick="_toggleMeta(this); return false">Hide details</a>
 </div>
 <div class="ifExpand">
 
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="changelog">
 <p>Change log</p>
 <div>
 <a href="/p/panopticon-osu/source/detail?spec=svn27&amp;r=25">r25</a>
 by rougechampion2002
 on Jun 10, 2010
 &nbsp; <a href="/p/panopticon-osu/source/diff?spec=svn27&r=25&amp;format=side&amp;path=/trunk/src/http_sniff.py&amp;old_path=/trunk/src/http_sniff.py&amp;old=24">Diff</a>
 </div>
 <pre>adding p3p helper function, details of
which will be in the documentation that i
will add shortly</pre>
 </div>
 
 
 
 
 
 
 <script type="text/javascript">
 var detail_url = '/p/panopticon-osu/source/detail?r=25&spec=svn27';
 var publish_url = '/p/panopticon-osu/source/detail?r=25&spec=svn27#publish';
 // describe the paths of this revision in javascript.
 var changed_paths = [];
 var changed_urls = [];
 
 changed_paths.push('/trunk/src/http_sniff.py');
 changed_urls.push('/p/panopticon-osu/source/browse/trunk/src/http_sniff.py?r\x3d25\x26spec\x3dsvn27');
 
 var selected_path = '/trunk/src/http_sniff.py';
 
 
 changed_paths.push('/trunk/src/p3p.py');
 changed_urls.push('/p/panopticon-osu/source/browse/trunk/src/p3p.py?r\x3d25\x26spec\x3dsvn27');
 
 
 function getCurrentPageIndex() {
 for (var i = 0; i < changed_paths.length; i++) {
 if (selected_path == changed_paths[i]) {
 return i;
 }
 }
 }
 function getNextPage() {
 var i = getCurrentPageIndex();
 if (i < changed_paths.length - 1) {
 return changed_urls[i + 1];
 }
 return null;
 }
 function getPreviousPage() {
 var i = getCurrentPageIndex();
 if (i > 0) {
 return changed_urls[i - 1];
 }
 return null;
 }
 function gotoNextPage() {
 var page = getNextPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoPreviousPage() {
 var page = getPreviousPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoDetailPage() {
 window.location = detail_url;
 }
 function gotoPublishPage() {
 window.location = publish_url;
 }
</script>

 
 <style type="text/css">
 #review_nav {
 border-top: 3px solid white;
 padding-top: 6px;
 margin-top: 1em;
 }
 #review_nav td {
 vertical-align: middle;
 }
 #review_nav select {
 margin: .5em 0;
 }
 </style>
 <div id="review_nav">
 <table><tr><td>Go to:&nbsp;</td><td>
 <select name="files_in_rev" onchange="window.location=this.value">
 
 <option value="/p/panopticon-osu/source/browse/trunk/src/http_sniff.py?r=25&amp;spec=svn27"
 selected="selected"
 >/trunk/src/http_sniff.py</option>
 
 <option value="/p/panopticon-osu/source/browse/trunk/src/p3p.py?r=25&amp;spec=svn27"
 
 >/trunk/src/p3p.py</option>
 
 </select>
 </td></tr></table>
 
 
 <div id="review_instr" class="closed">
 <a class="ifOpened" href="/p/panopticon-osu/source/detail?r=25&spec=svn27#publish">Publish your comments</a>
 <div class="ifClosed">Double click a line to add a comment</div>
 </div>
 
 </div>
 
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="older_bubble">
 <p>Older revisions</p>
 
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/panopticon-osu/source/detail?spec=svn27&r=24">r24</a>
 by rougechampion2002
 on Apr 28, 2010
 &nbsp; <a href="/p/panopticon-osu/source/diff?spec=svn27&r=24&amp;format=side&amp;path=/trunk/src/http_sniff.py&amp;old_path=/trunk/src/http_sniff.py&amp;old=23">Diff</a>
 <br>
 <pre class="ifOpened">fixed the domains so they dont add
more of the same domain IE: if we are
at facebook.com and no web bugs we
wont add it to the database if
facebook.com 0 is already there.  Also
...</pre>
 </div>
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/panopticon-osu/source/detail?spec=svn27&r=23">r23</a>
 by rougechampion2002
 on Apr 15, 2010
 &nbsp; <a href="/p/panopticon-osu/source/diff?spec=svn27&r=23&amp;format=side&amp;path=/trunk/src/http_sniff.py&amp;old_path=/trunk/src/http_sniff.py&amp;old=22">Diff</a>
 <br>
 <pre class="ifOpened">Think i got the connections dictionary
working, it checks to see if either ip
cat'd with the non 80 port is in the
dictionary, if it is we accept it, we
can probably add soemthing to the
...</pre>
 </div>
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/panopticon-osu/source/detail?spec=svn27&r=22">r22</a>
 by rougechampion2002
 on Mar 15, 2010
 &nbsp; <a href="/p/panopticon-osu/source/diff?spec=svn27&r=22&amp;format=side&amp;path=/trunk/src/http_sniff.py&amp;old_path=/trunk/src/http_sniff.py&amp;old=21">Diff</a>
 <br>
 <pre class="ifOpened">domains had a bug in it, fixed</pre>
 </div>
 
 
 <a href="/p/panopticon-osu/source/list?path=/trunk/src/http_sniff.py&start=25">All revisions of this file</a>
 </div>
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="fileinfo_bubble">
 <p>File info</p>
 
 <div>Size: 27354 bytes,
 577 lines</div>
 
 <div><a href="//panopticon-osu.googlecode.com/svn/trunk/src/http_sniff.py">View raw file</a></div>
 </div>
 
 <div id="props">
 <p>File properties</p>
 <dl>
 
 <dt>svn:executable</dt>
 <dd>*</dd>
 
 </dl>
 </div>
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 </div>
 </div>


</div>

</div>
</div>

<script src="https://ssl.gstatic.com/codesite/ph/13997016681179179006/js/prettify/prettify.js"></script>
<script type="text/javascript">prettyPrint();</script>


<script src="https://ssl.gstatic.com/codesite/ph/13997016681179179006/js/source_file_scripts.js"></script>

 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/13997016681179179006/js/kibbles.js"></script>
 <script type="text/javascript">
 var lastStop = null;
 var initialized = false;
 
 function updateCursor(next, prev) {
 if (prev && prev.element) {
 prev.element.className = 'cursor_stop cursor_hidden';
 }
 if (next && next.element) {
 next.element.className = 'cursor_stop cursor';
 lastStop = next.index;
 }
 }
 
 function pubRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftDestroyed(data) {
 updateCursorForCell(data.cellId, 'nocursor');
 if (initialized) {
 reloadCursors();
 }
 }
 function reloadCursors() {
 kibbles.skipper.reset();
 loadCursors();
 if (lastStop != null) {
 kibbles.skipper.setCurrentStop(lastStop);
 }
 }
 // possibly the simplest way to insert any newly added comments
 // is to update the class of the corresponding cursor row,
 // then refresh the entire list of rows.
 function updateCursorForCell(cellId, className) {
 var cell = document.getElementById(cellId);
 // we have to go two rows back to find the cursor location
 var row = getPreviousElement(cell.parentNode);
 row.className = className;
 }
 // returns the previous element, ignores text nodes.
 function getPreviousElement(e) {
 var element = e.previousSibling;
 if (element.nodeType == 3) {
 element = element.previousSibling;
 }
 if (element && element.tagName) {
 return element;
 }
 }
 function loadCursors() {
 // register our elements with skipper
 var elements = CR_getElements('*', 'cursor_stop');
 var len = elements.length;
 for (var i = 0; i < len; i++) {
 var element = elements[i]; 
 element.className = 'cursor_stop cursor_hidden';
 kibbles.skipper.append(element);
 }
 }
 function toggleComments() {
 CR_toggleCommentDisplay();
 reloadCursors();
 }
 function keysOnLoadHandler() {
 // setup skipper
 kibbles.skipper.addStopListener(
 kibbles.skipper.LISTENER_TYPE.PRE, updateCursor);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_top', 50);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_bottom', 100);
 // Register our keys
 kibbles.skipper.addFwdKey("n");
 kibbles.skipper.addRevKey("p");
 kibbles.keys.addKeyPressListener(
 'u', function() { window.location = detail_url; });
 kibbles.keys.addKeyPressListener(
 'r', function() { window.location = detail_url + '#publish'; });
 
 kibbles.keys.addKeyPressListener('j', gotoNextPage);
 kibbles.keys.addKeyPressListener('k', gotoPreviousPage);
 
 
 kibbles.keys.addKeyPressListener('h', toggleComments);
 
 }
 </script>
<script src="https://ssl.gstatic.com/codesite/ph/13997016681179179006/js/code_review_scripts.js"></script>
<script type="text/javascript">
 function showPublishInstructions() {
 var element = document.getElementById('review_instr');
 if (element) {
 element.className = 'opened';
 }
 }
 var codereviews;
 function revsOnLoadHandler() {
 // register our source container with the commenting code
 var paths = {'svn27': '/trunk/src/http_sniff.py'}
 codereviews = CR_controller.setup(
 {"projectName": "panopticon-osu", "projectHomeUrl": "/p/panopticon-osu", "profileUrl": "/u/115368015194065129388/", "token": "ABZ6GAcyt1dMU9RFW3eWmwpjxglIUw4cqw:1406256704307", "relativeBaseUrl": "", "domainName": null, "assetVersionPath": "https://ssl.gstatic.com/codesite/ph/13997016681179179006", "assetHostPath": "https://ssl.gstatic.com/codesite/ph", "loggedInUserEmail": "lukeKrantz@gmail.com"}, '', 'svn27', paths,
 CR_BrowseIntegrationFactory);
 
 // register our source container with the commenting code
 // in this case we're registering the container and the revison
 // associated with the contianer which may be the primary revision
 // or may be a previous revision against which the primary revision
 // of the file is being compared.
 codereviews.registerSourceContainer(document.getElementById('lines'), 'svn27');
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, showPublishInstructions);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_PUB_PLATE, pubRevealed);
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, draftRevealed);
 codereviews.registerActivityListener(CR_ActivityType.DISCARD_DRAFT_COMMENT, draftDestroyed);
 
 
 
 
 
 
 
 var initialized = true;
 reloadCursors();
 }
 window.onload = function() {keysOnLoadHandler(); revsOnLoadHandler();};

</script>
<script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/13997016681179179006/js/dit_scripts.js"></script>

 
 
 
 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/13997016681179179006/js/ph_core.js"></script>
 
 
 
 
</div> 

<div id="footer" dir="ltr">
 <div class="text">
 <a href="/projecthosting/terms.html">Terms</a> -
 <a href="http://www.google.com/privacy.html">Privacy</a> -
 <a href="/p/support/">Project Hosting Help</a>
 </div>
</div>
 <div class="hostedBy" style="margin-top: -20px;">
 <span style="vertical-align: top;">Powered by <a href="http://code.google.com/projecthosting/">Google Project Hosting</a></span>
 </div>

 
 


 
 </body>
</html>

