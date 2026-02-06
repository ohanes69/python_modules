class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    """-> class Plant : -> allows you to store the name, height and age
        information of each plant"""

    def grow_plant(self, amount) -> int:
        if (self.name == "Rose"):
            self.height += 1
            amount += 1
        elif (self.name == "Sunflower"):
            self.height += 3
            amount += 3
        else:
            self.height += 2
            amount += 2
        return (amount)

    """-> grow_plant function : -> this function is useful for calculate
        the growth of the plant, the iteration depend of the type of
        the plant"""

    def age_plant(self):
        self.age += 1

    """-> age_plant function : -> this function is useful for calculate
        the age of the plant"""

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    """-> get_info function : -> this function is useful for print
        the informations of the plant"""

    def choose_flower(self, name) -> int:
        amount = 0
        if (name == "Rose"):
            for i in range(6):
                rose.age_plant()
                amount += rose.grow_plant(0)
            rose.get_info()
        elif (name == "Sunflower"):
            for i in range(6):
                amount += sunflower.grow_plant(0)
                sunflower.age_plant()
            sunflower.get_info()
        elif (name == "Cactus"):
            for i in range(6):
                amount += cactus.grow_plant(0)
                cactus.age_plant()
            cactus.get_info()
        return (amount)

    """-> choose_flower function : -> this function is useful
        when someone choose the type of the plant in the main ;
        it will call the other functions and return the amount
        for the last print (Growth this week)"""


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Day 1 ===")
    rose.get_info()
    amount = 0
    print("=== Day 7 ===")
    amount = rose.choose_flower("Rose")
    print(f"Growth this week: +{amount}cm")
