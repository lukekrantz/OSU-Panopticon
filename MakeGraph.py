



<!DOCTYPE html>
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
 <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" >
 
 <meta name="ROBOTS" content="NOARCHIVE">
 
 <link rel="icon" type="image/vnd.microsoft.icon" href="https://ssl.gstatic.com/codesite/ph/images/phosting.ico">
 
 
 <script type="text/javascript">
 
 
 
 
 var codesite_token = "ABZ6GAeCp5BJamYWO4zT7eJQkWvi3ongRQ:1406256684634";
 
 
 var CS_env = {"relativeBaseUrl": "", "projectHomeUrl": "/p/panopticon-osu", "profileUrl": "/u/115368015194065129388/", "assetVersionPath": "https://ssl.gstatic.com/codesite/ph/13997016681179179006", "assetHostPath": "https://ssl.gstatic.com/codesite/ph", "loggedInUserEmail": "lukeKrantz@gmail.com", "domainName": null, "token": "ABZ6GAeCp5BJamYWO4zT7eJQkWvi3ongRQ:1406256684634", "projectName": "panopticon-osu"};
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
 
 
 <title>MakeGraph.py - 
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
 | <a href="https://www.google.com/accounts/Logout?continue=https%3A%2F%2Fcode.google.com%2Fp%2Fpanopticon-osu%2Fsource%2Fbrowse%2Ftrunk%2Fsrc%2FMakeGraph.py" 
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
 <span id="crumb_links" class="ifClosed"><a href="/p/panopticon-osu/source/browse/trunk/">trunk</a><span class="sp">/&nbsp;</span><a href="/p/panopticon-osu/source/browse/trunk/src/">src</a><span class="sp">/&nbsp;</span>MakeGraph.py</span>
 
 


 </td>
 
 
 <td nowrap="nowrap" width="33%" align="center">
 <a href="/p/panopticon-osu/source/browse/trunk/src/MakeGraph.py?edit=1"
 ><img src="https://ssl.gstatic.com/codesite/ph/images/pencil-y14.png"
 class="edit_icon">Edit file</a>
 </td>
 
 
 <td nowrap="nowrap" width="33%" align="right">
 <table cellpadding="0" cellspacing="0" style="font-size: 100%"><tr>
 
 
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
></table></pre>
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
</td>
<td id="lines">
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
<pre class="prettyprint lang-py"><table id="src_table_0"><tr
id=sl_svn27_1

 onmouseover="gutterOver(1)"

><td class="source">#!/usr/bin/env python<br></td></tr
><tr
id=sl_svn27_2

 onmouseover="gutterOver(2)"

><td class="source">import sys, os, re, urllib2<br></td></tr
><tr
id=sl_svn27_3

 onmouseover="gutterOver(3)"

><td class="source">from pysqlite2 import dbapi2 as sqlite<br></td></tr
><tr
id=sl_svn27_4

 onmouseover="gutterOver(4)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_5

 onmouseover="gutterOver(5)"

><td class="source">if len(sys.argv) &lt; 3:<br></td></tr
><tr
id=sl_svn27_6

 onmouseover="gutterOver(6)"

><td class="source">    print &quot;Usage: ./&quot; + sys.argv[0] + &quot; &lt;dbname&gt; (webbugs|cookies) [--consolidate]&quot;<br></td></tr
><tr
id=sl_svn27_7

 onmouseover="gutterOver(7)"

><td class="source">    sys.exit()<br></td></tr
><tr
id=sl_svn27_8

 onmouseover="gutterOver(8)"

