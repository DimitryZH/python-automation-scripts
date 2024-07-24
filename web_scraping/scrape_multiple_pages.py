# import relevant libraries
import requests 
from bs4 import BeautifulSoup
from time import sleep

# for loop to iterate over the range of page numbers you want to scrape from
# note: python includes the first argument and excludes the second argument in the range function
for page_number in range(1, 3):

    # define the url
    url = "https://librairie.cantook.com/collections/coups-de-coeur-romance?page=" + str(page_number)

    # send a request to get html code from that url
    response = requests.get(url, headers={"Accept": "text/html"}) 

    # parse the response
    parsed_response = BeautifulSoup(response.text, "html.parser") 

    # extract all the elements specific to book titles from that page
    title_elements = [div.find('img')['alt'] for div in parsed_response.find_all("div", class_="product-card__image-wrapper") if div.find('img')]

    # extract all the elements specific to book authors from that page
    author_elements = [a.text.strip() for a in parsed_response.find_all("a", class_="product-card__author")]

    # print out the page number 
    print("\nPage Number:", page_number)

    # print out the book titles appearing on that page
    print("\nBook Titles:", title_elements)

    # print out the book authors appearing on that page
    print("\nBook Authors:", author_elements)

    # pause the program for 1 second between iterations of the loop
    sleep(1)

