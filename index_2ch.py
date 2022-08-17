import os
import random
from time import sleep
import requests
from bs4 import BeautifulSoup

# from url_2ch import url

def get_url(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0"
    }
    req = requests.get(url=url, headers=headers)

    with open(f"2ch_{catalog}.html", "w") as file:
        file.write(req.text)
    if not os.path.exists(catalog):
        os.makedirs(catalog)
    return req.text

def get_content(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0"
    }
    req = requests.get(url=url, headers=headers)

    with open(f"2ch_{catalog}.html", "w") as file:
        file.write(req.text)
    if not os.path.exists(catalog):
        os.makedirs(catalog)
    return req.text

url = str(input("ВВедите URL "))
# print(url)

url_name = url.split("#")
catalog = url_name[-1]
main_link = "https://2ch.hk/"
soup = BeautifulSoup(get_url(url), "lxml")

all_hrefs = soup.find_all("a", class_="post__image-link")
# print(all_hrefs)
count = 0
for item in all_hrefs:
    sleep(random.randint(1, 5))
    file_name = item.find("img").get("data-title")
    file_href = main_link + item.get("href")
    print(file_href, file_name)
    req_content = requests.get(file_href)
    response = req_content.content
    with open(f"{catalog}/{file_name}", "wb") as file:
        file.write(response)
    count += 1
    print(f"Файл под номером {count} скачан под именем {file_name}")

label = ["http", "vk", "mamba", "https", "://", "mail", "yandex", "disk", "instagram"]
array_of_hrefs = []
dop_info = soup.find_all("a")
url_plus = url + " " + "\n"

with open(f"{catalog}/info.txt", "a") as file:
    file.write(url_plus)

for item in dop_info:
    for element in label:
        if element in item.text:
            line = item.text + " " + "\n"
            if line not in array_of_hrefs:
                array_of_hrefs.append(line)
                with open(f"{catalog}/info.txt", "a") as file:
                    file.write(line)
