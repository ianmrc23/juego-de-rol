import random
import os
from classPaths import Deva, Asuras, Manushyas, Tiryak, Pretas, Narakas

def configuration():
    while True:
        try:
            final_level = int(input("\n* What level do you want to finish the game at? (between 2 and 100): "))
            if final_level < 2 or final_level > 100:
                print("\nThe level must be between 2 and 100. Please try again.")
            else:
                press_enter_to_continue()
                clear_terminal()
                return final_level
        except ValueError:
            print("\nPlease enter a valid integer.")

def generate_character():
    print("-" * 50)
    print("\nSelect your path:\n")
    print("-" * 50)
    print("\n1. Deva")
    print("\n2. Asuras")
    print("\n3. Manushyas")
    print("\n4. Tiryak")
    print("\n5. Pretas")
    print("\n6. Narakas")
    option = input("\n* Choose a number corresponding to the desired path: ")

    if option.isdigit():
        option = int(option)
        if 1 <= option <= 6:
            if option == 1:
                return Deva()
            elif option == 2:
                return Asuras()
            elif option == 3:
                return Manushyas()
            elif option == 4:
                return Tiryak()
            elif option == 5:
                return Pretas()
            elif option == 6:
                return Narakas()
        else:
            print("Invalid option. Please choose again.")
            return generate_character()
    else:
        print("Invalid input. Please enter a number.")
        return generate_character()

def generate_enemy(level):
    option = random.randint(1, 6)

    if option == 1:
        enemy = Deva()
    elif option == 2:
        enemy = Asuras()
    elif option == 3:
        enemy = Manushyas()
    elif option == 4:
        enemy = Tiryak()
    elif option == 5:
        enemy = Pretas()
    elif option == 6:
        enemy = Narakas()

    increase = 10 * level
    min_random = 20 + increase
    max_random = 80 + increase

    enemy.healthPoints = 1000 + increase
    enemy.strength = random.randint(min_random, max_random)
    enemy.resistance = random.randint(min_random, max_random)
    enemy.defense = random.randint(min_random, max_random)
    enemy.intelligence = random.randint(min_random, max_random)
    enemy.agility = random.randint(min_random, max_random)

    return enemy
    
def character_actions_menu(player, enemy):
    print("\nCharacter Actions Menu:")
    print("\n1. Analyze Enemy")
    print("\n2. Fight")
    print("\n3. Flee")
    print("\n4. Menu")
    print("\n5. Quit Game")
    
    choice = input("\n* Choose an action: ")

    if choice == "1":
        clear_terminal()
        analyze_enemy(player, enemy)
        press_enter_to_continue()
    elif choice == "2":
        """ clear_terminal() """
        fight(player, enemy)
    elif choice == "3":
        clear_terminal()
        flee(player, enemy)
        press_enter_to_continue()
    elif choice == "4":
        clear_terminal()
        character_menu(player, enemy)
    elif choice == "5":
        clear_terminal()
        quit_game()
    else:
        clear_terminal()
        print("Invalid choice. Please select again.")
        character_actions_menu(player, enemy)

def character_menu(player, enemy):
    print("-" * 50)
    print("\nCharacter Menu:\n")
    print("-" * 50)
    print("\n1. View Statistics")
    print("\n2. Assign Free Points")
    print("\n3. View Coins")
    print("\n4. Inventory")
    print("\n5. Shop")
    print("\n6. Return to Main Menu")

    choice = input("\n* Choose an option: ")

    if choice == "1":
        clear_terminal()
        menu_view_statistics(player)
        press_enter_to_continue()
        
    elif choice == "2":
        clear_terminal()
        assign_free_points(player)
        press_enter_to_continue()
    elif choice == "3":
        clear_terminal()
        menu_view_coins(player)
        press_enter_to_continue()
    elif choice == "4":
        clear_terminal()
        view_inventory(player)
        press_enter_to_continue()
    elif choice == "5":
        clear_terminal()
        visit_shop(player)
        press_enter_to_continue()
    elif choice == "6":
        clear_terminal()
        character_actions_menu(player, enemy)
    else:
        clear_terminal()
        print("Invalid choice. Please select again.")
        character_menu(player, enemy)
        
