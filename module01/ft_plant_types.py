class Plant:
    def __init__(
            self,
            name: str,
            height: int,
            age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info_plants(self):
        return (
            f"{self.name} ({self.__class__.__name__}): "
            f"{self.height}cm, "
            f"{self.age} days, "
        )
    """Plant is the Parent of the class below (Flower, Tree, Vegetable)"""


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            color: str) -> None:
        super().__init__(name, height, age)
        """super().__init__() -> is to don' repeat this self.name = name..."""
        self.color = color

    def bloom(self):
        return (f"{self.name} is blooming beautifully!")

    def get_info(self):
        return (
            f"{super().get_info_plants()}"
            """super().get_info_plants() -> is to gets the informations
            returned by the Parent class"""
            f"{self.color} color\n"
            f"{self.bloom()}\n"
        )
    """Flower(Plant) -> (Plant) allows you to take after the information of the
    Parent class"""


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        sheld = 3.14 * 5 * 5
        return (f"Oak provides {int(sheld)} square meters of shade")

    def get_info(self):
        return (
            f"{super().get_info_plants()}"
            f"{self.trunk_diameter}cm diameter\n"
            f"{self.produce_shade()}\n"
        )


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        return (
            f"{super().get_info_plants()}"
            f"{self.harvest_season} harvest\n"
            f"Tomato is rich in {self.nutritional_value}"
        )


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    flower = Flower("Rose", 25, 30, "red")
    print(flower.get_info())
    tree = Tree("Oak", 500, 1825, 50)
    print(tree.get_info())
    vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(vegetable.get_info())
