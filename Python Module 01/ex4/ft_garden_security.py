class SecurePlant:
    """class that defines a plant"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """initialize a plant with name, heigth, age"""
        self._name = name
        self._height = height
        self._age = age

    @property
    def name(self) -> str:
        """return the plant's name"""
        return self._name

    @property
    def height(self) -> int:
        """return the height of the plant"""
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        """set the plant's height with security validation"""
        if value < 0:
            print(f"Invalid operation attempted: height {value} [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {self._height} [OK]")

    @property
    def age(self) -> int:
        """return the current age"""
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        """set the plant's age with security validation"""
        if value < 0:
            print(f"Invalid operation attempted: age {value} [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {self._age} [OK]")

    def __str__(self) -> str:
        """representation of a plant string"""
        return f"{self._name} ({self._height}cm, {self._age} days)"


if __name__ == "__main__":
    plant = SecurePlant("Rose", 20, 30)
    print("=== Garden Security System ===")
    print(f"Plant Created: {plant.name}")
    plant.height = 25
    plant.age = 30
    print()
    plant.height = -20
    print()
    print(f"Current plant: {plant}")