def analyze_enemy(player, enemy):
    enemy_avg_stats = enemy.average_statistics()
    
    enemy_strength = enemy.enemy_strength(player)
    
    print("-" * 50)
    print("\nEnemy Analysis:\n")
    print("-" * 50)
    print(f"\nEnemy Strength: {enemy_strength}")
    print(f"\nAverage Statistics of Enemy: {enemy_avg_stats}")    

def fight(player, enemy):
    instant_result = player.instant_defeat(enemy)
    if instant_result == "defeat":
        player.defeat_losses(enemy)
        return False
    elif instant_result == "victory":
        player.victory_reward(enemy)
        return True

    player_hp = player.healthPoints
    player_resistance = player.resistance
    
    enemy_hp = enemy.healthPoints
    enemy_resistance = enemy.resistance

    while player_hp > 0 and enemy_hp > 0:
        player_attack, player_attack_type, player_defense, player_defense_type = select_attack_defense(player, enemy, player_resistance)
        enemy_attack, enemy_attack_type, enemy_defense, enemy_defense_type = select_enemy_attack_defense(enemy, enemy_resistance)

        print(f"Enemy hp:   {enemy_hp}")
        enemy_damage = calculate_damage(player_attack, player_attack_type, enemy_defense, enemy_defense_type)
        print(f"Damage: {enemy_damage}")
        enemy_hp -= enemy_damage
        print(f"Enemy hp actualizado:   {enemy_hp}")

        print(enemy.view_statistics())
        if enemy_hp <= 0:
            player.victory_reward(enemy)
            return True

        print(f"Player hp:   {player_hp}")
        player_damage = calculate_damage(enemy_attack, enemy_attack_type, player_defense, player_defense_type)
        print(f"Damage recibido: {player_damage}")
        player_hp -= player_damage
        print(f"Player hp actualizado:   {player_hp}") 

        if player_hp <= 0:
            player.defeat_losses(enemy)
            return False

def flee(player, enemy):
    enemy_agility = enemy.agility
    if player.avoid_combat(enemy_agility):
        print("-" * 50)
        print("\nYou successfully flee from the enemy!\n")
        print("\nAn enemy has been successfully generated.\n")
        print("-" * 50)
        generate_enemy(player.level)
    else:
        print("-" * 50)
        print("\nYou couldn't flee from the enemy!\n")
        print("-" * 50)

def menu_view_statistics(self):
    print("-" * 50)
    print("\nView Statistics\n")
    print("-" * 50, "\n")
    return print(self.view_statistics())

def assign_free_points(self):
    print("-" * 50)
    print("\nAvailable statistics:\n")
    print("-" * 50)
    print("\n1. Health Points")
    print("\n2. Strength")
    print("\n3. Resistance")
    print("\n4. Defense")
    print("\n5. Intelligence")
    print("\n6. Agility")
    print("\n0. Exit")
    
    statistic_options = ["healthPoints", "strength", "resistance", "defense", "intelligence", "agility"]
    while True:
        statistic_choice = input("\n* Choose a statistic to assign points to (or enter 0 to exit): ")
        if statistic_choice.isdigit():
            statistic_choice = int(statistic_choice)
            if statistic_choice == 0:
                return  # Salir del método
            elif statistic_choice in range(1, 7):
                chosen_statistic = statistic_options[statistic_choice - 1]
                break
            else:
                print("Invalid choice. Please choose a number between 0 and 6.")
        else:
            print("Invalid choice. Please enter a number.")
    
    clear_terminal()
    print("-" * 50)
    print(f"\nFree points available: {self.freePoints}\n")
    print("-" * 50)
    
    while True:
        points_to_assign = input(f"\n* How many points do you want to assign to {chosen_statistic}? (Enter 0 to exit) ")
        if points_to_assign.isdigit():
            points_to_assign = int(points_to_assign)
            if points_to_assign == 0:
                return  # Salir del método
            elif 1 <= points_to_assign <= self.freePoints:
                break
            else:
                print(f"Invalid amount. Please enter an integer between 0 and {self.freePoints}.")
        else:
            print("Invalid amount. Please enter an integer.")

    self.assign_points(chosen_statistic, points_to_assign)

def menu_view_coins(self):
    print("-" * 50)
    print("\nCoins:\n")
    print("-" * 50)
    coins_str = self.view_coins()
    print(coins_str)
        
def view_inventory(self):
    print("-" * 120)
    print("\nComing soon in version 2.0: Inventory management with armor, weapons, and consumables using linked lists.\n")
    print("-" * 120)

