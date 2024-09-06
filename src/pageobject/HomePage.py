from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage():
    def __init__(self, driver:Chrome):
        self.driver = driver

    selector_btn_sign_up="(//a[normalize-space()='Signup / Login'])[1]"
    select_icono_home="//a[@href='/']"
    select_icono_loggen='//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a'
    select_link_text_delete="Delete Account"
    select_logout='//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a'
    select_contact_us='//*[@id="header"]/div/div/div/div[2]/div/ul/li[8]/a'
    select_btn_test_cases='//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a'
    select_btn_products="//a[@href='/products']"
    select_text_email_suscribirse="susbscribe_email"

    def navegar_home_page(self):
        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()
    def verificar_carga_de_pagina(self):
        assert self.driver.find_element(By.CLASS_NAME,"title").is_displayed()

    def click_en_sign_up(self):
        self.driver.find_element(By.XPATH, self.selector_btn_sign_up).click()

    def verificar_nombre_de_loggend(self):
        nombre="Diego"
        text_verificar=f"Logged in as {nombre}"
        text_loggen=self.driver.find_element(By.XPATH ,self.select_icono_loggen)
        assert  text_loggen.text== text_verificar
    def click_delete_account(self):
         self.driver.find_element(By.LINK_TEXT, self.select_link_text_delete).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.select_logout).click()

    def click_contact_us(self):
        self.driver.find_element(By.XPATH, self.select_contact_us).click()

    def click_test_cases(self):
        self.driver.find_element(By.XPATH, self.select_btn_test_cases).click()

    def click_products(self):
        self.driver.find_element(By.XPATH,self.select_btn_products).click()

    def scroll_footer(self):
        bajar = self.driver.find_element(By.ID, "footer")
        self.driver.execute_script("arguments[0].scrollIntoView();", bajar)

    def completar_email_y_suscribirse(self):
        email="1233@gmail.com"
        self.driver.find_element(By.ID,self.select_text_email_suscribirse).send_keys(email)
        self.driver.find_element(By.ID,"subscribe").click()

    def verificar_mensaje_de_suscripcion(self):
        driverwait = WebDriverWait(self.driver, 10)
        mensaje=driverwait.until(ec.visibility_of_element_located((By.ID,"success-subscribe")))
        assert mensaje.text=="You have been successfully subscribed!"





