#!/usr/bin/env python3
"""
Setup script to initialize the warehouse with the specified storage locations:
- Bulk 1-6 (6 locations)
- Miscellaneous 1-2 (2 locations)
- Side 1-2 (2 locations)
"""

from warehouse_manager import WarehouseManager

def setup_storage_locations():
    """Initialize the warehouse with the required storage locations."""
    wm = WarehouseManager()
    
    # Storage locations to create
    locations = [
        "Bulk_1", "Bulk_2", "Bulk_3", "Bulk_4", "Bulk_5", "Bulk_6",
        "Miscellaneous_1", "Miscellaneous_2",
        "Side_1", "Side_2"
    ]
    
    print("Setting up warehouse storage locations...")
    
    # Create each storage location as a warehouse
    for location in locations:
        if location not in wm.warehouses:
            wm.add_warehouse(location, copy_items=False)
            print(f"Created storage location: {location}")
        else:
            print(f"Storage location already exists: {location}")
    
    # Set the first location as the current warehouse
    if wm.warehouses:
        wm.select_warehouse("Bulk_1")
        print("Set Bulk_1 as the active storage location")
    
    print("Setup complete!")
    print(f"Available storage locations: {', '.join(wm.warehouses)}")

if __name__ == "__main__":
    setup_storage_locations()