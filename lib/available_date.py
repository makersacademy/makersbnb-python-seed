class AvailableDate: # a single available date for a particular space
    def __init__(s, date: str, space_id):
        s.date = date #dd/mm/yy format as a string for now
        s.space_id = space_id