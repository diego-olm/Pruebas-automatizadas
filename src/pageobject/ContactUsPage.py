import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ContactUsPage():
    def __init__(self, driver : Chrome):
        self.driver = driver

    select_titulo_get='//*[@id="contact-page"]/div[2]/div[1]/div/h2'
    select_form_name= "name"
    select_form_email="email"
    select_text_tarea='message'
    select_btn_submit='//*[@id="contact-us-form"]/div[6]/input'
    select_from_subject="subject"
    select_mensaje_exito='//*[@class="status alert alert-success"]'
    select_btn_home='//*[@id="form-section"]/a/span'
    def verificar_titulo_get_in_touch(self):
        titulo_verificar="GET IN TOUCH"
        text_titulo=self.driver.find_element(By.XPATH,self.select_titulo_get)
        assert text_titulo.text==titulo_verificar

    def completar_formulario(self,name,email,subject, message):

        self.driver.find_element(By.NAME, self.select_form_name).send_keys(name)
        self.driver.find_element(By.NAME,self.select_form_email).send_keys(email)
        self.driver.find_element(By.ID,self.select_text_tarea).send_keys(message)
        self.driver.find_element(By.NAME, self.select_from_subject).send_keys(subject)
        bajar=self.driver.find_element(By.NAME, "upload_file")
        self.driver.execute_script("arguments[0].scrollIntoView();",bajar)
        self.driver.find_element(By.NAME, "submit").click()


    def click_alerta_ok(self):

        Alert(self.driver).accept()

    def verificar_mensaje_envia_con_exito(self):
        mensaje_esperado="Success! Your details have been submitted successfully."
        driverwait = WebDriverWait(self.driver, 10)
        mensaje=driverwait.until(ec.visibility_of_element_located((By.XPATH, self.select_mensaje_exito)))
        assert mensaje_esperado==mensaje.text

    def click_boton_home(self):
        self.driver.find_element(By.XPATH, self.select_btn_home).click()