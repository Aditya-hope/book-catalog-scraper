#http://books.toscrape.com

#what to scrape
"""Book Title
Price
Rating (One, Two, Three, Four, Five)
Availability (In stock or not)"""



#todo
"""Step 1 → Open books.toscrape.com and inspect elements
         Find class names for title, price, rating, availability

Step 2 → Setup Selenium and open the site

Step 3 → Hand page source to BeautifulSoup
         Extract all 4 fields from each book card

Step 4 → Scrape multiple pages
         Hint → look at the URL when you click next page

Step 5 → Clean with Pandas
         Remove duplicates, fix any messy data

Step 6 → Save to Excel

Step 7 → Tell me your result!"""
import openpyxl
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
availability=[]
prices=[]
ratings=[]
titles=[]

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
for page in range(1,51):
    url=f"http://books.toscrape.com/catalogue/page-{page}.html"

    driver.get(url)

    soup=BeautifulSoup(driver.page_source,"html.parser")
    all_titles=soup.find_all(name='h3')
    # print(all_titles)

    for title in all_titles:
        temp=title.find("a")
        titles.append(temp.get("title"))


    #all ratings in 1 page
    all_ratings = soup.select("p.star-rating")

    for rate in all_ratings:
        rating = rate.get("class")[1]  # [0]=star-rating, [1]=Three/One/Five
        ratings.append(rating)


    # all price for 1 page
    all_price=soup.find_all(name="p",class_="price_color")

    for pri in all_price:
        prices.append(pri.getText())



    #all availability of 1 page
    availability_list=soup.find_all(name="p",class_="instock availability")

    for stock in availability_list:
        availability.append(stock.getText().strip())



df = pd.DataFrame({
    'Title'       : titles,
    'Rating'      : ratings,
    'Price'       : prices,
    'Availability': availability,
})
print(df)

df.to_excel("book_scraper.xlsx",index=False)

driver.quit()