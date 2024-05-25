import allure
from selene import browser, have
from pages.cart_page import add_products_to_cart


def test_add_book_to_cart(page_of_product):
    with allure.step('Add book to cart'):
        add_products_to_cart.open_cart_with_products(
            url=f'{page_of_product}/13/1/1')
    browser.open('/')
    with allure.step('Open cart with book'):
        add_products_to_cart.cart_open()

    browser.element('.product-name').should(have.text('Computing and Internet'))
    browser.element('.product-subtotal').should(have.text('10.00'))
    browser.element('.product-unit-price').should(have.text('10.00'))


def test_add_laptop_to_cart(page_of_product):
    with allure.step('Add laptop to cart'):
        add_products_to_cart.open_cart_with_products(
            url=f'{page_of_product}/31/1/1')
    browser.open('/')
    with allure.step('Open cart with laptop'):
        add_products_to_cart.cart_open()

    browser.element('.product-name').should(have.text('14.1-inch Laptop'))
    browser.element('.product-subtotal').should(have.text('1590.00'))
    browser.element('.product-unit-price').should(have.text('1590.00'))


def test_add_jeans_to_cart(page_of_product):
    with allure.step('Add jeans to cart'):
        add_products_to_cart.open_cart_with_products(
            url=f'{page_of_product}/36/1/1')
    browser.open('/')
    with allure.step('Open cart with jeans'):
        add_products_to_cart.cart_open()

    browser.element('.product-name').should(have.text('Blue Jeans'))
    browser.element('.product-subtotal').should(have.text('1.00'))
    browser.element('.product-unit-price').should(have.text('1.00'))


def test_add_phone_to_cart(page_of_product):
    with allure.step('Add phone to cart'):
        add_products_to_cart.open_cart_with_products(
            url=f'{page_of_product}/43/1/1')
    browser.open('/')
    with allure.step('Open cart with smartphone'):
        add_products_to_cart.cart_open()

    browser.element('.product-name').should(have.text('Smartphone'))
    browser.element('.product-subtotal').should(have.text('100.00'))
    browser.element('.product-unit-price').should(have.text('100.00'))
