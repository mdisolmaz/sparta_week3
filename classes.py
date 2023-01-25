class CAR:
    def __init__(self, color, style, door):
        self.color = color
        self.style = style
        self.door = door
        
    def check_km(self):
        name = input("please insert what type of car you want : 'Honda' , 'Toyota', 'Porsche' ? ")
        car_name = ["honda","toyota","porsche"]

        if name.lower() == "honda":
            print(name, "has 10 km on it")
            self.out_put(name)
        elif name.lower() == "toyota":
            print(name," has 25 km on it")
            self.out_put(name)
        elif name.lower() == "porsche":
            print(name," has 50 km on it :)")
            self.out_put(name)
        else:
            print("The input value is not correct")

    def out_put(self, name):
        print('the model of the car is ',name, 'the color of the car is ',self.color, 'it has ',self.style,'style and it has ',self.door)

vehicle = CAR("Silver","Sport","4 doors")
vehicle.check_km()

''' the example out put is ==> 

toyota  has 25 km on it
the model of the car is  toyota the color of the car is  Silver it has  Sport style and it has  4 doors  '''


##################################################################

class ElectricCar(CAR):
    def __init__(self, color, style, door):
        super().__init__(color, style, door) 
        self.battery_capacity = 100 # in kwh
        self.range = 0
        
    def check_km(self):
        name = input("please insert what type of Electric car you want : 'Tesla' , 'Nissan Leaf', 'BMW i3' ? ")
        if name.lower() == "tesla":
            self.range = 300
        elif name.lower() == "nissan leaf":
            self.range = 150
        elif name.lower() == "bmw i3":
            self.range = 200
        else:
            print("The input value is not correct")
        self.out_put(name)

    def out_put(self, name):
        print('the model of the car is ',name, 'the color of the car is ',self.color, 'it has ',self.style,'style and it has ',self.door)
        print('the battery capacity of the car is ',self.battery_capacity,' Kwh and this electric car only traveld',self.range,' Km')

vehicle = ElectricCar("Silver","Sport","4 door")
vehicle.check_km()


##########################################################################################
# class WINDOW(ElectricCar):

#     def __init__(self, color, style, door):
#         super().__init__(color, style, door)
#         self.win_tint = tint
#         self.win_thickness = thickness
#         self.win_material = material
#         self.win_handle = w_handle

        



