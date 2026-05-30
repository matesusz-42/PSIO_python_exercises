#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
from typing import Dict, Any, Optional


class Product:
    def __init__(self, id_ : str, name : str, price : float):
        self.id = id_
        self.name = name
        self.price = price
    def __str__(self) -> str:
        return f"{self.nazwa} [{self.id}] : ${self.price:.2f}"
    def __eq__(self, other : Any) -> bool:
        if not isinstance(other, Product):
            return False
        return self.id == other.id and self.name == other.name and self.price == other.price


        


Inventory = Dict[str, Product]
        
class Catalogue:
    Inventory = Dict[str, Product]
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

     