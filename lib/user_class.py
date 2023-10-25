class User:
    def __init__(self,name,username,password,email,phone_number,id=None,):
        self.id = id
        self.username = username
        self.name = name
        self.password = password
        self.email = email
        self.phone_number = phone_number
    
    # def __eq__(self,other):
    #     return self.__dict__==other.__dict__

    def __repr__(self):
        return (f'User ({self.id},{self.name},{self.username},{self.password},{self.email},{self.phone_number})')