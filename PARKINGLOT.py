#PARKINGLOT

class Vehicle:
    def __init__(self, licensePlate, color):
        self.licensePlate = licensePlate
        self.color = color
        

    def get_licensePlate(self):
        return self.licensePlate

    def set_licensePlate(self, licensePlate):
        self.licensePlate = licensePlate

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

        

class Car(Vehicle):
    
    def __init__(self, licensePlate, color):
        self.licensePlate = licensePlate
        self.color = color
        self.size = 2


class Bike(Vehicle):
    def __init__(self, licensePlate, color):
        self.licensePlate = licensePlate
        self.color = color
        self.size = 1


class Bus(Vehicle):
    def __init__(self, licensePlate, color):
        self.licensePlate = licensePlate
        self.color = color
        self.size = 3

# class parkingSpots:
#     def __init__(self, type):       
#         self.type = type
#         self.vehicle = None

#     def isAvailable(self):
#         return self.vehicle == None

#     def park(self, vehicle):
#         if self.vehicle:
#             pass
#         else:
#             if vehicle.get_Type() != self.type:
#                 pass
#             else:
#                 self.vehicle = vehicle

#     def removeVehicle(self):
#         self.vehicle = None
#         return self.vehicle

#     def getVehicle(self):
#         return self.vehicle




class ParkingLot:
    def __init__(self, size):
        self.max_parking_size = size
        self.current_size = self.max_parking_size
        self.parked_vehicles = []


    def parkVehicle(self , vehicle):
        if self.current_size < vehicle.size:
            print('too full')
        else:
            self.parked_vehicles.append(vehicle)
            self.current_size = self.current_size - vehicle.size

    def leave(self,vehicle):

        index_to_remove = self.find_vehicle(vehicle.licensePlate)
        if index_to_remove == -1:
            print('Car with plate # not found here')
        else:
            self.parked_vehicles.pop(index_to_remove)

            self.current_size = self.current_size + vehicle.size
        
    def find_vehicle(self, licensePlate):
        if len(self.parked_vehicles) == 0:
            print('no parked vehicles')

        else:
            for i in self.parked_vehicles:
                if licensePlate == i.licensePlate:
                    return self.parked_vehicles.index(i)       

            return -1



total = ParkingLot(10)
Car1 = Car('gavdaddy','black')
print(Car1)
print(Car1.color)

Car1 = ParkingLot.parkVehicle('gavdaddy')
print(ParkingLot.current_size)