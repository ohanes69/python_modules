class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

        """-> class Plant : -> allows you to store the name, height and age
        information of each plant"""

    def get_infos(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


def ft_garden_data():
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print(rose.get_infos())
    print(sunflower.get_infos())
    print(cactus.get_infos())


if __name__ == "__main__":
    ft_garden_data()
