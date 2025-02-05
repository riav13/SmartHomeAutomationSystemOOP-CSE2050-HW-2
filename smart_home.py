
#GOAL
#The goal of this assignment is to design a simple smart home automation system using objectoriented programming concepts in Python. 
# You will model different smart home devices (lights, thermostats, and speakers) using classes, and allow them to interact with each 
# other through composition and inheritance. 
# You will also implement magic methods (and operator overloading) 
# to simulate a realistic smart home system.

#PART 1:  BASIC CLASS DESIGN SmartDevice Class (Base Class)
#name (string): The name of the device (e.g., “Living Room Light”). 
# • status (boolean): The on/off status of the device (True = on, False = off).
#  Default status should be False.

#class ia a blueprint, referring to an attribute you are running it on self , placeholder, whatever object ,generic word for whatever instance we are talking about 
class SmartDevice: #BaseClass
    def __init__(self, name): # 2 attributes: name and status #__ means magic method
        #self is a reference to smrtdevice and need it everywhere
        self.name = name # intializes the device with a given name
        self.status = False # sets the status to false and users cannot change it 
    """
    This function initializes our smart device with a given name, and later on this will be used in the child classes.
    """
    
    def turn_on(self): #connected to initialize 
        self.status = True # turns the device on by setting the status attribute to True
    """
    This function turns the device on by setting the status attribute to True.
    """
    
    def turn_off(self): #method of your class
        self.status = False # turns the device off by setting the status attribute to False
    """
    This function turns off the device by setting the status attribute to False.
    """
    
    def __str__(self):
        # True = On, False = Off
        #A string that includes the device name and its current status (i.e.,
        #“Living Room Light: ON” or “Living Room Light: OFF”
        if self.status == True:
            return f"{self.name}: ON"
        else:
            return f"{self.name}: OFF"
    """
    This function is a string function which returns the device name and its current status by setting its status to On if the boolean is true and vice versa. 

    """
    
        
# 2 underscores magic method, part of python (init,str)
# 1 underscore private 
        
#PART 2: Light Class which Inherits traits from SmartDevice
class Light(SmartDevice): 
    def __init__(self,name): #initializer method, add the same parameters from the parent class
        super().__init__(name) #**HERE IS WHERE WE USE SUPER.() INIT - why does it need name in it? do we even need a init method
        self.brightness = 100 #automatically be 100, not a user input that they can change so we dont put it in ()
    """
    This is the initalizer function which just initializes the Light object and we called the intializer from the super class because we want it to inherit the same functions from it. We set the brightness equal to a default value, not an input.
    """
    
    def adjust_brightness(self,level): #level is an input
        if level >= 1 and level <= 100:
            self.brightness = level
    """
    This function adjusts the brightness by only changing it to the user input level if it is between 1 and 100.
    """
       
    
    def __str__(self): #inputs: none
        a = super().__str__(self,self.brightness) #do we need brightness in here?
        return f"({a}, 'Brightness:' {self.brightness})"
    """
    This string function outputs the Brightness of the light and the status of the light.
    """
    

class Thermostat(SmartDevice):#inhertiing from SmartDevice
    def __init__(self,name):
        super().__init__(name)
        self.temperature = 65.0 #default temperature, user cannot change so its not a parameter in ()
    """
    This is the initalizer function which just initializes the Thermostat object and we called the intializer from the super class because we want it to inherit the same functions from it. We set the temperature equal to a default value, not an input.
    """
    
    def adjust_temperature(self,temp): # inputs are temp
        if Thermostat._check_temperature_limits(self,temp) == True: #uses helper method _check_temperature_limits
            self.temperature = temp
    """
    This is the adjust temperature function which uses the helper method _check_temperature_limits to check if the temperature is within 55 and 80. If it is, we change the temperature to the user input.
    """
     
    def _check_temperature_limits(self,temp): #defined a new private internal method in this class 
        if temp >= 55 and temp<=80:
            return True
        else:
            return False
    """
    This is the helper function which checks if the temperature is within the limits of 55 and 80. If it is, it returns True, if not, it returns False.
    """

    
    def __str__(self):
        b = super().__str__(self,self.temperature)
        return f"({b}, 'Temperature:' {self.temperature})"
    """
    This string function outputs the Temperature of the thermostat and the status of the thermostat.
    """
    
class Speaker(SmartDevice):
    def __init__(self,name):
        super().__init__(name)
        self.volume = 3 #default temperature should be 3
    """
    This is the initalizer method which just initializes the Speaker object and we called the intializer from the super class because we want it to inherit the same functions from it. We set the volume equal to a default value, not an input.
    """

    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1

    """
    This function increases the volume by 1 if the volume is less than 10.
    """

    def decrease_volume(self):
        if self.volume > 1:
            self.volume -= 1
    """
    This function decreases the volume by 1 if the volume is greater than 1.
    """

    def __str__(self):
        c = super().__str__(self,self.volume)
        return f"({c}, 'Volume:' {self.volume})"
    """
    This string function outputs the Volume of the speaker and the status of the speaker.
    """
    


class SmartHome():
    def __init__(self):# adds more than needed
        self.devices = []
    """
    This is the initalizer method which initializes the SmartHome object and creates an empty list of devices."""

    def __add__(self,other):
        if isinstance(other,SmartDevice): #have to return statement checks if objects are of type smart device
            self.devices.append(other)
        
        return self
    """
    This function adds a device to the list of devices if the object is of type SmartDevice.
    """


    def turn_off_all(self):
        for i in self.devices:
            i.turn_off()
    """This function turns off all the devices in the list of devices.
    """
    
    
    def __str__(self):
        for i in self.devices: 
            d = super().__str__(self)
            return f"({d})"
    """
    This string function outputs the status of all the devices in the list of devices.
    """



    

    




    
    




    






    
        
    

    
