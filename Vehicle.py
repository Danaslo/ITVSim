from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, license_plate, wheels, owner_id, age, lights, gas_emissions):
        self.__set_owner_id(owner_id)
        self.__set_license_plate(license_plate)
        self.__set_wheels(wheels)
        self.age = age
        self.__set_lights(lights)
        self.__set_gas_emissions(gas_emissions)

    # Checks if the owner's id follows the correct pattern:
    def __set_owner_id(self,owner_id):
        if len(owner_id) != 9:
            raise ValueError('Owner ID must be composed of 8 numbers and 1 letter. ')
        
        owner_number = owner_id[:8]
        if not owner_number.isdigit():
            raise ValueError('The first 8 characters must be numbers')

        owner_letter = owner_id[8:]
        if owner_letter.isdigit() or len(owner_letter) != 1:
            raise ValueError('Last character must be a letter')
        
        self.owner_id = owner_id
        
    def get_owner_id(self):
        return self.owner_id
    
    # Checks if the license plate follows the correct pattern.
    def __set_license_plate(self,license_plate):
        if ' ' not in license_plate:
            raise ValueError('License plate must have 4 numbers and 3 letters separated by one space')
        
        split_plate = license_plate.split(' ')
        
        number = split_plate[0]
        if not number.isdigit() or len(number) != 4:
            raise ValueError('License plate must contain 4 numbers')
        
        letters = split_plate[1]
        if not letters.isalpha() or len(letters) != 3:
            raise ValueError('License plate must contain 3 letters')
        
        self.license_plate = license_plate
    
    def get_license_plate(self):
        return self.license_plate
    
    # Checks if the number of wheels is correct:
    def __set_wheels(self,wheels):
        if wheels != 2 and wheels != 4:
            raise ValueError('Wheels must be either 2 or 4')
        self.wheels = wheels
    
    def get_wheels(self):
        return self.wheels

    # Checks if the array containing the lights has the correct ammount.
    def __set_lights(self,lights):
        if len(lights) != 2:
            raise ValueError('Only front and rear lights are considered for the inspection')
        self.lights = lights

    def get_lights(self):
        return self.lights

    def __set_gas_emissions(self, gas_emissions):
        if len(gas_emissions) != 3:
            raise ValueError('CO, HC and NOx must be provided in order to begin inspection')
        self.gas_emissions = gas_emissions

    def get_gas_emissions(self):
        return self.gas_emissions

    #Abstract method to test a bit of polymorphism:
    @abstractmethod
    def honk(self):
        pass

    def to_string(self):
        lights_str = "  " + "\n  ".join([f"{k}: {v}" for k, v in self.lights.items()])
        gases_str = "  " + "\n  ".join([f"{k}: {v}" for k, v in self.gas_emissions.items()])
        return (
        f"Owner's ID: {self.owner_id}\n"
        f"License plate: {self.license_plate}\n"
        f"Wheel amount: {self.wheels}\n"
        f"Age: {self.age}\n"
        f"Lights condition:\n{lights_str}\n"
        f"Gas emissions:\n{gases_str}"
        )   