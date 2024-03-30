import random
from classPaths import Deva, Asuras, Manushyas, Tiryak, Pretas, Narakas

def configuration():
    while True:
        try:
            final_level = int(input("What level do you want to finish the game at? (between 2 and 100): "))
            if final_level < 2 or final_level > 100:
                print("The level must be between 2 and 100. Please try again.")
            else:
                return final_level
        except ValueError:
            print("Please enter a valid integer.")

def generate_character():
    print("Select your path:")
    print("1. Deva")
    print("2. Asuras")
    print("3. Manushyas")
    print("4. Tiryak")
    print("5. Pretas")
    print("6. Narakas")
    option = input("Choose a number corresponding to the desired path: ")

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
    
def character_actions_menu():
    print("Character Actions Menu:")
    print("1. Analyze Enemy")
    print("2. Fight")
    print("3. Flee")
    print("4. Menu")
    print("5. Quit Game")
    
    choice = input("Choose an action: ")

    if choice == "1":
        analyze_enemy()
    elif choice == "2":
        fight()
    elif choice == "3":
        flee()
    elif choice == "4":
        character_menu()
    elif choice == "5":
        quit_game()
    else:
        print("Invalid choice. Please select again.")
        character_actions_menu()

def character_menu():
    print("Character Menu:")
    print("1. View Statistics")
    print("2. Assign Free Points")
    print("3. View Coins")
    print("4. Inventory")
    print("5. Shop")
    print("6. Return to Main Menu")

    choice = input("Choose an option: ")

    if choice == "1":
        menu_view_statistics()
    elif choice == "2":
        assign_free_points()
    elif choice == "3":
        menu_view_coins()
    elif choice == "4":
        view_inventory()
    elif choice == "5":
        visit_shop()
    elif choice == "6":
        character_actions_menu()
    else:
        print("Invalid choice. Please select again.")
        character_menu()

def analyze_enemy(player, enemy):
    enemy_avg_stats = enemy.average_statistics()
    
    enemy_strength = enemy.enemy_strength(player)
    
    print("Enemy Analysis:")
    print(f"Enemy Strength: {enemy_strength}")
    print(f"Average Statistics of Enemy: {enemy_avg_stats}")    

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
        player_attack, player_attack_type, player_defense, player_defense_type = select_attack_defense(player, player_resistance)
        enemy_attack, enemy_attack_type, enemy_defense, enemy_defense_type = select_enemy_attack_defense(enemy, enemy_resistance)

        enemy_damage = calculate_damage(player_attack, player_attack_type, enemy_defense, enemy_defense_type)
        enemy_hp -= enemy_damage

        if enemy_hp <= 0:
            player.victory_reward(enemy)
            return True

        player_damage = calculate_damage(enemy_attack, enemy_attack_type, player_defense, player_defense_type)
        player_hp -= player_damage

        if player_hp <= 0:
            player.defeat_losses(enemy)
            return False

def flee(player, enemy_agility):
    if player.avoid_combat(enemy_agility):
        print("You successfully flee from the enemy!")
        generate_enemy(player.level)
    else:
        print("You couldn't flee from the enemy!")

def menu_view_statistics(self):
    return self.view_statistics()

def assign_free_points(self):
    print("Available statistics:")
    print("1. Health Points")
    print("2. Strength")
    print("3. Resistance")
    print("4. Defense")
    print("5. Intelligence")
    print("6. Agility")
    print("0. Exit")
    
    statistic_options = ["healthPoints", "strength", "resistance", "defense", "intelligence", "agility"]
    while True:
        statistic_choice = input("Choose a statistic to assign points to (or enter 0 to exit): ")
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
    
    print(f"Free points available: {self.freePoints}")
    
    while True:
        points_to_assign = input(f"How many points do you want to assign to {chosen_statistic}? (Enter 0 to exit) ")
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

def menu_view_coins(player):
    return player.view_coins()

def view_inventory():
    print("Coming soon in version 2.0: Inventory management with armor, weapons, and consumables using linked lists.")

def visit_shop():
    print("Coming soon in version 2.0: Shop feature with armor, weapons, and consumables using linked lists.")
  
def quit_game():
    # Implementation for quitting the game
    pass  
    
