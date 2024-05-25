import allure
from selene import browser, have
from pages.cart import add_products_to_cart
from pages.cart import page_of_product


def test_add_phone_to_cart():
    with allure.step('Add phone to cart'):
        add_products_to_cart.open_cart_with_products(
            url=f'{page_of_product}/43/1/1')
    browser.open('/')
    with allure.step('Open cart with smartphone'):
        add_products_to_cart.cart_open()

    browser.element('.product-name').should(have.text('Smartphone'))
    browser.element('.product-subtotal').should(have.text('100.00'))
    browser.element('.product-unit-price').should(have.text('100.00'))
