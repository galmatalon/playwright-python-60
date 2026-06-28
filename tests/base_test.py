from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class BaseTest:

    login_page: LoginPage
    products_page: ProductsPage
    cart_page: CartPage


