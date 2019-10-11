The hint for the flag should be in the challange name itself.I guess some people would think that answer for the flag location has to do something with that tv series called "Mr.Robot" (at least I thought lol)<br>
![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/05.Mr.Robots/hint.png)

But seriously now,the hint was actually leading us to <a href="https://www.robotstxt.org/robotstxt.html">Robots.txt</a>  

This is a file with instructions for web robots,most of robots are representing unique <code>User-agent</code> .With those instructions we can restrict robots for doing certain actions,for example access to certain path.  

So if we go to <code>http://2018shell.picoctf.com:40064/robots.txt</code> :  

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/05.Mr.Robots/robotstxt.png)

We see can see <code>Disallow: /30de1.html</code> which is the path of the flag location.  

Flag :  

<code>picoCTF{th3_w0rld_1s_4_danger0us_pl4c3_3lli0t_30de1}</code>
