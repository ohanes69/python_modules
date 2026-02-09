class Plant:
    def __init__(self, name: str, height: int) -> None:

        self.name: str = name
        self.height: int = height

    def grow(self, size_growth: int) -> int:

        self.height += size_growth

        print(f"{self.name} grew {size_growth}cm")
        return size_growth

    """Plant -> it's a class to create the Plant with
    differents attributes (name and height)"""

    """grow() -> is used to update the growth of the plant.
    We pass the size of growth as a parameter."""


class FloweringPlant(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            color: str,
            is_blooming: bool) -> None:

        super().__init__(name, height)
        self.color: str = color
        self.is_blooming: bool = is_blooming

    """FloweringPlant(Plant) -> take as parameter the class Plant
    to use its attributes, we added color and is_blooming"""


class PrizeFlower(FloweringPlant):
    def __init__(
            self,
            name: str,
            height: int,
            color: str,
            is_blooming: bool,
            points: int) -> None:

        super().__init__(name, height, color, is_blooming)
        self.points: int = points

    """PrizeFlower(FloweringPlant) -> take as parameter the class
    FloweringPlant, we added points"""


class Garden:
    def __init__(
            self,
            gardener_name: str) -> None:

        self.gardener_name: str = gardener_name
        self.list_plants: list[Plant] = []
        self.plants_added: int = 0
        self.total_growth: int = 0

    def add_plant(self, plant: Plant) -> None:

        self.list_plants.append(plant)
        self.plants_added += 1

        print(f"Added {plant.name} to {self.gardener_name}'s garden")

    """def add_plant(self, plant: Plant) -> takes a Plant object as a parameter
      and adds it to the garden's plant list. It also increments
      the plants_added counter"""

    def growth_all(self) -> None:

        print(f"\n{self.gardener_name} is helping all plants grow...")

        for p in self.list_plants:
            self.total_growth += p.grow(1)

    """def growth_all(self) -> grow all plants of 1cm with grow()
    and add centimeter to total_growth"""

    def get_infos(self) -> None:

        regular: int = 0
        flowering: int = 0
        prize_flowers: int = 0

        print(
            f"\n=== {self.gardener_name}'s Garden Report ===\n"
            "Plants in garden:"
        )

        for p in self.list_plants:
            if isinstance(p, PrizeFlower):
                status = "blooming" if p.is_blooming else "not blooming"
                print(
                    f"- {p.name}: {p.height}cm, {p.color} flowers ({status}),"
                    f" Prize points: {p.points}"
                )
                prize_flowers += 1

            elif isinstance(p, FloweringPlant):
                status = "blooming" if p.is_blooming else "not blooming"
                print(
                    f"- {p.name}: {p.height}cm, {p.color} flowers ({status})"
                )
                flowering += 1

            else:
                print(f"- {p.name}: {p.height}cm")
                regular += 1

        print(
            f"\nPlants added: {self.plants_added},"
            f" Total growth: {self.total_growth}cm"
        )

        print(
            f"Plant types: {regular} regular, {flowering} flowering,"
            f" {prize_flowers} prize flowers\n"
        )

        """isinstance() -> checks if plant is PrizeFlower, FloweringPlant,
        or basic Plant"""


class GardenManager:
    def __init__(self) -> None:
        self.gardens: dict[str, Garden] = {}

    def add_garden(self, garden: Garden) -> None:
        self.gardens[garden.gardener_name] = garden

    @staticmethod
    def display_intro() -> None:
        print("=== Garden Management System Demo ===\n")

    @classmethod
    def create_garden_network(cls) -> "GardenManager":

        manager = cls()

        """manager = cls() -> creates a new GardenManager object"""

        alice_garden = Garden("Alice")
        oak = Plant("Oak Tree", 100)
        rose = FloweringPlant("Rose", 25, "red", True)
        sunflower = PrizeFlower("Sunflower", 50, "yellow", True, 10)

        alice_garden.add_plant(oak)
        alice_garden.add_plant(rose)
        alice_garden.add_plant(sunflower)
        alice_garden.growth_all()

        manager.add_garden(alice_garden)

        return manager

    def get_garden_scores(self) -> dict:

        scores: dict = {}

        for gardener_name, garden in self.gardens.items():
            score = 0
            for plant in garden.list_plants:
                if isinstance(plant, PrizeFlower):
                    score += plant.points
            scores[gardener_name] = score

        return scores

    """get_garden_scores(self) -> Calculates and returns
    the score of each garden"""

    def display_network_report(self) -> None:

        stats = self.GardenStats(self)
        is_valid: bool = stats.validate_plant_heights()

        print(f"Height validation test: {is_valid}")

        scores: dict = self.get_garden_scores()

        for name, score in scores.items():
            print(f"Garden scores - {name}: {score}")

        print(f"Total gardens managed: {len(self.gardens)}")

        """display_network_report(self) -> Displays a complete report
        of the garden network"""

    class GardenStats:
        def __init__(self, manager: "GardenManager") -> None:

            self.manager: "GardenManager" = manager

        def validate_plant_heights(self) -> bool:

            for garden in self.manager.gardens.values():
                for plant in garden.list_plants:
                    if plant.height <= 0:
                        return False
            return True

        """validate_plant_heights(self) -> Ensures all plants
        have positive heights"""


if __name__ == "__main__":
    GardenManager.display_intro()

    manager = GardenManager.create_garden_network()

    for garden in manager.gardens.values():
        garden.get_infos()

    manager.display_network_report()
