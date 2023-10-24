class AvailableDate: # a single available date for a particular space
    def __init__(s, id: int, date_name: str, space_id: int):
        s.id = id
        s.date_name = date_name #dd/mm/yy format as a string for now
        s.space_id = space_id
    def __repr__(s):
        return(f"AvailableDate({s.id}, {s.date_name}, {s.space_id})")
    def __eq__(self, other) -> bool:
        return(self.__dict__ == other.__dict__)