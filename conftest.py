from pytest import fixture
from selenium import webdriver


@fixture(scope="function")
def driver(browser, request):
    if browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    request.addfinalizer(driver.quit)
    return driver


def pytest_addoption(parser):
    group = parser.getgroup('selenium', 'Selenium options')
    group.addoption("--navegador", action="store", default="chrome")


@fixture()
def browser(request):
    return request.config.getoption("--navegador")