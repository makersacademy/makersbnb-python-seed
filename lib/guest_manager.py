class GuestManager:
    def __init__(self):
        self.guests = []

    def add_guest(self, username, password):
        new_guest = Guest(username, password)
        self.guests.append(new_guest)
        return new_guest

    def get_guest(self, username):
        for guest in self.guests:
            if guest.username == username:
                return guest
        return None

class Guest:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f"Username: {self.username}"

# Example usage
def main():
    guest_manager = GuestManager()

    # Sign up a new guest named Adam
    new_guest = guest_manager.add_guest("Adam", "password123")
    print(f"Guest signed up: {new_guest}")

    # Get guest by username
    existing_guest = guest_manager.get_guest("Adam")
    if existing_guest:
        print(f"Found guest: {existing_guest}")
    else:
        print("Guest not found")

if __name__ == "__main__":
    main()
