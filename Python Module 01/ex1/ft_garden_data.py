class Plant:
    """
    class that defines a plant
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """initialize a plant with name, heigth, age"""
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        """representation of a plant string"""
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(plant_1)
    print(plant_2)
    print(plant_3)