def select_attack_defense(player, player_resistance):
    while True:
        print("Select attack method:")
        print("1. Physical attack")
        print("2. Mana attack")
        print("3. Special ability")
        print("4. Back")

        attack_option = input("Choose an option: ")
        if attack_option == "1":
            attack = player.basic_attack()
            attack_type = 1
            break
        elif attack_option == "2":
            attack = player.mana_attack()
            attack_type = 2
            break
        elif attack_option == "3":
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
            break
        elif attack_option == "4":
            return None, None, None, None
        else:
            print("Invalid option. Please choose a valid option.")

    while True:
        print("Select defense method:")
        print("1. Defend")
        print("2. Evade")
        print("3. Special ability")
        print("4. Back")

        defense_option = input("Choose an option: ")
        if defense_option == "1":
            defense = "defend"
            break
        elif defense_option == "2":
            defense = "evade"
            break
        elif attack_option == "3":
            player_class = player.__class__
            special_ability = select_attack_ability(player_class)
            if special_ability:
                if special_ability == "defense_ability":
                    defense_type = 1
                elif special_ability == "evasion_ability":
                    defense_type = 2
                defense = getattr(player, special_ability)(player_resistance)
            else:
                defense = None
            break
        elif defense_option == "4":
            return None, None, None, None
        else:
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

    # Mapeo de habilidades especiales de ataque para cada clase de enemigo
    attack_ability_options = {
        "Asuras": ["attack_ability"],
        "Manushyas": ["mana_ability"],
        "Tiryak": ["attack_ability"],
        "Pretas": ["mana_ability"],
        "Narakas": ["attack_ability"]
    }

    # Definir las opciones de ataque y defensa básicas
    attack_options = ["1", "2"]
    defense_options = ["1", "2"]

    # Verificar si la clase del enemigo está en el mapeo de habilidades de ataque
    if enemy_class in attack_ability_options:
        attack_options.append("3")
    
    # Verificar si la clase del enemigo está en el mapeo de habilidades de defensa
    defense_ability_options = {
        "Deva": ["defense_ability"],
        "Asuras": ["defense_ability"],
        "Manushyas": ["evasion_ability"],
        "Tiryak": ["evasion_ability"],
        "Pretas": ["defense_ability"]
    }

    if enemy_class in defense_ability_options:
        defense_options.append("3")

    # Seleccionar aleatoriamente la opción de ataque y defensa
    enemy_attack_option = random.choice(attack_options)
    enemy_defense_option = random.choice(defense_options)

    # Si la opción de ataque es una habilidad especial (3)
    if enemy_attack_option == "3":
        # Obtener las habilidades especiales de ataque del enemigo
        special_attacks = attack_ability_options[enemy_class]
        # Si solo hay una habilidad especial disponible
        if len(special_attacks) == 1:
            enemy_attack = getattr(enemy, special_attacks[0])(enemy_resistance)
        # Si hay más de una habilidad especial disponible, elegir una al azar
        else:
            random_index = random.randint(0, len(special_attacks) - 1)
            enemy_attack = getattr(enemy, special_attacks[random_index])(enemy_resistance)
    # Si la opción de ataque es básica (1 o 2)
    else:
        enemy_attack = enemy.basic_attack() if enemy_attack_option == "1" else enemy.mana_attack()

    # Si la opción de defensa es una habilidad especial (3)
    if enemy_defense_option == "3":
        # Obtener las habilidades especiales de defensa del enemigo
        special_defenses = defense_ability_options[enemy_class]
        # Si solo hay una habilidad especial disponible
        if len(special_defenses) == 1:
            enemy_defense = getattr(enemy, special_defenses[0])(enemy_resistance)
        # Si hay más de una habilidad especial disponible, elegir una al azar
        else:
            random_index = random.randint(0, len(special_defenses) - 1)
            enemy_defense = getattr(enemy, special_defenses[random_index])(enemy_resistance)
    # Si la opción de defensa es básica (1 o 2)
    else:
        enemy_defense = "defend" if enemy_defense_option == "1" else "evade"

    return enemy_attack, enemy_defense 
    
def calculate_damage(player_attack, player_attack_type, enemy_defense, enemy_defense_type):
    pass

    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def comenzar_juego(nivel_final, personaje):
    while nivel_jugador <= nivel_final:
        print("\nComienza el nivel", nivel_jugador)
        enemigo = generar_enemigo(nivel_jugador)

        while personaje.hp > 0 and enemigo.hp > 0:
            accion = input("\n¿Qué acción desea realizar? (analizar/enfrentar/huir): ")

            if accion == "analizar":
                personaje.analizar_enemigo(enemigo)
            elif accion == "enfrentar":
                pelear(personaje, enemigo)
            elif accion == "huir":
                if personaje.huir(enemigo.agilidad):
                    print("Has logrado huir del enemigo.")
                    break
                else:
                    print("No has podido huir del enemigo. ¡Prepárate para enfrentarlo!")

        if personaje.hp <= 0:
            print("Has sido derrotado. ¡Fin del juego!")
            terminar_juego()
            break
        elif enemigo.hp <= 0:
            print("Has derrotado al enemigo. ¡Continúa al siguiente nivel!")
            nivel_jugador += 1

    print("¡Has completado todos los niveles! ¡Felicidades!")

def pelear(personaje, enemigo):
    # Lógica del combate
    pass

def terminar_juego(vidas_jugador, nivel_jugador, nivel_final):
    if vidas_jugador <= 0:
        print("Game Over. Tus vidas han llegado a cero.")
    elif nivel_jugador > nivel_final:
        print("¡Has completado todos los niveles! ¡Felicidades!")
    else:
        print("Regresando al menú principal.")

def main():
    print("¡Bienvenido al juego!")

    nivel_final = configuracion()
    personaje = generar_personaje()

    comenzar_juego(nivel_final, personaje)

if __name__ == "__main__":
    main()
