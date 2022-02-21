import requests
from urllib import parse
from colorama import *
from datetime import datetime

def subDomainResearch(url):
    NOW = datetime.utcnow().replace(microsecond=0)
    url = parse.urlsplit(url).netloc
    with open("subdomains-wordlist.txt","r") as wordlistFile:
        for line in wordlistFile:
            word = line.strip()
            mainUrl = word + "." + str(url)
            #print(mainUrl)
            try:
                response = requests.get("https://" + mainUrl)
                if response:
                    print(f"{Style.BRIGHT}[{NOW}]{Fore.GREEN}[SUCCESS] {Fore.BLUE}Discovered SubDomain => {mainUrl}{Style.RESET_ALL}")
                    with open("success-subdomain.txt", "a") as f:
                        f.write(mainUrl+"\n")
            except:
                print(f"{Style.BRIGHT}[{NOW}]{Fore.RED}[FAILED] {Fore.YELLOW}Failed search subdomain => {mainUrl}{Style.RESET_ALL}")