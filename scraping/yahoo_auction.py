import time
from datetime import datetime
import re

import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class scrape_auction:
    def __init__(self, 
                 exec_path="/mnt/d/app/chromedriver/chromedriver.exe", 
                 is_headless=False):
        op = Options()
        op.add_argument("--disable-gpu")
        op.add_argument("--disable-extensions")
        op.add_argument("--proxy-server='direct://'")
        op.add_argument("--proxy-bypass-list=*")
        op.add_argument("--start-maximized")
        op.add_argument("--ignore-certificate-errors")
        op.add_argument("--ignore-ssl-errors")
        op.add_argument("--log-level=3")
        if is_headless:
            op.add_argument("--headless")

        self.driver = webdriver.Chrome(executable_path=exec_path, options=op)
        self.waiting_time = 1

    def get(self, url):
        """seleniumで特定のURLを開く.
        
        Parameters
        ----------
        url : str   開くURL
        """
        self.driver.get(url)
    
    def quit(self):
        """seleniumを終了する.
        """
        self.driver.quit()

    def wait_selector(self, selector:str):
        """スクレイピング対象のCSSセレクタが出現するまで待つ.
        最大で30秒待機し、出現しない場合はエラー.

        Parameter
        ---------
        selector : str  スクレイピング対象のCSSセレクタ
        """
        time.sleep(self.waiting_time)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )

    def scrape(self, key_word, item_num):
        """落札相場をスクレイピングする.

        Parameters
        ----------
        key_word : str  検索ワード
        item_num : int  検索個数
        """
        
        # ---------------------------トップページ--------------------------- #
        top_url = "https://auctions.yahoo.co.jp/"
        self.get(top_url)
        self.wait_selector("#sbn")
        search = self.driver.find_element_by_xpath("//*[@id='sbn']/div/div[1]/div/input")
        search.send_keys(key_word)
        search.send_keys(Keys.ENTER)
        self.wait_selector(".SearchMode__closedLink")
        self.driver.find_element_by_class_name("SearchMode__closed").find_element_by_tag_name("a").click()
        

        # ---------------------------落札一覧--------------------------- #
        price_list = []
        date_list = []
        page = 1
        item = 0
        break_flag = False
        while True:
            self.wait_selector(".Product")
            products = self.driver.find_elements_by_class_name("Product")
            for product in products:
                # name = product.find_element_by_class_name("Product__titleLink").text
                # seller = product.find_element_by_class_name("Product__closedSeller").text
                price = product.find_element_by_class_name("Product__priceValue").text
                date = product.find_element_by_class_name("Product__time").text
                price_list.append(int(re.sub("\\D", "", price)))
                date_list.append(date)
                
                item += 1
                if item >= item_num:
                    break_flag = True
                    break
            
            if break_flag:
                break

            self.driver.find_element_by_class_name("Pager__lists").find_element_by_link_text(str(page+1)).click()
            page += 1
        self.quit()


        # ---------------------------描画--------------------------- #
        plt.hist(price_list, range=(0, 10000))
        plt.title("price distribution")
        plt.xlabel("price")
        plt.ylabel("amount")
        plt.savefig("image/price.png")
        plt.cla()

        hour = [int(re.split("[ :]", x)[-2]) for x in date_list]
        plt.hist(hour, range=(0, 24))
        plt.title("time distribution")
        plt.xlabel("time")
        plt.ylabel("amount")
        plt.savefig("image/time.png")


if __name__ == "__main__":
    s = scrape_auction()
    s.scrape("スマホケース", 100)