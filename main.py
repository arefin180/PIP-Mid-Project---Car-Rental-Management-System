# 22-48766-3 (Interface + Integration + Demo)
# Interactive CLI menu loop integrating FleetManager and Validation


import os
from car import Car, VALID_STATUSES
from fleet_manager import FleetManager
import validation  

DATA_FILE = "fleet_data.json"


#menu option
def display_menu():
    print("\n****************************************")
    print("      FLEETHUB - VEHICLE RENTAL SYSTEM    ")
    print("******************************************")
    print("1. Add a new car")
    print("2. List all cars")
    print("3. List available cars only")
    print("4. Search a car by license plate")
    print("5. Update a car's status")
    print("6. Delete a car from fleet")
    print("7. Show fleet statistics (NumPy)")
    print("8. Exit (Save & Quit)")
    print("****************************************")


# for formattting and printing car details
def print_car_details(car):
    print(f"  - Plate: {car.plate:<10} | Model: {car.model:<18} | Year: {car.year} | Status: {car.status:<18} | Rate: ${car.price_per_day:.2f}/day")


# adding a new vehicle using validators
def handle_add_car(manager):
    print("\n--- Add a New Vehicle ---")
    
    
    model = None
    while model is None:
        raw_model = input("Enter vehicle model (e.g. Toyota Corolla): ")
        model = validation.validate_model(raw_model)

   
    year = None
    while year is None:
        raw_year = input("Enter manufacturing year (1990-2026): ")
        year = validation.validate_year(raw_year)

    
    plate = ""
    while not plate:
        raw_plate = input("Enter license plate: ")
        plate = validation.clean_plate(raw_plate)
        if not plate:
            print("Validation Error: License plate cannot be empty.")
        elif manager.find_car(plate) is not None:
            print(f"Validation Error: Plate '{plate}' already exists in fleet. Please enter a unique plate.")
            plate = ""

    
    print(f"Allowed statuses: {', '.join(VALID_STATUSES)}")
    status = None
    while status is None:
        raw_status = input("Enter status: ")
        status = validation.validate_status(raw_status)

    
    price = None
    while price is None:
        raw_price = input("Enter daily rental rate ($): ")
        price = validation.validate_price(raw_price)

    
    new_car = Car(model=model, year=year, plate=plate, status=status, price_per_day=price)
    success = manager.add_car(new_car)
    if success:
        print(f"Success: Vehicle '{model}' [{plate}] added to fleet.")


# For handling listing all vehicles
def handle_list_all(manager):
    print("\n--- All Fleet Vehicles ---")
    cars = manager.list_all()
    if not cars:
        print("No vehicles registered in fleet.")
        return
    for car in cars:
        print_car_details(car)


# Handling listing available vehicles only
def handle_list_available(manager):
    print("\n--- Available Vehicles Only ---")
    cars = manager.list_available()
    if not cars:
        print("No available vehicles currently.")
        return
    for car in cars:
        print_car_details(car)


# searching 
def handle_search_car(manager):
    print("\n--- Search Vehicle ---")
    raw_plate = input("Enter license plate to search: ")
    plate = validation.clean_plate(raw_plate)
    car = manager.find_car(plate)
    if car is not None:
        print("Vehicle Found:")
        print_car_details(car)
    else:
        print(f"No vehicle found with license plate '{plate}'.")


# for updating a vehicle's status
def handle_update_status(manager):
    print("\n--- Update Vehicle Status ---")
    raw_plate = input("Enter license plate: ")
    plate = validation.clean_plate(raw_plate)
    car = manager.find_car(plate)
    if car is None:
        print(f"No vehicle found with license plate '{plate}'.")
        return

    print(f"Current status of '{plate}' is: {car.status}")
    print("Choose new status:")
    for idx, stat in enumerate(VALID_STATUSES, 1):
        print(f"  {idx}. {stat}")
    
    choice = input("Enter option number (1-3) or status name: ").strip()
    new_status = None
    if choice == "1":
        new_status = "Available"
    elif choice == "2":
        new_status = "Rented"
    elif choice == "3":
        new_status = "Under Maintenance"
    else:
        new_status = validation.validate_status(choice)

    if new_status is not None:
        success = manager.update_status(plate, new_status)
        if success:
            print(f"Success: Updated status of '{plate}' to '{new_status}'.")
    else:
        print("Update cancelled due to invalid status selection.")


# deleting a vehicle from fleet
def handle_delete_car(manager):
    print("\n--- Delete Vehicle ---")
    raw_plate = input("Enter license plate to delete: ")
    plate = validation.clean_plate(raw_plate)
    success = manager.remove_car(plate)
    if success:
        print(f"Success: Vehicle with plate '{plate}' removed from fleet.")
    else:
        print(f"Error: Vehicle with plate '{plate}' not found.")


# dispaying fleet statistics calculated as per NumPy module
def handle_show_stats(manager):
    print("\n--- Fleet Statistics (NumPy Analysis) ---")
    stats = manager.get_stats()
    
    print(f"Total Fleet Size     : {stats['total_cars']} vehicles")
    print(f"Total Daily Value    : ${stats['total_fleet_value']:.2f}")
    print(f"Average Car Age      : {stats['avg_car_age']:.1f} years")
    print(f"Average Price / Day  : ${stats['avg_price_per_day']:.2f}")
    print(f"Oldest Model Year    : {stats['oldest_year']}")
    print(f"Newest Model Year    : {stats['newest_year']}")
    print("Status Breakdown     :")
    for status, count in stats["status_counts"].items():
        print(f"  - {status:<18}: {count}")



def main():
    manager = FleetManager()
    
    # Load dataset at startup
    manager.load_from_file(DATA_FILE)

    while True:
        try:
            display_menu()
            choice = input("Enter menu option (1-8): ").strip()
            
            if choice == "1":
                handle_add_car(manager)
            elif choice == "2":
                handle_list_all(manager)
            elif choice == "3":
                handle_list_available(manager)
            elif choice == "4":
                handle_search_car(manager)
            elif choice == "5":
                handle_update_status(manager)
            elif choice == "6":
                handle_delete_car(manager)
            elif choice == "7":
                handle_show_stats(manager)
            elif choice == "8":
                print("\nSaving data and exiting FleetHub...")
                manager.save_to_file(DATA_FILE)
                print("Goodbye!")
                break
            else:
                print(" INVALID. Please enter a number from 1 to 8.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Returning to main menu.")


if __name__ == "__main__":
    main()
