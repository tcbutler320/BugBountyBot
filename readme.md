# Bug Bounty Bot   

> A telegram bot with commands to simplify bug bounty tasks 

![](/docs/resources/readme.png)

+  [Installation](#installation)
+  [Use](#use)
+  [Road Map](#road-map)


## Installation  

BugBountyBot is open-source so you can run the bot on your own server. The following installation instructions are designed to be used with an Ubunto Virtual Private Server, from a vendor such as [digitalocean](https://www.digitalocean.com/).  

### Provision Virtual Private Server 

1. Create a Virtual Private Server. See [digitalocean](https://www.digitalocean.com/)

2. Make a new non-root sudo user. see [tutorial](https://www.digitalocean.com/community/tutorials/how-to-create-a-sudo-user-on-ubuntu-quickstart)

3.  Install PiP

`sudo apt install python3-pip`

4. Install python3-pip Package Manager

`sudo apt install python3-pip`

5.  Install pyTelegramBotAPI package

`pip3 install pyTelegramBotAPI`


### App BugBountyBot

1. Clone the bot to your server

`git clone https://github.com/tcbutler320/BugBountyBot.git`

### Create Telegram API Key 

1.  Message (botfather)[] on telegram to get a new api key

`/newbot`

2. Create a `.env` file in the root of your bugbountybot application folder with your new apikey

`echo "API_KEY=[KEY]" > .env`  

### Start BugBountyBot  

1. Start the bot  

`python3 bbbot.py`  

2. (A) Alternatively, schedule your bot using cron 

`crontab -e`

2. (B) Set your cronjob to run at [requested intervals](https://crontab.guru/every-1-minute)

*Use a bash script to check if bugbountybot is already running*

Crontab entry  

`* * * * * /home/bugbountybot/scripts/isRunning.sh`

Script  

```bash
#!/bin/sh
if ps -ef | grep -v grep | grep bbbot.py ; then
        exit 0
else
        /usr/bin/python3 /home/bugbountybot/app/bbbot.py >>  ~/cron.log 2>&1
        exit 0
fi
```




## Use

| Function  	|   Command	|  Output 	|
|---	|---	|---	|
| DNS Subdomain Enumeration  	| dnsenum tbutler.org  	|  www.tbutler.org,mail.tbutler.org 	|


## Roadmap   

- [ ] Multithreading to improve dns reconnaissance speed 
- [ ] Anonymous scan mode to run dns enumeration over tor network
- [ ] Custom User Agent Strings  
- [ ] Allow users to determine how many subdomains to enumerate, ex. `dnsenum domain.tld -l 500`
