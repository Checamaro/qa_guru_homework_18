import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def open_browser(request):
    browser.config.base_url = 'https://demowebshop.tricentis.com/'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()

@pytest.fixture(scope='session')
def page_of_product():
    return 'https://demowebshop.tricentis.com/addproducttocart/catalog'
