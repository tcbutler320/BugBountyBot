# dnsrecon
import requests
import logging
import telebot

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

logging.basicConfig(filename='../logs/api.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')



def dnsenum(domain_requested):
    output = dns_scanner(domain_requested)
    return output

def dns_scanner(domain_requested):

    try:
        file = open("/Users/tylerbutler/Documents/projects/programming/Github/bugbountybot/app/resources/subdomains.txt")
        content = file.read()
        subdomains = content.splitlines()

        discovered_subdomains = []
        for subdomain in subdomains:

            url = f"http://{subdomain}.{domain_requested}"
            try:
                # if this raises an ERROR, that means the subdomain does not exist
                requests.get(url)
            except requests.ConnectionError:
                # if the subdomain does not exist, just pass, print nothing
                pass
            else:
                print("[+] Discovered subdomain:", url)
                # append the discovered subdomain to our list
                discovered_subdomains.append(url)
    except FileNotFoundError:
        print('{X} Cant Find Subdomains File')
        sys.exit()

    data = " ".join(discovered_subdomains)

     
    return data