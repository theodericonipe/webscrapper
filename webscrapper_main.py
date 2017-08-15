#This is created to get the site link of the query
import requests
from bs4 import BeautifulSoup
file = open('test2.txt', 'w')
print("type in a Valid search tag")
research_later = input("Search: ")
goog_search = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + research_later


r = requests.get(goog_search)

soup = BeautifulSoup(r.text, "html.parser")
siteName= "The Main site link for these query --> {}: \n".format(research_later)
str_file_data = siteName + soup.find('cite').text
file.write(str_file_data)
print(siteName + soup.find('cite').text)

