class SpaceParametersValidator:
    def __init__(self, name, description, size, price):
        self.name = name
        self.description = description
        self.size = size
        self.price = price

    def _is_valid(self):
        return self._is_name_valid() and self._is_description_valid() and self._is_size_present() and self._is_size_digit() and self._is_price_present() and self._is_price_digit()

    def get_valid_name(self):
        if not self._is_name_valid():
            raise ValueError('Cannot get valid name')
        return self.name
    
    def get_valid_description(self):
        if not self._is_description_valid():
            raise ValueError('Cannot get valid description')
        return self.description
    
    def get_valid_size(self):
        if not self._is_size_present() or not self._is_size_digit():
            raise ValueError('Cannot get valid size')
        return self.size
    
    def get_valid_price(self):
        if not self._is_price_present() or not self._is_price_digit():
            raise ValueError('Cannot get valid price')
        return self.price

    def generate_errors(self):
        errors = []
        if not self._is_name_valid():
            errors.append('Name must not be blank')
        if not self._is_description_valid():
            errors.append('Description must not be blank')
        if not self._is_size_present():
            errors.append('Size must not be blank')
        if self._is_size_present() and not self._is_size_digit():
            errors.append('Size must be a digit')
        if not self._is_price_present():
            errors.append('Price must not be blank')
        if self._is_price_present() and not self._is_price_digit():
            errors.append('Price must be a digit')
        return errors      

    def _is_name_valid(self):
        if self.name is None or self.name == '':
            return False
        return True
        
    def _is_description_valid(self):
        if self.description is None or self.description == '':
            return False
        return True
        
    def _is_size_present(self):
        if self.size is None or self.size == '':
            return False
        return True
    
    def _is_size_digit(self):
        if self._is_size_present() and not self.size.isdigit():
            return False
        return True

    def _is_price_present(self):
        if self.price is None or self.price == '':
            return False
        return True
    
    def _is_price_digit(self):
        if self._is_price_present() and not self.price.isdigit():
            return False
        return True