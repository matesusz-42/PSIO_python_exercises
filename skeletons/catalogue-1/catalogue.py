#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
from typing import Dict, Any, Optional


class Product:
    def __init__(self, id_: str, name: str, price: float) -> None:
        # TODO: Zaimplementuj.
        
        self.id = id
        self.name = name
        self.price = price
    def __str__(self) -> str:
        return f"{self.name} [{self.id}]: ${self.price:.2f}"
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Product):
            return False
        return self.id == other.id and self.name == other.name and self.price == other.price
        


class Catalogue:
    # TODO: Zaimplementuj.
     Inventory = Dict[str, Product]
     def __init__(self, inventory:Inventory = None) -> None:
        if inventory is None:
            self.inventory: Catalogue.Inventory = {}
        else:
            self.inventory: Catalogue.Inventory == copy.deepcopy(inventory)
    def add_product(self, product: Product) -> None:
        product_copy = copy.deepcopy(product)
        self.inventory[product_copy.id] = product_copy
    def __contains__(self, id : str) -> bool:
        return id in self.inventory       