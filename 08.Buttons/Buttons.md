In this one we have 2 buttons,first one is leading to the page with button that is an actually anchor tag with href.And then you get rick rolled........  

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/08.Buttons/Buttons.gif)  

By inspecting we can see the difference between 2 'buttons', first one is actual button wrapped in a form tag   

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/08.Buttons/formbtn1.png)  

and the second one is just a anchor tag with href to other path which is supposed to be 'button2.php' tho it is redirecting us to boo.html   

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/08.Buttons/btn2href.png)

So by changing the the first form tag action attribute to 'button2.php' we are actually making a request to that page and we are getting the flag.  

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/08.Buttons/flag.png)