def visit_shop(self):
    print("-" * 100)
    print("\nComing soon in version 2.0: Shop feature with armor, weapons, and consumables using linked lists.\n")
    print("-" * 100)
  
def quit_game():
    raise SystemExit  
    
def select_attack_defense(player, enemy, player_resistance):
    while True:
        print("Select attack method:")
        print("1. Physical attack")
        print("2. Mana attack")
        """ print("3. Special ability") """
        print("4. Return to Main Menu")
        
        attack_option = input("Choose an option: ")
        clear_terminal()
        if attack_option == "1":
            attack = player.basic_attack()
            attack_type = 1
            break
        elif attack_option == "2":
            attack = player.mana_attack()
            attack_type = 2
            break
            """ elif attack_option == "3":
                player_class = player.__class__
                special_ability = select_attack_ability(player_class)
                if special_ability:
                    if special_ability == "attack_ability":
                        attack_type = 1
                    elif special_ability == "mana_ability":
                        attack_type = 2
                    attack = getattr(player, special_ability)(player_resistance)
                else:
                    attack = None
                break """
        elif attack_option == "4":
            clear_terminal()
            character_actions_menu(player, enemy)
        else:
            clear_terminal()
            print("Invalid option. Please choose a valid option.")

    while True:
        print("Select defense method:")
        print("1. Defend")
        print("2. Evade")
        """ print("3. Special ability") """
        print("4. Return to Main Menu")

        defense_option = input("Choose an option: ")
        clear_terminal()
        if defense_option == "1":
            defense = player.basic_defense()
            defense_type = 1
            break
        elif defense_option == "2":
            defense = player.basic_evasion()
            defense_type = 2
            break
            """ elif defense_option == "3":
                player_class = player.__class__
                special_ability = select_defense_ability(player_class)  # Corregir aquí
                if special_ability:
                    if special_ability == "defense_ability":
                        defense_type = 1
                    elif special_ability == "evasion_ability":
                        defense_type = 2
                    defense = getattr(player, special_ability)(player_resistance)
                else:
                    defense = None
                break """
        elif defense_option == "4":
            clear_terminal()
            character_actions_menu(player, enemy)
        else:
            clear_terminal()
            print("Invalid option. Please choose a valid option.")

    return attack, attack_type, defense, defense_type

def select_attack_ability(player_class):
    attack_ability_options = {
        "Asuras": ["attack_ability"],
        "Manushyas": ["mana_ability"],
        "Tiryak": ["attack_ability"],
        "Pretas": ["mana_ability"],
        "Narakas": ["attack_ability"]
    }

    if player_class in attack_ability_options:
        print("Attack abilities submenu:")
        for i, ability in enumerate(attack_ability_options[player_class], start=1):
            print(f"{i}. {ability.replace('_', ' ').title()} ({player_class})")
        print(f"{len(attack_ability_options[player_class]) + 1}. Back")

        attack_ability_option = input("Choose an attack ability: ")
        if attack_ability_option.isdigit():
            attack_ability_option = int(attack_ability_option)
            if 1 <= attack_ability_option <= len(attack_ability_options[player_class]) + 1:
                if attack_ability_option == len(attack_ability_options[player_class]) + 1:
                    return None
                else:
                    return attack_ability_options[player_class][attack_ability_option - 1]
            else:
                print("Invalid option. Please choose a valid option.")
                return select_attack_ability(player_class)
        else:
            print("Invalid option. Please choose a valid option.")
            return select_attack_ability(player_class)
    else:
        print("No attack abilities available for this class.")
        return None

def select_defense_ability(player_class):
    defense_ability_options = {
        "Deva": ["defense_ability"],
        "Asuras": ["defense_ability"],
        "Manushyas": ["evasion_ability"],
        "Tiryak": ["evasion_ability"],
        "Pretas": ["defense_ability"]
    }

    if player_class in defense_ability_options:
        print("Defense abilities submenu:")
        for i, ability in enumerate(defense_ability_options[player_class], start=1):
            print(f"{i}. {ability.replace('_', ' ').title()} ({player_class})")
        print(f"{len(defense_ability_options[player_class]) + 1}. Back")

        defense_ability_option = input("Choose a defense ability: ")
        if defense_ability_option.isdigit():
            defense_ability_option = int(defense_ability_option)
            if 1 <= defense_ability_option <= len(defense_ability_options[player_class]) + 1:
                if defense_ability_option == len(defense_ability_options[player_class]) + 1:
                    return None
                else:
                    return defense_ability_options[player_class][defense_ability_option - 1]
            else:
                print("Invalid option. Please choose a valid option.")
                return select_defense_ability(player_class)
        else:
            print("Invalid option. Please choose a valid option.")
            return select_defense_ability(player_class)
    else:
        print("No defense abilities available for this class.")
        return None
 
