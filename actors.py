import enquiries

class Enemy:
    def __init__(self, name, health, maxhealth, damage):
        self.name = name
        self.health = health
        self.maxhealth = maxhealth
        self.damage = damage

class Player:
    def __init__(self, name = "Player", health = 15, maxhealth = 15, damage = 4):
        self.name = name
        self.health = health
        self.maxhealth = maxhealth
        self.damage = damage
