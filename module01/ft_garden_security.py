class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:

        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0

        print(f"Plant created: {self.name}")

        self.set_height(height)
        self.set_age(age)

    """double underscore -> it's a security, with need to be in the
    class to modify height and age"""

    def get_infos(self) -> None:

        print(
            f"Current plant: {self.name} "
            f"({self.get_height()}cm, "
            f"{self.get_age()} days)"
        )

    def get_height(self) -> int:
        return (self.__height)

    def get_age(self) -> int:
        return (self.__age)

    def set_height(self, set: int) -> None:

        if set < 0:
            print(
                f"\nInvalid operation attempted: height {set}cm [REJECTED]\n"
                "Security: Negative height rejected\n"
            )

        else:
            print(f"Height updated: {set}cm [OK]")
            self.__height = set

    def set_age(self, set: int) -> None:

        if set < 0:
            print(
                f"\nInvalid operation attempted: age {set} "
                "days old [REJECTED]\n"
                "Security: Negative age rejected\n"
            )

        else:
            print(f"Age updated: {set} days [OK]")
            self.__age = set

    """The set_* methods allow us to set the value if it is greater than 0,
    otherwise a message is print"""


if __name__ == "__main__":

    print("=== Garden Security System ===")

    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-5)
    rose.get_infos()
