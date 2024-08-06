import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='function')
def browser_firefox():
    firefox_service = FirefoxService(GeckoDriverManager.install())
    driver = webdriver.Firefox(service=firefox_service)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def browser_chrome():
    chrome_service = ChromeService(ChromeDriverManager.install())
    driver = webdriver.Chrome(service=chrome_service)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def browser_edge():
    edge_service = EdgeService(EdgeChromiumDriverManager.install())
    driver = webdriver.Edge(service=edge_service)
    yield driver
    driver.quit()

