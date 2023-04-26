class Character:
    def __init__(self, name, health, attack, defense):
        # self.name, self.health, self.attack, and self.defense are our class attributes
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    # get_health() is a class method
    def get_health(self):
        print("{} has {}pp remaining.".format(self.name, self.health))

    # attack_enemy() is a class method
    def attack_enemy(self):
        return self.attack


def main():
    # Creating two Character objects.
    protagonist = Character("Link", 100, 50, 50)
    final_boss = Character("Ganon", 200, 50, 50)

    # Calling two different Character methods.
    final_boss.health -= protagonist.attack_enemy()
    final_boss.get_health()


if __name__ == '__main__':
    main()
