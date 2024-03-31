import pulp

class Vehicle:
    def __init__(self, refrigeratedSpace, nonRefrigeratedSpace, fuelConsumption) -> None:
        self.refrigeratedSpace = refrigeratedSpace
        self.nonRefrigeratedSpace = nonRefrigeratedSpace
        self.fuelConsumption = fuelConsumption

if __name__ == "__main__":
    VehicleA = Vehicle(36, 12, 1200)
    VehicleB = Vehicle(12, 24, 480)

    #DEFINE PROBLEM
    minimumFuelUsage = pulp.LpProblem("Minimum Fuel Usage") # pulp.const.LpMinimize is set by default

    #DEFINE VARIABLES
    vehicle_A_Travels = pulp.LpVariable("Vehicle A Travels", lowBound = 0, cat = "Integer")
    vehicle_B_Travels = pulp.LpVariable("Vehicle B Travels", lowBound = 0, cat = "Integer")

    #DEFINE OBJECTIVE
    minimumFuelUsage += ((vehicle_A_Travels * VehicleA.fuelConsumption) + (vehicle_B_Travels * VehicleB.fuelConsumption))

    #DEFINE CONSTRAINTS
    minimumFuelUsage += ((vehicle_A_Travels * VehicleA.refrigeratedSpace) + (vehicle_B_Travels * VehicleB.refrigeratedSpace)) >= 1800
    minimumFuelUsage += ((vehicle_A_Travels * VehicleA.nonRefrigeratedSpace) + (vehicle_B_Travels * VehicleB.nonRefrigeratedSpace)) >= 1200

    #SOLVE PROBLEM
    status = minimumFuelUsage.solve()
    
    if(status == 1):
        fuelUsed = (vehicle_A_Travels.varValue * VehicleA.fuelConsumption) + (vehicle_B_Travels.varValue * VehicleB.fuelConsumption)
        refAreaCovered = (vehicle_A_Travels.varValue * VehicleA.refrigeratedSpace) + (vehicle_B_Travels.varValue * VehicleB.refrigeratedSpace)
        nonRefAreaCovered = (vehicle_A_Travels.varValue * VehicleA.nonRefrigeratedSpace) + (vehicle_B_Travels.varValue * VehicleB.nonRefrigeratedSpace)

        print("RESULTS")
        print("Vehicle A Travels: %d" % vehicle_A_Travels.varValue)
        print("Vehicle B Travels: %d" % vehicle_B_Travels.varValue)
        print("Total Refrigerated Space Avaliable: %d" % refAreaCovered)
        print("Total Non Refrigerated Space Avaliable: %d" % nonRefAreaCovered)
        print("Fuel Used: %d liters\n\n" % fuelUsed)

    else:
        print("Optimal Result not found")
        print("Status: %d\n\n" % status)