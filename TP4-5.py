# exercises 4 et 5
from dataclasses import dataclass
import random


class Hero:

    def __init__(self, nom):
        self.est_vivant = True
        self.hp = random.randint(1, 10) + random.randint(1, 10)
        self.attack_power = random.randint(1, 6)
        self.defence = random.randint(1, 6)
        self.nom = nom

    def attaquer(self):
        degat = self.attack_power + random.randint(1, 6)

        print(f"{self.nom} attaque pour {degat} dégats!")

    def endommage(self):
        dommage = random.randint(1, 6)

        if dommage - self.defence < 0:
            print(f"{self.nom} recoit 0 dégats")
        else:
            self.hp -= dommage - self.defence
            print(f"{self.nom} recoit {dommage - self.defence} dégats")

    def vivant_check(self):
        if self.hp <= 0:
            print(f"{self.nom} est pas vivant")
            self.est_vivant = False
        else:
            print(f"{self.nom} est vivant")
            self.est_vivant = True


bernard = Hero('Bernard')

print(
    f"il a {bernard.hp} hp.\nson nom est {bernard.nom}\n"
    f"il a {bernard.defence} défence\nsa force est {bernard.attack_power}")

bernard.attaquer()
bernard.endommage()
bernard.vivant_check()

print(f"il a {bernard.hp} hp.")

# exercise 5
print("\n\n\nexercise 5!!!!!")


@dataclass
class AbilityScore:
    str = random.randint(1, 20)
    dex = random.randint(1, 20)
    con = random.randint(1, 20)
    int = random.randint(1, 20)
    sag = random.randint(1, 20)
    cha = random.randint(1, 20)
