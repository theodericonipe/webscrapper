import requests
from bs4 import BeautifulSoup

class Webscrapper(object):

	def __init__(self, search_query):
		search_query = (input("Search: "))
		self.search_query = search_query
		

class Webscrapper_main(object):

	def __init__(self):
		self.search_query = search_query

	def webscrapper_print_to_file(self):
		if self.search_query:
			print("The Number of valid results that can be inputed is 10, 20, 30----100")
			file = open('test2.txt','w')
			search_query = self.search_query
			# search_query = input("Search: ") #this is the search input
			results = int(input("Enter a Valid number of results that you need: ")) # valid options 10, 20, 30, 40, 50, and 100
			page = requests.get("https://www.google.com/search?q={}&num={}".format(search_query, results))
			soup = BeautifulSoup(page.content, "html5lib") #to get the requested page content 
			links = soup.findAll("a") #to find all the anchor tags withing the page
			for link in links :
			    link_href = link.get('href')
			    if "url?q=" in link_href and not "webcache" in link_href: # to get the non-google Urls
			        test_file = link.get('href').split("?q=")[1].split("&sa=U")[0] #assign a variable to store the search results
			        file.write(test_file) #to write the results to the file
			        print(link.get('href').split("?q=")[1].split("&sa=U")[0])


	def webscrapper_print_alone(self):
		if self.search_query:
			search_query = self.search_query
			# search_query = input("Search: ") #this is the search input
			results = int(input("Enter a Valid number of results that you need: ")) # valid options 10, 20, 30, 40, 50, and 100
			page = requests.get("https://www.google.com/search?q={}&num={}".format(search_query, results))
			soup = BeautifulSoup(page.content, "html5lib") #to get the requested page content 
			links = soup.findAll("a") #to find all the anchor tags withing the page
			for link in links :
			    link_href = link.get('href')
			    if "url?q=" in link_href and not "webcache" in link_href: # to get the non-google Urls
			        test_file = link.get('href').split("?q=")[1].split("&sa=U")[0] #assign a variable to store the search results
			        print(link.get('href').split("?q=")[1].split("&sa=U")[0])


	def webscrapper_cite_print_to_file(self):
		if self.search_query:
			file = open('test2.txt', 'w')
			search_query= self.search_query
			goog_search = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + search_query


			r = requests.get(goog_search)

			soup = BeautifulSoup(r.text, "html.parser")
			siteName= "The Main site link for these query --> {}: \n".format(search_query)
			str_file_data = siteName + soup.find('cite').text
			file.write(str_file_data)
			print(siteName + soup.find('cite').text)
					
	

	def webscrapper_cite_print_alone(self):
		if self.search_query:
			research_later = self.search_query
			goog_search = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + research_later
			r = requests.get(goog_search)
			soup = BeautifulSoup(r.text, "html.parser")
			siteName= "The Main site link for these query --> {}: \n".format(research_later)
			str_file_data = siteName + soup.find('cite').text
			print(siteName + soup.find('cite').text)


class Webscraper_final(Webscrapper, Webscrapper_main):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


web = Webscraper_final(object)

web.webscrapper_cite_print_alone()
#web.webscrapper_print_alone()
#web.webscrapper_print_to_file()
#web.webscrapper_cite_print_to_file()









		



	