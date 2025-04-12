from Vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, license_plate, wheels, owner_id, age, lights, gas_emissions,seatbelts_quality,windshield_wipers_quality,transmission_quality,airbag_quality):
        super().__init__(license_plate, wheels, owner_id, age, lights, gas_emissions)
        self.seatbelts_quality = seatbelts_quality
        self.windshield_wipers_quality = windshield_wipers_quality
        self.transmission_quality = transmission_quality
        self.airbag_quality = airbag_quality
    
    def get_seatbelts(self):
        return self.seatbelts_quality
    
    def get_windshield_wipers(self):
        return self.windshield_wipers_quality
    
    def get_transmission_quality(self):
        return self.transmission_quality
    
    def get_airbag_quality(self):
        return self.airbag_quality

    def honk(self):
        return "PI PI PI PI, PI PIIIIIIIIIIIII"
    
    def to_string(self):
        return super().to_string() + (
            f"\nSeatbelts quality: {self.seatbelts_quality}\n"
            f"Windshield wipers quality: {self.windshield_wipers_quality}\n"
            f"Transmission quality: {self.transmission_quality}\n"
            f"Airbag quality: {self.airbag_quality}"
        )