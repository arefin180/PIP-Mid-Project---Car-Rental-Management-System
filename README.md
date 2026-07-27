# FleetHub- Vehicle Rental Management System


FleetHub is a CLI based vehicle rental management system built using Python, made to track car fleets, validate input, generate analytical statistics using **NumPy**, and push data in JSON format.



# Team Member Roles & Responsibilities

| Member | Scope & Responsibilities | Working Files |

| ESRAT  | Data Model (OOP), File Storage (JSON I/O), Initial Dataset | `car.py`, `fleet_manager.py`, `fleet_data.json` |
| NABIL | Input Validation, Exception Handling, Statistical Analysis (NumPy) | `validation.py`, `analysis.py` |
| AREFIN | CLI Menu Interface, User Interaction, System Integration, Documentation | `main.py`, `README.md` |


# Project Structure


fleethub/
├── main.py            # Menu loop & interactive interface (Arefin)
├── car.py             # Car class data model & VALID_STATUSES constant (Esrat)
├── fleet_manager.py   # FleetManager class & JSON file operations (Esrat)
├── validation.py      # Input validation functions (Nabil)
├── analysis.py        # NumPy statistical analysis module (Nabil)
├── fleet_data.json    # JSON dataset containing primary vehicle records (Esrat)
└── README.md          # Project description & run instructions (Arefin)




# Data Structures Used

1. **`list`** (`self.cars` in `FleetManager`): For Storing ordered collections of `Car` objects.
2. **`dict`** (Returned by `to_dict()` and `get_stats()`): For formatting data for JSON storage and statistical summaries.
3. **`tuple`** (`VALID_STATUSES` in `car.py`): For constant definition of allowed vehicle states.
4. **`set`** (`self.used_plates` in `FleetManager`): For ensuring O(1) duplicate prevention for license plates.



Run Instructions

# Prior Requirements
*Python version 3.x
*NumPy

# Launch Application
Navigate to the project directory and run:
in terminal
python main.py

