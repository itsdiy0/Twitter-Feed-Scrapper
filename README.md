<b>Tweeter Feed Scrapper</b>

![Alt text](https://i.ibb.co/18jJhCy/Screenshot-from-2024-01-18-11-06-06.png)

package required :<br>
```bash
pip install chromedriver_py
pip install Requests
pip install selenium
pip install selenium_wire

```
the purpose of this project is to stream and store tweets from the home page of your twitter account in a JSON file<br>
in main.py, select a duration for run time, your username and password<br>
in proxies.txt file, add the list of your proxies. the proxy list file should only contain a proxy server in each line, the code will itterate through all proxies and
will choose a working one<br>
note : the code is not optimised to bypass the twitter account authentication, in order to proper function, please log in<br>
once with your credintials in your own chrome browser then run the code 
