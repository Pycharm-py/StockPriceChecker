import bs4
import requests
try:
    while True:
        # go to that web page
        req = requests.get("https://finance.yahoo.com/quote/%5EIXIC?p=")
        # get the code of page
        content = req.content
        # parse the code of page
        soup = bs4.BeautifulSoup(content, "lxml")
        # get the price
        price = soup.find("div", {"class": "My(6px) Pos(r) smartphone_Mt(6px)"})
        print("price =", price.find("span").text)
except Exception:
    pass
