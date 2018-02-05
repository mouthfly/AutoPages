from selenium import webdriver

class BocPage(object):
    
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://cmcoins.boc.cn/BOC15_CoinSeller/welcome.html")
    
    def close(self):
        self.driver.close()

    def find_popup(self):
        return 1
