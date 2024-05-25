import allure
from selene import browser, have
from pages.cart import add_products_to_cart
from pages.cart import page_of_product


def test_add_laptop_to_cart():
    with allure.step('Add laptop to cart'):
        add_products_to_cart.open_cart_with_products(
            url=f'{page_of_product}/31/1/1')
    browser.open('/')
    with allure.step('Open cart with laptop'):
        add_products_to_cart.cart_open()

    browser.element('.product-name').should(have.text('14.1-inch Laptop'))
    browser.element('.product-subtotal').should(have.text('1590.00'))
    browser.element('.product-unit-price').should(have.text('1590.00'))
