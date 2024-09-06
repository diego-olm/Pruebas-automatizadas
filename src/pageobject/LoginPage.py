from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage():
    def __init__(self, driver : Chrome):
        self.driver = driver

    select_title_login_form = '//*[@class="login-form"]/h2'
    select_email_address="email"
    select_password="password"
    select_btn_login='//*[@id="form"]/div/div/div[1]/div/form/button'
    select_text_error_emeil='//*[@id="form"]/div/div/div[1]/div/form/p'
    select_text_new_user='//*[@id="form"]/div/div/div[3]/div/h2'
    select_name_registro="name" #name
    select_email_registro='//*[@id="form"]/div/div/div[3]/div/form/input[3]' #email
    select_signuo='//*[@id="form"]/div/div/div[3]/div/form/button'
    select_mensaje_error_email_usado='//*[@id="form"]/div/div/div[3]/div/form/p'


    def verify_Login_to_your_account_is_visible(self):
        text_h2= self.driver.find_element(By.XPATH,self.select_title_login_form)
        assert text_h2.text=="Login to your account"

    def completar_email_password(self,email,password):

        self.driver.find_element(By.NAME ,self.select_email_address ).send_keys(email)
        self.driver.find_element(By.NAME, self.select_password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH , '//*[@id="form"]/div/div/div[1]/div/form/button').click()

    def mensaje_de_contrasenia_o_email_incorrecto(self):
        driverwait= WebDriverWait(self.driver,10)
        verificar_mensaje="Your email or password is incorrect!"
        text_alerta=driverwait.until(ec.visibility_of_element_located((By.XPATH, self.select_text_error_emeil)))
        assert text_alerta.text==verificar_mensaje

    def verificar_mensaje_new_user_signup(self):
        verificar_mensaje="New User Signup!"
        text_new_user=self.driver.find_element(By.XPATH,self.select_text_new_user)
        assert text_new_user.text==verificar_mensaje

    def registrar_nuevo_usuario(self,name, email):
        self.driver.find_element(By.NAME, self.select_name_registro).send_keys(name)
        self.driver.find_element(By.XPATH, self.select_email_registro).send_keys(email)

    def click_signout(self):
        self.driver.find_element(By.XPATH, self.select_signuo).click()

    def verificar_mensaje_error_email_ya_registrado(self):
        mensaje_verificar="Email Address already exist!"
        driverwait = WebDriverWait(self.driver, 10)
        mensaje_error_mostrado=driverwait.until(ec.visibility_of_element_located((By.XPATH, self.select_mensaje_error_email_usado)))
        assert mensaje_error_mostrado.text==mensaje_verificar










