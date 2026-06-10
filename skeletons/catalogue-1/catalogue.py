#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
from typing import Dict, Any, Optional
Inventory = Dict[str, 'Product']

class Product:
    MAX_PRICE: float = 100.00
    def __init__(self, id_ : Optional[str] = None, name : str = "", price : float = 0.0) -> None:
        if id_ is None:
            self.id = Product.generate_id(name)
        else:
            self.id = id_
        self.name = name
        self.price = price
    @property
    def price(self) -> float:
        return self._price
    @price.setter
    def price(self, value : float) -> None:
        if value > Product.MAX_PRICE:
            self._price = float(Product.MAX_PRICE)
        else:
            self._price = float(value)
    @classmethod
    def generate_id(cls, name : str) -> str:
        name_no_spaces = name.replace(" ", "")
        total_length = len(name)
        return f"{name_no_spaces}_{total_length}"
    def __str__(self) -> str:
        return f"{self.nazwa} [{self.id}] : ${self.price:.2f}"
    def __eq__(self, other : Any) -> bool:
        if not isinstance(other, Product):
            return False
        return self.id == other.id and self.name == other.name and self.price == other.price


        



        
class Catalogue:
    Inventory = Inventory
    def __init__(self, inventory: Optional[Inventory] = None) -> None:
        if inventory is None:
            self.inventory : Inventory = {}
        else:
            self.inventory = invertory.copy()
        
    def add_product(self, product:Product) -> None:
        self.inventory[product.id] = product
        print(f"[katalog] dodano produkt : {product.name}")
    def __contains__(self, id_ : str) -> bool:
        return id_ in self.inventory

     