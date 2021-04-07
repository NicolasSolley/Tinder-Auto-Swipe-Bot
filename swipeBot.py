from selenium import webdriver
import time


class SwipeBot():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.tinder.com")
        self.driver.maximize_window()
        time.sleep(1)
        acceptCookies = self.driver.find_element_by_xpath('//*[@id="t-690321948"]/div/div[2]/div/div/div[1]/button')
        acceptCookies.click()
        print("Cookies Accepted")
        time.sleep(1)
        loginButton = self.driver.find_element_by_xpath(
            '//*[@id="t-690321948"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
        loginButton.click()
        print("Login Button Clicked")
        time.sleep(2)
        fbLogin = self.driver.find_element_by_xpath(
            '//*[@id="t--1349883856"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fbLogin.click()
        baseWindowOne = self.driver.window_handles[0]
        self.driver.switch_to_window(bot.driver.window_handles[1])
        time.sleep(1)
        emailEntered = self.driver.find_element_by_xpath('//*[@id="email"]')
        emailEntered.send_keys("Email")
        passwordEntered = self.driver.find_element_by_xpath('//*[@id="pass"]')
        passwordEntered.send_keys("Password")
        time.sleep(1)
        completeLogin = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        completeLogin.click()
        self.driver.switch_to_window(baseWindowOne)
        time.sleep(3)

    def allowLocation(self):
        time.sleep(2)
        allowLoc = self.driver.find_element_by_xpath('//*[@id="t--1349883856"]/div/div/div/div/div[3]/button[1]')
        allowLoc.click()
        time.sleep(1)
        allowNot = self.driver.find_element_by_xpath('//*[@id="t--1349883856"]/div/div/div/div/div[3]/button[1]')
        allowNot.click()

    def likeMatch(self):
        likeButton = self.driver.find_element_by_xpath(
            '//*[@id="t-690321948"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        likeButton.click()

    def autoSwipeMatch(self):
        time.sleep(5)
        matching = True
        time.sleep(0.5)
        while matching:
            try:
                self.likeMatch()
            except Exception:
                try:
                    self.closeNotificationHomeScreen()
                except Exception:
                    try:
                        self.superLikeClose()
                    except:
                        print("No matches found")
                        time.sleep(20)






    def closeNotificationHomeScreen(self):
        closeHomeScreenNotification = self.driver.find_element_by_xpath(
            '//*[@id="t--1349883856"]/div/div/div[2]/button[2]')
        closeHomeScreenNotification.click()

    def superLikeClose(self):
        closeSuperLike = self.driver.find_element_by_xpath('//*[@id="t--1349883856"]/div/div/button[2]')
        closeSuperLike.click()


bot = SwipeBot()
bot.login()
bot.allowLocation()
bot.autoSwipeMatch()
