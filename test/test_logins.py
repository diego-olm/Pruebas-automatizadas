import time

from pytest import mark
from src.pageobject.DeletedAccountPage import DeletedAccountPage
from src.pageobject.HomePage import HomePage
from src.pageobject.LoginPage import LoginPage
from src.pageobject.ContactUsPage import ContactUsPage
from src.pageobject.ProductDetailsPage import ProductDetailsPage
from src.pageobject.ProductPage import ProductPage
from src.pageobject.SignUpPage import SignUpPage
from src.pageobject.TestCasesPage import TestCasesPage


class loginTest():
    @mark.registro
    def test_login_user_with_correct_email_and_password(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        deleted_account_page = DeletedAccountPage(driver)
        email = "diego.94olm@gmail.com"
        password = "1234"
        home_page.navegar_home_page()
        home_page.verificar_carga_de_pagina()
        home_page.click_en_sign_up()

        login_page.verify_Login_to_your_account_is_visible()
        login_page.completar_email_password(email,password)
        login_page.click_login_button()

        home_page.verificar_nombre_de_loggend()
        home_page.click_delete_account()
        deleted_account_page.verificar_mensaje_de_eliminar_cuente()

    @mark.registro
    def test_case_3_login_user_with_incorrect_email_and_password(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        email = "diego.94olm@gmail.com"
        password = "basura"
        home_page.navegar_home_page()
        home_page.verificar_carga_de_pagina()
        home_page.click_en_sign_up()

        login_page.verify_Login_to_your_account_is_visible()
        login_page.completar_email_password(email, password)
        login_page.click_login_button()
        login_page.mensaje_de_contrasenia_o_email_incorrecto()

    @mark.registro
    def test_case_4_logout_user(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        deleted_account_page = DeletedAccountPage(driver)
        email = "diego.94olm@gmail.com"
        password = "1234"
        home_page.navegar_home_page()
        home_page.verificar_carga_de_pagina()
        home_page.click_en_sign_up()

        login_page.verify_Login_to_your_account_is_visible()
        login_page.completar_email_password(email, password)
        login_page.click_login_button()

        home_page.verificar_nombre_de_loggend()
        home_page.click_logout()
        login_page.verify_Login_to_your_account_is_visible()

    @mark.registro
    def test_case_5_register_user_with_existing_email(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        email = "diego.94olm@gmail.com"
        nombre = "Diego"
        home_page.navegar_home_page()
        home_page.verificar_carga_de_pagina()
        home_page.click_en_sign_up()
        login_page.registrar_nuevo_usuario(nombre,email)
        login_page.click_signout()
        login_page.verificar_mensaje_error_email_ya_registrado()

    @mark.producto
    def test_case_6_contact_us_form(self, driver):
        nombre="diego"
        email = "diego.94olm@gmail.com"
        subject="adassadad"
        mensaje="buenas tardes"
        home_page = HomePage(driver)
        contact_us= ContactUsPage(driver)
        home_page.navegar_home_page()
        home_page.verificar_carga_de_pagina()
        home_page.click_contact_us()
        contact_us.verificar_titulo_get_in_touch()
        contact_us.completar_formulario(nombre,email,subject,mensaje)
        contact_us.click_alerta_ok()
        contact_us.verificar_mensaje_envia_con_exito()
        contact_us.click_boton_home()
        home_page.verificar_carga_de_pagina()

    @mark.producto
    def test_case_7_verify_test_cases_Page(self, driver):
        home_page = HomePage(driver)
        test_cases_page=TestCasesPage(driver)
        home_page.navegar_home_page()
        home_page.verificar_carga_de_pagina()
        home_page.click_test_cases()
        test_cases_page.verificar_carga_pagina()

    @mark.producto
    def test_case_8_verify_all_products_and_product_detail_page(self, driver):
        home_page = HomePage(driver)
        product_page=ProductPage(driver)
        product_details_page=ProductDetailsPage(driver)
        home_page.navegar_home_page()
        home_page.verificar_carga_de_pagina()
        home_page.click_products()
        product_page.verificar_titulo_all_product()
        product_page.verificar_que_sean_visible_los_productos()
        product_page.seleccionar_primer_producto()
        product_details_page.verificar_cargar_de_pagina()
        product_details_page.verificar_detalle_producto()

    @mark.producto
    def test_case_9_search_product(self, driver):
        producto="Dress"
        home_page = HomePage(driver)
        product_page = ProductPage(driver)
        home_page.navegar_home_page()
        home_page.verificar_carga_de_pagina()
        home_page.click_products()
        product_page.verificar_titulo_all_product()
        product_page.completar_campo_de_busqueda_producto(producto)
        product_page.verificar_carga_pagina_all_products()
        product_page.verificar_que_sean_visible_los_productos()

    @mark.registro
    def test_case_10_verify_subscription_in_home_page(self,driver):
        home_page = HomePage(driver)
        home_page.navegar_home_page()
        home_page.verificar_carga_de_pagina()
        home_page.scroll_footer()
        home_page.completar_email_y_suscribirse()

        time.sleep(5)




