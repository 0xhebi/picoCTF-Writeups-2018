In this one we have a site with a login form.<br>
I've tried inserting random input for username and password.

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/03.Logon/login1.png) 

We can see that it let us login but we are not getting access to the flag because we are not an admin. I've tried to look up for the <code>.js</code> file but there was no any that is showing some request logic.So I started investigating in browser network to see how the server is checking if we are an admin.

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/03.Logon/cookiefalse.png)  

when our browser makes a request to this page it sets cookie to <code>Cookie: password=; username=; admin=False</code>   
so init value of admin is false and when we proceed to make request to the login page ,server is checking if the user is admin based on that value of the cookie.    

Then we can just change the admin value to true :  

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/03.Logon/cookietrue.png)    
  
And then refresh the page  
  
![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/03.Logon/flag.png)

And there goes the flag:  
  
<code>picoCTF{l0g1ns_ar3nt_r34l_a280e12c}</code>  
