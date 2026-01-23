class Plant:
    """class that defines a plant"""
    def __init__(self, name: str, height: int) -> None:
        """initialize a plant with name, heigth"""
        self.name = name
        self.height = height

    def __str__(self) -> str:
        """representation of a plant string"""
        return f"- {self.name}: {self.height}cm"

    def grow(self, amount: int = 1) -> None:
        """grow the plant by amount number"""
        self.height += amount


class FloweringPlant(Plant):
    """Creating a subclass that receives the class
    Plant and add specific atributtes"""
    def __init__(self, name: str, height: int, color: str) -> None:
        """add color feature"""
        super().__init__(name, height)
        self.color = color

    def __str__(self) -> str:
        """representation of a plant string"""
        return (f"- {self.name}: {self.height}cm,"
                f" {self.color} flowers (blooming)")

    def show_info(self) -> None:
        """print the plants string and bloom message"""
        print(self)


class PrizeFlower(FloweringPlant):
    """class that receives the subclass FloweringPlant
    and adds specific atributtes"""
    def __init__(self, name: str,
                 height: int,
                 color: str,
                 prize_points: int) -> None:
        """initialize a prize flower with prize points"""
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        """string representation inclunding prize points"""
        return (f"- {self.name}: {self.height}cm, {self.color} flowers"
                f" (blooming), Prize points: {self.prize_points}")


class GardenManager:
    """Manages a collection of plants and tracks garden statistics"""
    counter = 0
    all_gardens = []

    def __init__(self, owner: str) -> None:
        """initialize the manager"""
        self.owner = owner
        self.plants = []
        self.total_growth = 0
        GardenManager.counter += 1
        GardenManager.all_gardens.append(self)

    def add_plant(self, plant: Plant) -> None:
        """add a plant to a garden list"""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        """grow all plants of the garden list"""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1
            print(f"{plant.name} grew 1cm")

    def count_types(self) -> None:
        """count the type of plants that are present in the garden list"""
        regular = 0
        flowering = 0
        prizes = 0
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                prizes += 1
            elif isinstance(plant, FloweringPlant):
                flowering += 1
            elif isinstance(plant, Plant):
                regular += 1
        return (f"{regular} regular, {flowering} flowering, {prizes}"
                f" prize flowers")

    def get_score(self) -> int:
        """calculate the total score based on height and points"""
        score = 0
        for plant in self.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score

    def get_report(self) -> None:
        """get full report of the garden status"""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plants in self.plants:
            print(plants)
        print()
        print(f"Plants added: {len(self.plants)}, Total growth:"
              f" {self.total_growth}cm")
        print(f"Plant types: {self.count_types()}")
        print()

    @staticmethod
    def validate_height() -> bool:
        """validate the height of the plants in the garden"""
        for garden in GardenManager.all_gardens:
            for plant in garden.plants:
                if plant.height <= 0:
                    return False
        return True

    @classmethod
    def get_stats(cls) -> str:
        """return a string with scores and total gardens"""
        scores = []
        for g in cls.all_gardens:
            scores.append(f"{g.owner}: {g.get_score()}")
        score_line = ", ".join(scores)
        return (f"Height validation test: {cls.validate_height()}\n"
                f"Garden scores - {score_line}\n"
                f"Total gardens managed: {cls.counter}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    oak = Plant("Oak", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(rose)
    alice.add_plant(oak)
    alice.add_plant(sunflower)

    old_pine = Plant("Old Pine", 80)
    print()
    alice.grow_all()
    print()
    alice.get_report()

    print(GardenManager.get_stats())
