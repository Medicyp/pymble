from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class Autoswiper:

    def __init__ (self):

        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:\\Users\Djinn\OneDrive\Documents\PycharmProjects\pinder\chromeprofile")

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.wait = WebDriverWait(self.driver, 6)

    # STEP 1. Open Chrome Browser and got to tinder.com
    def open_browser(self, url):

        self.driver.get(url)

    # STEP 2&3. Click on Login Button, then Click on option to login with FB credentials
    def click_button(self, text):
        sleep(2)
        login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//span[text()='{text}']")))
        login_button.click()

    # STEP 4. Switch to the front window to Accept all cookies
    def accept_cookies(self):
        sleep(3)
        self.driver.find_element_by_css_selector(".button_main").click()

    # STEP 4. Switch to new window
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    # STEP 5. Enter FB Credentials
    def input_text(self, input_id, text):
        sleep(2)
        input_text = self.wait.until(EC.visibility_of_element_located((By.ID, f"{input_id}")))
        input_text.send.keys(text)

    # INTERMEDIARY STEPS: Pop up, etc
    # By using the same Chrome session, I don't need to go through these steps

    # STEP 6. Swipe_right
    def swipe_like(self):
        sleep(2)
        selector = "#main > div > div.page__layout > main > div.page__content-inner > div > div > span > div.encounters-user__controls > div > div:nth-child(2) > div > div:nth-child(3) > div > div.encounters-action__icon > span"
        swipe_like = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        swipe_like.click()

    # STEP 7. Swipe_left
    def swipe_dislike(self):
        sleep(2)
        selector = "#main > div > div.page__layout > main > div.page__content-inner > div > div > span > div.encounters-user__controls > div > div:nth-child(2) > div > div:nth-child(1) > div > div.encounters-action__icon > span"
        swipe_like = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        swipe_like.click()

    # STEP 8. Swiping left or right with random function
    def random_finger(self):
        from random import random
        while True:
            rand = random()
            sleeping_time = rand * 3
            sleep(sleeping_time)

            dice = random()
            if dice < .71:
                self.swipe_like()
            else:
                self.swipe_dislike()


if __name__ == '__main__':
    run = Autoswiper()
    run.open_browser('https://bumble.com/app')
    run.random_finger()
