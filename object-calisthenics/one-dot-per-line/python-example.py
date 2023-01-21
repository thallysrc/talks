from dataclasses import dataclass

@dataclass
class Stock:
    location: str
    quantity: int

@dataclass
class Product:
    stock: Stock

    def formatted_quantity(self):
        return f"{self.stock.quantity} N"


class Shelf:

    @staticmethod
    def show_stock():
        product = Product(stock=Stock(location="Joinville", quantity=3))

        # correct
        print(product.formatted_quantity())

        # incorrect
        print(f"{product.stock.quantity} N")

shelf = Shelf()

shelf.show_stock()