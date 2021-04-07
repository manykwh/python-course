import requests
from bs4 import BeautifulSoup

def scrape_dailysmarty(): 
    r = requests.get("http://dailysmarty.com/")
    if r.status_code != 200:
        return "error, could not pull from daily smarty, http error code: " + str(r.status_code)
    soup = BeautifulSoup(r.text, "html.parser")
    print("DailySmarty posts")
    print("-" * 24)
    for x in soup.find_all("a"):
        if(str(x).find("/posts/") > -1): # so its not -1 
            print("Title: " + scrape_dailysmarty_get_post_title(str(x)))
            print("Link: " + scrape_dailysmarty_get_post_link(str(x)))
            print("-" * 24)

    return "success"

def scrape_dailysmarty_get_post_link(x):
    after_href_index = x.find("href=") + 6
    ending_of_link_index = x.find("\"", after_href_index)
    return "http://dailysmarty.com" + x[after_href_index:ending_of_link_index]

def scrape_dailysmarty_get_post_title(x):
    after_greater_than_sign = x.find(">") + 1
    ending_of_post_title = x.find("</a>", after_greater_than_sign)
    return x[after_greater_than_sign:ending_of_post_title]

scrape_dailysmarty()

