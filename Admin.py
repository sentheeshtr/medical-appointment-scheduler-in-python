from Doctor import Doctor
from Patient import Patient


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        
        return self.__username in username and self.__password == password

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name = input('Enter the first name: ')
        surname = input('Enter the surname: ')
        speciality = input('Enter the speciality: ')
        return first_name, surname, speciality
    
    def get_patient_details(self):
        first_name = input('Enter the first name: ')
        surname = input('Enter the surname: ')
        age = input('Enter the age: ')
        mobile = input('Enter the mobile: ')
        postcode = input('Enter the postcode: ')
        symptoms = input('Enter the Symptoms: ')
        return first_name, surname, age, mobile, postcode, symptoms

    def doctor_management(self, doctors, patients):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input('Input: ')



        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            first_name, surname, speciality = self.get_doctor_details()
            new_doctor = Doctor(first_name, surname, speciality)

            doctors.append(new_doctor)
            print('Doctor registered.')
            return

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            self.view(doctors) 

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                except ValueError: # the entered id could not be changed into an int
                    print('Expects number not string')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            
            try: 
                op = int(input('Input: '))
                        
                if op == 1:
                    new_first_name = input("Enter the new first name: ")
                    doctors[index].set_first_name(new_first_name)
                    print("The doctors first name has been updated")
                
                elif op == 2:
                    new_surname = input("Enter the new second name: ")
                    doctors[index].set_surname(new_surname)
                    print("The doctors surname has been updated")
                elif op == 3:
                    new_speciality = input("Enter the new speciality: ")
                    doctors[index].set_speciality(new_speciality)
                    print("The doctors speciality has been updated")
                    
                else: 
                    print('Inputted number has to be in the menu')
                    
            except ValueError: # the entered id could not be changed into an int
                    print('Expects number not string')
            
            
        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)
        
            try: 
            
                doctor_index = int(input('Enter the ID of the doctor to be deleted: ')) - 1
            
                if doctor_index in range(0,len(doctors)):
                        del doctors[doctor_index]
                        print("Doctor has been deleted")
                    
                else:
                    print('The ID is not in the list of doctors')  
               
            except ValueError:
                print("Expects number not string")
            
                

    def patient_management(self, patients):
        
    
        print("-----Patient Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Add symptoms')
        
        
        op = input('Input: ')
        
        # register
        if op == '1':
            print("-----Register-----")

            # get the patient details
            print('Enter the patient\'s details:')
            first_name, surname, age, mobile, postcode, symptoms = self.get_patient_details()
            new_patient = Patient(first_name, surname, age, mobile, postcode, symptoms)
            
            
            """
            The code block below is not needed as patients with same names can exist
            for patient in patients:
                if first_name == patient.get_first_name() and surname == patient.get_surname():
                    print('Patient already exists.')
                    return
            """
            
            patients.append(new_patient)
            print('Patient registered.')
            return
        
        # View
        elif op == '2':
            print("-----List of Patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |       Symptoms    |')
            self.view(patients) 
            
        elif op == '3':
            print("-----List of Patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |       Symptoms    |')
            self.view(patients) 
            
            patient_index = input('Please enter the patient ID: ')
            
            try:
                # patient_index is the patient ID mines one (-1)
                patient_index = int(patient_index) -1

                # check if the id is not in the list of patients
                if patient_index not in range(len(patients)):
                    print('The id entered was not found.')
                    return # stop the procedures

                else:
                    inputSymptoms = input("Enter an additional symptom: ")
                    patients[patient_index].add_symptoms(inputSymptoms)
                    print("Additional symptom has been added")

            except ValueError: # the entered id could not be changed into an int
                print('Number expected not string')
                return # stop the procedures
            
            

        else:
             print('Input not found in list')

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |       Symptoms    |')
        self.view(patients)
        
  
    

    def assign_doctor_to_patient(self, patients, doctors):
        """
        When a doctor has been assigned to a patient,
        the patient can be relocated a new doctor by 
        replacing the current doctor through the same function
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |       Symptoms    |')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('Number expected not string')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
   

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                
                patientName = patients[patient_index].full_name()
                doctor_name = doctors[doctor_index].full_name()
                
                patients[patient_index].link(doctor_name)
                doctors[doctor_index].add_patient(patientName)
                
                print('The patient is now assigned to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('Number expected not string')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        try:
            patient_index = int(input('Please enter the patient ID: ')) - 1
        
            if patient_index in range(len(patients)):
                deletedPatient = patients.pop(patient_index)
            
                discharge_patients.append(deletedPatient)
                print("The patient has been discharged")
                
            else: 
                print("The ID was not found")
                
        except ValueError: # the entered id could not be changed into an in
            print('Number expected not string')
        

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |       Symptoms    |')
        self.view(discharged_patients)
        
    def patient_write_data(self, patients):
            
            
            try:
                
                patient_data_file = open('patientdata.txt', 'w')
                i = 0
                count = 1
                
            except FileNotFoundError:
                print("File is not found")
                
            else:
                while i < len(patients):
                    patient_data_file.write(str(count))
                    patient_data_file.write(str(" "))
                    patient_data_file.write(str(patients[i].full_name()))
                    patient_data_file.write(str(" "))
                    patient_data_file.write(str(patients[i].get_doctor()))
                    patient_data_file.write(str(" "))
                    patient_data_file.write(str(patients[i].age()))
                    patient_data_file.write(str(" "))
                    patient_data_file.write(str(patients[i].mobile()))
                    patient_data_file.write(str(" "))
                    patient_data_file.write(str(patients[i].postcode()))
                    patient_data_file.write(str(" "))
                    patient_data_file.write(str(patients[i].print_symptoms()))
                    patient_data_file.write(str("\n"))
                    i = i + 1
                    count = count + 1
                    
                    
                    
            
            patient_data_file.close()
    
    def request_management_report(self, doctors):
        print("----- Management Report-----")

        # menu
        print('Request a report from the following choices:')
        print(' 1 - Total number of doctors in the system')
        try:
            op = input('Input: ')
        
            if op == '1':
                print("Number of doctors: ", len(doctors))
                
            else:
                print("Incorrect number selected")
                
        except ValueError: 
            print("Number input expected not string")
            
        
    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            username = input('Enter the new username: ')
            # validate the username

            if username == input('Enter the username again: '):
                self.__username = username
                print("username has been updated")
            
            else:
                print("username does not match previous inputted username")

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
                print("password has been updated")
                
            else:
                print("password does not match previous inputted password")

        elif op == 3:
            address = input('Enter the address: ')
            
            if address == input('Enter the address again: '):
                self.__address = address
                print("address has been updated")
                
            else:
                print("address does not match previous inputted address")

        else:
            print('Invalid operation choosen. Check your spelling!')
        
       