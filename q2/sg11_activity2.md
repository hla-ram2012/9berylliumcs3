# Polymorphism - *Activity 2*
## Number 1:
### What is duck typing, as explained in the video?

According to the video, duck typing is a programming concept in Python used to achieve polymorphism without relying on inheritance.

### What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?

The car class need to have the same method name and parameters so that it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class.

## Number 2:
### Python Code:

![Python Code](9berylliumcs3/q2/sg11_activity2.py)
```python
class Car(): #Creates a class that represents a car
    def start_trip(self, vehicle): #Creates a method that indicates the start trip of the car
        vehicle.move() #Calls another one of its function move() to indicate the start trip of the car
    def move(self): #Creates a method that indicates the car is driving on a road
        print("The car drives on the road.") #Prints the indication of the car driving on the road - Output: The car drives on the road.

class Boat(): #Creates a class that represents a boat
    def start_trip(self, vehicle): #Creates a method that indicates the start trip of the boat
        vehicle.move() #Calls another one of it function move() to indicate the start trip of the boat
    def move(self): #Creates a method that indicates the boat is sailing on water
        print(f"The boat sails on water.") #Prints the indication of the boat sailing on water - Output: The boat sails on water.

class Drone(): #Creates a class that represents a drone
    def start_trip(self, vehicle): #Creates a method that indicates the start trip of the boat
        vehicle.move() #Calls another one of it function move() to indicate the start trip of the drone
    def move(self): #Creates a method that indicates the drone flying in the sky
        print(f"The drone flies in the sky.") #Prints the indication of the drone flying in the sky - Output: The drone flies in the sky.

Vehicles = [Car(), Boat(), Drone()] #Creates a list of the classes so that the required output can be done by a loop

for vehicle in Vehicles: #Creates a loop for the output
    vehicle.start_trip(vehicle) #Outputs their respective move() output
```


## Number 3:
### How does the code in 2.2 demonstrate polymorphism?

The code in 2.2 represent polymorphism by having the same function and method that can behave differently but depends on the object it works with. Thus, different vehicles represents and outputs different move() method despite having the same function and method.
