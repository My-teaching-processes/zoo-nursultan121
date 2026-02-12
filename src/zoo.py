"""Класс Zoo, демонстрирующий композицию и управление коллекцией."""

from typing import List, Optional
from src.animal import Animal


class Zoo:
    """
    Класс Zoo, управляющий коллекцией животных.
    """

    def __init__(self, name: str, location: str) -> None:
        """
        Инициализация зоопарка.
        
        Аргументы:
            name: Название зоопарка
            location: Локация зоопарка
        """
        self._name = name
        self._location = location
        self._animals: List[Animal] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> str:
        return self._location

    @property
    def animals(self) -> List[Animal]:
        return list(self._animals)

    def get_animal_count(self) -> int:
        return len(self._animals)

    def add_animal(self, animal: Animal) -> None:
        self._animals.append(animal)

    def remove_animal(self, animal: Animal) -> bool:
        if animal in self._animals:
            self._animals.remove(animal)
            return True
        return False

    def find_animal_by_name(self, name: str) -> Optional[Animal]:
        for animal in self._animals:
            if animal.name == name:
                return animal
        return None

    def get_species_count(self, species: str) -> int:
        count = 0
        for animal in self._animals:
            if animal.species == species:
                count += 1
        return count

    def get_all_sounds(self) -> List[str]:
        sounds = []
        for animal in self._animals:
            sounds.append(animal.make_sound())
        return sounds