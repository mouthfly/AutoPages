from selenium import webdriver

class AutoPage(object):
    def setUp(self):
        self.driver =  webdriver.Firefox()
    
    def tearDown(self):
        self.driver.close()
    
    def preRun(self):
        pass

    def run(self):
        print("Run in AutoPage")
        pass

    def __init__(self):
        self.setUp()
        self.run()
        self.tearDown()