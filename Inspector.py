class Inspector:

    def __init__(self,name, greetings, lights_inspection, gas_inspection, 
                 noise_inspection, seatbelt_inspection, windshield_wiper_inspection,
                 transmission_inspection, airbag_inspection ):
        self.name = name
        self.greetings = greetings
        self.lights_inspection = lights_inspection
        self.gas_inspection = gas_inspection
        self.noise_inspection = noise_inspection
        self.seatbelt_inspection = seatbelt_inspection
        self.windshield_wiper_inspection = windshield_wiper_inspection
        self.transmission_inspection = transmission_inspection
        self.airbag_inspection = airbag_inspection

    def get_name(self):
        return self.name

    def get_greetings(self):
        return self.greetings

    def get_lights_inspection(self,option):
        return self.lights_inspection.get(option)

    def get_gas_inspection(self,option):
        return self.gas_inspection.get(option)

    def get_noise_inspection(self,option):
        return self.noise_inspection.get(option)

    def get_seatbelt_inspection(self,option):
        return self.seatbelt_inspection.get(option)

    def get_windshield_wiper_inspection(self,option):
        return self.windshield_wiper_inspection.get(option)

    def get_transmission_inspection(self,option):
        return self.transmission_inspection.get(option)

    def get_airbag_inspection(self,option):
        return self.airbag_inspection.get(option)
