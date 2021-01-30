from bs4 import BeautifulSoup
import time
from time import sleep
import requests
from random import randint
from html.parser import HTMLParser
import json

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

class SearchEngine:
    @staticmethod
    def search(query, sleep=True):
        if sleep: # Prevents loading too many pages too soon
            time.sleep(randint(10, 100))
        temp_url = '+'.join(query.split()) #for adding + between words for the query
        url = 'http://www.ask.com/web?q=' + temp_url
        soup = BeautifulSoup(requests.get(url, headers=USER_AGENT).text,"html.parser")
        
        
        new_results = SearchEngine.scrape_search_result(soup)
        return new_results

    @staticmethod
    def scrape_search_result(soup):
        raw_results = soup.find_all("div", attrs = {"class" : "PartialSearchResults-item-title"})
        results = []
        visited = set()
        #implement a check to get only 10 results and also check that URLs must not be duplicated
        for result in raw_results [:10]:
            link = result.find('a').get('href')
            if not visited.__contains__(link): 
                results.append(link)
                visited.add(link)
        return results

def json_output(data):
    with open('output.json', 'w+') as outfile:
        json.dump(data, outfile)

def read_queries(input_file):
    queries = []
    f = open(input_file, "r")
    for query in f:
        queries.append(query)
    return queries
#############Driver code############

dict = {}
queries = read_queries("100QueriesSet3.txt")
#print(queries)
#queries = ["Who discovered x-rays in 1885", "The European Union includes how many countries"]
for query in queries: 
    results = SearchEngine.search(query)
    dict[query] = results
json_output(dict)

####################################