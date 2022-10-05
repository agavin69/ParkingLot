#PARKINGLOT



class Vehicle():
    pass


    def __init__(self, licensePlate, color, vechicleType ):
        self.licensePlate = licensePlate
        self.color = color
        self.vehicleType = vechicleType


    def getType(self):
        return self.vehicleType

class Car(Vehicle):
    def __init__(self, licensePlate, color):
        self.licensePlate = licensePlate
        self.color = color

class Bike(Vehicle):
    def __init__(self, licensePlate, color):
        self.licensePlate = licensePlate
        self.color = color

class Bus(Vehicle):
    def __init__(self, licensePlate, color):
        self.licensePlate = licensePlate
        self.color = color

class Spots():
    def __init__(self, row , spotNumber, vehicleType):
        self.vehicle = None
        self.row = row
        self.spotNumber = spotNumber 
        self.vehicleType = vehicleType

    def isAvailable(self):
        return self.vehicle == None

    def park(self, vehicle):
        if vehicle.vehicleType == self.vehicleType:
            self.vehicle = vehicle

    def removeVehicle(self):
        self.vehicle = None
        return self.vehicle

    def getVehicle(self):
        return self.vehicle

class Levels:
    def __init__(self, floorNumber, spots_per_row):
        self.floorNumber = floorNumber
        self.spots_per_row = spots_per_row
        self.number_spots = 0
        self.availableSpots = []



class ParkingLot():
    def __init__(self, number_of_Levels , rows , numberSlots):
        self.levels =[]
        self.number_of_Levels = number_of_Levels
        self.rows = rows
        self.numberSlots = numberSlots

        for i in range(number_of_Levels):
            self.levels.append(Levels(i, rows , numberSlots))

    def parkVehicle(self , vehicle):
        for level in self.levels:
            if level.parkVehicle(vehicle):
                return True
            return False

    def leave(self,vehicle):
        for level in self.levels:
            if level.remove(vehicle):
                return True

            