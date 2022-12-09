# EXERCISE 6
import random

print("EXERCISE 6 (final)")


class HeroExerciseSix:
    nom: str
    str = random.randint(1, 20)
    dex = random.randint(1, 20)
    con = random.randint(1, 20)
    int = random.randint(1, 20)
    sag = random.randint(1, 20)
    cha = random.randint(1, 20)
    est_vivant = True
    hp = random.randint(1, 10) + random.randint(1, 10)
    attack_power = random.randint(1, 6)
    defence = random.randint(1, 6)

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
