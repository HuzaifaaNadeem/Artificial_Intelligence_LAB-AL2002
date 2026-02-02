class Vehicle:
    def __init__(self, vehicle_id, brand, rent_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.rent_per_day = rent_per_day

    def display_details(self):
        print("Vehicle ID:", self.vehicle_id)
        print("Brand:", self.brand)
        print("Rent per day:", self.rent_per_day)

    def calculate_rent(self, days):
        return self.rent_per_day * days

vehicle1 = Vehicle("ABC-123", "Mercedes", 5000)
vehicle2 = Vehicle("XYZ-000", "Honda", 4500)
vehicle1.display_details()
print("Rent for 3 days:", vehicle1.calculate_rent(3))
print()
vehicle2.display_details()
print("Rent for 5 days:", vehicle2.calculate_rent(5))
