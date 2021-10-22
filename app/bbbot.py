# bug bounty bot 

import os
import sys
import logging
from common.dnsrecon import *
from common.botserver import *
from dotenv import load_dotenv, find_dotenv

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

logging.basicConfig(filename='../logs/api.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')


# Get Enviorment Variables and API Keys
def initialize():
    try: 
        load_dotenv(find_dotenv())
        logging.info('{!} 🔑 Importing API Keys')
        return os.getenv('API_KEY')
    except:
        sys.exit()

def main():
    APIKEY = initialize()
    botserver(APIKEY)
    sys.exit()


if __name__ == "__main__":
    main()