import allure
from selene import browser, have
from pages.cart import add_products_to_cart
from pages.cart import page_of_product


def test_add_book_to_cart():
    with allure.step('Add book to cart'):
        add_products_to_cart.open_cart_with_products(
            url=f'{page_of_product}/13/1/1')
    browser.open('/')
    with allure.step('Open cart with book'):
        add_products_to_cart.cart_open()

    browser.element('.product-name').should(have.text('Computing and Internet'))
    browser.element('.product-subtotal').should(have.text('10.00'))
    browser.element('.product-unit-price').should(have.text('10.00'))
