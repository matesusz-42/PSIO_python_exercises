#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import TypeVar, Iterable
C = TypeVar('C', bound = 'Vehicle')
class Movable:
    def __init__(self, x : float, y : float) -> None:
        self.x = x
        self.y = y
    def move(self, dx : float, dy : float) -> None:
        self.x += float(dx)
        self.y += float(dy)
class Vehicle(ABC, Movable):
    def __init__(self, id_ : str, brand : str) -> None:
        
        Movable.__init__(self, x = 0.0, y = 0.0)
        self.id = id_
        self.brand = brand
    @abstractmethod
    def max_speed(self) -> float:
        pass
    def __str__(self) -> str:
        return f"{self.brand} :  {self.id}"
    
class Car(Vehicle):
    def __init__(self, id_ : str, brand : str, engine_hp : float) -> None:
        super().__init__(id_, brand):
        self.engine_hp = engine_hp
    def max_speed(self) -> float:
        return float(self.engine_hp)

class Bicycle(Vehicle):
    def __init__(self, id : str, brand : str, n_gears : int) -> None:
        super().__init__(id_, brand) #przekazujemy id i brand do konstruktora Vehicle
        self.n_gears = n_gears
    def max_speed(self) -> float:
        return float(self.n_gears) * 3.0
def vehicle_collection_as_string(vehicles : Iterable[Vehicle])-> str:
    #zwraca tekstowa reprezentacje kolekcji pojazdow rozdzielona znakami nowej linii
    #przechodzimy petla i wywolujemy str() dla kazdego obiektu
    #a to odpala metode __str__ z klasy Vehicle
    lines = [str(vehicle) for vehicle in vehicles]
    return "\n".join(lines)

def compute_min_travel_duration(distance : float, vehicle : Vehicle) -> float:
    return float(distance/vehicle.max_speed())
def compute_min_travel_duration_as_string(distance: float, vehicle : Vehicle) -> str:
    duration = compute_min_travel_duration(distance, vehicle)
    return f"{duration:.3f} h"
    
