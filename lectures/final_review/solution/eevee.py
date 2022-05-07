VALUE_IDX = 1
INFO_PER_STONE = {
    "water_stone": {
        # Water stone information
        "eeveelution": "Vaporeon",
        "type": "water"
    },
    "thunder_stone": {
        # Thunder stone information
        "eeveelution": "Jolteon",
        "type": "electric"
    },
    "fire_stone": {
        # Fire stone information
        "eeveelution": "Flareon",
        "type": "fire"
    }
}


class Eevee:
    def __init__(self, nickname, description_filename):
        # These three attributes are the same for all Eevee objects, regardless of the existence of the file
        self.nickname = nickname
        self.eeveelution_status = None
        self.type = "normal"

        try:
            file = open(description_filename, 'r')
        except FileNotFoundError:
            # If the file doesn't exist, we set the specified "default" values for the remaining parameters and return
            self.nature = None
            self.level = 5
            return

        # If they file does exist...
        file.readline()  # get rid of the header first

        """
        And extract the information in the exact same way for the remaining two lines:
           1. Read the line,
           2. Strip it to get rid of the '\n',
           3. Split it by spaces to separate the stat's name from its value as separate elements in a list,
           4. Isolate the actual value from the list, which is in index 1.
        """
        self.nature = file.readline().strip().split()[VALUE_IDX]
        self.level = int(file.readline().strip().split()[VALUE_IDX])  # in the case of level, we have to cast to int

        file.close()

    def can_evolve(self, stone_name):
        """
        As per the prompt, we DON'T evolve if:
            - eeveelution_status is None, or
            - stone_name is not either "water_stone", "electric_stone", or "fire_stone".
        """
        return (not self.eeveelution_status) and (stone_name in INFO_PER_STONE)

    def evolve(self, stone_name):
        # Check if Eevee can evolve first
        if not self.can_evolve(stone_name):
            return

        """
        To evolve, we simply update eeveelution_status and type to their appropriate values:
           - If stone_name is "water_stone", eeveelution_status will become "Vaporeon" and type will become "water".
           - If stone_name is "electric_stone", eeveelution_status will become "Jolteon" and type will become 
             "electric".
           - If stone_name is "fire_stone", eeveelution_status will become "Flareon" and type will become "fire".
        """
        self.eeveelution_status = INFO_PER_STONE[stone_name]["eeveelution"]
        self.type = INFO_PER_STONE[stone_name]["type"]

    def get_stats(self):
        """
        List comprehension logic:
           1. Give me the stat
           2. For every stat
           3. In the list of every single attribute
           4. If that stat is not None
        """
        return [stat for stat in [self.nickname, self.eeveelution_status, self.nature, self.level, self.type]
                if stat is not None]


def main():
    # If the file exists...
    camille = Eevee("Camille", "description.txt")
    print(camille.get_stats())  # Pre-evolution

    camille.evolve("thunder_stone")
    print(camille.get_stats())  # Post-evolution

    # If the file doesn't exist...
    fryderyk = Eevee("Fryderyk", "not_description.txt")
    print(fryderyk.get_stats())  # Pre-evolution

    fryderyk.evolve("fire_stone")
    print(fryderyk.get_stats())  # Post-evolution


main()
