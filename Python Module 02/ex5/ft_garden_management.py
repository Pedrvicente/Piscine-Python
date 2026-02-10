class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plant_list = []

    def add_plant(self, plant_name: str) -> None:
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        self.plant_list.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        try:
            print("Opening watering system")
            for plant in self.plant_list:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self,
                           plant_name: str,
                           water: int,
                           sunlight: int) -> str:
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        if water < 1:
            raise WaterError(f"Water level {water} is too low (min 1)")
        if water > 10:
            raise WaterError(f"Water level {water} is too high (max 10)")
        if sunlight < 2:
            raise ValueError(f"Sunlight level {sunlight} is too low (min 2)")
        if sunlight > 12:
            raise ValueError(f"Sunlight level {sunlight} is too high (max 12)")
        return f"{plant_name}: healthy (water: {water}, sun: {sunlight})"


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    garden = GardenManager()
    try:
        garden.add_plant("tomato")
    except PlantError as e:
        print(f"Error adding plant: {e}")
    try:
        garden.add_plant("lettuce")
    except PlantError as e:
        print(f"Error adding plant: {e}")
    try:
        garden.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}")
    print()
    print("Watering plants...")
    garden.water_plants()
    print()
    print("Checking plant health...")
    try:
        result = garden.check_plant_health("tomato", 5, 8)
        print(result)
    except (PlantError, ValueError, WaterError) as e:
        print(e)
    try:
        result = garden.check_plant_health("lettuce", 15, 8)
        print(result)
    except (PlantError, WaterError, ValueError) as e:
        print(f"Error checking lettuce: {e}")
    print()
    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
