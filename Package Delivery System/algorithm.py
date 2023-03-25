import csv
import datetime

# LISTS OF TRUCKS INITIALIZED TO HOLD PACKAGE INFORMATION
first_truck = []
second_truck = []
third_truck = []

# LIST THAT HOLDS DELIVERY ROUTES AFTER INPUT INTO SHORTEST ROUTE ALGORITHM
first_delivery = []
second_delivery = []
third_delivery = []

# LIST THAT HOLDS TRUCKS ADDRESS ROUTES
first_truck_address_route = []
second_truck_address_route = []
third_truck_address_route = []

# HOLDS DISTANCE TOTAL FOR EACH TRUCK
first_distance_total = 0
second_distance_total = 0
third_distance_total = 0

# INITIALIZE LISTS THAT WILL HOLD ALL TIMES THE TRUCKS LEAVES DESTINATIONS
first_truck_times = ['8:00:00']
second_truck_times = ['9:05:00']
third_truck_times = ['10:20:00']

# Dictionary initialized to hold address and address index
my_dict = {}

# READ DISTANCE CSV FILES INTO LISTS
# TIME COMPLEXITY -> 0(1)
with open('Distance Table.csv') as csvfile:
    distance_csv = list(csv.reader(csvfile, delimiter=','))
with open('Distance names.csv') as csvfile2:
    distanceNames_csv = list(csv.reader(csvfile2, delimiter=','))


# Get distance from csv through row and column - 0(1)
def getDistance(row, col):
    distance = distance_csv[row][col]
    if distance == '':
        distance = distance_csv[col][row]
    return float(distance)


# Returns distance total from csv
# TIME COMPLEXITY -> 0(1)
def getDistanceTotal(row, col, total):
    distance = distance_csv[row][col]
    if distance == '':
        distance = distance_csv[col][row]
    return total + float(distance)


# Get address data from csv distance names - 0(N)
def checkAddress():
    return distanceNames_csv


# HashMap code was built and based from video with personal updates -> Python: Creating a HASHMAP using Lists by Joe
# James. 
class HashMap:
    def __init__(self):
        self.size = 40
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def update(self, key, value):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
        else:
            print('Error: could not update key: ' + key)

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

    def keys(self):
        arr = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                arr.append(self.map[i][0])
        return arr

    def print(self):
        print('---PACKAGES----')
        for item in self.map:
            if item is not None:
                print(str(item))


# INSTANCE OF HASHMAP
myHash = HashMap()


# Loads csv package file to parse and add into hashmap
# TIME COMPLEXITY -> 0(N²)
def loadPackageData(filename):
    with open(filename) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)  # SKIPS HEADER
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDelivery = package[5]
            pWeight = package[6]
            pNotes = package[7]
            delivery_start = ''
            address_location = ''
            pdelivery_status = 'At hub'

            # PACKAGE VALUES
            values = [pID, pAddress, pCity, pState, pZip, pDelivery, pWeight, pNotes, delivery_start,
                      address_location,
                      pdelivery_status]

            # CONSTRAINTS TO APPEND PACKAGES INTO CORRECT TRUCKS
            if pDelivery != 'EOD' or pID == 19:
                if 'Must' in pNotes or pNotes == '':
                    first_truck.append(values)

            if 'Can only be' in pNotes or 'Delayed' in pNotes:
                second_truck.append(values)

            if values not in first_truck and values not in second_truck:
                if len(third_truck) < len(second_truck):
                    third_truck.append(values)
                else:
                    second_truck.append(values)

            for f, value in enumerate(first_truck):  # SETS ALL FIRST TRUCK PACKAGES DELIVERY START TIMES
                first_truck[f][8] = '8:00:00'
            for j, value in enumerate(second_truck):  # SETS ALL SECOND TRUCK PACKAGES DELIVERY START TIMES
                second_truck[j][8] = '9:05:00'
            for k, value in enumerate(third_truck):  # SETS ALL THIRD TRUCK PACKAGES DELIVERY START TIMES
                third_truck[k][8] = '10:20:00'

            # INSERT INTO HASHMAP
            myHash.add(pID, values)


# LOAD PACKAGES FROM PACKAGE CSV FILE ONTO HASHMAP AND TRUCKS
loadPackageData('Package File.csv')

# LOOPS ADDRESSES AND TRUCK PACKAGES, CHANGES FIRST TRUCK PACKAGE ADDRESS TO ADDRESS INDEX
# TIME COMPLEXITY -> 0(N²)
try:
    count = 0
    for k in first_truck:
        for j in checkAddress():
            if k[1] in j[2]:
                my_dict[j[0]] = k[1]
                first_truck[count][1] = j[0]
                break
        count += 1
except IndexError:
    pass

# LOOPS ADDRESSES AND TRUCK PACKAGES, CHANGES SECOND TRUCK PACKAGE ADDRESS TO ADDRESS INDEX
# TIME COMPLEXITY -> 0(N²)
try:
    count = 0
    for k in second_truck:
        for j in checkAddress():
            if k[1] in j[2]:
                my_dict[j[0]] = k[1]
                second_truck[count][1] = j[0]
                break
        count += 1
except IndexError:
    pass

    # LOOPS ADDRESSES AND TRUCK PACKAGES, CHANGES THIRD TRUCK PACKAGE ADDRESS TO ADDRESS INDEX
    # TIME COMPLEXITY -> 0(N²)
