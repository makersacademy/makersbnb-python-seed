class Booking():
<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self, id, property_id, requested_from, requested_to, is_confirmed, created_at) -> None:
=======
    def __init__(self, id, property_id, requested_from, requested_to, is_confirmed, total_price, created_at) -> None:
>>>>>>> main
=======
    def __init__(self, id, property_id, requested_from, requested_to, is_confirmed, total_price, created_at) -> None:
>>>>>>> e3998440b4b4ac986f7155f490ddc71a50c54719
        self.id = id
        self.property_id = property_id
        self.requested_from = requested_from
        self.requested_to = requested_to
        self.is_confirmed = is_confirmed
        self.created_at = created_at
<<<<<<< HEAD
<<<<<<< HEAD
    
    def __repr__(self) -> str:
        return f'Booking({self.id}, {self.property_id}, {self.requested_from}, {self.requested_to}, {self.is_confirmed}, {self.created_at})'
=======
=======
>>>>>>> e3998440b4b4ac986f7155f490ddc71a50c54719
        self.total_price = total_price
    
    def __repr__(self) -> str:
        return f'Booking({self.id}, {self.property_id}, {self.requested_from}, {self.requested_to}, {self.is_confirmed}, {self.total_price:.2f}, {self.created_at})'
<<<<<<< HEAD
>>>>>>> main
=======
>>>>>>> e3998440b4b4ac986f7155f490ddc71a50c54719
    
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__