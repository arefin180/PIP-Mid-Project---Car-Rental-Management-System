import json
import os
from car import Car, VALID_STATUSES
import analysis


class FleetManager:

    def __init__(self):
        self.cars = []
        self.used_plates = set()

    def add_car(self, car):
        cleaned_plate = car.plate.upper()
        if cleaned_plate in self.used_plates:
            print(f"Error: Plate '{cleaned_plate}' already exists in fleet.")
            return False
        
        self.cars.append(car)
        self.used_plates.add(cleaned_plate)
        return True

    def remove_car(self, plate):
        cleaned_plate = str(plate).strip().upper()
        car_to_remove = None
        for car in self.cars:
            if car.plate == cleaned_plate:
                car_to_remove = car
                break
        
        if car_to_remove is not None:
            self.cars.remove(car_to_remove)
            self.used_plates.remove(cleaned_plate)
            return True
        return False

    def find_car(self, plate):
        cleaned_plate = str(plate).strip().upper()
        for car in self.cars:
            if car.plate == cleaned_plate:
                return car
        return None

    def update_status(self, plate, new_status):
        if new_status not in VALID_STATUSES:
            print(f"Error: Status '{new_status}' is not valid.")
            return False
        
        car = self.find_car(plate)
        if car is not None:
            car.status = new_status
            return True
        return False

    def list_all(self):
        return self.cars

    def list_available(self):
        available_cars = []
        for car in self.cars:
            if car.status == "Available":
                available_cars.append(car)
        return available_cars

    def save_to_file(self, filename):
        try:
            data_list = []
            for car in self.cars:
                data_list.append(car.to_dict())
            
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data_list, f, indent=4)
            print(f"Fleet successfully saved to '{filename}'.")
            return True
        except Exception as e:
            print(f"Failed to save fleet data to '{filename}': {e}")
            return False

    def load_from_file(self, filename):
        self.cars = []
        self.used_plates = set()

        if not os.path.exists(filename):
            print(f"Data file '{filename}' not found. Starting with empty fleet.")
            return False

        try:
            with open(filename, "r", encoding="utf-8") as f:
                data_list = json.load(f)

            if not isinstance(data_list, list):
                print(f"Warning: File '{filename}' is invalid format. Initializing empty fleet.")
                return False

            for item in data_list:
                try:
                    car = Car.from_dict(item)
                    if car.plate not in self.used_plates:
                        self.cars.append(car)
                        self.used_plates.add(car.plate)
                except KeyError as ke:
                    print(f"Skipping corrupted car entry missing field {ke}.")

            print(f"Successfully loaded {len(self.cars)} vehicles from '{filename}'.")
            return True

        except json.JSONDecodeError:
            print(f"Error: Data file '{filename}' is corrupted (bad JSON). Starting with empty fleet.")
            return False
        except Exception as e:
            print(f"Error loading file '{filename}': {e}. Starting with empty fleet.")
            return False

    def get_stats(self):
        return analysis.get_stats(self.cars)