try:
    count = 0
    for k in third_truck:
        for j in checkAddress():
            if k[1] in j[2]:
                my_dict[j[0]] = k[1]
                third_truck[count][1] = j[0]
                break
        count += 1
except IndexError:
    pass


# Greedy algorithm approach where the function takes the unsorted truck packages, the truck it is on, and the current
# location which always starts at the hub. The approach to this algorithm is to loop through the trucks packages
# and find the lowest value distance and update the minValue variable. After that depending on which truck it is,
# it will append that package to the delivery list and append the package address to an address route list
# Lastly it will remove the package from the truck list and update the current location to the location of the last
# package and recursively call itself until the truck list is empty.
# TIME COMPLEXITY -> 0(N²) DUE TO TWO FOR LOOPS
def getShortestRoute(truckList, truckNum, currentLocation):
    if not truckList:
        return truckList

    minValue = 40
    location = 0

    for package in truckList:
        value = int(package[1])
        if getDistance(currentLocation, value) <= minValue:
            minValue = getDistance(currentLocation, value)
            location = value

    for package in truckList:
        if getDistance(currentLocation, int(package[1])) == minValue:
            if truckNum == 1:
                first_delivery.append(package)
                first_truck_address_route.append(package[1])
                truckList.pop(truckList.index(package))
                currentLocation = location
                getShortestRoute(truckList, 1, currentLocation)
            elif truckNum == 2:
                second_delivery.append(package)
                second_truck_address_route.append(package[1])
                truckList.pop(truckList.index(package))
                currentLocation = location
                getShortestRoute(truckList, 2, currentLocation)
            elif truckNum == 3:
                third_delivery.append(package)
                third_truck_address_route.append(package[1])
                truckList.pop(truckList.index(package))
                currentLocation = location
                getShortestRoute(truckList, 3, currentLocation)


# Insert 0 for the first index of each list to represent starting at hub location
first_truck_address_route.insert(0, '0')
second_truck_address_route.insert(0, '0')
third_truck_address_route.insert(0, '0')


# Calculates distance total of truck - 0(N)
def truck_time(distance, truck_values):
    time = distance / 18
    time_minutes = '{0:02.0f}:{1:02.0f}'.format(
        *divmod(time * 60, 60))
    time_minutes = time_minutes + ':00'
    truck_values.append(time_minutes)
    total = datetime.timedelta()
    for value in truck_values:
        (hrs, mins, secs) = value.split(':')
        total += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
    return total


# CALLING ALGORITHM TO SORT PACKAGES INTO THE SHORTEST ROUTE
getShortestRoute(first_truck, 1, 0)
getShortestRoute(second_truck, 2, 0)
getShortestRoute(third_truck, 3, 0)


# Calculates distance total of a truck - 0(N)
def truck_time(distance, truck_values):
    time = distance / 18
    minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(time * 60, 60))
    minutes = minutes + ':00'
    truck_values.append(minutes)
    total = datetime.timedelta()
    for value in truck_values:
        (hrs, mins, secs) = value.split(':')
        total += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
    return total


# CALCULATE TOTAL DISTANCE FOR TRUCK 1 AND DISTANCES OF EACH PACKAGE
# TIME COMPLEXITY -> 0(N)
for i in range(len(first_truck_address_route)):
    try:
        first_distance_total = getDistanceTotal(int(first_truck_address_route[i]),
                                                int(first_truck_address_route[i + 1]), first_distance_total)
        delivery_status = truck_time(
            getDistance(int(first_truck_address_route[i]), int(first_truck_address_route[i + 1])), first_truck_times)
        first_delivery[i][10] = (str(delivery_status))
    except IndexError:
        pass

# CALCULATE TOTAL DISTANCE FOR TRUCK 2 AND DISTANCES OF EACH PACKAGE
# TIME COMPLEXITY -> 0(N)
for i in range(len(second_truck_address_route)):
    try:
        second_distance_total = getDistanceTotal(int(second_truck_address_route[i]),
                                                 int(second_truck_address_route[i + 1]), second_distance_total)
        delivery_status = truck_time(
            getDistance(int(second_truck_address_route[i]), int(second_truck_address_route[i + 1])), second_truck_times)
        second_delivery[i][10] = (str(delivery_status))
    except IndexError:
        pass

# CALCULATE TOTAL DISTANCE FOR TRUCK 3 AND DISTANCES OF EACH PACKAGE
# TIME COMPLEXITY -> 0(N)
for i in range(len(third_truck_address_route)):
    try:
        third_distance_total = getDistanceTotal(int(third_truck_address_route[i]),
                                                int(third_truck_address_route[i + 1]), third_distance_total)
        delivery_status = truck_time(
            getDistance(int(third_truck_address_route[i]), int(third_truck_address_route[i + 1])), third_truck_times)
        third_delivery[i][10] = (str(delivery_status))
    except IndexError:
        pass

# Function that returns distance total of all trucks
def get_distance_total():
    return first_distance_total + second_distance_total + third_distance_total

# Function that returns hashmap: myHash
def get_hash_map():
    return myHash

# Function that returns dictionary: my_dict
def get_my_dict():
    return my_dict
