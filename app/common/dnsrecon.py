# dnsrecon
import requests
import logging
import telebot
import sys
import os

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

logging.basicConfig(filename='../logs/api.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')



def dnsenum(domain_requested):
    output = dns_scanner(domain_requested)
    return output

def dns_scanner(domain_requested):

    try:
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, '../resources/subdomains-100.txt')

        file = open(filename)
        content = file.read()
        subdomains = content.splitlines()

        discovered_subdomains = []
        for subdomain in subdomains:

            url = f"http://{subdomain}.{domain_requested}"
            item_builder = f"✅ {subdomain}.{domain_requested}"
            item_builder += f"\n"
            try:
                # if this raises an ERROR, that means the subdomain does not exist
                requests.get(url)
            except requests.ConnectionError:
                # if the subdomain does not exist, just pass, print nothing
                pass
            else:
                print("[+] Discovered subdomain:", item_builder)
                # append the discovered subdomain to our list
                discovered_subdomains.append(item_builder)
    except FileNotFoundError:
        print('{X} Cant Find Subdomains File')
        sys.exit()

    data = " ".join(discovered_subdomains)

     
    return data