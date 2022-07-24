from symtable import Symbol
import requests
from bs4 import BeautifulSoup

SearchString=input("Input an item to search in amazon\n")
SearchString = SearchString.replace(" " , "+")
url = "https://www.amazon.in/s?k=" + SearchString
re=requests.get(url)
#print(re)
re_html = re.text
soup = BeautifulSoup(re_html, features="lxml")




search_list = soup.find("span",class_="rush-component s-latency-cf-section")
results = search_list.find_all("div",class_="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20" )

for result in results:
    name = result.find("span",class_="a-size-base-plus a-color-base a-text-normal").text
    if result.find("span",class_="a-price-symbol") is not None:
        sym = result.find("span",class_="a-price-symbol").text
        price = result.find("span",class_="a-price-whole").text
    else:
        sym=""
        price=""

    print(name + "\n" +sym + price +"\n")