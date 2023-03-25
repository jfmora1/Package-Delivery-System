# Author: Jose Mora

import datetime
import time
from algorithm import get_distance_total, get_hash_map, get_my_dict

# Function that returns all package information when called and takes in package id and statuses
def print_package_info(packageId, status1, status2, number):
    if number == 1:
        print('\nPackage id: ' + str(get_hash_map().get(int(packageId))[0]) + '\nStreet address: ' +
              get_my_dict().get(get_hash_map().get(int(packageId))[1]) + ' ' + get_hash_map().get(int(packageId))[2] +
              ' ' + get_hash_map().get(int(packageId))[3] + ' ' + get_hash_map().get(int(packageId))[4] +
              '\nRequired delivery time: ' + get_hash_map().get(int(packageId))[
                  5] + '\nPackage weight: ' + get_hash_map().get(int(packageId))[6] + '\nTruck Status: ' +
              status1 + '\nDelivery Status: ' + status2)
    if number == 2:
        print('\nPackage id: ' + str(get_hash_map().get(packageId)[0]) + '\nStreet address: ' +
              get_my_dict().get(get_hash_map().get(int(packageId))[1]) + ' ' + get_hash_map().get(int(packageId))[2] +
              ' ' + get_hash_map().get(int(packageId))[3] + ' ' + get_hash_map().get(int(packageId))[4] +
              '\nRequired delivery time: ' + get_hash_map().get(packageId)[
                  5] + '\nPackage weight: ' + get_hash_map().get(packageId)[
                  6] + '\nTruck Status: ' +
              status1 + '\nDelivery Status: ' + status2)
    if number == 3:
        print('ID: ' + str(get_hash_map().get(packageId)[0]) + ' ' + get_hash_map().get(packageId)[6] +
              ' Truck Status: ' + status1 + ' Delivery Status: ' + status2)

# Start of main class
class main:
    # Main display message for when the program is first ran
    print('\nWELCOME TO THE WGUPS ROUTING PROGRAM\n')
    user_input = ''

    # While loop to determine user menu selection and keep program running until user terminates
    while user_input != '4':

        # Selection menu for user input
        print(
            '\nPlease enter the number corresponding to your selection:\n 1. Total mileage of trucks \n 2. Information '
            'of a specific package\n 3. Information of all packages\n 4. Quit program')
        user_input = input('Enter selection here: ')

        # Gets mileage of all trucks and displays to user
        if user_input == '1':
            print('\n The total mileage of all trucks is: {:0.2f}\n'.format(get_distance_total()))
            time.sleep(3)

        # Gets info for one package at a specific time
        elif user_input == '2':
            try:
                packageId = input('Enter a package ID: ')
                package_deliver_time = get_hash_map().get(int(packageId))[8]
                package_location = get_hash_map().get(int(packageId))[10]
                user_input_time = input('Please enter a time (HH:MM:SS): ')
                (hr, min, sec) = user_input_time.split(':')
                user_time = datetime.timedelta(hours=int(hr), minutes=int(min), seconds=int(sec))
                (hr, min, sec) = package_deliver_time.split(':')
                start_time = datetime.timedelta(hours=int(hr), minutes=int(min), seconds=int(sec))
                (hr, min, sec) = package_location.split(':')
                deliver_time = datetime.timedelta(hours=int(hr), minutes=int(min), seconds=int(sec))

                if start_time >= user_time:
                    status1 = 'At hub'
                    status2 = 'Package ' + packageId + ' leaves at ' + package_deliver_time
                    print_package_info(packageId, status1, status2, 1)

                elif start_time <= user_time:
                    if user_time < deliver_time:
                        status1 = 'Package in transit'
                        status2 = 'Package ' + packageId + ' left at ' + package_deliver_time
                        print_package_info(packageId, status1, status2, 1)

                    else:
                        status1 = 'Package delivered at ' + package_location
                        status2 = 'Package ' + packageId + ' left at ' + package_deliver_time
                        print_package_info(packageId, status1, status2, 1)

            except ValueError:
                print('Invalid package ID, try again')

        # Gets info for all packages at a specific time specified by the user input
        elif user_input == '3':
            try:
                user_input_time = input('Please enter a time (HH:MM:SS): ')
                (hr, min, sec) = user_input_time.split(':')
                user_time = datetime.timedelta(hours=int(hr), minutes=int(min), seconds=int(sec))

                for packageId in range(1, 41):
                    package_deliver_time = get_hash_map().get(packageId)[8]
                    package_location = get_hash_map().get(packageId)[10]
                    (hr, min, sec) = package_deliver_time.split(':')
                    start_time = datetime.timedelta(hours=int(hr), minutes=int(min), seconds=int(sec))
                    (hr, min, sec) = package_location.split(':')
                    deliver_time = datetime.timedelta(hours=int(hr), minutes=int(min), seconds=int(sec))

                    if start_time >= user_time:
                        status1 = 'At hub'
                        status2 = 'Package ' + str(packageId) + ' leaves at ' + package_deliver_time
                        print_package_info(packageId, status1, status2, 2)

                    elif start_time <= user_time:
                        if user_time < deliver_time:
                            status1 = 'Package in transit'
                            status2 = 'Package ' + str(packageId) + ' left at ' + package_deliver_time
                            print_package_info(packageId, status1, status2, 2)

                        else:
                            status1 = 'Package delivered at ' + package_location
                            status2 = 'Package ' + str(packageId) + ' left at ' + package_deliver_time
                            print_package_info(packageId, status1, status2, 2)

            except ValueError:
                print('Invalid package ID, try again')

        elif user_input == 'screenshot':
            user_input_time = input('Please enter a time (HH:MM:SS): ')
            (hr, min, sec) = user_input_time.split(':')
            user_time = datetime.timedelta(hours=int(hr), minutes=int(min), seconds=int(sec))

            for packageId in range(1, 41):
                package_deliver_time = get_hash_map().get(packageId)[8]
                package_location = get_hash_map().get(packageId)[10]
                (hr, min, sec) = package_deliver_time.split(':')
                start_time = datetime.timedelta(hours=int(hr), minutes=int(min), seconds=int(sec))
                (hr, min, sec) = package_location.split(':')
                deliver_time = datetime.timedelta(hours=int(hr), minutes=int(min), seconds=int(sec))

                if start_time >= user_time:
                    status1 = 'At hub'
                    status2 = 'Package ' + str(packageId) + ' leaves at ' + package_deliver_time
                    print_package_info(packageId, status1, status2, 3)

                elif start_time <= user_time:
                    if user_time < deliver_time:
                        status1 = 'Package in transit'
                        status2 = 'Package ' + str(packageId) + ' left at ' + package_deliver_time
                        print_package_info(packageId, status1, status2, 3)

                    else:
                        status1 = 'Package delivered at ' + package_location
                        status2 = 'Package ' + str(packageId) + ' left at ' + package_deliver_time
                        print_package_info(packageId, status1, status2, 3)

        # Closes program if user input is a 4
        elif user_input == '4':
            print('\nCLOSING WGUPS ROUTING PROGRAM, GOODBYE!\n')

        # If user input is invalid, error prints
        else:
            print('\nINVALID SELECTION ENTRY, PLEASE TRY AGAIN\n')
            time.sleep(2)
