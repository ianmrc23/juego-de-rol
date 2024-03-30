# Class Base

La clase `Base` representa un personaje en el juego. Contiene atributos y métodos comunes a todos los personajes.

## Attributes

- `healthPoints`: Puntos de vida del personaje.
- `strength`: Fuerza del personaje.
- `resistance`: Resistencia del personaje.
- `defense`: Defensa del personaje.
- `intelligence`: Inteligencia del personaje.
- `agility`: Agilidad del personaje.
- `freePoints`: Puntos de habilidad disponibles para asignar.
- `coins`: Diccionario que contiene la cantidad de monedas de `gold`, `silver` y `copper` del personaje.
- `level`: Nivel del personaje.
- `lives`: Vidas del personaje.

## Methods

1. `total_copper_coins()`: 
    - Devuelve la cantidad total de monedas de oro, plata y cobre en unidades de cobre.
    - Parámetros: 
        - `none`.
    - Retorna: Un `entero` que representa la cantidad total de monedas en unidades de cobre.

2. `convert_from_copper(coins)`: (Método estático)
    - Convierte una cantidad de monedas de cobre a oro, plata y cobre.
    - Parámetros:
        - `coins`: Cantidad de monedas en cobre.
    - Retorna: Una `tupla` con tres valores enteros que representan la cantidad de oro, plata y cobre respectivamente.

3. `average_statistics()`:
    - Calcula el promedio de las siguientes estadísticas healthPoints, strength, resistance, defense, intelligence, agility
    - Parámetros:
        - `none`.
    - Retorna: Un `entero` que representa el promedio de las estadísticas del personaje.

4. `assign_points(statistic, amount)`:
    - Asigna puntos a una estadística específica del personaje.
    - Parámetros:
        - `statistic`: Cadena que representa la estadística a la que se asignarán puntos.
        - `amount`: Cantidad de puntos que se asignarán a la estadística.
    - Retorna: Una `cadena` que indica si se han asignado los puntos correctamente o no.

5. `view_statistics()`:
    - Devuelve una cadena con las estadísticas del personaje.
    - Parámetros:
        - `none`.
    - Retorna: Una `cadena` que contiene las estadísticas del personaje formateadas.

6. `view_coins()`:
    - Devuelve una cadena con la cantidad de monedas del personaje.
    - Parámetros:
        - `none`.
    - Retorna: Una `cadena` que contiene la cantidad de monedas del personaje formateadas.

7. `enemy_strength(enemy)`: 
    - Determina si el enemigo es más fuerte, más débil o equilibrado en comparación con el personaje.
    - Parámetros:
        - `enemy`: Instancia de la clase enemiga para comparar.
    - Retorna: Una `cadena` que indica si el enemigo es más fuerte, más débil o equilibrado en comparación con el personaje.

8. `victory_reward(enemy)`:
    - Calcula y otorga la recompensa al personaje por ganar una batalla.
    - Parámetros:
        - `enemy`: Instancia de la clase enemiga que fue derrotada.
    - Retorna: Una `cadena` que indica las recompensas obtenidas por ganar la batalla.

9. `defeat_losses(enemy)`:
    - Calcula y aplica las pérdidas al personaje por perder una batalla.
    - Parámetros:
        - `enemy`: Instancia de la clase enemiga que lo derrotó.
    - Retorna: Una `cadena` que indica las pérdidas sufridas por perder la batalla.

10. `training_increase()`: 
    - Incrementa aleatoriamente todas las estadísticas del personaje durante el entrenamiento.
    - Parámetros: 
        - `none`.
    - Retorna: `none`.

11. `instant_defeat(enemy)`: 
    - Determina si un personaje puede derrotar instantáneamente a otro personaje.
    - Parámetros:
        - `enemy`: Instancia de la clase enemiga a la que se enfrenta.
    - Retorna: Una `cadena` si el personaje es derrotado instantáneamente o sale victorioso instantáneamente.

12. `mana_attack()`: 
    - Calcula el valor de ataque basado en la inteligencia del personaje.
    - Parámetros: 
        - `none`.
    - Retorna: Un `entero` que representa el valor de ataque basado en la inteligencia del personaje.

13. `basic_attack()`: 
    - Calcula el valor de ataque básico del personaje.
    - Parámetros: 
        - `none`.
    - Retorna: Un `entero` que representa el valor de ataque básico del personaje.

14. `basic_defense()`: 
    - Calcula el valor de defensa básica del personaje.
    - Parámetros:
        - `none`.
    - Retorna: Un `entero` que representa el valor de defensa básica del personaje.

15. `basic_evasion()`:
    - Calcula la probabilidad básica de evasión del personaje.
    - Parámetros: 
        - `none`.
    - Retorna: Un `entero` que representa la capacidad básica de evasión del personaje.

16. `avoid_combat(enemy_agility)`: 
    - Determina si el personaje puede evitar el combate basado en la agilidad del enemigo.
    - Parámetros:
        - `enemy_agility`: Valor de agilidad del enemigo.
    - Retorna: `True` si el personaje puede evitar el combate, `False` si no puede.

17. `use_ability(resistance, ability_cost)`:
    - Intenta usar una habilidad y actualiza la resistencia auxiliar del personaje.
    - Parámetros:
        - `resistance`: Valor de resistencia actual del personaje guardada en una variable auxiliar.
        - `ability_cost`: Costo de resistencia para usar la habilidad.
    - Retorna: Una `tupla` donde el primer elemento es un `booleano` que indica si se puedo usar la habilidad y el segundo elemento es el valor `entero` actualizado de resistencia.

18. `rebirth()`: (Método abstracto) 
    - Define el comportamiento de renacimiento del personaje.
    - Parámetros: 
        - `none`.
    - Retorna: `none`.

19. `mana_ability()`: (Método abstracto) 
    - Define el comportamiento de la habilidad relacionada con la inteligencia.
    - Parámetros: 
        - `none`.
    - Retorna: Un `entero` que representa el valor de la habilidad relacionada con la inteligencia.

20. `attack_ability()`: (Método abstracto)
    - Define el comportamiento de la habilidad relacionada con la fuerza.
    - Parámetros: 
        - `none`.
    - Retorna: Un `entero` que representa el valor de la habilidad relacionada con la fuerza.

21. `defense_ability()`: (Método abstracto) 
    - Define el comportamiento de la habilidad relacionada con la defensa.
    - Parámetros: 
        - `none`.
    - Retorna: Un `entero` que representa el valor de la habilidad relacionada con la defensa.

22. `evasion_ability()`: (Método abstracto)
    - Define el comportamiento de la habilidad relacionada con la evasión.
    - Parámetros:
        - `none`.
    - Retorna: Un `entero` que representa el valor de la habilidad relacionada con la evasión.