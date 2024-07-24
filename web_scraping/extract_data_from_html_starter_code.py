# import all necessary libraries
import requests 
from bs4 import BeautifulSoup 

# define url of webpage to scrape from
url = "https://librairie.cantook.com/"

# send a request to get html code from the url and save the response 
response = requests.get(url, headers={"Accept": "text/html"}) 

# use BeautifulSoup to parse the text from the response 
parsed_response = BeautifulSoup(response.text, "html.parser") 

# find all divs with class 'product-card__image-wrapper' and then extract the 'alt' attribute of the img tag within each
titles = [div.find('img')['alt'] for div in parsed_response.find_all("div", class_="product-card__image-wrapper") if div.find('img')]

# iterate over the titles and print each
for title in titles:
    print(title)
