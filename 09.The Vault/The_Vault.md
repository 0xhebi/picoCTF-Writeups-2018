In this challenge we have a login page and php login code.

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/09.The%20Vault/loginphp.png)  

If we take a look at <code>$pattern ="/.*['\"].*OR.*/i"</code>  
This regular expression is preventing us for doing input with starting quotes and with classic 1 OR 1 example.  
There are alot of examples of an input to bypass this one, the one that I've used was <code>admin' --</code> to make SQL injection.



