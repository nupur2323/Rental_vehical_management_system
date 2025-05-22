vehicles = {
    '101': {'type': 'Car', 'name': 'Honda City', 'rent_per_day': 1500, 'available': True},
    '102': {'type': 'Bike', 'name': 'Royal Enfield', 'rent_per_day': 800, 'available': True},
    '103': {'type': 'Truck', 'name': 'Tata Ace', 'rent_per_day': 2000, 'available': True}
}

bookings = []

while True:
    print("\nVehicle Rental Management System")
    print("1. View Available Vehicles")
    print("2. Rent a Vehicle")
    print("3. View Bookings")
    print("4. Return a Vehicle")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("\nAvailable Vehicles:")
        print("-" * 70)
        print("|{:^10}|{:^15}|{:^20}|{:^15}|".format("ID", "Type", "Name", "Rent per Day"))
        print("-" * 70)
        for vid, details in vehicles.items():
            if details['available']:
                print("|{:^10}|{:^15}|{:^20}|{:^15}|".format(vid, details['type'], details['name'], details['rent_per_day']))
        print("-" * 70)
    
    elif choice == '2':
        vid = input("Enter Vehicle ID to Rent: ")
        if vid in vehicles and vehicles[vid]['available']:
            name = input("Enter Your Name: ")
            days = int(input("Enter Number of Days for Rent: "))
            total_cost = vehicles[vid]['rent_per_day'] * days
            vehicles[vid]['available'] = False
            bookings.append({'Vehicle ID': vid, 'Name': name, 'Days': days, 'Total Cost': total_cost})
            print(f"Vehicle {vehicles[vid]['name']} booked successfully for {days} days. Total Cost: {total_cost}")
        else:
            print("Invalid ID or Vehicle Not Available.")
    
    elif choice == '3':
        print("\nBookings:")
        if not bookings:
            print("No bookings yet.")
        else:
            print("-" * 70)
            print("|{:^10}|{:^15}|{:^20}|{:^15}|".format("Vehicle ID", "Name", "Days", "Total Cost"))
            print("-" * 70)
            for booking in bookings:
                print("|{:^10}|{:^15}|{:^20}|{:^15}|".format(booking['Vehicle ID'], booking['Name'], booking['Days'], booking['Total Cost']))
            print("-" * 70)
    
    elif choice == '4':
        vid = input("Enter Vehicle ID to Return: ")
        for booking in bookings:
            if booking['Vehicle ID'] == vid:
                vehicles[vid]['available'] = True
                bookings.remove(booking)
                print(f"Vehicle {vehicles[vid]['name']} returned successfully!")
                break
        else:
            print("Invalid Vehicle ID or Vehicle not booked.")
    
    elif choice == '5':
        print("Exiting System. Thank you!!")
        break
    
    else:
        print("Invalid choice! Please try again.")