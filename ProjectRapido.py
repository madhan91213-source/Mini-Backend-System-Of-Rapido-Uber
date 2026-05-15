print("RideEase!!!")
print("Ride Smarter, Ride Faster :)")
class User():
    def __init__(self):
        self.user_id=input("Enter Your UserId:")
        self.user_name=input("Enter YourName:")
        self.user_location=input("Enter Your Location:")

    def display_user_info(self):
        print("--------------------------------------------")
        print("User Information:")
        print("User ID:", self.user_id)
        print("User Name:", self.user_name)
        print( "User Location:", self.user_location)
        print("--------------------------------------------")
    

user=User() 
user.display_user_info()     
choice=input("Enter the Vehicle Type (CAR/BIKE/AUTO):").upper()
if choice=="CAR":
    print("You have selected Car")
elif choice=="BIKE":
    print("You have selected Bike")
elif choice=="AUTO":
    print("You have selected Auto")
else:
    print("Invalid Vehicle Type")
print("--------------------------------------------")

class  RideManager():
    def __init__(self):
        self.drivers={}
    def add_driver(self,driver_name,vehicle_type):
        self.drivers[driver_name]=vehicle_type
    def find_driver(self):
        if choice in self.drivers.values():
            print("Driver is Available")
            driver_name=list(self.drivers.keys())[list(self.drivers.values()).index(choice)]
            print("Driver Name:", driver_name)
            print("Vehicle Type:", choice)
        else:            
            print("Driver is Not Available")
RideMemory=RideManager()
RideMemory.add_driver("Mani","CAR")
RideMemory.add_driver("Lakshman","BIKE")
RideMemory.add_driver("Pradeep","AUTO")
class Driver(RideManager):
    def __init__(self,rating,no_of_rides):
        self.rating=rating
        self.no_of_rides=no_of_rides
    def display_driver_info(self):
        if choice in RideMemory.drivers.values():
            RideMemory.find_driver()
            print("Rating:", self.rating)
            print("Number of Rides:", self.no_of_rides)
    def update_rides(self):
        if choice in RideMemory.drivers.values():
            self.no_of_rides=self.no_of_rides+1
objDriver=Driver(4.5,100)
objDriver.display_driver_info()
print("--------------------------------------------")

 
class Ride():
    def __init__(self,distance,status):
        self.distance=distance
        self.status=status
    def display_ride_info(self):
        if choice in RideMemory.drivers.values():
            print("Ride Information:")
            print("Distance:", self.distance,"KM")
            print("Status:", self.status)
    def complete_ride(self):
        if choice in RideMemory.drivers.values():
            print("Ride Information:")
            self.status="COMPLETED"
            print("Ride Completed")
            objDriver.update_rides()
            print("Number of Rides:",objDriver.no_of_rides)
    def cancel_ride(self):
        if choice in RideMemory.drivers.values():
            print("Ride Information:")
            self.status="CANCELLED"
            print("Ride Cancelled")
objRide=Ride(40,"ONGOING")
objRide.display_ride_info()
print("--------------------------------------------")

class Fare():
    def __init__(self):
        self.Total_amount_payable=0
    def calculate_fare(self):
        if choice=="BIKE" and objRide.status=="COMPLETED":
            self.Total_amount_payable=12*objRide.distance
            print("Total Amount Payable:", self.Total_amount_payable)
        elif choice=="CAR" and objRide.status=="COMPLETED":
            self.Total_amount_payable=20*objRide.distance      
            print("Total Amount Payable:", self.Total_amount_payable) 
        elif choice=="AUTO" and objRide.status=="COMPLETED":
            self.Total_amount_payable=15*objRide.distance   
            print("Total Amount Payable:", self.Total_amount_payable)
objFare=Fare()
objFare.calculate_fare()



