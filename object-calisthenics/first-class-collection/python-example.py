# 4 first class collection
class Bill:
    def __init__(self):
        self._payments = []
        self._attachments = []

    def add_payment(self, payment):
        self._payments.append(payment)

    def add_attachment(self, attachment):
        self._attachments.append(attachment)




from dataclasses import dataclass
from typing import List

@dataclass
class Payment:
    mode: int
    value: int


class PaymentCollection:
    def __init__(self):
        self._payments: List[Payment] = []

    def add(self, payment: dict):
        if payment.mode == 3:
            raise Exception("Not supportted payment mode")

        self._payments.append(payment)

    def get_all(self) -> List[Payment]:
        return self._payments

    def total(self) -> int:
        return sum([payment.value for payment in self._payments])


class AttachmentCollection:
    def __init__(self):
        self._attachments = []

    def add(self, file: bytes):
        if len(file) > 5_000_000_000:
            raise Exception("too big")
        self._attachments.append(file)




class Bill:
    def __init__(self, payment, attachment):
        self.value = 100
        self._payments = []
        self._payment_collection: PaymentCollection = payment
        self._attachment_collection: AttachmentCollection = attachment

    def add_payment(self, payment):
        self._payment_collection.add(payment)

    def total_payment(self):
        return self._payment_collection.total()

    def get_all_payments(self) -> List[Payment]:
        return self._payment_collection.get_all()

    def add_attachment(self, attachment):
        self._attachment_collection.add(attachment)


bill = Bill(payment=PaymentCollection(), attachment=AttachmentCollection())
