class Space:
    def __init__(self, name, description, price_per_night, availability):
        self.name = name
        self.description = description
        self.price_per_night = price_per_night
        self.availability = availability

def display_space_listings(spaces):
    print("Space Listings:")
    for i, space in enumerate(spaces, 1):
        print(f"{i}. {space.name}: {space.description}")
        print(f" Price per Night: ${space.price_per_night}")
        print(f" Availability: {space.availability}")
        print()

# Example usage
def main():
    # Sample spaces
    space1 = Space("London", "Smallest flat in the city with expensive rooms", 3000, "2024-03-24")
    space2 = Space("Manchester", "Modern loft apartment near two largest universities", 100, "2024-03-15")
    space3 = Space("Ireland", "Beautiful townhouse with stunning views", 4000, "2024-03-11")

    # List of spaces
    spaces = [space1, space2, space3]

    # Display space listings
    display_space_listings(spaces)

if __name__ == "__main__":
    main()
