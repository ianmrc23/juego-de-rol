# Main del Juego

Este es el archivo principal del juego que sigue la estructura y lógica detallada a continuación:

## Estructura del Juego

1. **Configuración**: Permite al jugador elegir el nivel en el que termina el juego.
2. **Generar Personaje**: Permite al jugador elegir un camino y genera el personaje correspondiente.
3. **Comenzar Juego**: Inicia el bucle del juego hasta que el jugador alcance el nivel definido.
4. **Generar Enemigo**: Genera un enemigo aleatorio basado en el nivel del jugador.
5. **Acciones Personajes**:
    - a) **Analizar Enemigo**: Ejecuta la función `promedio_estadisticas(enemigo)`.
    - b) **Huir**: Ejecuta la función `evitar_combate(self, agilidad_enemigo)`.
    - c) **Pelear**: Lógica del combate.
    - d) **Terminar Juego**: Lógica para finalizar el juego y volver al menú de configuración que es el paso 1.
    - e) **Menú Personaje**: Contiene las siguientes opciones:
        - i) **Ver Estadísticas**: Ejecuta `ver_estadisticas(self)`.
        - ii) **Asignar Puntos Libres**: Ejecuta `asignar_puntos(self, estadistica, cantidad)`.
        - iii) **Ver Monedas**: Ejecuta `ver_monedas(self)`.
        - iv) **Inventario**: Próximamente.
        - v) **Tienda**: Próximamente.
    

6. **Finaliza el Juego**: El nivel del personaje llega a su fin, se cierra el bucle.

## Función de Pelea

Esta función es responsable del combate y sigue los siguientes pasos:

1. **Verificar Derrota o Victoria Instantánea**: Se ejecuta `derrota_instantanea(self, otra_clase)`.
2. **Si no hay victoria o derrota instantánea**: Se crean variables auxiliares.
    - a) Puntos de Vida = `self.hp`.
    - b) Resistencia para habilidades = `self.resistencia`.
3. **Comienza el Combate**: Se inicia un bucle hasta que los puntos de vida del jugador o del enemigo lleguen a 0 o menos.
4. **Lógica de Ataque y Defensa para Cada Ronda**:
    - a) El jugador elige su ataque y defensa, el enemigo elige aleatoriamente.
5. **Lógica de Pérdida de HP**:
    - a) Se calcula el daño basado en las elecciones de ataque y defensa.
    - b) Se reduce el HP del jugador o del enemigo según el daño calculado.
    - c) Se repite la lógica de pérdida de HP utilizando las mismas reglas para calcular el daño.
6. **Recompensa por la Pelea**:
    - a) Si el jugador pierde: Se ejecuta `perdidas_derrota(self, otra_clase)`.
    - b) Si el jugador gana: Se ejecuta `recompensa_victoria(self, otra_clase)`.
    - c) Se verifica automáticamente si el nivel del jugador alcanza la condición de finalización del juego durante la recompensa.
