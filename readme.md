# Bug Bounty Bot   

> A telegram bot with commands to simplify bug bounty tasks 

![](/docs/resources/sample.gif)

+  [Installation](#installation)
+  [Use](#use)
+  [Road Map](#road-map)


## Installation  

BugBountyBot is open-source so you can run the bot on your own server. The following installation instructions are designed to be used with an Ubunto Virtual Private Server, from a vendor such as [digitalocean](https://www.digitalocean.com/).  

### Provision Virtual Private Server 

4. Make a new non-root sudo user. see [tutorial](https://www.digitalocean.com/community/tutorials/how-to-create-a-sudo-user-on-ubuntu-quickstart)


### Create Telegram API Key 

1.  Message (botfather)[] on telegram to get a new api key

`/newbot`

2. Create a `.env` file in the root of your bugbountybot application folder with your new apikey

`echo "API_KEY=[KEY]" > .env`  

### Start BugBountyBot  

1. Start the bot  

`python3 bbbot.py`  



## Use

| Function  	|   Command	|  Output 	|
|---	|---	|---	|
| DNS Subdomain Enumeration  	| dnsenum tbutler.org  	|  www.tbutler.org,mail.tbutler.org 	|


## Roadmap   

- [ ] Multithreading to improve dns reconnaissance speed 
- [ ] Anonymous scan mode to run dns enumeration over tor network
- [ ] Custom User Agent Strings  
- [ ] Allow users to determine how many subdomains to enumerate, ex. `dnsenum domain.tld -l 500`
