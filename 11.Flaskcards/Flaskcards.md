In this challenge we have a website with to register and login form. Once you make a user you can create a 'card' where you can write a question and answer to it.  
First thought this would be some sort of XSS or SQL injection.
But since this server is being ran on Python's framework (Flask) , it had to do something with Flask exploit. After doing some research on this i found out about SSTI.

<a href="https://pequalsnp-team.github.io/cheatsheet/flask-jinja2-ssti">Flask && jinja2 SSTI </a>  

You can read more about SSTI <a href="https://portswigger.net/research/server-side-template-injection">here</a> for general concept.  

