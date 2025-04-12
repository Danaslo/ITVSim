from Car import Car
from Bike import Bike
from Inspection import Inspection

if __name__ == "__main__":
    try:
        inspection = Inspection("Calle Lagartija Nº 9","Chipiona de la Frontera")
        car1 = Car("1958 HFX",4,"98789789A",10,{"Front": "Good", "Rear": "Good"},{"CO":0.45,"HC":0.03,"NOx":0.03},"Good","Good","Good","Good")
        car2 = Car("1958 HFX",4,"98789789A",10,{"Front": "Faulty", "Rear": "Good"},{"CO":0.6,"HC":0.03,"NOx":0.03},"Good","Broken","Good","Good")
        bike1 = Bike("1958 HFX",2,"98789789A",10,{"Front": "Faulty", "Rear": "Good"},{"CO":0.6,"HC":0.03,"NOx":0.03},50,False,"Sport",90)
        inspection.inspection(car2)

    except ValueError as ve:
        print(ve)
    
   