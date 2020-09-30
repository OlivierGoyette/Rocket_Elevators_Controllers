#-----------------------Summary-------------------------------#
#
#   1- Variables
#   2- Residential Controller
#   3- Columns
#   4- 
#   5-
#   6-
#   7-  
#
#-----------------------Variables-------------------------------#
numberOfColumns = '1'
numberOfFloors = 10
numberOfElevator = 2
waitingTime = '7 seconds'
maxWeight = '1200 kg'

#-----------------------Residential Controller-------------------------------#

class ResiCont:
    def __init__(self, numberOfColumns, numberOfFloors, numberOfElevator):
        print("Controller Constructor")
        self.numberOfColumns = numberOfColumns
        self.numberOfFloors = numberOfFloors
        self.numberOfElevator = numberOfElevator
        self.column = Columns(numberOfElevator, numberOfFloors) 

    def get_Columns(self):
        return self.numberOfColumns
        print(numberOfColumns)

    def get_Floors(self):
        return self.numberOfFloors
        print(numberOfFloors)

    def get_Elevator(self):
        return self.numberOfElevator
        print(numberOfElevator)

#-----------------------Columns-------------------------------#

class Columns:
    def __init__(self, numberOfElevator, numberOfFloors):
        self.numberOfElevator = numberOfElevator
        self.numberOfFloors = numberOfFloors
        self.elevatorsList = []
        self.callbuttonDown = []
        self.callbuttonUp = []
        self.status = 'on'
        self.createElevatorsList(numberOfElevator)


    def createElevatorsList(self, numberOfElevator):
        print('test')
        for x in range(numberOfElevator):
            newElevator = Elevator()
            self.elevatorsList.append(elevator)
            TEMPID +=1

    def createButtonUpList(self, numberOfFloors):
        print('test2')
        for x in range(numberOfFloors):
            if TEMPID != minFloors():
                self.callbuttonUp.append
            TEMPID +=1

    def createButtonDownList(self, numberOfFloors):
        print('test3')
        for x in range(numberOfFloors):
            if TEMPID > minFloors():
                self.callbuttonDown.append
            TEMPID +=1

    def FindBestElevator(self, currentFloor, currentDirection, elevatorsList):
        ActiveElevatorList = []
        IdleElevatorList = []
        for x in range(numberOfElevator in elevatorsList):
            if (numberOfElevator != status.IDLE and numberOfElevator < currentDirection):
                if (numberOfElevator.status is "UP" and numberOfFloors < currentFloor or numberOfElevator.status is "DOWN" and numberOfElevator > currentFloor):
                self.numberOfElevator.append(ActiveElevatorList)


        if(ActiveElevatorList != [])
        print('list empty!')
            
 



#class Elevator
#    def ElevatorObj(self, numberOfFloors, floors):



#-- TESTS SECTION
#controller = ResiCont(numberOfColumns, numberOfFloors, numberOfElevator)
#print(controller.column)
#print(controller.column.elevatorsList)



#-----------------------Weight Limit-------------------------------#


#if weight < maxWeight
#    get_Elevator=on
#if weight > maxWeight
#    elevatoroff