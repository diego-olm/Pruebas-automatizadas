from selenium.webdriver import Chrome
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class ProductPage():
    def __init__(self, driver : Chrome):
        self.driver = driver

    select_contenedor_producto='/html/body/section[2]/div/div/div[2]/div'
    select_btn_view_product=href="//a[@href='/product_details/1']"
    select_search_product="search_product"
    select_btn_search="submit_search"
    select_searched_products='title'





    def verificar_que_sean_visible_los_productos(self):
        assert  self.driver.find_element(By.XPATH, self.select_contenedor_producto).is_displayed()

    def seleccionar_primer_producto(self):
        bajar = self.driver.find_element(By.XPATH, self.select_btn_view_product)
        self.driver.execute_script("arguments[0].scrollIntoView();", bajar)
        self.driver.find_element(By.XPATH, self.select_btn_view_product).click()

    def completar_campo_de_busqueda_producto(self,producto):
        self.driver.find_element(By.ID,self.select_search_product).send_keys(producto)
        self.driver.find_element(By.ID, self.select_btn_search).click()

    def verificar_titulo_all_product(self):
        text_verificar="ALL PRODUCTS"
        text_titulo = self.driver.find_element(By.CLASS_NAME, self.select_searched_products)
        assert text_titulo.text==text_verificar
    def verificar_carga_pagina_all_products(self):
        text_verificar="SEARCHED PRODUCTS"

        text_titulo=self.driver.find_element(By.CLASS_NAME,self.select_searched_products)

        assert text_titulo.text==text_verificar