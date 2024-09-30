class HilbertsHotel:
    def __init__(self):
        # Dictionary to represent rooms with their guests
        self.rooms = {}

    def check_in(self, guest: str):
        # Shift all guests to the next room, starting from the last room
        if self.rooms:
            for room in sorted(self.rooms.keys(), reverse=True):
                self.rooms[room + 1] = self.rooms[room]
        # Add the new guest to room 1
        self.rooms[1] = guest
        print(f"Guest {guest} has been checked into room 1.")
    
    def display_rooms(self, num_rooms=10):
        # Display the state of the first few rooms
        for room in range(1, num_rooms + 1):
            guest = self.rooms.get(room, "Empty")
            print(f"Room {room}: {guest}")

# Initialize the hotel
hotel = HilbertsHotel()

# Check in initial guests (simulating an infinite number of guests by adding a large number)
for i in range(1, 101):
    hotel.check_in(f"Guest {i}")

print("Initial room assignments (first 10 rooms):")
hotel.display_rooms()

# New guest arrives
hotel.check_in("New Guest")

print("\nRoom assignments after new guest (first 10 rooms):")
hotel.display_rooms()
