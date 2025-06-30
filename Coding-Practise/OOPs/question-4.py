'''
4. Vehicle Class Hierarchy

Create a base class Vehicle, and derive Car, Bike, and Truck from it.

Implement common methods like start(), stop(), and override them where necessary.
Use constructor chaining via super().
'''
import random
__list_of_vehicle_id = []

def generate_unique_id():
    id = random.randint(1000,9999)
    while id in __list_of_vehicle_id: id = random.randint(1000,9999)
    return id

class Vehicle:
    __electric_vehicle = {}
    __ICE_vehicles = {}
    __total_vehicles = 0
    info_dict = {}

    def __init__(self, vehicle_id, size_category, pollution_category, powertrain_type, start_type, stop_type):
        self.__vehicle_id = vehicle_id
        self.__size_category = size_category
        self.__pollution_category = pollution_category
        self.__powertrain_type = powertrain_type
        self.__start_type = start_type
        self.__stop_type = stop_type
        if self.__powertrain_type == 'ICE':
            self.info_dict['vehicle_id']={self.__vehicle_id}
            self.info_dict['pollution_category']={self.__pollution_category}
            self.info_dict['powertrain_type']={self.__powertrain_type}
            self.info_dict['start_type']={self.__start_type}
            self.info_dict['stop_type']={self.__stop_type}
            Vehicle.__ICE_vehicles[self.__vehicle_id]=self.info_dict
            Vehicle.__total_vehicles+=1
        elif self.__powertrain_type == 'Electric':
            self.info_dict['vehicle_id']={self.__vehicle_id}
            self.info_dict['pollution_category']={self.__pollution_category}
            self.info_dict['powertrain_type']={self.__powertrain_type}
            self.info_dict['start_type']={self.__start_type}
            self.info_dict['stop_type']={self.__stop_type}
            Vehicle.__electric_vehicle[self.__vehicle_id]=self.info_dict
            Vehicle.__total_vehicles+=1
    
    @classmethod
    def get_vehicle_details(cls, vehicle_id):
        if vehicle_id in cls.__electric_vehicle:
            # print(cls.__electric_vehicle[vehicle_id])
            print(f"Vehicle ID: {cls.__electric_vehicle[vehicle_id]['vehicle_id']}")
            print(f'Pollution category: {cls.__electric_vehicle[vehicle_id]["pollution_category"]}')
            print(f'Powertrain type: {cls.__electric_vehicle[vehicle_id]["powertrain_type"]}')
            print(f'Start type: {cls.__electric_vehicle[vehicle_id]["start_type"]}')
            print(f'Stop type: {cls.__electric_vehicle[vehicle_id]["stop_type"]}')
        elif vehicle_id in cls.__ICE_vehicles:
            print(f"Vehicle ID: {cls.__ICE_vehicles[vehicle_id]['vehicle_id']}")
            print(f'Pollution category: {cls.__ICE_vehicles[vehicle_id]["pollution_category"]}')
            print(f'Powertrain type: {cls.__ICE_vehicles[vehicle_id]["powertrain_type"]}')
            print(f'Start type: {cls.__ICE_vehicles[vehicle_id]["start_type"]}')
            print(f'Stop type: {cls.__ICE_vehicles[vehicle_id]["stop_type"]}')
        else:
            pass
        
nexon_id = generate_unique_id()
nexon_id_v = generate_unique_id()
nexon = Vehicle(nexon_id, 'Mid', 'BS6', 'ICE', 'non-hybrid', 'manual')
nexon_ev = Vehicle(nexon_id_v, 'Mid', 'EV', 'Electric', 'hybrid', 'manual')

nexon.get_vehicle_details(nexon_id)
nexon_ev.get_vehicle_details(nexon_id_v)