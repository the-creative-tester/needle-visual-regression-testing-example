from needle.cases import NeedleTestCase
from selenium import webdriver

class SydneyMorningHeraldNetworkStripTest(NeedleTestCase):

    engine_class = 'needle.engines.perceptualdiff_engine.Engine'
    viewport_width = 1024
    viewport_height = 768

    def test_check_network_strip_of_sydney_morning_herald_home_page(self):
        self.driver.set_page_load_timeout(20)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('http://www.smh.com.au/')
        self.assertScreenshot('#network-strip', 'network-strip-capture')
