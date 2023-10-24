class AvailableDateRepository: # a single available date for a particular space
    def __init__(s, connection):
        s._connection = connection
    