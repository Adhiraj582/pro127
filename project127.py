from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver_win32\chromedriver.exe")
browser.get(url)
time.sleep(10)


def scrape():
    headers = ["name", "distance",
               "mass", "radius"]
    planet_data = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for ul_tag in soup.find_all("table", attrs={"class", "wikitable"}):
        li_tags = ul_tag.find_all("td")
        temp_list = []
        for index, li_tag in enumerate(li_tags):
            if index == 0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")
        planet_data.append(temp_list)
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)


scrape()
