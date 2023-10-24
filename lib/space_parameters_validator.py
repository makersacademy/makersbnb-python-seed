
class SpaceParametersValidator:
    def __init__(self, name, description, size, price):
        self.name = name
        self.description = description
        self.size = size
        self.price = price

    def _is_valid(self):
        self._is_name_valid() and self._is_description_valid() and self._is_size_empty() and self._is_size_digit() and self._is_price_empty() and self._is_price_digit()

    def get_valid_name(self):
        if not self._is_name_valid():
            raise ValueError('Cannot get valid name')
        return self.name
    
    def get_valid_description(self):
        if not self._is_description_valid():
            raise ValueError('Cannot get valid description')
        return self.description
    
    def get_valid_size(self):
        if not self._is_size_empty() or self._is_size_digit():
            raise ValueError('Cannot get valid size')
        return self.size
    
    def get_valid_price(self):
        if not self._is_price_empty() or self._is_price_digit():
            raise ValueError('Cannot get valid price')
        return self.price

    def generate_errors(self):
        errors = []
        if not self._is_name_valid():
            errors.append('Name must not be blank')
        if not self._is_description_valid():
            errors.append('Description must not be blank')
        if not self._is_size_empty():
            errors.append('Size must not be blank')
        if not self._is_size_digit():
            errors.append('Size must be a digit')
        if not self._is_price_empty():
            errors.append('Price must not be blank')
        if not self._is_price_digit():
            errors.append('Price must be a digit')
        return errors      

    def _is_name_valid(self):
        if self.name is None or self.name == '':
            return False
        
    def _is_description_valid(self):
        if self.description is None or self.description == '':
            return False
        
    def _is_size_empty(self):
        if self.size is None:
            return False
        return True
    
    def _is_size_digit(self):
        if not self.size.isdigit():
            return False
        return True

    def _is_price_empty(self):
        if self.price is None:
            return False
        return True
    
    def _is_price_digit(self):
        if not self.price.isdigit():
            return False
        return True