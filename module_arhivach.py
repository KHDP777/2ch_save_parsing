import os
import random
from time import sleep
import requests
# from bs4 import BeautifulSoup
from proxy_auth import proxies

def get_req(url, catalog):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0"
    }
    req = requests.get(url=url, headers=headers, proxies=proxies)
    if not os.path.exists(catalog):
        os.makedirs(catalog)
    with open(f"{catalog}/2ch_{catalog}.html", "w") as file:
        file.write(req.text)
    return req.text


def get_catalog(url):
    url_name = url.split("/")
    return url_name[-2]


def word_ending(count):
    y = [1, 4, 5, 9, 0]
    o = [2, 6, 7, 8]
    i = [3]
    lol = [11, 12, 13, 14, 15, 16, 17, 18, 19]
    if count % 100 in lol:
        return "ый"
    else:
        if count % 10 in y:
            return "ый"
        if count % 10 in o:
            return "ой"
        if count % 10 in i:
            return "ий"


def put_content(soup, catalog):
    all_hrefs = soup.find_all("a", class_="img_filename")
    main_link = "https://arhivach.ng"
    count = 0
    for item in all_hrefs:
        sleep(random.randint(1, 5))
        if "http" in item.get("href"):
            file_href = item.get("href")
        else:
            file_href = main_link + item.get("href")
        buffer = file_href.split("/")
        file_name = buffer[-1]
        print(file_href, file_name)
        req_content = requests.get(file_href)
        response = req_content.content
        with open(f"{catalog}/{file_name}", "wb") as file:
            file.write(response)
        count += 1
        ending = word_ending(count)
        print(f"{count}-{ending} файл скачан под именем {file_name}")
    print("ВСЕ!!!")


def put_txt(soup, catalog, url):
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


# url = str(input("ВВедите URL "))
# catalog = get_catalog(url)
# soup = BeautifulSoup(get_req(url), "lxml")
# put_content(soup)
# put_txt(soup)



