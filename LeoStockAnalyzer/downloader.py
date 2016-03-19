import bs4
import urllib2
import json
from bs4 import BeautifulSoup

from stock import Stock


class Downloader:

    def __init__(self):
        self.sp500_stock_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        self.nasdaq100_stock_url = "https://en.wikipedia.org/wiki/NASDAQ-100"

    def download_sp500_stock_info(self):

        stock_list = []

        request = urllib2.Request(self.sp500_stock_url)
        request.add_header("User-Agent",
                           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36")
        response = urllib2.urlopen(request)
        resp_soup = BeautifulSoup(response.read(), 'html.parser')
        table_tag = resp_soup.find("table")
        table_soup = BeautifulSoup(str(table_tag).replace("\n", ""), 'html.parser')
        tr_tag_list = table_soup.find_all("tr")
        row_index = 0
        for tr_tag in tr_tag_list:
            if row_index != 0:
                tr_tag_soup = BeautifulSoup(str(tr_tag), "html.parser")
                td_tag_list = tr_tag_soup.find_all("td")
                stock = Stock()
                stock.symbol = td_tag_list[0].string
                stock.name = td_tag_list[1].string
                stock.sector = td_tag_list[3].string
                stock.industry = td_tag_list[4].string
                stock_list.append(stock)

            row_index += 1
        return stock_list

    def download_nasdaq100_stock_info(self):

        stock_list = []
        request = urllib2.Request(self.nasdaq100_stock_url)
        request.add_header("User-Agent",
                           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36")
        response = urllib2.urlopen(request)
        resp_soup = BeautifulSoup(response.read(), "html.parser")
        ol_tag = resp_soup.find("ol")
        ol_tag_soup = BeautifulSoup(str(ol_tag).replace("\n", ""), "html.parser")
        li_tag_list = ol_tag_soup.find_all("li")
        for li_tag in li_tag_list:
            stock_str = unicode(li_tag.a["title"]).encode("utf-8") + unicode(li_tag.contents[1]).encode("utf-8")
            stock_name = stock_str[:stock_str.find("(")].lstrip().rstrip()
            stock_symbol = stock_str[stock_str.find("("):].replace("(", "").replace(")", "").lstrip().rstrip()
            stock = Stock()
            stock.name = stock_name
            stock.symbol = stock_symbol
            stock_list.append(stock)
            print stock.to_json()

        return stock_list

    def download_stock_history_data(self, symbol, start_date, end_date):
        pass

if __name__ == "__main__":
    downloader = Downloader()
    downloader.download_nasdaq100_stock_info()