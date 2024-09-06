from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestCasesPage():
    def __init__(self, driver : Chrome):
        self.driver = driver

    text_primer_test_cases= '//*[@id="form"]/div/div[2]/div/div[1]/h4/a/u'

    def verificar_carga_pagina(self):
        text_esperado="Test Case 1: Register User"
        texto_titulo=self.driver.find_element(By.XPATH, self.text_primer_test_cases)
        assert  texto_titulo.text==text_esperado