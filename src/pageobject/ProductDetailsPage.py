from selenium.webdriver import Chrome
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ProductDetailsPage():
    def __init__(self, driver : Chrome):
        self.driver = driver

    select_add_cart="cart"
    select_product_name='/html/body/section/div/div/div[2]/div[2]/div[2]/div/h2'
    select_category='/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[1]'
    select_price='/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/span'
    select_availability='/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[2]'
    select_condition="/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[3]/b"
    select_brand="/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[4]/b"

 #product name, category, price, availability, condition, brand
    def verificar_cargar_de_pagina(self):

       assert self.driver.find_element(By.CLASS_NAME, self.select_add_cart).is_displayed()

    def verificar_detalle_producto(self):
        assert self.driver.find_element(By.XPATH,self.select_product_name).is_displayed()
        assert self.driver.find_element(By.XPATH, self.select_category).is_displayed()
        assert self.driver.find_element(By.XPATH, self.select_price).is_displayed()
        assert self.driver.find_element(By.XPATH, self.select_condition).is_displayed()
        assert self.driver.find_element(By.XPATH, self.select_brand).is_displayed()
