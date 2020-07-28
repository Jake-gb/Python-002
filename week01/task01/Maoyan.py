import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

base_usrl = "https://maoyan.com/films?showType=3"
User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
Cookie = 'uuid_n_v=v1; uuid=3F678EF0CD8411EA9F13033660F9F0D7069D26FEF6AE4DF4AE237200EF7F7A0D; _csrf=c64bba4a877a2caca3c143c8d16432512672e6f4d8b308e2422f53d1204e86b8; mojo-uuid=6d471d47bce7c2fe312373d6bca135e2; _lxsdk_cuid=1737fd9d83ac8-06643e4e9e53c4-b7a1334-e1000-1737fd9d83ac8; _lxsdk=3F678EF0CD8411EA9F13033660F9F0D7069D26FEF6AE4DF4AE237200EF7F7A0D; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595577851,1595777572; mojo-session-id={"id":"286c689c7649dc1c160a1722bf7be6b1","time":1595866341767}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595867675; mojo-trace-id=5; __mta=42849690.1595577853353.1595867649762.1595867675076.10; _lxsdk_s=173910be161-2a2-ccb-87f%7C%7C11'
header = {"user-agent": User_Agent, "Cookie": Cookie}

response = requests.get(url=base_usrl, headers=header)
response.encoding = 'utf-8'
bs_info = bs(response.text, 'html.parser')
# print(bs_info.prettify())

mv_info = []
mv_list = bs_info.find_all("div", attrs={"class": "movie-item-hover"})
for i, tags in enumerate(mv_list):
    mv_name = tags.find(attrs={"class": "name"}).get_text()
    mv_type = tags.find_all(attrs={"class": "movie-hover-title"})[1].text[4:].strip()
    mv_time = tags.find_all(attrs={"class": "movie-hover-title"})[3].text[6:].strip()
    print(mv_name, mv_type, mv_time)
    mv_info.append((mv_name, mv_type, mv_time))
    if i == 9: break

top10 = pd.DataFrame(mv_info)
top10.to_csv('top10.csv', encoding='utf-8')
