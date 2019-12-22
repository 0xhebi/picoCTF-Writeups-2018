This challenge is sort of a second part of Flaskcard challenge, in the Flaskcard challenge as we know we had SSTI exploit where we could get the secret key from flask config object by utilizing specific payload.  
Now in this one they provided us a secret key : <br><br>
<quote><code>Nice! You found out they were sending the Secret_key: a155eb4e1743baef085ff6ecfed943f2. Now, can you find a way to log in as admin? http://2018shell.picoctf.com:53588</code></quote>

One of the hints was a question <quote>"What can you do with a secret key?"</quote>, and apparently flask session cookies can be decoded and the result of that are the JSON object. I've used this <a href="https://www.kirsle.net/wizards/flask-session.cgi">online decoder</a>.

The decoded session cookie should look something like this:  

<code>{
    "_fresh": true,
    "_id": "e2b430a83dac634e2ccd8cf7e6835bd647f05a7c4325cede1dbbc9c969da5caed0f6d4fccdfe32eeabb60d1d5d8e82f19f666ba94a7940445a5f299f15e14316",
    "csrf_token": "61485c6b72b51209d4894183814b0b82948c2bd4",
    "user_id": "20"
}</code>

With a some research you can find out that default <b>user_id</b> for admin should be 0 or 1 ,so we should generate a new cookie but with value of e.g 1 for admin. And hash it again with the secret key that we were given.  

Particularly in Flask we are using <a href="https://flask.palletsprojects.com/en/1.1.x/api/#flask.sessions.SecureCookieSessionInterface">SecureCookieSessionInterface lib</a> with itsdangerous module.

So we can write some script to make that happen,check it out <a href="https://github.com/DejanJS/picoCTF-Writeups/blob/master/14.Flaskcards%20Skeleton%20Key/CTF_cookie.py">here</a>

After we generate new cookie and replace session cookie that we are sending,when we are trying to get to log as an admin,we get the flag:  

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/14.Flaskcards%20Skeleton%20Key/flag.png)
