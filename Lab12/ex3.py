# parse the faculty webpage and extract specific contents using Beautifulsoup
#https://shidler.hawaii.edu/itm/people
from bs4 import BeautifulSoup
import urllib.request
import ssl

ssl._create_default_https_context=ssl._create_unverified_context


url = "https://shidler.hawaii.edu/itm/people"
print(f"Opening {url}...")
#opens the url save as variable
itm_html = urllib.request.urlopen(url)
html_to_parse = BeautifulSoup(itm_html, "html.parser")

#find just the people in the itm page.  create a list
list_of_people = html_to_parse.find_all('h2', class_= 'title')
itm_people = []
for element in list_of_people:
    itm_people.append(element.text)
    print(element.text)