class Zoo:
    _animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []
    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo._animals += 1
    def get_info(self, species):
        if species == "mammal":
            return f"{self.mammals} in {self.name}: {" ".join(self.mammals)}\n"
        elif species == "fishes":
            return f"{self.fishes} in {self.name}: {" ".join(self.mammals)}\n"
        elif species == "bird":
            return f"{self.birds} in {self.name}: {" ".join(self.mammals)}\n"
        return f"Total animals: {Zoo._animals}"
zoo_name = input()
zoo = Zoo(zoo_name)
n_lines = int(input())
for animal in range(n_lines):
    animal_info = input().split(" ")
    species_info = animal_info[0]
    name_info = animal_info[1]
    zoo.add_animal(species_info, name_info)
info = input()
print(zoo.get_info(info))