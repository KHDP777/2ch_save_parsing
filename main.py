from bs4 import BeautifulSoup

url = str(input("ВВедите URL "))
if "arhivach" in url:
    print("Это ссылка с arhivach.ng")
    import module_arhivach
    catalog = module_arhivach.get_catalog(url)
    soup = BeautifulSoup(module_arhivach.get_req(url, catalog), "lxml")
    module_arhivach.put_content(soup, catalog)
    module_arhivach.put_txt(soup, catalog, url)
elif "2ch" in url:
    print("Это ссылка с 2ch.hk")
    import module_2ch
    catalog = module_2ch.get_catalog(url)
    soup = BeautifulSoup(module_2ch.get_req(url, catalog), "lxml")
    module_2ch.put_content(soup, catalog)
    module_2ch.put_txt(soup, catalog, url)
else:
    print("Error")



