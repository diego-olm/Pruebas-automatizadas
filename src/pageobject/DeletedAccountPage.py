from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class DeletedAccountPage():
    def __init__(self, driver : Chrome):
        self.driver = driver

    select_mensaje_confirmacion_eliminar_cuenta='//*[@id="form"]/div/div/div/h2/b'

    def verificar_mensaje_de_eliminar_cuente(self):
        text_a_verificar="ACCOUNT DELETED!"
        mensaje_de_eliminar=  self.driver.find_element(By.XPATH , self.select_mensaje_confirmacion_eliminar_cuenta)
        print(mensaje_de_eliminar.text)
        print(mensaje_de_eliminar)
        assert mensaje_de_eliminar.text==text_a_verificar