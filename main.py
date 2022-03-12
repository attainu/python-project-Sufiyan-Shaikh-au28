from sys import exit
import math

class trip:
  
    name = "" ; num = 0 ; pickup = "" ; drop = ""

    nam ="" ; nu = 0 ; cos = ""

    x1=0 ; x2=0 ; y1=0 ; y2=0

    available = "" ; distance = 0


    def riderInformation():
        
        trip.name = input("\nEnter Rider Name : ")
        
        trip.num = int(input("\nEnter Mobile Mumber : "))
        
        trip.pickup = input("\nPickup Address : ")
            
        trip.drop = input("\nDropping Address : ")

    
    def driverInformation():
        trip.nam = input("\nEnter Driver Name : ")
        
        trip.nu = int(input("\nEnter Mobile Number : "))

        trip.cos = "20 RS Per Kilometer"


    def driverOnOff():

        trip.available = input("\nis Driver Available Enter( yes / no ) : ")  


    def cabBook():

        if trip.available == "yes":
            print("\nCab booked for the Ride")    
            
            trip.x1 = int(input("\nEnter Location of Rider (x1 coordinate) : "))

            trip.y1 = int(input("\nEnter Location of Rider (y1 coordinate) : "))
        
        else:
            print("Cab is Not Available")
        

    def updateCabLocation():
        
        if trip.available == "yes":
            print("\nCab is Availabel")

            trip.x2 = int(input("\nEnter Location of Cab (x2 coordinate) : "))

            trip.y2 = int(input("\nEnter Location of Cab (y2 coordinate) : "))

        else :
            print("\nCab is Not Available")


    def _distance():

            trip.distance = math.sqrt((trip.x1-trip.x2)**2 + (trip.y1-trip.y2)**2)

            print("\nDistance between Rider and cab  is : ",trip.distance)

    
    def display():
    
     if trip.available == "yes":
        print("\nRider Name : ",trip.name)

        print("\nmobile Number : ",trip.num)

        print("\npickup Address : ",trip.pickup)

        print("\ndropping Address : ",trip.drop)

        print("\nDriver Name : ",trip.nam)

        print("\nRider Number : ",trip.nu)

        print("\nFair : ",trip.cos)


    def end():
        print("End of Trip")
        exit()


   


if __name__ == '__main__':
    tr= trip
    

    while True:

        print("\n1. Register Rider Detail")
        print("\n2. Register Driver Detail")
        print("\n3. driver On Off function")
        print("\n4. Rider Book A Cab")
        print("\n5. Update cab Location")
        print("\n6. calculate Distance between Rider and Cab")
        print("\n7. Information about Trip")
        print("\n8. End The Trip")

        choice =int(input("\nselect choice from above : "))

        if choice == 1:
            tr.riderInformation()

        elif choice == 2:
            tr.driverInformation()

        elif choice == 3:
            tr.driverOnOff()
        
        elif choice == 4:
            tr.cabBook()

        elif choice == 5:
            tr.updateCabLocation()
        
        elif choice == 6:
            tr._distance()

        elif choice == 7:
            tr.display()

        elif choice == 8:
            tr.end()
