# Start Bot Service Handler, Define Bot Function
from common.dnsrecon import * 
import logging
import telebot

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

logging.basicConfig(filename='../logs/api.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')


def botserver(API_KEY):
    print('{!} Starting Bot Service')
    try:
        bot = telebot.TeleBot(API_KEY)
        logging.info('{!} 🤖 Starting Bot Server')

        @bot.message_handler(commands=['Greet','greet'])
        def greet(message):
            # telebot.logger.info("MESSAGE RECIEVED:",message)
            bot.reply_to(message,"Message Received, Thanks!")

        def dns_enum_check(message):
            request = message.text.split()
            if len(request) < 2 or request[0].lower() not in "dnsenum":
                bot.reply_to(message,"{X} Error in Request")
                return False 
            else: 
                bot.reply_to(message,"🔭 Searching for SubDomains, Check Back in a Bit")
                return True

        
        @bot.message_handler(func=dns_enum_check)
        def send_summary(message):
            request = message.text.split()
            domain_requested = str(request[1])
            output = 'Results: '
            output += dnsenum(domain_requested)

            bot.reply_to(message,output)
            return




        bot.polling() # constantly look for new messages
    except:
        logging.error('{X} Error running bot')


    print('{!} Ending Bot Service')
    return