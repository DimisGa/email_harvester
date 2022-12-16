import requests
from bs4 import BeautifulSoup as bs
import re
import argparse

def url(domain):
    url="https://www.google.com/search?sxsrf=ALeKk02F0jyUQ6pLWkQ-WI2PXMImRIAgJA%3A1608570388331&ei=FNbgX7jUE8ybkwW8j6mACA&q=site:"+domain+"+intext%3A%40gmail.com&oq=site%3Aart.com+intext%3A%40gmail.com&gs_lcp=CgZwc3ktYWIQA1AAWABgy58BaABwAHgAgAGBAogBggSSAQUwLjIuMZgBAKoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwi4rt7Ux9_tAhXMzaQKHbxHCoAQ4dUDCA0&uact=5"
    
    r=requests.get(url)
    
    soup=bs(r.content,"lxml")
    
    for i  in soup.find_all("div",string=re.compile("@gmail.com")):
        if("@gmail.com" in str(i)):
            
            email=str(i)
         
            print(str(i))
    
            with open("fname.txt", "w", encoding="utf-8") as f:
                f.write(email)


def main():
    parser = argparse.ArgumentParser("%prod <Target Domain>")
    parser.add_argument("-d",dest="domain",type=str)

    args=parser.parse_args()

    d=args.domain
    if(args.domain):
        url(d)

    
main()