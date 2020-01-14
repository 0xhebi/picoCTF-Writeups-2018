In this challenge we got login page with some crypto logic <a href="https://github.com/DejanJS/picoCTF-Writeups/blob/master/13.Secure%20Logon/server_noflag.py">here</a>  

We can see that we have AES encryption included, after research you can see this is intro to <a href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation">CBC</a>(cipher-block chaining)-byte flipping attack.
On the page if we try to login as admin we will get a response of not being an admin. If we log as a any user we will get the cookie and the decoded cookie response like this <br><code>Cookie: {'admin': 0,'username': 'asd','password':'asd'}</code>    

So let's see how the CBC-byte flipping attack works, here we have flow chart for encryption diagram D1:  


![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/13.Secure%20Logon/encrypt.jpg)  

The purpose of this attack is to change a byte in plaintext(Our Cookie in this case) by corrupting byte in ciphertext.Our Cookie is plaintext that is gonna be encrypted. According to attack description CBC works on a fixed length group called 'blocks'. In <a href="https://github.com/DejanJS/picoCTF-Writeups/blob/master/13.Secure%20Logon/server_noflag.py">code</a> that we are provided by the challenge, we can see that BLOCK_SIZE is 16 bytes each.Our goal is to change the <code>'{'admin':0 '</code> to 1.  
We have to split this json into 16 byte parts.
For example we can do it like this:  

```python
import json
cookie = "{'admin':'0','username':'123','password':'123'}"
str_byte = cookie.encode()
block_size = 16
for i in range(1,round(len(str_byte)/block_size)):
  if i is 1:
    tmp = None
    print(str_byte[tmp:block_size])
  tmp = block_size
  block_size = tmp + block_size
  print(str_byte[tmp:block_size])  
```

We have 3 blocks :  
1.{'admin':'0','us  
2.ername':'asd','p<br>
3.assword':'asd'}<br>

CBC Encryption and Decryption can be represented with this formula:  

<code><b>C<sub>n</sub> = Ek(P<sub>n</sub> ⊕ C<sub>n</sub>-1)</b></code>  
<code><b>C<sub>0</sub> = IV </b></code>    
<br>
<b>P<sub>n</sub> = Dk(C<sub>n</sub>) ⊕ C<sub>n</sub>-1<br>
C<sub>0</sub> = IV </b>

<b>C<sub>n</sub></b> and <b>P<sub>n</sub></b> are nth ciphertext blocks and plaintext , IV(Initializtion Vector) role of C<sub>0</sub> or the first starting block.
<br>So basically we are encrypting (Ek = encrypt); Encrypt(P<sub>n</sub> XOR C<sub>n</sub> -1)<br>
nth Plaintext block XOR with Ciphertext block - 1<br>
<b>IV</b> should be always random and unique for each sequence, you can find more about it <a href="https://en.wikipedia.org/wiki/Initialization_vector">here</a>.We will see how this implies to our attack later..  
So if we look at the diagram(D1) we can see that ciphertext of the first block will be used for the next block which is creating a chain to further blocks , every upcoming block is using previous ciphertext.<br>  
In decryption process it is gonna be similar tho ciphertext is going to be used as <b>IV</b> for further blocks which we can see on this diagram.
<br>
![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/13.Secure%20Logon/decrypt.jpg)  

In our <a href='https://github.com/DejanJS/picoCTF-Writeups/blob/master/13.Secure%20Logon/server_noflag.py'>server_no_flag.py </a>  

We see those two functions :  

```python

BLOCK_SIZE = 16  # Bytes

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
                
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

 def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:])).decode('utf8')
```
<br>
So let's proceed with an attack and some basic explanation. <br>
First we can take a look at <a href="https://github.com/DejanJS/picoCTF-Writeups/blob/master/13.Secure%20Logon/bitflip.py">bitflip.py</a>.  

```python
from base64 import b64encode,b64decode

cookie = 'p0AHKFY4ZazN2iPT0OfjxKBdo9XeP0MpVQXyfodZqRY0kDxq4coWRLhxMW+nZw3shqk4FmTSizeTayEoXYZp6f8YI/aneFp/g8jbsQrXMqE='
user_cookie = "{'admin': 0, 'username': '123', 'password': '123'}"
user_cookie_with_iv = ("X" * 16) + user_cookie # 16 is block size in bytes
byte_offset = user_cookie_with_iv.find("0") # that is value of admin 
byte_to_flip = byte_offset - 16
token = b64decode(cookie)

cookie_chars = bytearray(token)
cookie_chars[byte_to_flip] = cookie_chars[byte_to_flip] ^ ord("0") ^ ord("1")
encode_cookie_admin = b64encode(cookie_chars).decode("utf-8")

print(encode_cookie_admin)  
```
<var>cookie</var> here is a variable for my cookie that has been generated. I should have used CURL or any other similar tool to make this piece of code more dynamical but at the moment for this purpose it will be enough as an example.<br>So as we can see we have base64 encoded value. We have our <var>user_cookie</var> with value  as a response from request.<br>  
Since our target (admin : 0) is in a first block we will have to generate IV to fill in the block and compute it with user_cookie.<br>
<var>byte_offset</var> is going to be a number of the bit position that we are looking to flip. <br>Then bit to flip is going to be byte_offset - 16(the our "X" values for iv).<br> From there we are going to b64decode our cookie convert it into bytearray , and use our byte_to_flip position for flipping part, which we achieve by XOR-ing <code>cookie_chars[byte_to_flip] ^ ord("0") ^ ord("1")</code>

