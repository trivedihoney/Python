import requests
from bs4 import BeautifulSoup

SearchString=input("Input job to search in LinkedIn\n")
SearchString = SearchString.replace(" " , "%20")
url = "https://in.linkedin.com/jobs/search?keywords=" + SearchString
re=requests.get(url)
print(re)
if re.status_code == 200:
    soup = BeautifulSoup(re.text,"lxml")

    search_results = soup.find("ul", class_="jobs-search__results-list")

    results = search_results.find_all("li")


    print(len(results))
    for result in results:
        print(result.h3.text.strip())
        print(result.h4.text.strip())
        print(result.time.text.strip())
        print("\n")
