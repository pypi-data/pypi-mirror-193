from __future__ import annotations
import json
from dataclasses import dataclass, asdict
from enum import Enum
from pydantic import BaseModel
from typing import List


class OrderStatus(Enum):

    '''
    Order created, but no payment information left
    '''
    Created = 1

    '''
    Payment information has been registered, but payment
    not confirmed by financial institution
    '''
    Paid = 2

    '''
    Payment confirmed by financial institution
    '''
    PaymentConfirmed = 2

    '''
    Order has been shipped
    '''
    Shipped = 3

    '''
    Order has been delivered
    '''
    Delivered = 4


@dataclass
class OrderStatusChangedEvent:
    version: int
    user_id: int
    order_id: int
    status: OrderStatus

    def from_str(val: str) -> OrderStatusChangedEvent:
        val_dict = json.loads(val)
        return OrderStatusChangedEvent(
            version=int(val_dict['version']),
            user_id=int(val_dict['user_id']),
            order_id=int(val_dict['order_id']),
            status=OrderStatus(val_dict['status'])
        )

    def json(self):
        d = asdict(self)
        d['status'] = self.status.value
        return json.dumps(d)


class ProductBaseDto(BaseModel):
    name: str
    price: int


class ProductDto(ProductBaseDto):
    id: int

    class Config:
        orm_mode = True


class OrderBaseDto(BaseModel):
    user_id: int
    status: OrderStatus


class OrderProductMinDto(BaseModel):
    product_id: int
    amount: int

    class Config:
        orm_mode = True


class OrderDto(OrderBaseDto):
    id: int
    products: List[OrderProductMinDto] = []

    class Config:
        orm_mode = True


class AddOrderProductsCommand(BaseModel):
    products: List[OrderProductMinDto]


class RemoveOrderProductsCommand(BaseModel):
    product_ids: List[int]


class OrderInvoiceDto(BaseModel):
    total_price: int
