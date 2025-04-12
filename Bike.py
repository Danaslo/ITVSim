from Vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, license_plate, wheels, owner_id, age, lights, gas_emissions,engine_displacement,has_sidecar,handlebar_type,noise):
        if wheels != 2:
            raise ValueError("Bike wheels ammount must be 2")
        super().__init__(license_plate, wheels, owner_id, age, lights, gas_emissions)
        self.__set_engine_displacement(engine_displacement)
        self.__set_handlebar_type(handlebar_type)
        self.noise = noise

    def __set_engine_displacement(self,engine_displacement):
        if engine_displacement < 50 or engine_displacement > 1000:
            raise ValueError("Bike engine displacement must be between 50cc and 1000cc")
        self.engine_displacement = engine_displacement

    def get_engine_displacement(self):
        return self.engine_displacement

    def get_noise(self):
        return self.noise

    def __set_handlebar_type(self,handlebar_type):
        if handlebar_type == "High" or handlebar_type == "Low" or handlebar_type == "Sport":
            self.handlebar_type = handlebar_type
        else:
             raise ValueError("Bike handlebar must be either High, Low or Sport")

    def honk(self):
        return "PIIIIIIIIIIIIIIIIIIuuuuuuuuuuuuu"