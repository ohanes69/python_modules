class Plant:
    def __init__(
            self,
            name: str,
            height: int,
            age: int) -> None:

        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info_plants(self) -> str:
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
        self.color: str = color

        """super().__init__() -> is to don't repeat this self.name = name..."""

    def bloom(self) -> str:
        return (f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        return (
            f"{super().get_info_plants()}"
            f"{self.color} color\n"
            f"{self.bloom()}\n"
        )

    """Flower(Plant) -> (Plant) allows you to take after the information of the
    Parent class"""

    """super().get_info_plants() -> is to gets the informations
            returned by the Parent class"""


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            trunk_diameter: int) -> None:

        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> str:

        sheld: float = 3.14 * 5 * 5
        return (f"Oak provides {int(sheld)} square meters of shade")

    def get_info(self) -> str:
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
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_info(self) -> str:
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
