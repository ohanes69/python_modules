class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self, size_growth: int) -> int:
        self.height += size_growth
        print(f"{self.name} grew {size_growth}cm")
        return size_growth


class FloweringPlant(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            color: str,
            is_blooming: bool) -> None:
        super().__init__(name, height)
        self.color = color
        self.is_blooming = is_blooming


class PrizeFlower(FloweringPlant):
    def __init__(
            self,
            name: str,
            height: int,
            color: str,
            is_blooming: bool,
            points: int) -> None:
        super().__init__(name, height, color, is_blooming)
        self.points = points


class Garden:
    def __init__(
            self,
            gardener_name: str,
            list_plants: list,
            plants_added: int,
            total_growth: int) -> None:
        self.gardener_name = gardener_name
        self.list_plants = list_plants
        self.plants_added = plants_added
        self.total_growth = total_growth

    def add_plant(self, plant: Plant):
        self.list_plants.append(plant)
        self.plants_added += 1
        print(f"Added {plant.name} to {self.gardener_name}'s garden")

    def growth_all(self):
        print(f"{self.gardener_name} is helping all plants grow...")
        for p in self.list_plants:
            self.total_growth += p.grow(1)

    def get_infos(self):
        regular = 0
        flowering = 0
        prize_flowers = 0
        print(
            f"=== {self.gardener_name}'s Garden Report ===\n"
            "Plants in garden:"
        )
        for p in self.list_plants:
            if isinstance(p, PrizeFlower):
                status = "blooming" if p.is_blooming else "not blooming"
                print(f"- {p.name}: {p.height}cm, {p.color} flowers ({status}), Prize points: {p.points}")
                prize_flowers += 1
            elif isinstance(p, FloweringPlant):
                status = "blooming" if p.is_blooming else "not blooming"
                print(f"- {p.name}: {p.height}cm, {p.color} flowers ({status})")
                flowering += 1
            else:
                print(f"- {p.name}: {p.height}cm")
                regular += 1
        print(f"Plants added: {self.plants_added}, Total growth: {self.total_growth}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering, {prize_flowers} prize flowers")


# class GardenManager:
#     def __init__(self) -> None:

#         @classmethod
#         def create_garden_network(cls):

#     class GardenStats:


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    rose = Plant("Rose", 10)
