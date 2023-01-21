from dataclasses import dataclass
from typing import List

@dataclass
class Payment:
    mode: int
    value: int


class PaymentCollection:
    def __init__(self):
        self._payments: List[Payment] = []

    def add(self, payment: Payment) -> None:
        if payment.mode == 3:
            raise Exception("Not supportted payment mode")

        self._payments.append(payment)

    def get_all(self) -> List[Payment]:
        return self._payments

    def total(self) -> int:
        return sum([payment.value for payment in self._payments])


class Bill:
    def __init__(self, collection):
        self.value = 100
        self._payment_collection: PaymentCollection = collection

    def add_payment(self, payment) -> None:
        self._payment_collection.add(payment)

    def total_payment(self) -> int:
        return self._payment_collection.total()

    def get_all_payments(self) -> List[Payment]:
        return self._payment_collection.get_all()

bill = Bill(collection=PaymentCollection())
