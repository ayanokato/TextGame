#!/usr/bin/env python3

import os
import enquiries as e
import random
from actors import *
from items import *

# BASIC FUNCTIONS
def clear():
    os.system("clear")

def ofile(file):
    f = open(file, "r")
    print(f.read())

def battle(player):
    enemy = random.choice(enemies)
    print(f"{enemy.name} is attacking you")
    while enemy.health > 0 and player.health > 0:
        attack(player, enemy)
        e_attack(player, enemy)
        if enemy.health <= 0:
            print("Enemy died")
        if player.health <= 0:
            print("You died")

def attack(player, enemy):
    options = ["Attack"]
    choice = enquiries.choose("", options)

    if choice == "Attack":
        enemy.health -= player.damage
        print(f"You chose to attack {enemy.name}\n{enemy.name}: {enemy.health} / {enemy.maxhealth}")

def e_attack(player, enemy):
    player.health -= enemy.damage
    print(f"Enemy attacked you for {enemy.damage} DMG: \nYou: {player.health} / {player.maxhealth}")

# MAIN
def main():
    clear()
    ofile("title.txt")

    options = ["New Game", "Exit"]
    choice = e.choose("", options)

    if choice == "Exit":
        exit()
    elif choice == "New Game":
        game_start()

def game_start():
    player = Player()
    clear()
    print("This is the start of the game")
    battle(player)

if __name__ == "__main__":
    enemies = [
        Enemy("Gobin", 10, 10, 3),
        Enemy("Karen", 15, 15, 5),
        Enemy("Kevin", 20, 20, 10)
    ]

    items = [
        Item("Glass", False, True, 0, 5),
        Item("Dagger", False, True, 0, 3),
        Item("Medkit", True, False, 5, 0)
    ]
    main()
