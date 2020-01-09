In this challenge we got login page with some crypto logic <a href="https://github.com/DejanJS/picoCTF-Writeups/blob/master/13.Secure%20Logon/server_noflag.py">here</a>  

We can see that we have AES encryption included, after research you can see this is intro to <a href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation">CBC</a>(cipher-block chaining)-byte flipping attack.
On the page if we try to login as admin we will get a response of not being an admin. If we log as a any user we will get the cookie and the decoded cookie response like this <br><code>Cookie: {'admin': 0,'username': 'asd','password':'asd'}</code>    

So let's see how the CBC-byte flipping attack works, here we have flow chart for encryption diagram D1:  


![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/13.Secure%20Logon/encrypt.jpg)  

The purpose of this attack is to change a byte in plaintext(Our Cookie in this case) by corrupting byte in ciphertext.Our Cookie is plaintext that is gonna be encrypted. According to attack description CBC works on a fixed length group called 'blocks'. In <a href="https://github.com/DejanJS/picoCTF-Writeups/blob/master/13.Secure%20Logon/server_noflag.py">code</a> that we are provided by the challenge, we can see that BLOCK_SIZE is 16 bytes each.Our goal is to change the <code>'{'admin':0 '</code> to 1.  
We have to split this json into 16 byte parts.
For example we can do it like this:  

<code>
import json
<br>
cookie = "{'admin':'0','username':'asd','password':'asd'}"
<br>
str_byte = cookie.encode()
<br>
block_size = 16
<br>
for i in range(2):
<br>
  if i is 0:
  <br>
    tmp = None
    <br>
    print(str_byte[tmp:block_size])
    <br>
  tmp = block_size
  <br>
  block_size = tmp + block_size
  <br>
  print(str_byte[tmp:block_size])  
 </code>
 