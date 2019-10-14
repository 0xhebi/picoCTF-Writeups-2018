In this challenge we have a page without login form.We only have a button that when it's clicked it makes a request.<br>If we click on a button we can see that we are not admin.

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/06.No%20Login/setcookie.png)

<code>Set-Cookie: session=eyJfZmxhc2hlcyI6W3siIHQiOlsid2FybmluZyIsIkknbSBzb3JyeSBpdCBkb2Vzbid0IGxvb2sgbGlrZSB5b3UgYXJlIHRoZSBhZG1pbi4iXX1dfQ.EIYQ7Q.TkPDH08qCTxeyCm-zXIw9IemvWk; HttpOnly; Path=/</code>  

As we know according to MDN,The <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie">Set-Cookie</a> HTTP response header is used to send cookies from the server to the user agent, so the user agent can send them back to the server later.  

Also we have <a href="https://www.owasp.org/index.php/HttpOnly">HttpOnly</a>   

<q><i>If the HttpOnly flag (optional) is included in the HTTP response header, the cookie cannot be accessed through client side script (again if the browser supports this flag). As a result, even if a cross-site scripting (XSS) flaw exists, and a user accidentally accesses a link that exploits this flaw, the browser (primarily Internet Explorer) will not reveal the cookie to a third party.</i></q>  

So from here we can see that response header sets our cookie to the session token. So when we request the flag again that cookie with session value will be sent.From the above statement we can't access the cookie from the client side but that doesn't mean we can't set it.<br>If we set cookie to <code>admin=eyJfZmxhc2hlcyI6W3siIHQiOlsid2FybmluZyIsIkknbSBzb3JyeSBpdCBkb2Vzbid0IGxvb2sgbGlrZSB5b3UgYXJlIHRoZSBhZG1pbi4iXX1dfQ</code>  and refresh the page.  

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/06.No%20Login/flag.png)

We get the flag:  
<code>picoCTF{n0l0g0n_n0_pr0bl3m_ed714e0e}</code>