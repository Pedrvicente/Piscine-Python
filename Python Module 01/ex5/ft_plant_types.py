class Plant:
    """class that defines a plant"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """initialize a plant with name, heigth, age"""
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        """representation of a plant string"""
        return f"{self.name}: {self.height}cm, {self.age} days old"


class Flower(Plant):
    """class that receives a basic plant and add specific atributtes"""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return f"{self.name} is blooming beautifully!"

    def __str__(self) -> str:
        """representation of a plant string"""
        return (f"{self.name} (Flower): {self.height}cm, {self.age} days,"
                f" {self.color} color")

    def show_info(self) -> None:
        print(self)
        print(self.bloom())


class Tree(Plant):
    """class that receives a basic plant and add specific atributtes"""
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        return (f"{self.name} provides {self.trunk_diameter * 2} square meters"
                f" of shade")

    def __str__(self) -> str:
        """representation of a plant string"""
        return (f"{self.name} (Tree): {self.height}cm, {self.age} days,"
                f" {self.trunk_diameter} diameter")

    def show_info(self) -> None:
        print(self)
        print(self.produce_shade())


class Vegetable(Plant):
    """class that receives a basic plant and add specific atributtes"""
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def is_rich(self) -> str:
        return f"{self.name} is rich in vitamin {self.nutritional_value}"

    def __str__(self) -> str:
        """representation of a plant string"""
        return (f"{self.name} (Vegetable): {self.height}cm, {self.age} days,"
                f" {self.harvest_season} harvest")

    def show_info(self) -> None:
        print(self)
        print(self.is_rich())


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    rose = Flower("Rose", 25, 30, "red")
    rose.show_info()
    print()
    oak = Tree("Oak", 500, 1825, 50)
    oak.show_info()
    print()
    tomato = Vegetable("Tomato", 80, 90, "summer", "C")
    tomato.show_info()
