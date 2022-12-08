"""
david A. V. gr 405
exercise 1
"""
from dataclasses import dataclass
from math import pi
import random

print("exercise 1")


class StringFoo:
    def __init__(self, message):
        self.message = message

    def print_string(self):
        print(f"{self.message.upper()}")


david = StringFoo('roger roger')

david.print_string()

# exercise 2: le rectangle

print("\n\n\nexercise 2")


class Rectangle:
    def __init__(self, longeur, hauteur):
        self.aire = None
        self.longeur = longeur
        self.hauteur = hauteur

    def calcul_aire(self):
        self.aire = self.longeur * self.hauteur

        return self.aire

    def afficher_info(self):
        print(f"Sa longeur est {self.longeur}, sa hauteur est {self.hauteur}\n"
              f"{self.longeur} * {self.hauteur} = {self.aire} \nSon aire est {self.aire}")


livre = Rectangle(15, 9.5)
livre.calcul_aire()
livre.afficher_info()

# exercise 3: le cercle


print("\n\n\nexercise 3")


class Cercle:

    def __init__(self, rayon):
        self.rayon = rayon
        self.circonference_cercle = None
        self.aire_cercle = None

    def calc_autour(self):
        self.circonference_cercle = 2 * pi * int(self.rayon)
        print(f"la circonférence est {self.circonference_cercle}")

    def calc_air(self):
        self.aire_cercle = self.rayon ** 2 * pi

        print(f"l'aire du cercle est {self.aire_cercle}")


assiette = Cercle(7)

print(f"le rayon est {assiette.rayon}")
assiette.calc_air()

assiette.calc_autour()

# exercise 4

print("\n\n\nexercise 4")


class Hero:

    def __init__(self, hp, attack_power, defence, nom, est_vivant):
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


bernard = Hero(random.randint(1, 10) + random.randint(1, 10),
               random.randint(1, 6), random.randint(1, 6), 'Bernard', True)

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

