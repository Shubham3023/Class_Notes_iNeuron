

#single inheritance

class car:

    def __init__(self, body, distance, fuel_con, time):
        self.body = body
        self.distance = distance
        self.fuel_con = fuel_con
        self.time = time

    def mileage(self):
        return "milage of car is: {} KM per Litre.".format(round((self.distance/self.fuel_con),2))

    def avg_speed(self):
        return "Average speed of car is: {} KM per Hr.".format(round((self.distance/self.time),2))

c1 = car("aluminium", 1000,50,15)

print("for car class: ",c1.mileage())
print("for car class: ",c1.avg_speed())

class tata(car) :
    pass

t1 = tata("HSS", 2000,80,18)

print("for tata class: ",t1.mileage())
print("for tata class: ",t1.avg_speed())
