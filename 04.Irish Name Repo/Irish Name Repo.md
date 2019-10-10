In this one we have login page where we have to try to login somehow.  

I was investigating around to see if anything weird is going on but it seems that wasn't the case.<br>
After inserting random input we are just getting to the login failed.Inspecting response and request behaviour didn't give us much info of some possible vulnerability...<br>So only thing that could cross my mind is that this will be some <code>XSS</code> exploitation.  
I've started with the classic <code>`<script>alert(1)</script>`</code>
but that didn't lead me anywhere, so I was wondering what could it be...  
![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/04.Irish%20Name%20Repo/hint.png)  
  
<q>If the users are kept in database</q>  
  
well from that point it was clear it will be <a src="https://en.wikipedia.org/wiki/SQL_injection">SQL injection</a>  
  
Inserting <code>' OR '1'='1</code> into user and password field resulted into  
  
![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/04.Irish%20Name%20Repo/loggedin.png)      
  
So the input was incorrectly filtered which is allowing us to do SQL injection and perform SQL query for pulling users and passwords from database.  
<code>OR 1=1</code> will evaluate to true which will return us all the passwords from the database.
  
Flag:  
  
<code>picoCTF{con4n_r3411y_1snt_1r1sh_c0d93e2f}</code>  
  
