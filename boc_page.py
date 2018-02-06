from auto_page import AutoPage
from selenium import webdriver

class BocPage(AutoPage):
    
    def preRun(self):
        self.driver.get("https://cmcoins.boc.cn/BOC15_CoinSeller/welcome.html")
    
    def run(self):
        self.value = 1
