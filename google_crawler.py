from selenium import webdriver
import pandas as pd 
import csv
from datetime import datetime
now = datetime.now()
nowDatetime = now.strftime('%Y.%m.%d %H시 %M분 %S초')

keyword = input("input keyword: ")
driver = webdriver.Chrome("./chromedriver.exe")

results = []

for page in range(0, 100, 10):
    driver.get("https://www.google.com/search?q="+keyword+"&tbm=nws&start="+str(page))

    articles = driver.find_elements_by_css_selector("div.gG0TJc")
    
    for ar in articles:
        title = ar.find_element_by_css_selector("h3").text
        source = ar.find_element_by_css_selector("span.xQ82C.e8fRJf").text
        summary = ar.find_element_by_css_selector("div.st").text
        link = ar.find_element_by_css_selector("a").get_attribute('href')
        
        temp = []
        temp.append(title)
        temp.append(source)
        temp.append(summary)
        temp.append(link)
        results.append(temp)

        #print(link)
        #print(summary)

    #print("="*50)
        #print(title)

f = open(f'{keyword} {"(google)"} {nowDatetime}.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in results:
    csvWriter.writerow(i)

f.close()

print('완료되었습니다.')
