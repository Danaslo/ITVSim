from Inspector import Inspector
from datetime import datetime
from Bike import Bike
from Car import Car
import random
import time

class Inspection:

    def __init__(self,address,location):
        self.address = address
        self.location = location
        self.date = datetime.now()
        self.inspectors = self.generate_inspectors()

    def generate_inspectors(self):
        # Array to insert inspectors
        inspectors = []

        #Angela generation:
        #Common for all vehicles:
        angela_name = "Angela"
        angela_greetings = ["Hi, i'm Angela! Let's hope this inspection goes well!",
                    "Good morning! My name is Angela Let's get you right in so you can be out in no time!",
                    "Hello! My name is Angela, i'll try my best to make this experience as painless as it can be"]
        angela_lights_inspection = {True: "Passed: Perfect! One check less to finish", False: "Failed: Mmm... It seems the state of your lights is not optimal. I'm really sorry but i can't let you pass the inspection with faulty lights. Let's continue, hopefully there isn't anything more that's faulty."}
        angela_gas_inspection = {True: "Passed: Gases are as good as they can be! On to the next!", False: "Failed: I'm sorry but your emission leves are above limits. I'm afraid your car must be disqualified from the inspection. Let's continue just in case there is anything more that is in need of repair."}
        #Bike specific:
        angela_noise_inspection = {True: "Passed: Nice! I hate noisy vehicles and yours is below the limits", False: "Failed: How noisy! I'm going to have to add a warning for that one."}
        #Car specific:
        angela_seatbelt_inspection = {True: "Passed: As secure and tight as a seatbelt should be.", False: "Failed: No, i'm afraid these seatbelts aren't secure at all... I'm sorry but i must confiscate the car after the inspection is finished."}
        angela_windshield_wiper_inspection = {True: "Passed: Perfect for cleaning any water you get under the rain!", False: "Failed: Mm... These wipers can't clean well, you'll have problems if you drive while it's raining with this. I'll have to issue a warning"}
        angela_transmission_inspection = {True: "Passed: You could go to the mountain with this car. Nice!", False: "Failed: I'm sorry but the transmission is faulty. You are going to have to step out of the vehicle once we finish the inspection"}
        angela_airbag_inspection = {True: "Passed: You'll be more secure in this car than inside a safe!", False: "Failed: These airbags are a no no, i'm sorry. Step out ot the vehicle and wait for the report, please."}
        inspectors.append(Inspector(angela_name,angela_greetings,angela_lights_inspection,
                                    angela_gas_inspection,angela_noise_inspection,angela_seatbelt_inspection,
                                    angela_windshield_wiper_inspection,angela_transmission_inspection,
                                    angela_airbag_inspection                                    
                                    ))
        #Manuel generation:
        #Common for all vehicles:
        manuel_name = "Manuel"
        manuel_greetings = ["Yet another pig for the butcher...",
                    "Yeah yeah, Good morning and all that. I'm Manuel. Now let's do this quickly so i can be done with it",
                    "No salutations or greetings or anything. Just drive forward and let's get on with it."]
        manuel_lights_inspection = {True: "Passed: Apparently you've escaped this one", False: "Failed: Disqualified on the first one! The state forces me to continue but if it were for me i would already kick you out of here."}
        manuel_gas_inspection = {True: "Passed: Congratulations, you are polluting the Earth a tiny bit less than the rest", False: "Failed: Wrong emission levels are what makes me happy."}
        #Bike specific:
        manuel_noise_inspection = {True: "Passed: Why do you ride a bike if it's not to make others deaf? Anyway, let's keep going", False: "Failed: Riding on a trumpet make you earn warnings."}
        #Car specific:
        manuel_seatbelt_inspection = {True: "Passed: Ok, apparently Darwin won't work it's magic if you have an accident with this car...", False: "Failed: Even i are not as crazy to drive in a car with faulty seatbelts"}
        manuel_windshield_wiper_inspection = {True: "Passed: Wipers are good. Let's go, two more to go", False: "Failed: A warning for not paying attention to your windshield"}
        manuel_transmission_inspection = {True: "Passed: Well, it seems your transmission works as intended. ", False: "Failed: Did you want to see your car on a tow truck? Well, this is how you do it."}
        manuel_airbag_inspection = {True: "Passed: I'm surprised the airbags are fine, i hoped your own head would do the same job", False: "Failed: As much as i would love to let you go, i'm afraid i'm forced to confiscate your car. Angry? Good, go yell at my boss" }
        inspectors.append(Inspector(manuel_name,manuel_greetings,manuel_lights_inspection,
                                    manuel_gas_inspection,manuel_noise_inspection,manuel_seatbelt_inspection,
                                    manuel_windshield_wiper_inspection,manuel_transmission_inspection,
                                    manuel_airbag_inspection                                    
                                    ))
        
        #Jose generation:
        #Common for all vehicles:
        jose_name = "Jose"
        jose_greetings = ["Good day to you. My name is Jose and i'll guide you trough this inspection",
                    "Hello there! I'm Jose, let's get this started",
                    "Good morning, my name is Jose and i'll be your nightmare today I'm jokin, i'm joking! Let's hope everything goes well"]
        jose_lights_inspection = {True: "Passed: These lights are as bright as the Sun!", False: "Failed: Oh, i'm sorry. There is something wrong with your lights. This disqualifies the vehicle but don't worry, let's finish it and then we'll see."}
        jose_gas_inspection = {True: "Passed: It seems the emission levels are acceptable, so on to the next one.", False: "Failed: I'm sorry but your car pollutes more than 5 smokers inside a bathroom. We'll continue, but this is not a good sign."}
        #Bike specific:
        jose_noise_inspection = {True: "Passed: You know? I usually don't like bikes because of the noise they make, but it seems i've found today one of the good ones.", False: "Failed: This is why i hate bikes. Does the helmet cover you from all that noise?"}
        #Car specific:
        jose_seatbelt_inspection = {True: "Passed: Everything's good on this end, nothing to complain about.", False: "Failed: Well if you wanted to have the true fast & furious experience, these seatbelts can definitely get you that."}
        jose_windshield_wiper_inspection = {True: "Passed: It seems your wipers work as intended", False: "Failed: I know you'll probably hate warnings but this windshield here forces me to give you one."}
        jose_transmission_inspection = {True: "Passed: Transmission is good... Ok, time for the last one! ", False: "Failed: I'm sorry but we'll need to call a tow truck after the inspection. Hey, at least you get to drive in a truck!"}
        jose_airbag_inspection = {True: "Passed: Airbag's good. Neat", False: "Failed: There is something wrong with these airbags and for your security i'm forced to confiscate your car. We'll call the tow truck, don't worry. " }
        inspectors.append(Inspector(jose_name,jose_greetings,jose_lights_inspection,
                                    jose_gas_inspection,jose_noise_inspection,jose_seatbelt_inspection,
                                    jose_windshield_wiper_inspection,jose_transmission_inspection,
                                    jose_airbag_inspection                                    
                                    ))
        return inspectors
    
    def inspection(self,vehicle):
        inspector = self.inspectors[random.randint(0,2)]

        #Preparing the greeting:
        random_greeting = random.randint(0,2)
        greeting = inspector.get_greetings()[random_greeting]
        print(greeting)
        self.__pass_time()

        #Preparing the inspection:
        warnings = 0
        warnings_where = 'No warnings or disqualifications. The vehicle passes the inspection'
        disqualification = False

        #Beginning the inspection:
        
        #Lights inspection
        print("Checking lights...\n")
        self.__pass_time()
        confirmation = self.__lights_inspection(vehicle)
        if not confirmation:
            disqualification = True
            warnings_where = 'Disqualified for having faulty lights.\n'
        print(inspector.get_lights_inspection(confirmation))


        #Emissions inspection:
        print("\nChecking gas emissions...\n")
        self.__pass_time()
        confirmation = self.__gas_inspection(vehicle)
        if not confirmation:
            disqualification = True
            warnings_where = warnings_where + "Disqualified for having gas emissions above level\n"
        print(inspector.get_gas_inspection(confirmation))

        
        #checking if it's a car or a bike:
        if isinstance(vehicle, Bike):
            #Bike specific: 

            #Noise inspection:
            print("\nChecking noise levels...\n")
            self.__pass_time()
            confirmation = self.__noise_inspection(vehicle)
            if not confirmation:
                disqualification = True
                warnings_where = warnings_where +  f"Disqualified due to noise levels above 94 db. Bike noise levels: {vehicle.get_noise()} \n"
            print(inspector.get_noise_inspection(confirmation))
        elif isinstance(vehicle, Car):  
            #Car specific:

            #Seatbelt Inspection:
            print("\nChecking seatbelts...\n")
            self.__pass_time()
            confirmation = vehicle.get_seatbelts() == "Good"
            if not confirmation:
                disqualification = True
                warnings_where = warnings_where + " Disqualified after having bad seatbelt state.\n"
            print(inspector.get_seatbelt_inspection(confirmation))


            #Windshield wipers inspection:
            print("\nChecking wipers...\n")
            self.__pass_time()
            confirmation = vehicle.get_windshield_wipers() == "Good"
            if not confirmation:
                warnings += 1
                warnings_where = warnings_where + f"Warning for having {vehicle.get_windshield_wipers()} wipers\n"
            print(inspector.get_windshield_wiper_inspection(confirmation))


            #Transmission inspection
            print("\nChecking transmission...\n")
            self.__pass_time()
            confirmation = vehicle.get_transmission_quality() == "Good"
            if not confirmation:
                warnings_where = warnings_where + f"Disqualified for having {vehicle.get_transmission_quality()}"
            print(inspector.get_transmission_inspection(confirmation))


            #Airbag inspection:
            print("\nChecking airbags...\n")
            self.__pass_time()
            confirmation = vehicle.get_airbag_quality() == "Good"
            if not confirmation:
                warnings_where = warnings_where + "Airbag quality below acceptable levels"
            print(inspector.get_airbag_inspection(confirmation))
            time.sleep(2)
            
            #Printing the results:
            print("\nNow, wait until we get your results.\n")
            time.sleep(2)
            self.__report(vehicle, warnings_where)
    
    def __report(self,vehicle,results):
        print (
            f"\nVehicle data: {vehicle.to_string() + "\n\n"}"
            f"Test performed in {self.address} on {self.location} on the day {self.date.strftime("%d/%m/%Y")}\n"
            f"Results for the vehicle  {vehicle.get_license_plate()} with owner's ID: {vehicle.get_owner_id()}\n"
            f"{results}"
        )

    def __noise_inspection(self,vehicle):
        noise = vehicle.get_noise()
        return noise < 94

    def __lights_inspection(self,vehicle):
        lights = vehicle.get_lights()
        front_lights = lights.get("Front") == "Good"
        rear_lights = lights.get("Rear") == "Good"
        return front_lights and rear_lights

    def __gas_inspection(self,vehicle):
        emissions = vehicle.get_gas_emissions()
        return emissions.get("CO") < 0.5 and emissions.get("HC") < 0.10 and emissions.get("NOx") < 0.06

    def __pass_time(self):
        time.sleep(random.randint(3,8))
    