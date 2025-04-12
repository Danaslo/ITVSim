[Ir a la sección en español](#descripción-del-proyecto)

# Project Overview:

This small project focuses on using OOP (Object-Oriented Programming) and inheritance. Its main objective is to practice key concepts such as class creation, inheritance, and polymorphism.

It revolves around Spain's vehicle inspections, where vehicles are thoroughly checked for defects that could pose a danger to the owner or others. The goal is to simulate the inspection of vehicles (both cars and motorbikes) and detect any issues that may make their use unsafe.

## **Classes:**

---

### **Vehicle**:  
The parent class for all vehicles undergoing inspection. It contains attributes common to all vehicles. This class **must** be abstract.

**Attributes**:  
- **license_plate**: The license plate that identifies all vehicles. It consists of 4 numbers and 3 letters. Example:
    - 0192 H3J  
    - 9283 BAZ  
- **wheels**: A common attribute for all vehicles, but varying between types.  
- **owner_id**: In Spain, it’s called DNI, following a pattern of 8 digits and 1 letter. The letter is determined via an algorithm, but we'll assume all IDs following this pattern are valid, even if the letter wouldn't be correct in real life.
- **age**: The age of the vehicle. In Spain, the time between inspections depends on the vehicle's age:
    - Less than 4 years old: No inspection required.
    - 4 to 10 years old: Inspection every 2 years.
    - More than 10 years old: Inspection annually.
- **lights**: Front and rear lights. There are 6 types of lights checked during the inspection, but we'll focus on front and rear.
- **gas_emissions**: A combination of 3 gases that must meet certain emission levels to pass the inspection:
    - *CO*: Below 0.50 g/km.  
    - *HC*: Below 0.10 g/km.  
    - *NOx*: Below 0.06 g/km.  

**Methods**:  
- **__init__()**: Constructor. Initializes the vehicle with the provided parameters and checks that:
    - The vehicle must have between 2 and 4 wheels (we're not tracking trucks yet).
    - The license plate follows the correct pattern (4 digits, 3 letters).
    - The age cannot be negative.
    - The owner ID follows the correct pattern (8 digits, 1 letter).
- **honk()**: A fun check during the inspection. The method can use polymorphism to behave differently based on the vehicle type.
- **Getters and setters**: For accessing and modifying the attributes.
- **toString()**: Returns a string representation of the vehicle’s attributes.

---

### **Bike**:  
Child class of **Vehicle**, representing motorbikes.

**Attributes**:  
- **engine_displacement**: The strength of the bike's engine. Must be between 50cc and 1000cc.  
- **has_sidecar**: Indicates whether the bike has a sidecar.  
- **handlebar_type**: Type of handlebars (e.g., High, Low, Sport).  
- **noise**: Represents the noise level in decibels the motorbike produces.

**Methods**:  
- **__init__()**: Constructor. Initializes the bike with the provided parameters and checks that:
    - The number of wheels must be 2 or 3 (4 wheels would make it a quad).
    - Engine displacement must be between 50cc and 1000cc.
    - Handlebar type must be one of the following: High, Low, or Sport.
- **Getters and setters**: For accessing and modifying the attributes.
- **toString()**: Returns a string representation of the bike’s attributes.

---

### **Car**:  
Child class of **Vehicle**, representing cars.

**Attributes**:  
- **seatbelts_quality**: The condition of the seatbelts (e.g., Good, Faulty, Broken).  
- **windshield_wipers_quality**: The condition of the windshield wipers (e.g., Good, Used, Broken).  
- **transmission_quality**: The condition of the transmission (e.g., Good, Faulty, Broken).  
- **airbag_status**: If the airbag light is on, the car *fails* the inspection.

**Methods**:  
- **__init__()**: Constructor. Initializes the car with the provided parameters and checks that:
    - The number of wheels must be 4.
- **Getters and setters**: For accessing and modifying the attributes.
- **toString()**: Returns a string representation of the car’s attributes.

---

### **Inspection**:  
Class that performs inspections on vehicles.

**Attributes**:  
- **address**: The street where the inspection building is located.  
- **location**: The city or town where the inspection building is located.  
- **date**: The date of the inspection.  
- **inspector**: Array of Inspector objects.

**Methods**:  
- **__init__()**: Constructor. Initializes the inspection with the provided parameters and checks that:
    - The date must be the local date.
- **inspection(Vehicle, inspector)**: Performs the inspection on a given vehicle and checks for:
    - **Common**:
        - *Lights*: Front and rear lights must work properly.
        - *Gas emissions*: CO, HC, and NOx levels must be below set limits.
    - **Bike**:
        - *Noise*: Based on engine displacement:
            - Less than 50cc: Noise must be below 80 dB.
            - More than 50cc: Noise must be below 72 dB.
    - **Car**:
        - *Seatbelts*: Faulty seatbelts get a warning; broken seatbelts mean confiscation.
        - *Wipers*: Worn wipers get a warning; broken wipers cause the vehicle to fail.
        - *Transmission*: Faulty transmission means failure.
        - *Airbag*: An airbag light on means confiscation.
- **report(inspection_results)**: Generates a report based on the inspection results, including:
    - Date of inspection.
    - Inspector's name.
    - Inspection results.
    - Inspection outcome (pass/fail, warnings, etc.).
    - Next inspection date, depending on the vehicle's age:
        - 4 to 10 years old: Next inspection in 2 years.
        - More than 10 years old: Next inspection in 1 year.

---

### **Inspector**:  
Class that adds a bit of humor to the inspection process by simulating the personality of ITV inspectors.
    - Angela: Loves to smile, she always try to uplift car owners whenever their car fails the test.
    - Manuel: Hates his job and he lashes out to the car owners at every chance he gets.
    - Jose: He is cheerful but tends to laugh whenever a driver fails one part of the test.




**Attributes**:  
- **name**: Must be one of the following: Angela, Manuel, or Jose.  
- **greetings**: An array containing 3 to 4 greetings for each inspector's personality.  
- **light_inspection**: A dictionary containing 2 arrays of sentences for light inspection outcomes.  
- **gas_inspection**: A dictionary containing 2 arrays of sentences for gas emission inspection outcomes.  
- **bike_noise_inspection**: A dictionary containing 2 arrays of sentences for bike noise inspection outcomes.  
- **seatbelt_inspection**: A dictionary containing 3 arrays of sentences for seatbelt inspection outcomes.  
- **wiper_inspection**: A dictionary containing 3 arrays of sentences for wiper inspection outcomes.  
- **transmission_inspection**: A dictionary containing 2 arrays of sentences for transmission inspection outcomes.  
- **airbag_inspection**: A dictionary containing 2 arrays of sentences for airbag inspection outcomes.

**Methods**:  
- **__init__()**: Constructor. Initializes the inspector with the provided parameters.
- getters and setters.

---

### **Additional Notes**:
- To simulate a real-life inspection, each checkup will have a random timeout between 2 to 5 seconds to represent the time taken for each test.

---

## Descripción del Proyecto:

Este pequeño proyecto se centra en el uso de POO (Programación Orientada a Objetos) y herencia. Su objetivo principal es practicar conceptos clave como la creación de clases, herencia y polimorfismo.

El proyecto gira en torno a las inspecciones de vehículos en España, donde los vehículos son revisados a fondo para detectar defectos que podrían poner en peligro al propietario o a otras personas. El objetivo es simular la inspección de vehículos (tanto coches como motos) y detectar cualquier problema que haga que su uso sea peligroso.

## **Clases:**

---

### **Vehículo**:  
La clase padre para todos los vehículos que pasan por la inspección. Contiene los atributos comunes a todos los vehículos. Esta clase **debe** ser abstracta.

**Atributos**:  
- **matricula**: La matrícula que identifica a todos los vehículos. Consiste en 4 números y 3 letras. Ejemplo:
    - 0192 H3J  
    - 9283 BAZ  
- **ruedas**: Un atributo común a todos los vehículos, pero que varía según el tipo.  
- **dni_propietario**: En España, se llama DNI, y sigue un patrón de 8 dígitos y 1 letra. La letra se calcula mediante un algoritmo, pero asumiremos que todos los DNI que sigan este patrón son válidos, aunque en la vida real la letra no sería correcta en algunos casos.
- **edad**: La edad del vehículo. En España, el tiempo entre inspecciones depende de la edad del vehículo:
    - Menos de 4 años: No es obligatorio pasar la inspección.
    - De 4 a 10 años: Inspección cada 2 años.
    - Más de 10 años: Inspección anual.
- **luces**: Luces delanteras y traseras. Se inspeccionan 6 tipos diferentes de luces en cada ITV, pero solo nos centraremos en las delanteras y traseras.
- **emisiones_gas**: Una combinación de 3 gases que deben cumplir ciertos límites para pasar la inspección:
    - *CO*: Debe estar por debajo de 0.50 g/km.  
    - *HC*: Debe estar por debajo de 0.10 g/km.  
    - *NOx*: Debe estar por debajo de 0.06 g/km.  

**Métodos**:  
- **__init__()**: Constructor. Inicializa el vehículo con los parámetros proporcionados y comprueba que:
    - El vehículo debe tener entre 2 y 4 ruedas (no estamos gestionando camiones por ahora).
    - La matrícula debe seguir el patrón correcto (4 dígitos, 3 letras).
    - La edad no puede ser negativa.
    - El DNI debe seguir el patrón correcto (8 dígitos, 1 letra).
- **claxon()**: Un chequeo algo curioso durante la inspección. El método puede usar polimorfismo para comportarse de manera diferente según el tipo de vehículo.
- **Getters y setters**: Para acceder y modificar los atributos.
- **toString()**: Devuelve una representación en forma de cadena de los atributos del vehículo.

---

### **Moto**:  
Clase hija de **Vehículo**, que representa motos.

**Atributos**:  
- **ruedas**: El número de ruedas, que puede ser 2 o 3.  
- **cilindrada_motor**: La potencia del motor de la moto. Debe estar entre 50cc y 1000cc.  
- **tiene_sidecar**: Indica si la moto tiene un sidecar o no.  
- **tipo_manillar**: Tipo de manillar (por ejemplo, Alto, Bajo, Deportivo).  
- **ruido**: Representa el nivel de ruido (en decibelios) que produce la moto.

**Métodos**:  
- **__init__()**: Constructor. Inicializa la moto con los parámetros proporcionados y comprueba que:
    - El número de ruedas debe ser 2 o 3 (si tiene 4, sería un Quad).
    - La cilindrada debe estar entre 50cc y 1000cc.
    - El tipo de manillar debe ser uno de los siguientes: Alto, Bajo, o Deportivo.
- **Getters y setters**: Para acceder y modificar los atributos.
- **toString()**: Devuelve una representación en forma de cadena de los atributos de la moto.

---

### **Coche**:  
Clase hija de **Vehículo**, que representa coches.

**Atributos**:  
- **calidad_cinturones**: El estado de los cinturones de seguridad (por ejemplo, Buen estado, Dañado, Roto).  
- **calidad_limpiaparabrisas**: El estado de los limpiaparabrisas (por ejemplo, Buen estado, Usado, Roto).  
- **calidad_transmision**: El estado de la transmisión (por ejemplo, Buena, Dañada, Rota).  
- **estado_airbag**: Si la luz del airbag está encendida, el coche *fallará* la inspección.

**Métodos**:  
- **__init__()**: Constructor. Inicializa el coche con los parámetros proporcionados y comprueba que:
    - El número de ruedas debe ser 4.
- **Getters y setters**: Para acceder y modificar los atributos.
- **toString()**: Devuelve una representación en forma de cadena de los atributos del coche.

---

### **Inspección**:  
Clase que realiza las inspecciones de los vehículos.

**Atributos**:  
- **dirección**: La calle donde se encuentra el edificio de inspección.  
- **ubicación**: La ciudad o pueblo donde se encuentra el edificio de inspección.  
- **fecha**: La fecha de la inspección.  
- **inspector**: Instancia de la clase *Inspector*.

**Métodos**:  
- **__init__()**: Constructor. Inicializa la inspección con los parámetros proporcionados y comprueba que:
    - La fecha debe ser la fecha local.
- **inspeccionar(Vehículo, inspector)**: Realiza la inspección en el vehículo dado y verifica:
    - **Común**:
        - *Luces*: Las luces delanteras y traseras deben funcionar correctamente.
        - *Emisiones de gas*: Los niveles de CO, HC y NOx deben estar por debajo de los límites establecidos.
    - **Moto**:
        - *Ruido*: Dependiendo de la cilindrada del motor:
            - Menos de 50cc: El ruido no debe superar los 80 dB.
            - Más de 50cc: El ruido no debe superar los 72 dB.
    - **Coche**:
        - *Cinturones*: Los cinturones dañados reciben una advertencia; los cinturones rotos provocan la confiscación del coche.
        - *Limpiaparabrisas*: Los limpiaparabrisas usados reciben una advertencia; los limpiaparabrisas rotos hacen que el coche falle.
        - *Transmisión*: Si la transmisión está dañada, el coche falla la inspección.
        - *Airbag*: Si la luz del airbag está encendida, el coche es confiscado.
- **informe(resultados_inspección)**: Genera un informe con los resultados de la inspección, incluyendo:
    - Fecha de la inspección.
    - Nombre del inspector.
    - Resultados de la inspección.
    - Resultado de la inspección (aprobado/no aprobado, advertencias, etc.).
    - Fecha de la próxima inspección, según la edad del vehículo:
        - De 4 a 10 años: La próxima inspección será en 2 años.
        - Más de 10 años: La próxima inspección será en 1 año.

---

### **Inspector**:  
Clase que añade un toque de humor al proceso, simulando la personalidad de los inspectores de ITV.

    - Angela: Le encanta sonreir e intenta subir el ánimo de los conductores cuando fallan la inspección.
    - Manuel: Odia su trabajo y tiende a enfocar su frustración en los dueños de los coches a cada oportunidad que tiene.
    - Jose: Es alegre pero tiende a reírse cada vez que un conductor falla una parte de la inspección.

**Atributos**:  
- **nombre**: Debe ser uno de los siguientes: Angela, Manuel o Jose.  
- **saludos**: Un array que contiene 3 o 4 saludos que coinciden con la personalidad de cada inspector.  
- **inspección_luces**: Un diccionario que contiene 2 arrays con frases para usar cuando se aprueban o fallan las luces.  
- **inspección_emisiones**: Un diccionario que contiene 2 arrays con frases para usar cuando se aprueban o fallan las emisiones de gas.  
- **inspección_ruido_moto**: Un diccionario que contiene 2 arrays con frases para usar cuando una moto aprueba o falla la inspección de ruido.  
- **inspección_cinturones**: Un diccionario que contiene 3 arrays con frases para usar cuando un coche aprueba, recibe una advertencia o falla la inspección de cinturones.  
- **inspección_limpiaparabrisas**: Un diccionario que contiene 3 arrays con frases para usar cuando un coche aprueba, recibe una advertencia o falla la inspección de limpiaparabrisas.  
- **inspección_transmisión**: Un diccionario que contiene 2 arrays con frases para usar cuando un vehículo aprueba o falla la inspección de transmisión.  
- **inspección_airbag**: Un diccionario que contiene 2 arrays con frases para usar cuando un vehículo aprueba o falla la inspección de airbag.


**Métodos**:  
- **__init__()**: Constructor. Inicializa el inspector con los parámetros proporcionados.

---

### **Notas Adicionales**:
- Para simular una inspección real, cada chequeo tendrá un tiempo aleatorio entre 2 a 5 segundos, representando el tiempo que toma cada prueba.
