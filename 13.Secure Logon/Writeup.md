In this challenge we got login page with some crypto logic <a href="https://github.com/DejanJS/picoCTF-Writeups/blob/master/13.Secure%20Logon/server_noflag.py">here</a>  

We can see that we have AES encryption included, after research you can see this is intro to <a href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation">CBC</a>(cipher-block chaining)-byte flipping attack.
On the page if we try to login as admin we will get a response of not being an admin. If we log as a any user we will get the cookie and the decoded cookie response like this <br><code>Cookie: {'admin': 0, 'username': 'asd', 'password': 'asd'}</code>  

