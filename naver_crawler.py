import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
now = datetime.now()
nowDatetime = now.strftime('%Y.%m.%d %H시 %M분 %S초')

keyword = input("input keyword: ")
results = []

for page in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?&where=news&query="+keyword+"&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&start="+str(page)+"&refresh_start=0",
                         headers = {"User-Agent" : "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    # 1. 컨테이너 수집
    articles = html.select("ul.type01 > li")
    # select는 선택자에 해당하는 모든 데이터를 리스트 형식으로 저장하는 함수이다.


    # 2. 기사별 데이터 수집(제목, 언론사)
    for ar in articles:
        title = ar.select_one("ul.type01 > li a._sp_each_title").text
        source = ar.select_one("ul.type01 > li span._sp_each_source").text
        summary = ar.select_one("dl > dd:nth-child(3)").text
        link = ar.select_one('a._sp_each_title').attrs['href']
        
        temp = []
        temp.append(title)
        temp.append(source)
        temp.append(summary)
        temp.append(link)
        results.append(temp)
        # .text는 가져온 raw데이터를 소스코드로 보기 위함.
        #print(title)
        #print(summary)
        #print(page, link.attrs['href'])
        #print(title, source, sep = "  //  ")
        # 기사 제목과 source가 "  //  "를 통해 구분된다.

    #print("="*50) # 페이지가 넘어갈때마다 구분해주기 위한 구분선
f = open(f'{keyword} {"(naver)"} {nowDatetime}.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in results:
    csvWriter.writerow(i)

f.close()

print('완료되었습니다.')