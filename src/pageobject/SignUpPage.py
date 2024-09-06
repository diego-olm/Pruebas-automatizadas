
from selenium.webdriver import Chrome
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SignUpPage():
    def __init__(self, driver : Chrome):
        self.driver = driver

    select_title="title"

    def verificar_carga_de_titulo(self):
        assert self.driver.find_element(By.CLASS_NAME,self.select_title).is_displayed()