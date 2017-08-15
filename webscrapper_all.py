import requests #to import the request
from bs4 import BeautifulSoup #to import the Beautiful Soup module
import re #to import Regular Expression to be used for the formatting of the data
print(" Remember 10,20,30,40.......100 are the search results that google understands")
file = open('test2.txt','w')
search = input("Search: ") #this is the search input
results = int(input("Enter a Valid number of results that you need: ")) # valid options 10, 20, 30, 40, 50, and 100
page = requests.get("https://www.google.com/search?q={}&num={}".format(search, results))
soup = BeautifulSoup(page.content, "html5lib") #to get the requested page content 
links = soup.findAll("a") #to find all the anchor tags withing the page
for link in links :
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href: # to get the non-google Urls
        test_file = link.get('href').split("?q=")[1].split("&sa=U")[0] #assign a variable to store the search results
        file.write(test_file) #to write the results to the file
        print(link.get('href').split("?q=")[1].split("&sa=U")[0])