"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture()
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(999) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False
        # TODO напишите проверки на метод check_quantity
        pass

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(0)
        assert product.quantity == 1000
        product.buy(1)
        assert product.quantity == 999
        product.buy(300)
        assert product.quantity == 699
        product.buy(699)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        assert len(cart.products) == 0
        cart.add_product(product)
        assert cart.products[product] == 1
        cart.add_product(product, 999)
        assert cart.products[product] == 1000

    def test_remove_product(self, product, cart):
        cart.add_product(product, 144)
        cart.remove_product(product, 7)
        assert cart.products[product] == 137
        cart.remove_product(product)
        assert len(cart.products) == 0
        # cart.add_product(product, 100)
        # cart.remove_product(product, 100)
        # assert cart.products[product] == 0
        cart.add_product(product, 300)
        cart.remove_product(product, 350)
        assert len(cart.products) == 0

    def test_clear(self, cart, product):
        cart.add_product(product, 45)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 36)
        assert cart.get_total_price() == 3600

    def test_buy(self, cart, product):
        cart.add_product(product, 10)
        cart.buy()
        assert len(cart.products) == 0

    def test_product_buy_more_than_available(self, cart, product):
        with pytest.raises(ValueError):
            product.buy(1001)
            assert cart.buy()
