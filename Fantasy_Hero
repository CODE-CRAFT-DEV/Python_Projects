class FantasyHero:
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level

    def __str__(self):
        return f"{self.name} with power level {self.power_level}"

    def is_stronger_than(self, other):
        return self.power_level > other.power_level

# Create two heroes
hero1 = FantasyHero("Hero1", float('inf'))
hero2 = FantasyHero("Hero2", float('inf') + 1)

# Display their power levels
print(hero1)
print(hero2)

# Compare their strength
if hero1.is_stronger_than(hero2):
    print(f"{hero1.name} is stronger than {hero2.name}")
elif hero2.is_stronger_than(hero1):
    print(f"{hero2.name} is stronger than {hero1.name}")
else:
    print(f"{hero1.name} and {hero2.name} have the same power level")
