import random
from classBase import Base

class Deva(Base):
    def __init__(self):
        super().__init__()
        self.immortality = random.int(11, 15)
        
    def rebirth(self):
        self.resistance = int(self.resistance * self.immortality // 10)
        self.defense = int(self.defeat * self.immortality // 10)

    def defense_ability(self, resistance):
        ability_cost = 40
        available = self.use_ability(resistance, ability_cost)
        if available:
            return int(self.defense * 4 * self.immortality // 10)
        else:
            return 0
 
class Asuras(Base):
    def __init__(self):
        super().__init__()
        self.superior_resistance = random.int(11, 15)
        
    def rebirth(self):
        self.strength = int(self.strength * self.superior_resistance // 10)
        self.defense = int(self.defeat * self.superior_resistance // 10)

    def attack_ability(self, resistance):
        ability_cost = 40
        available = self.use_ability(resistance, ability_cost)
        if available:
            return int(self.strength * 4 * self.superior_resistance // 10)
        else:
            return 0

    def defense_ability(self, resistance):
        ability_cost = 40
        available = self.use_ability(resistance, ability_cost)
        if available:
            return int(self.defense * 4 * self.superior_resistance // 10)
        else:
            return 0

class Manushyas(Base):
    def __init__(self):
        super().__init__()
        self.adaptability = random.int(11, 15)
        
    def rebirth(self):
        self.agility = int(self.agility * self.adaptability // 10)
        self.intelligence = int(self.intelligence * self.adaptability // 10)

    def mana_ability(self, resistance):
        ability_cost = 40
        available = self.use_ability(resistance, ability_cost)
        if available:
            return int(self.intelligence * 4 * self.adaptability // 10)
        else:
            return 0

    def evasion_ability(self, resistance):
        ability_cost = 40
        available = self.use_ability(resistance, ability_cost)
        if available:
            return int(self.agility * 4 * self.adaptability // 10)
        else:
            return 0
    
class Tiryak(Base):
    def __init__(self):
        super().__init__()
        self.animal_strength = random.int(11, 15)
        
    def rebirth(self):
        self.strength = int(self.strength * self.animal_strength // 10)
        self.agility = int(self.agility * self.animal_strength // 10)

    def attack_ability(self, resistance):
        ability_cost = 40
        available = self.use_ability(resistance, ability_cost)
        if available:
            return int(self.strength * 4 * self.animal_strength // 10)
        else:
            return 0

    def evasion_ability(self, resistance):
        ability_cost = 40
        available = self.use_ability(resistance, ability_cost)
        if available:
            return int(self.agility * 4 * self.animal_strength // 10)
        else:
            return 0
    
class Pretas(Base):
    def __init__(self):
        super().__init__()
        self.invisibility = random.int(11, 15)
        
    def rebirth(self):
        self.defense = int(self.defense * self.invisibility // 10)
        self.intelligence = int(self.intelligence * self.invisibility // 10)

    def mana_ability(self, resistance):
        ability_cost = 40
        available = self.use_ability(resistance, ability_cost)
        if available:
            return int(self.intelligence * 4 * self.invisibility // 10)
        else:
            return 0

    def defense_ability(self, resistance):
        ability_cost = 40
        available = self.use_ability(resistance, ability_cost)
        if available:
            return int(self.defense * 4 * self.invisibility // 10)
        else:
            return 0
 
class Narakas(Base):
    def __init__(self):
        super().__init__()
        self.infernal_power = random.int(11, 15)
        
    def rebirth(self):
        self.resistance = int(self.resistance * self.infernal_power // 10)
        self.strength = int(self.strength * self.infernal_power // 10)

    def attack_ability(self, resistance):
        ability_cost = 40
        available = self.use_ability(resistance, ability_cost)
        if available:
            return int(self.strength * 4 * self.infernal_power // 10)
        else:
            return 0
