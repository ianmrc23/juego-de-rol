import random
from abc import ABC, abstractclassmethod

class Base(ABC):
    def __init__(self):
        self.lives = 3
        self.level = 1
        self.freePoints = 10
        self.healthPoints = 1000
        self.strength = random.randint(20, 80)
        self.resistance = random.randint(20, 80)
        self.defense = random.randint(20, 80)
        self.intelligence = random.randint(20, 80)
        self.agility = random.randint(20, 80)
        self.coins = {"gold": 3, "silver": 500, "copper": 100}
        
    @staticmethod
    def convert_from_copper(coins):
        gold = coins // 10000
        silver = (coins // 100) % 100
        copper = coins % 100
        return gold, silver, copper
        
    def total_copper_coins(self):
        total = self.coins["gold"] * 100 * 100 + self.coins["silver"] * 100 + self.coins["copper"]
        return int(total)

    def average_statistics(self):
        statistics = [self.healthPoints, self.strength, self.resistance, self.defense, self.intelligence, self.agility]
        return int(sum(statistics) / len(statistics))

    def assign_points(self, statistic, amount):
        setattr(self, statistic, getattr(self, statistic) + amount)
        self.freePoints -= amount
        return f"Points assigned to {statistic} successfully."

    def view_statistics(self):
        statistics = ["lives", "level", "healthPoints", "strength", "resistance", "defense", "intelligence", "agility"]
        return "\n\n".join([f"{s.capitalize()}: {getattr(self, s)}" for s in statistics])

    def view_coins(self):
        coins_str = "\n\n".join([f"{currency.capitalize()}: {amount}" for currency, amount in self.coins.items()])
        return f"\n{coins_str}"
 
    def enemy_strength(self, enemy):
        difference = (enemy.average_statistics() - self.average_statistics())
        return "strong" if difference > 0 else "weak" if difference < 0 else "balanced"

    def victory_reward(self, enemy):
        self.level += 1
        self.freePoints += 10
        
        health_increase = 10 * self.level
        self.healthPoints += health_increase

        relationship = self.enemy_strength(enemy)
        coins_copper = 15000

        bonus = {"strong": 1.5, "balanced": 1.4, "weak": 1.3}.get(relationship)

        gold, silver, copper = self.convert_from_copper(coins_copper * bonus)
        self.coins["gold"] += gold
        self.coins["silver"] += silver
        self.coins["copper"] += copper

        return (f"You have won the battle!\n"
                f"You have leveled up! You are now at level {self.level}.\n"
                f"You have gained {10 * self.level} free points! You now have {self.freePoints} free points.\n"
                f"Your health Points have increased by {health_increase}. Your current total healthPoints is {self.healthPoints}.\n"
                "Coins obtained:\n"
                f"Gold: {gold}\n"
                f"Silver: {silver}\n"
                f"Copper: {copper}")

    def defeat_losses(self, enemy):
        self.lives -= 1
        self.level -= 1
        
        health_decrease = 10 * self.level
        self.healthPoints -= health_decrease
        
        relationship = self.enemy_strength(enemy)
        
        penalty = {"strong": 1.3, "balanced": 1.4, "weak": 1.5}.get(relationship)

        coins_to_lose = int(15000 * penalty)
        gold, silver, copper = self.convert_from_copper(coins_to_lose)

        for currency in self.coins:
            if currency == 'gold':
                self.coins[currency] = max(0, self.coins[currency] - gold)
            elif currency == 'silver':
                self.coins[currency] = max(0, self.coins[currency] - silver)
            elif currency == 'copper':
                self.coins[currency] = max(0, self.coins[currency] - copper)
        
        attribute_to_reduce = random.choice(["strength", "resistance", "defense", "intelligence", "agility"])
        setattr(self, attribute_to_reduce, max(0, getattr(self, attribute_to_reduce) - 10))
        
        return (f"You've been defeated!\n"
                f"You've lost a life. You now have {self.lives} lives left.\n"
                f"Your level has decreased! You are now at level {self.level}.\n"
                f"Your {attribute_to_reduce} has decreased by 10 points.\n"
                "You've also lost coins due to defeat:\n"
                f"Gold: {gold}\n"
                f"Silver: {silver}\n"
                f"Copper: {copper}")

    def training_increase(self):
        if self.coins['gold'] >= 1:
            self.coins['gold'] -= 1
            
            statistic = random.choice(['strength', 'defense', 'resistance', 'agility', 'intelligence', 'healthPoints'])
            
            increase = random.randint(1, 10)
            
            setattr(self, statistic, getattr(self, statistic) + increase)
            
            return f"You have invested one gold coin in your training and your {statistic} has increased by {increase}!"
        else:
            return "You don't have enough gold coins to train. Get more gold coins to improve your skills!"

    def instant_defeat(self, opponent_class):
        strong_enemies = {"Deva": "Asuras", "Asuras": "Manushyas", "Manushyas": "Tiryak", "Tiryak": "Pretas", "Pretas": "Deva", "Narakas": "Manushyas"}
        weak_enemies = {"Deva": "Narakas", "Asuras": "Deva", "Manushyas": "Pretas", "Tiryak": "Manushyas", "Pretas": "Asuras", "Narakas": "Deva"}
        
        if opponent_class.__class__.__name__ == strong_enemies.get(self.__class__.__name__):
            if opponent_class.average_statistics() - self.average_statistics() >= 100:
                return "defeat"
        elif opponent_class.__class__.__name__ == weak_enemies.get(self.__class__.__name__):
            if self.average_statistics() - opponent_class.average_statistics() >= 100:
                return "victory"
        
        return None

    def mana_attack(self):
        return int(self.intelligence * 5 // 2)
    
    def basic_attack(self):
        return int(self.strength * 5 // 2)

    def basic_defense(self):
        return int(self.defense * 3 // 2)

    def basic_evasion(self):
        return int(self.agility * 3 // 2)

    def avoid_combat(self, enemy_agility):
        return self.agility > enemy_agility

    def use_ability(self, resistance, ability_cost):
        if resistance >= ability_cost:
            resistance -= ability_cost
            return True
        else:
            return False

    def rebirth(self):
        pass
    
    def mana_ability(self):
        pass

    def attack_ability(self):
        pass

    def defense_ability(self):
        pass

    def evasion_ability(self):
        pass
