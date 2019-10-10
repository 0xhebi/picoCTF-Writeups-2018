In this one we have login page where we have to try to login somehow.  

I was investigating around to see if anything weird is going on but it seems that wasn't the case.<br>
After inserting random input we are just getting to the login failed.Inspecting response and request behaviour didn't give us much info of some possible vulnerability...<br>So only thing that could cross my mind is that this will be some <code>XSS</code> exploitation.  
I've started with the classic <code>`<script>alert(1)</script>`</code>
but that didn't lead me anywhere, so I was wondering what could it be...  
![Alt text]