><td class="source">if(len(sys.argv) &gt; 3 and (sys.argv[3] == &#39;--consolidate&#39;)):<br></td></tr
><tr
id=sl_svn27_9

 onmouseover="gutterOver(9)"

><td class="source">    consolidate = True<br></td></tr
><tr
id=sl_svn27_10

 onmouseover="gutterOver(10)"

><td class="source">else:<br></td></tr
><tr
id=sl_svn27_11

 onmouseover="gutterOver(11)"

><td class="source">    consolidate = False<br></td></tr
><tr
id=sl_svn27_12

 onmouseover="gutterOver(12)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_13

 onmouseover="gutterOver(13)"

><td class="source">domain_re = re.compile(&#39;.*http:\/\/(?P&lt;domain&gt;.*?)\/&#39;)<br></td></tr
><tr
id=sl_svn27_14

 onmouseover="gutterOver(14)"

><td class="source">sqlitedbname = sys.argv[1]<br></td></tr
><tr
id=sl_svn27_15

 onmouseover="gutterOver(15)"

><td class="source">datatype = sys.argv[2]<br></td></tr
><tr
id=sl_svn27_16

 onmouseover="gutterOver(16)"

><td class="source">connection = sqlite.connect(sqlitedbname)<br></td></tr
><tr
id=sl_svn27_17

 onmouseover="gutterOver(17)"

><td class="source">connection.row_factory = sqlite.Row<br></td></tr
><tr
id=sl_svn27_18

 onmouseover="gutterOver(18)"

><td class="source">cursor = connection.cursor()<br></td></tr
><tr
id=sl_svn27_19

 onmouseover="gutterOver(19)"

><td class="source">if(datatype == &quot;webbugs&quot;):<br></td></tr
><tr
id=sl_svn27_20

 onmouseover="gutterOver(20)"

><td class="source">    f = open(&quot;webbugs.graphml&quot;, &#39;w&#39;)<br></td></tr
><tr
id=sl_svn27_21

 onmouseover="gutterOver(21)"

><td class="source">elif(datatype == &quot;cookies&quot;):<br></td></tr
><tr
id=sl_svn27_22

 onmouseover="gutterOver(22)"

><td class="source">    f = open(&quot;cookies.graphml&quot;, &#39;w&#39;)<br></td></tr
><tr
id=sl_svn27_23

 onmouseover="gutterOver(23)"

><td class="source">else:<br></td></tr
><tr
id=sl_svn27_24

 onmouseover="gutterOver(24)"

><td class="source">    print &quot;unknown data type: &quot; + str(datatype)<br></td></tr
><tr
id=sl_svn27_25

 onmouseover="gutterOver(25)"

><td class="source">    sys.exit(1)<br></td></tr
><tr
id=sl_svn27_26

 onmouseover="gutterOver(26)"

><td class="source">    <br></td></tr
><tr
id=sl_svn27_27

 onmouseover="gutterOver(27)"

><td class="source">header = &quot;&quot;&quot;&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;<br></td></tr
><tr
id=sl_svn27_28

 onmouseover="gutterOver(28)"

><td class="source">&lt;graphml xmlns=&quot;http://graphml.graphdrawing.org/xmlns/graphml&quot; xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot; xmlns:y=&quot;http://www.yworks.com/xml/graphml&quot; xsi:schemaLocation=&quot;http://graphml.graphdrawing.org/xmlns/graphml http://www.yworks.com/xml/schema/graphml/1.0/ygraphml.xsd&quot;&gt;<br></td></tr
><tr
id=sl_svn27_29

 onmouseover="gutterOver(29)"

><td class="source">  &lt;key for=&quot;node&quot; id=&quot;d0&quot; yfiles.type=&quot;nodegraphics&quot;/&gt;<br></td></tr
><tr
id=sl_svn27_30

 onmouseover="gutterOver(30)"

><td class="source">  &lt;key attr.name=&quot;description&quot; attr.type=&quot;string&quot; for=&quot;node&quot; id=&quot;d1&quot;/&gt;<br></td></tr
><tr
id=sl_svn27_31

 onmouseover="gutterOver(31)"

><td class="source">  &lt;key for=&quot;edge&quot; id=&quot;d2&quot; yfiles.type=&quot;edgegraphics&quot;/&gt;<br></td></tr
><tr
id=sl_svn27_32

 onmouseover="gutterOver(32)"

><td class="source">  &lt;key attr.name=&quot;description&quot; attr.type=&quot;string&quot; for=&quot;edge&quot; id=&quot;d3&quot;/&gt;<br></td></tr
><tr
id=sl_svn27_33

 onmouseover="gutterOver(33)"

><td class="source">  &lt;key for=&quot;graphml&quot; id=&quot;d4&quot; yfiles.type=&quot;resources&quot;/&gt;<br></td></tr
><tr
id=sl_svn27_34

 onmouseover="gutterOver(34)"

><td class="source">  &lt;graph edgedefault=&quot;directed&quot; id=&quot;G&quot; parse.order=&quot;free&quot;&gt;&quot;&quot;&quot;<br></td></tr
><tr
id=sl_svn27_35

 onmouseover="gutterOver(35)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_36

 onmouseover="gutterOver(36)"

><td class="source">footer = &quot;&quot;&quot;\n&lt;/graph&gt;\n&lt;data key=&quot;d4&quot;&gt;\n&lt;y:Resources/&gt;\n&lt;/data&gt;\n&lt;/graphml&gt;&quot;&quot;&quot;<br></td></tr
><tr
id=sl_svn27_37

 onmouseover="gutterOver(37)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_38

 onmouseover="gutterOver(38)"

><td class="source">if(datatype == &quot;webbugs&quot;):<br></td></tr
><tr
id=sl_svn27_39

 onmouseover="gutterOver(39)"

><td class="source">    query = &#39;select host,referer from rawpkt where status=&quot;200&quot; and contenttype like &quot;image/gif%&quot; and contentlength &lt; 44 and referer like &quot;http://%&quot;&#39;<br></td></tr
><tr
id=sl_svn27_40

 onmouseover="gutterOver(40)"

><td class="source">elif(datatype == &quot;cookies&quot;):<br></td></tr
><tr
id=sl_svn27_41

 onmouseover="gutterOver(41)"

><td class="source">    query = &#39;select p.host,d.domain from cookie_has c,domains d, rawpkt p where (c.domain_id=d.id and c.pkt_id=p.id) and (d.domain != p.host and d.domain != &quot;(null)&quot; and p.host !=&quot;(null)&quot;)&#39;<br></td></tr
><tr
id=sl_svn27_42

 onmouseover="gutterOver(42)"

><td class="source">else:<br></td></tr
><tr
id=sl_svn27_43

 onmouseover="gutterOver(43)"

><td class="source">    print &quot;error in determining the SQL query to use&quot;<br></td></tr
><tr
id=sl_svn27_44

 onmouseover="gutterOver(44)"

><td class="source">    sys.exit(1)<br></td></tr
><tr
id=sl_svn27_45

 onmouseover="gutterOver(45)"

><td class="source">    <br></td></tr
><tr
id=sl_svn27_46

 onmouseover="gutterOver(46)"

><td class="source">cursor.execute(query)<br></td></tr
><tr
id=sl_svn27_47

 onmouseover="gutterOver(47)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_48

 onmouseover="gutterOver(48)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_49

 onmouseover="gutterOver(49)"

><td class="source">print &quot;Stage 1: Parse the data into a set of nodes and a set of edge tuples&quot;<br></td></tr
><tr
id=sl_svn27_50

 onmouseover="gutterOver(50)"

><td class="source">edges = set() #built-in set type<br></td></tr
><tr
id=sl_svn27_51

 onmouseover="gutterOver(51)"

><td class="source">nodes = set()<br></td></tr
><tr
id=sl_svn27_52

 onmouseover="gutterOver(52)"

><td class="source">for row in cursor:<br></td></tr
><tr
id=sl_svn27_53

 onmouseover="gutterOver(53)"

><td class="source">    try:<br></td></tr
><tr
id=sl_svn27_54

 onmouseover="gutterOver(54)"

><td class="source">        if(datatype == &#39;webbugs&#39;):<br></td></tr
><tr
id=sl_svn27_55

 onmouseover="gutterOver(55)"

><td class="source">            if(row[&#39;referer&#39;] != None):<br></td></tr
><tr
id=sl_svn27_56

 onmouseover="gutterOver(56)"

><td class="source">                domain_result = domain_re.match(str(row[&#39;referer&#39;]))<br></td></tr
><tr
id=sl_svn27_57

 onmouseover="gutterOver(57)"

><td class="source">                if (domain_result):<br></td></tr
><tr
id=sl_svn27_58

 onmouseover="gutterOver(58)"

><td class="source">                    domain = domain_result.group(&#39;domain&#39;)<br></td></tr
><tr
id=sl_svn27_59

 onmouseover="gutterOver(59)"

><td class="source">                    if(domain != row[&#39;host&#39;]):<br></td></tr
><tr
id=sl_svn27_60

 onmouseover="gutterOver(60)"

><td class="source">                        edges.add((domain.replace(&#39;&amp;&#39;,&#39;&#39;),row[&#39;host&#39;].replace(&#39;&amp;&#39;,&#39;&#39;)))<br></td></tr
><tr
id=sl_svn27_61

 onmouseover="gutterOver(61)"

><td class="source">                        nodes.add(domain.replace(&#39;&amp;&#39;,&#39;&#39;))<br></td></tr
><tr
id=sl_svn27_62

 onmouseover="gutterOver(62)"

><td class="source">                        nodes.add(row[&#39;host&#39;].replace(&#39;&amp;&#39;,&#39;&#39;))<br></td></tr
><tr
id=sl_svn27_63

 onmouseover="gutterOver(63)"

><td class="source">        elif(datatype == &#39;cookies&#39;):<br></td></tr
><tr
id=sl_svn27_64

 onmouseover="gutterOver(64)"

><td class="source">            if(row[&#39;host&#39;].find(row[&#39;domain&#39;]) == -1): #cookie isn&#39;t for the same domain<br></td></tr
><tr
id=sl_svn27_65

 onmouseover="gutterOver(65)"

><td class="source">                if(row[&#39;host&#39;].count(&#39;&amp;&#39;) &gt; 0 or row[&#39;domain&#39;].count(&#39;&amp;&#39;) &gt; 0) or (row[&#39;host&#39;].count(&#39;,&#39;) &gt; 0 or row[&#39;domain&#39;].count(&#39;,&#39;) &gt; 0) or (row[&#39;host&#39;].count(&#39;&quot;&#39;) &gt; 0 or row[&#39;domain&#39;].count(&#39;&quot;&#39;) &gt; 0):<br></td></tr
><tr
id=sl_svn27_66

 onmouseover="gutterOver(66)"

><td class="source">                    print row<br></td></tr
><tr
id=sl_svn27_67

 onmouseover="gutterOver(67)"

><td class="source">                else:<br></td></tr
><tr
id=sl_svn27_68

 onmouseover="gutterOver(68)"

><td class="source">                    edges.add((row[&#39;host&#39;],row[&#39;domain&#39;]))<br></td></tr
><tr
id=sl_svn27_69

 onmouseover="gutterOver(69)"

><td class="source">                    nodes.add(row[&#39;domain&#39;])<br></td></tr
><tr
id=sl_svn27_70

 onmouseover="gutterOver(70)"

><td class="source">                    nodes.add(row[&#39;host&#39;])<br></td></tr
><tr
id=sl_svn27_71

 onmouseover="gutterOver(71)"

><td class="source">        else:<br></td></tr
><tr
id=sl_svn27_72

 onmouseover="gutterOver(72)"

><td class="source">            print &quot;error in determining how to process the query results&quot;<br></td></tr
><tr
id=sl_svn27_73

 onmouseover="gutterOver(73)"

><td class="source">            sys.exit(1)<br></td></tr
><tr
id=sl_svn27_74

 onmouseover="gutterOver(74)"

><td class="source">    except:<br></td></tr
><tr
id=sl_svn27_75

 onmouseover="gutterOver(75)"

><td class="source">        print row<br></td></tr
><tr
id=sl_svn27_76

 onmouseover="gutterOver(76)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_77

 onmouseover="gutterOver(77)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_78

 onmouseover="gutterOver(78)"

><td class="source">cursor.close()<br></td></tr
><tr
id=sl_svn27_79

 onmouseover="gutterOver(79)"

><td class="source">connection.close()<br></td></tr
><tr
id=sl_svn27_80

 onmouseover="gutterOver(80)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_81

 onmouseover="gutterOver(81)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_82

 onmouseover="gutterOver(82)"

><td class="source">####IMCOMPLETE<br></td></tr
><tr
id=sl_svn27_83

 onmouseover="gutterOver(83)"

><td class="source">if(consolidate):<br></td></tr
><tr
id=sl_svn27_84

 onmouseover="gutterOver(84)"

><td class="source">    print &quot;Stage 2: Remove subdomains and consolidate into a single domain&quot;<br></td></tr
><tr
id=sl_svn27_85

 onmouseover="gutterOver(85)"

><td class="source">    consolidated_edges = set()<br></td></tr
><tr
id=sl_svn27_86

 onmouseover="gutterOver(86)"

><td class="source">    consolidated_nodes = set()<br></td></tr
><tr
id=sl_svn27_87

 onmouseover="gutterOver(87)"

><td class="source">    #http://data.iana.org/TLD/tlds-alpha-by-domain.txt<br></td></tr
><tr
id=sl_svn27_88

 onmouseover="gutterOver(88)"

><td class="source">    tlds = urllib2.urlopen(&#39;http://data.iana.org/TLD/tlds-alpha-by-domain.txt&#39;)<br></td></tr
><tr
id=sl_svn27_89

 onmouseover="gutterOver(89)"

><td class="source">    for tld in tlds:<br></td></tr
><tr
id=sl_svn27_90

 onmouseover="gutterOver(90)"

><td class="source">        tld = tld.lower().strip()<br></td></tr
><tr
id=sl_svn27_91

 onmouseover="gutterOver(91)"

><td class="source">        if(tld.isalpha()): #ignore first line which is a comment<br></td></tr
><tr
id=sl_svn27_92

 onmouseover="gutterOver(92)"

><td class="source">            for n in nodes:<br></td></tr
><tr
id=sl_svn27_93

 onmouseover="gutterOver(93)"

><td class="source">                if(n[-(len(tld)+1):] == &#39;.&#39; + tld): #end of domain string is the tld?<br></td></tr
><tr
id=sl_svn27_94

 onmouseover="gutterOver(94)"

><td class="source">                    idx = n.rfind(&#39;.&#39;, 0, -(len(tld)+1)) # find the last &#39;.&#39; before the tld<br></td></tr
><tr
id=sl_svn27_95

 onmouseover="gutterOver(95)"

><td class="source">                    if(idx != -1): #if this contains a dot besides between the domain and tld<br></td></tr
><tr
id=sl_svn27_96

 onmouseover="gutterOver(96)"

><td class="source">                        print n + &quot; -&gt; &quot; + n[idx+1:]<br></td></tr
><tr
id=sl_svn27_97

 onmouseover="gutterOver(97)"

><td class="source">                        if(n[idx+1:] not in nodes):<br></td></tr
><tr
id=sl_svn27_98

 onmouseover="gutterOver(98)"

><td class="source">                            consolidated_nodes.add(n[idx+1:])<br></td></tr
><tr
id=sl_svn27_99

 onmouseover="gutterOver(99)"

><td class="source">                        for host,domain in edges:<br></td></tr
><tr
id=sl_svn27_100

 onmouseover="gutterOver(100)"

><td class="source">                            if(host == n):<br></td></tr
><tr
id=sl_svn27_101

 onmouseover="gutterOver(101)"

><td class="source">                                host = n[idx+1:]<br></td></tr
><tr
id=sl_svn27_102

 onmouseover="gutterOver(102)"

><td class="source">                            if(domain == n):<br></td></tr
><tr
id=sl_svn27_103

 onmouseover="gutterOver(103)"

><td class="source">                                domain = n[idx+1:]<br></td></tr
><tr
id=sl_svn27_104

 onmouseover="gutterOver(104)"

><td class="source">                            consolidated_edges.add((host,domain))<br></td></tr
><tr
id=sl_svn27_105

 onmouseover="gutterOver(105)"

><td class="source">    nodes = consolidated_nodes<br></td></tr
><tr
id=sl_svn27_106

 onmouseover="gutterOver(106)"

><td class="source">    edges = consolidated_edges<br></td></tr
><tr
id=sl_svn27_107

 onmouseover="gutterOver(107)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_108

 onmouseover="gutterOver(108)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_109

 onmouseover="gutterOver(109)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_110

 onmouseover="gutterOver(110)"

><td class="source">#write to a graphml file<br></td></tr
><tr
id=sl_svn27_111

 onmouseover="gutterOver(111)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_112

 onmouseover="gutterOver(112)"

><td class="source">f.write(header)<br></td></tr
><tr
id=sl_svn27_113

 onmouseover="gutterOver(113)"

><td class="source">    <br></td></tr
><tr
id=sl_svn27_114

 onmouseover="gutterOver(114)"

><td class="source">for id in nodes:<br></td></tr
><tr
id=sl_svn27_115

 onmouseover="gutterOver(115)"

><td class="source">    node_string = &#39;&lt;node id=&quot;&#39; + id + &#39;&quot;&gt;\n&#39;<br></td></tr
><tr
id=sl_svn27_116

 onmouseover="gutterOver(116)"

><td class="source">    node_string += &#39;&lt;data key=&quot;d0&quot;&gt;\n&#39;<br></td></tr
><tr
id=sl_svn27_117

 onmouseover="gutterOver(117)"

><td class="source">    node_string += &#39;&lt;y:ShapeNode&gt;\n&#39;<br></td></tr
><tr
id=sl_svn27_118

 onmouseover="gutterOver(118)"

><td class="source">    node_string += &#39;&lt;y:NodeLabel&gt;&#39; + id + &#39;&lt;/y:NodeLabel&gt;\n&#39;<br></td></tr
><tr
id=sl_svn27_119

 onmouseover="gutterOver(119)"

><td class="source">    node_string += &#39;&lt;/y:ShapeNode&gt;\n&#39;<br></td></tr
><tr
id=sl_svn27_120

 onmouseover="gutterOver(120)"

><td class="source">    node_string += &#39;&lt;/data&gt;\n&lt;/node&gt;\n&#39;<br></td></tr
><tr
id=sl_svn27_121

 onmouseover="gutterOver(121)"

><td class="source">    f.write(node_string)<br></td></tr
><tr
id=sl_svn27_122

 onmouseover="gutterOver(122)"

><td class="source"><br></td></tr
><tr
id=sl_svn27_123

 onmouseover="gutterOver(123)"

><td class="source">i = 0<br></td></tr
><tr
id=sl_svn27_124

 onmouseover="gutterOver(124)"

><td class="source">for host,domain in edges:<br></td></tr
><tr
id=sl_svn27_125

 onmouseover="gutterOver(125)"

><td class="source">    i += 1 <br></td></tr
><tr
id=sl_svn27_126

 onmouseover="gutterOver(126)"

><td class="source">    edge_string = &#39;&lt;edge id=&quot;&#39; +  str(i) + &#39;&quot; source=&quot;&#39; + host + &#39;&quot; target=&quot;&#39; + domain + &#39;&quot;&gt;\n&#39;<br></td></tr
><tr
id=sl_svn27_127

 onmouseover="gutterOver(127)"

><td class="source">    edge_string += &#39;&lt;data key=&quot;d2&quot;&gt;\n&#39;<br></td></tr
><tr
id=sl_svn27_128

 onmouseover="gutterOver(128)"

><td class="source">    edge_string += &#39;&lt;y:PolyLineEdge&gt;\n&#39;<br></td></tr
><tr
id=sl_svn27_129

 onmouseover="gutterOver(129)"

><td class="source">    edge_string += &#39;&lt;y:Path sx=&quot;0.0&quot; sy=&quot;0.0&quot; tx=&quot;0.0&quot; ty=&quot;0.0&quot;/&gt;\n&#39;<br></td></tr
><tr
id=sl_svn27_130

 onmouseover="gutterOver(130)"

><td class="source">    edge_string += &#39;&lt;y:LineStyle type=&quot;line&quot; width=&quot;1.0&quot; color=&quot;#000000&quot; /&gt;\n&#39;<br></td></tr
><tr
id=sl_svn27_131

 onmouseover="gutterOver(131)"

><td class="source">    edge_string += &#39;&lt;y:Arrows source=&quot;none&quot; target=&quot;standard&quot;/&gt;\n&#39;<br></td></tr
><tr
id=sl_svn27_132

 onmouseover="gutterOver(132)"

><td class="source">    edge_string += &#39;&lt;y:BendStyle smoothed=&quot;false&quot;/&gt;\n&#39;<br></td></tr
><tr
id=sl_svn27_133

 onmouseover="gutterOver(133)"

><td class="source">    edge_string += &#39;&lt;/y:PolyLineEdge&gt;\n&#39;<br></td></tr
><tr
id=sl_svn27_134

 onmouseover="gutterOver(134)"

><td class="source">    edge_string += &#39;&lt;/data&gt;\n&lt;data key=&quot;d3&quot;/&gt;\n&lt;/edge&gt;\n&#39;<br></td></tr
><tr
id=sl_svn27_135

 onmouseover="gutterOver(135)"

><td class="source">    f.write(edge_string)<br></td></tr
><tr
id=sl_svn27_136

 onmouseover="gutterOver(136)"

><td class="source">    <br></td></tr
><tr
id=sl_svn27_137

 onmouseover="gutterOver(137)"

><td class="source">f.write(footer)<br></td></tr
><tr
id=sl_svn27_138

 onmouseover="gutterOver(138)"

><td class="source">f.close()<br></td></tr
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
 <a href="/p/panopticon-osu/source/detail?spec=svn27&amp;r=15">r15</a>
 by rougechampion2002
 on Jan 21, 2010
 &nbsp; <a href="/p/panopticon-osu/source/diff?spec=svn27&r=15&amp;format=side&amp;path=/trunk/src/MakeGraph.py&amp;old_path=/trunk/src/MakeGraph.py&amp;old=">Diff</a>
 </div>
 <pre>forgot to re-add the files after i moved
them, fixing</pre>
 </div>
 
 
 
 
 
 
 <script type="text/javascript">
 var detail_url = '/p/panopticon-osu/source/detail?r=15&spec=svn27';
 var publish_url = '/p/panopticon-osu/source/detail?r=15&spec=svn27#publish';
 // describe the paths of this revision in javascript.
 var changed_paths = [];
 var changed_urls = [];
 
 changed_paths.push('/trunk/src/MakeGraph.py');
 changed_urls.push('/p/panopticon-osu/source/browse/trunk/src/MakeGraph.py?r\x3d15\x26spec\x3dsvn27');
 
 var selected_path = '/trunk/src/MakeGraph.py';
 
 
 changed_paths.push('/trunk/src/charcheck.py');
 changed_urls.push('/p/panopticon-osu/source/browse/trunk/src/charcheck.py?r\x3d15\x26spec\x3dsvn27');
 
 
 changed_paths.push('/trunk/src/filecheck.py');
 changed_urls.push('/p/panopticon-osu/source/browse/trunk/src/filecheck.py?r\x3d15\x26spec\x3dsvn27');
 
 
 changed_paths.push('/trunk/src/http_sniff.py');
 changed_urls.push('/p/panopticon-osu/source/browse/trunk/src/http_sniff.py?r\x3d15\x26spec\x3dsvn27');
 
 
 changed_paths.push('/trunk/src/makeDB.php');
 changed_urls.push('/p/panopticon-osu/source/browse/trunk/src/makeDB.php?r\x3d15\x26spec\x3dsvn27');
 
 
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
 
 <option value="/p/panopticon-osu/source/browse/trunk/src/MakeGraph.py?r=15&amp;spec=svn27"
 selected="selected"
 >/trunk/src/MakeGraph.py</option>
 
 <option value="/p/panopticon-osu/source/browse/trunk/src/charcheck.py?r=15&amp;spec=svn27"
 
 >/trunk/src/charcheck.py</option>
 
 <option value="/p/panopticon-osu/source/browse/trunk/src/filecheck.py?r=15&amp;spec=svn27"
 
 >/trunk/src/filecheck.py</option>
 
 <option value="/p/panopticon-osu/source/browse/trunk/src/http_sniff.py?r=15&amp;spec=svn27"
 
 >/trunk/src/http_sniff.py</option>
 
 <option value="/p/panopticon-osu/source/browse/trunk/src/makeDB.php?r=15&amp;spec=svn27"
 
 >/trunk/src/makeDB.php</option>
 
 </select>
 </td></tr></table>
 
 
 <div id="review_instr" class="closed">
 <a class="ifOpened" href="/p/panopticon-osu/source/detail?r=15&spec=svn27#publish">Publish your comments</a>
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
 
 <a href="/p/panopticon-osu/source/list?path=/trunk/src/MakeGraph.py&start=15">All revisions of this file</a>
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
 
 <div>Size: 5647 bytes,
 138 lines</div>
 
 <div><a href="//panopticon-osu.googlecode.com/svn/trunk/src/MakeGraph.py">View raw file</a></div>
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
 var paths = {'svn27': '/trunk/src/MakeGraph.py'}
 codereviews = CR_controller.setup(
 {"relativeBaseUrl": "", "projectHomeUrl": "/p/panopticon-osu", "profileUrl": "/u/115368015194065129388/", "assetVersionPath": "https://ssl.gstatic.com/codesite/ph/13997016681179179006", "assetHostPath": "https://ssl.gstatic.com/codesite/ph", "loggedInUserEmail": "lukeKrantz@gmail.com", "domainName": null, "token": "ABZ6GAeCp5BJamYWO4zT7eJQkWvi3ongRQ:1406256684634", "projectName": "panopticon-osu"}, '', 'svn27', paths,
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