def select_enemy_attack_defense(enemy, enemy_resistance):
    enemy_class = enemy.__class__.__name__

    attack_ability_options = {
        "Asuras": ["attack_ability"],
        "Manushyas": ["mana_ability"],
        "Tiryak": ["attack_ability"],
        "Pretas": ["mana_ability"],
        "Narakas": ["attack_ability"]
    }

    attack_options = ["1", "2"]
    defense_options = ["1", "2"]

    """ if enemy_class in attack_ability_options:
        attack_options.append("3") """
    
    defense_ability_options = {
        "Deva": ["defense_ability"],
        "Asuras": ["defense_ability"],
        "Manushyas": ["evasion_ability"],
        "Tiryak": ["evasion_ability"],
        "Pretas": ["defense_ability"]
    }

    """ if enemy_class in defense_ability_options:
        defense_options.append("3") """

    enemy_attack_option = random.choice(attack_options)
    enemy_defense_option = random.choice(defense_options)

    if enemy_attack_option == "1":
        enemy_attack_type = 1
        enemy_attack = enemy.basic_attack()
    elif enemy_attack_option == "2":
        enemy_attack_type = 2
        enemy_attack = enemy.mana_attack()
    elif enemy_attack_option == "3":
        special_attacks = attack_ability_options.get(enemy_class)
        if special_attacks:
            enemy_attack_type = 1 if special_attacks[0] == "attack_ability" else 2
            enemy_attack = getattr(enemy, special_attacks[0])(enemy_resistance)

    if enemy_defense_option == "1":
        enemy_defense_type = 1
        enemy_defense = enemy.basic_defense()
    elif enemy_defense_option == "2":
        enemy_defense_type = 2
        enemy_defense = enemy.basic_evasion()
    elif enemy_defense_option == "3":
        special_defenses = defense_ability_options.get(enemy_class)
        if special_defenses:
            enemy_defense_type = 1 if special_defenses[0] == "defense_ability" else 2
            enemy_defense = getattr(enemy, special_defenses[0])(enemy_resistance)

    return enemy_attack, enemy_attack_type, enemy_defense, enemy_defense_type
    
def calculate_damage(damage, type1, defense, type2):
    if type1 == 1 and type2 == 1:
        # Tipo de ataque físico y tipo de defensa física
        damageTotal = int(max(0, damage * 2.5 - defense))
    elif type1 == 1 and type2 == 2:
        # Tipo de ataque físico y tipo de defensa de evasión
        damageTotal = int(max(0, damage * 0.9 - defense))
    elif type1 == 2 and type2 == 1:
        # Tipo de ataque mágico y tipo de defensa física
        damageTotal = int(max(0, damage * 0.9 - defense))
    elif type1 == 2 and type2 == 2:
        # Tipo de ataque mágico y tipo de defensa de evasión
        damageTotal = int(max(0, damage * 2.5 - defense))
    return damageTotal

def start_game(player, final_level):
    try:
        while player.level <= final_level and player.lives > 0:
            clear_terminal()
            player_level = player.level
            print("-" * 50)
            print(f"\nNIVEL: {player_level}\n")
            print("-" * 50)
            enemy = generate_enemy(player_level)

            while True:
                if not character_actions_menu(player, enemy):
                    break

        print("¡Has completado todos los niveles! ¡Felicidades!")
    except SystemExit:
        print("-" * 50)
        print("\n¡Has salido del juego!\n")  
        print("-" * 50) 
    
def clear_terminal():
    os.system('clear')  # Este comando limpia la terminal en sistemas Linux

def press_enter_to_continue():
    input("\n* Press Enter to continue...")
    
def main():
    clear_terminal()
    
    print("-" * 50)
    print("\n¡Bienvenido al juego!\n")
    print("-" * 50)
    
    nivel_final = configuration()
    personaje = generate_character()
    
    press_enter_to_continue()
    clear_terminal()
    
    start_game(personaje, nivel_final)

if __name__ == "__main__":
    main()