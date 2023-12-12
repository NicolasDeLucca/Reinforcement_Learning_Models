# Dominio del Acrobot de doble Péndulo

## **Entorno Extendido del Acrobot**

El objetivo principal es preparar el entorno para el entrenamiento del agente Q-learning en un sistema de doble péndulo.

Se extendió el entorno Acrobot para abordar el desafío de dos péndulos. Se creó la clase AcrobotEnvExtended, que hereda del entorno Acrobot original, y se agregaron modificaciones para manejar dos péndulos conectados linealmente.

son los ángulos de los péndulos del sistema Acrobot. Estos describen la posición de los péndulos en un momento dado, es decir la configuración actual del sistema.

Se puede visualizar cómo este ambiente está basado en diferencias temporales:

![acrobot_env_extended](../Image%20Captures/acrobot_env_extended.png)

También se puede notar existe el hiperparámetro max_steps que define la cantidad máxima de pasos sobre el ambiente.

## **Diseño e Inicialización del Agente Q-learning**

Se diseñó e implementó la clase Q Learning Agent para abordar el problema del doble péndulo.

El valor Q (quality value) representa las recompensas futuras acumuladas esperadas que un agente puede obtener al realizar una acción específica en un estado determinado, con una policy particular.

El agente Q-learning se configuró con los parámetros esenciales, como alpha, gamma y epsilon.

**Alfa** (tasa de aprendizaje)

Determina el tamaño del paso en el que se actualizan los valores Q durante el proceso de aprendizaje.

Un alfa más pequeño hace que el aprendizaje sea más lento pero puede conducir a una convergencia más estable, mientras que demasiado grande puede provocar oscilaciones o inestabilidad.

**Gamma** (factor de descuento)

Controla la importancia de las futuras recompensas.

Los valores más pequeños hacen que el agente se concentre más en las recompensas inmediatas, mientras que en valores más grandes considera consecuencias a largo plazo.

**Epsilon** (compensación exploración-explotación)

Controla el equilibrio entre la exploración (probar nuevas acciones) y la explotación (seleccionar la acción más conocida).

Un épsilon más alto fomenta una mayor exploración, mientras que un valor más bajo conduce a una mayor explotación.

Finalmente optamos por los siguientes hiperparámetros:

![hyperparameters](../Image%20Captures/hyperparameters.png)

## **Entrenamiento del Agente en el Acrobot Extendido**

Se centró en entrenar el agente Q-learning en el entorno del Acrobot extendido.

Durante el entrenamiento, el agente interactuó con el entorno, seleccionó acciones según la política epsilon-greedy, y actualizó sus valores Q utilizando el algoritmo Q-learning.

![epsilon_greedy_policy](../Image%20Captures/greedy_policy.png)

![update_q_value](../Image%20Captures/q_value_reinforcement.png)

## **Análisis**

Para la simulación del agente q learning se utilizó el siguiente código:

![simulation_method](../Image%20Captures/simulation_method.png)

donde podemos observar como el agente discretiza entre los estados a partir de la obtención de observaciones, para posteriormente decidir su siguiente acción.

![q_learning_algorithm_methods](../Image%20Captures/q_learning_algorithm_methods_capture.png)

Se realizó un experimento de 50 episodios donde se entrenó y evaluó el agente para cada uno de los hiperparámetros definidos anteriormente.

Los hiperparámetros más eficaces fueron los siguientes según la evaluación de la policy:

![optimal_policy](../Image%20Captures/optimal_policy_result.png)

Por último visualizamos la simulación del agente con dichos hiperparámetros:

![simulation](../Image%20Captures/simulation_capture_result.png)

Recompensa:

![reward_result](../Image%20Captures/utility_result.png)

Tiempo de ejecución: al menos una hora.

![execution_time_capture](../Image%20Captures/execution_time_capture.png)

El tiempo de ejecución fue mayor pero debido a que el entorno de ejecución se desconectaba con el paso del tiempo, y el contador se reiniciaba, no se refleja el tiempo real en la imágen.