class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:

        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_infos(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":

    print("=== Plant Factory Output ===")

    plants: list = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    """plants -> i created a list and inside the list there are 5 tuples,
    lists and tuples works with index, just tuples informations can't be
    change after"""

    garden: list[Plant] = []

    for data in plants:
        new_plant: Plant = Plant(*data)
        garden.append(new_plant)

    """Plant(*data) -> we add * to add all data ;
    append -> add new_plants to garden list"""

    count: int = 0

    for plant in garden:
        plant.get_infos()
        count += 1

    print(f"\nTotal plants created: {count}")
