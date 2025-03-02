class Vehicle:

    def __init__ (self, name , max_speed ,  mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus (Vehicle):
    pass

school_bus = Bus('School Volvo', 18, 12)
print('vehicle Name : ', school_bus.name , 'vehicle max speed : ',
      school_bus.max_speed, 'Bus mileage = ', school_bus.mileage)
