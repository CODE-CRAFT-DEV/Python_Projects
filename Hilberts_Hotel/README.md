# Hilbert's Hotel: An Infinite Paradox

Imagine a hotel with an infinite number of rooms – a hotel that can never be fully booked. This is the famous thought experiment by David Hilbert, one of the greatest mathematicians of the 20th century. Hilbert's Hotel demonstrates that even if every room in this infinite hotel is occupied, there is always room for one more guest. How is this possible?

## The Paradox Explained

Suppose a new guest arrives at a fully occupied hotel. The seemingly paradoxical solution is to simply move each guest to the next room: the guest in room 1 moves to room 2, the guest in room 2 moves to room 3, and so on. This way, room 1 becomes free, and the new guest can check in. This illustrates the incredible flexibility and counterintuitive nature of infinite sets.

## Example in Python

```python
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
        self.rooms = guest
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
```

This example illustrates how a new room is created by shifting guests and showcases the fascinating property of infinity.

---
