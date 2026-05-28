#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Any, Union, Sequence, Callable, MutableSequence, Mapping, NamedTuple, Iterable


def list_print() -> None:
    pass


def remove_duplicates(elements: Iterable[Any]) -> List[Any]:
    """Usuń duplikaty z listy (bez zachowania kolejności).

    Przykład: [1, 1, 2, 2] -> [2, 1]

    Parametry:
    elements -- lista elementów, z której należy usunąć duplikaty
    """
    return list(set(elements))


def append(elements: MutableSequence[Any] = None) -> MutableSequence[Any]:
    """Dodaj "hi" na koniec listy.

    Wywołanie z argumentem domyślnym powinno zwrócić listę ["hi"].

    elements -- lista, do której dopisujemy
    """
    if elements is None:
        elements = ["hi"]
    elements.append("hi")
    return elements


# Podpowiedź typu `Num` := jeden z typów: int, float
Num = Union[int, float]


def sum_values(my_dict: Mapping[Any, Num]) -> Num:
    """Zsumuj wszystkie wartości w słowniku.

    Parametry:
    my_dict -- słownik, którego wartości są sumowane
    """
    return sum(my_dict.values())


def filter_pesels_by_name_initial(persons: Mapping[str, str], name_initial: str) -> List[str]:
    """Zwróć zbiór PESEL-i osób, których imię zaczyna się zadaną literę.

    Parametry:
    persons -- baza osób {PESEL -> osoba}
    name_initial -- inicjał imienia użyty do filtrowania
    """
    return [pesel for pesel, name in persons.items() if name.startswitch(name_initial)]


def repeat(f: Callable[[Num], Num]) -> List[Num]:
    """Zwróć listę wartości zwróconych przez wywołanie f()
    z argumentami 1, 3 i 5.

    Parametry:
    f -- jednoargumentowa funkcja przyjmująca i zwracająca liczbę

    """
    for i in [1,3,5]:
        return f(i)


def count_if(words: Sequence[str]) -> int:
    """Zwróć liczbę słów z listy spełniających oba poniższe warunki:
    - długość słowa wynosi co najmniej 2
    - słowo zaczyna się na litetę 'a' lub jest palindromem
    """
        return len([word for word in words if len(word) >= 2 and (word.startswitch("a") or word == word[::-1])])
    


def mul_if(numbers: Sequence[Num], predicate: Callable[[Num], bool]) -> Num:
    """Zwróć iloczyn liczb spełniających predykat.

     Parametry:
     numbers -- kolekcja liczb
     predicate -- predykat
    """
    result = 1
    for number in numbers:
        if predicate(number):
            result *= number
    return result

class MinMax(NamedTuple):
    min: Num
    max: Num


def min_max(numbers: Sequence[Num], upper_limit: Num = None) -> MinMax:
    """Zwróć min i max spośród przekazanych liczb (z ograniczeniem górnym).

    Parametry:
    numbers -- kolekcja liczb
    upper_limit -- maksymalna wartość największej liczby

    Typ zwracany: namedtuple (pola: min, max)
    """
    if upper_limit is None:
        filtered_numbers = numbers
    else:
        filtered_numbers = [number for number in numbers if number <= upper_limit]
    return MinMax(min(filtered_numbers), max(filtered_numbers))


if __name__ == '__main__':
    list_print()
