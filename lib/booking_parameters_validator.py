
class BookingParametersValidator:
    def __init__(self, space_id, start_date, end_date, booker_id):
        self.space_id = space_id
        self.start_date = start_date
        self.end_date = end_date
        self.booker_id = booker_id

    def _is_valid(self):
        return self._is_space_id_present() and self._is_end_date_present() and self._is_booker_id_present()

    def get_valid_space_id(self):
        if not self._is_space_id_present():
            raise ValueError('Cannot get valid space')
        return self.space_id
    
    def get_valid_start_date(self):
        if not self._is_start_date_present():
            raise ValueError('Cannot get valid start date')
        return self.start_date
    
    def get_valid_end_date(self):
        if not self._is_end_date_present():
            raise ValueError('Cannot get valid end date')
        return self.end_date
    
    def get_valid_booker_id(self):
        if not self._is_booker_id_present():
            raise ValueError('Cannot get valid user')
        return self.booker_id

    def generate_errors(self):
        errors = []
        if not self._is_start_date_present():
            errors.append('Start date must not be blank')
        if not self._is_end_date_present():
            errors.append('End date must not be blank')
        return errors      

    def _is_space_id_present(self):
        if self.space_id is None or self.space_id == '':
            return False
        return True
        
    def _is_start_date_present(self):
        if self.start_date is None or self.start_date == '':
            return False
        return True
        
    def _is_end_date_present(self):
        if self.end_date is None or self.end_date == '':
            return False
        return True

    def _is_booker_id_present(self):
        if self.booker_id is None or self.booker_id == '':
            return False
        return True