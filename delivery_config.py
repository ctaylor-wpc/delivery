# delivery_config.py
# This file contains all delivery types, pricing, and minimums
# Edit this file to update pricing without touching the main app

# Delivery type configurations
# Format: "Type Name": (frankfort_minimum, lexington_minimum, rate_per_mile)
DELIVERY_TYPES = {
    "Single": {
        "frankfort_minimum": 45,
        "lexington_minimum": 50,
        "rate_per_mile": 2.00,
        "allows_to_the_hole": True
    },
    "Double": {
        "frankfort_minimum": 60,
        "lexington_minimum": 70,
        "rate_per_mile": 2.95,
        "allows_to_the_hole": True
    },
    "Bulk": {
        "frankfort_minimum": 55,
        "lexington_minimum": 65,
        "rate_per_mile": 2.65,
        "allows_to_the_hole": True
    },
    "Bulk Plus": {
        "frankfort_minimum": 65,
        "lexington_minimum": 80,
        "rate_per_mile": 3.05,
        "allows_to_the_hole": True
    },
    "Simple": {
        # Simple type uses fixed pricing by city, not mileage-based
        "frankfort_price": 8.00,
        "lexington_price": 30.00,
        "allows_to_the_hole": False
    }
}

# To-The-Hole add-on pricing
TO_THE_HOLE_FEE = 20.00

# Origin addresses
ORIGIN_ADDRESSES = {
    "Frankfort": "3690 East West Connector, Frankfort, KY 40601",
    "Lexington": "2700 Palumbo Drive, Lexington, KY 40509"
}

# Helper function to get delivery type names for dropdown
def get_delivery_type_names():
    return list(DELIVERY_TYPES.keys())

# Helper function to validate to-the-hole option
def is_to_the_hole_allowed(delivery_type):
    return DELIVERY_TYPES[delivery_type].get("allows_to_the_hole", False)
