class Hero:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def reveal_identity(self):
        return f"I am {self.name} from {self.origin}."


class Superhero(Hero):
    def __init__(self, name, origin, superpower, weakness):
        super().__init__(name, origin)
        self._superpower = superpower
        self._weakness = weakness

    def use_power(self):
        return f"⚡ {self.name} uses {self._superpower}!"

    def reveal_weakness(self):
        return f"☠️ {self.name}'s weakness is {self._weakness}."

    def full_profile(self):
        return f"{self.reveal_identity()} Superpower: {self._superpower}, Weakness: {self._weakness}"


hero = Superhero("Captain Thunder", "Neptune", "Electro-blast", "Salt water")

print(hero.full_profile())
print(hero.use_power())
print(hero.reveal_weakness())
