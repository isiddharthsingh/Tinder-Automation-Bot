from selenium import webdriver
from time import sleep
from random import random
import sys


class Tinderbot():
    def __init__(self):
        self.right = 0
        self.left = 0
        self.driver = webdriver.Chrome(service_args=["--verbose"])

    def login(self, id, password):
        self.driver.get("https://tinder.com/")
        sleep(4)

        #For facebook Login
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'More Options')]").click()
            sleep(2)
            fb_bt = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button').click()
        except:
            pass
        try:
            fb_bt = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button').click()
        except:
            pass
        try:
            fb_bt = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button').click()
        except:
            pass
        try:
            fb_bt = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[3]/button').click()
        except:
            pass


        sleep(2)
        b_win = self.driver.window_handles[0]
        popup = self.driver.switch_to_window(self.driver.window_handles[1])

        #Enter Login Details 
        self.driver.find_element_by_xpath("//input[@name=\"email\"]").send_keys(id)
        self.driver.find_element_by_xpath("//input[@name=\"pass\"]").send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="u_0_0"]').click()
        sleep(3)
        self.driver.switch_to_window(b_win)
        
        #Handle Popups
        sleep(7)
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/button').click()
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
        sleep(4)
        #self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button').click()

    def swipe_R(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()

    def swipe_L(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button').click()

    def auto_swipe(self):
        while True:
            rand = random()
            sleep(.5)
            try:
                if rand > .15:
                    self.swipe_R()
                    self.right = self.right + 1
                else:
                    self.swipe_L()
                    self.left = self.left + 1
                print("\r[+] Right Swipes : " + str(self.right) + " [-] Left Swipes : " + str(self.left), end="")
                #sys.stdout.flush()
            except KeyboardInterrupt:
                exit()
            except Exception:
                try:
                    self.close_match()
                except Exception:
                    self.close_popup()

    def close_match(self):
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button').click()

    def close_popup(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click()
        except Exception:
            try:
                self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]').click()
            except Exception:
                try:
                    self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/button[2]').click()
                except Exception:
                    pass

bot = Tinderbot()
#Type Your Username and Password here
bot.login('type your username', 'type your password')
print("'Ctrl + C' to exit")
bot.auto_swipe()