class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'No Doctor assigned'
        self.__symptoms = [symptoms]

    
    def full_name(self) :
        """full name is first_name and surname"""
        return self.__first_name + ' ' + self.__surname
    
    def get_first_name(self) :
        return self.__first_name
    
    def get_surname(self):
        return self.__surname

    def age(self):
        return self.__age
    
    def mobile(self):
        return self.__mobile
    
    def postcode(self):
        return self.__postcode
    
    def get_doctor(self) :
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        return self.__symptoms
    
    def add_symptoms(self, symptom):
        self.__symptoms.append(symptom)
        
   
        

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}|{self.__symptoms}'
