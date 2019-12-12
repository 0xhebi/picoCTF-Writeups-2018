In this challenge we have a website with to register and login form. Once you make a user you can create a 'card' where you can write a question and answer to it.  
First thought this would be some sort of XSS or SQL injection.
But since this server is being ran on Python's framework (Flask) , it had to do something with Flask exploit. After doing some research on this i found out about SSTI.

<a href="https://pequalsnp-team.github.io/cheatsheet/flask-jinja2-ssti">Flask && jinja2 SSTI </a>  

You can read more about SSTI <a href="https://portswigger.net/research/server-side-template-injection">here</a> for general concept.

So simple test that we can do is executing this kind of payload <code>{{7*7}}</code>  
And we actually get this evaluation :  

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/11.Flaskcards/inputexample.png)

We see that this kind of input is being evaluated , so this template language is in use. This means we can access global config object of flask app, if we enter <code>{{config}}</code> we get all the info on it :  

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/11.Flaskcards/flag.png)  

<b>FLAG : picoCTF{secret_keys_to_the_kingdom_2a7bf92c} </b>

