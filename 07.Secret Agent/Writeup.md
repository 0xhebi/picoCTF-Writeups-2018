This challenge was about <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent">User Agent</a>  

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/07.Secret%20Agent/notgoogle.png)  

As we can see by clicking on flag the server is expecting the google as a User Agent. We can change that simply in chrome devtools :  

<b>Three vertical dots(Customize and control chrome devtools) > More tools > Network conditions </b>  

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/07.Secret%20Agent/networkcondition.png)  

Then flag is there:  

![Alt text](https://github.com/DejanJS/picoCTF-Writeups/blob/master/07.Secret%20Agent/flagSagent.png)

<b>FLAG :  picoCTF{s3cr3t_ag3nt_m4n_12387c22} </b>  

Summary :  

<p>Using browser detection generally is bad idea... you can read more <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Browser_detection_using_the_user_agent">here.</a>
