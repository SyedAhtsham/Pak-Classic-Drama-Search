
# Medicine class
class Medicine:
    def __init__(self, n, t):
        self.name = n
        self.type = t

# Patient class
class Patient:
    def __init__(self, n, g, w):
        self.name = n
        self.gender = g
        self.weight = w

# In-Patient class
class In_Patient (Patient):
    def __init__(self, n, g, w, ns):
        Patient.__init__(self, n, g, w)
        self.nightSpent = ns
        self.medicines = []
    # Function  to add medicine for patient
    # Including exception handling
    def addMedicine(self):
        name = input('Enter Medicine Name: ')
        type = input('Enter Medicine Type: ')
        try:
            if len(self.medicines) > 5:
                raise Exception
        except:
            print('Cannot add medicine')
    def dropMedicine(self, name):
        try:
            for i in range(len(self.medicines)):
                if self.medicines[i].name == name:
                    del self.medicines[i]
                    print('Deleted ...')
                    return True
            raise Exception
        except:
            print('Medicine not found ...')
    def display(self):
        print(self.name, self.gender, self.weight, self.nightSpent)
        for m in self.medicines:
            print(m.name, m.type)

# Out-Patient class
class Out_Patient (Patient):
    def __init__(self, n, g, w):
        Patient.__init__(self, n, g, w)
        self.medicines = []
    # Function  to add medicine for patient
    # Including exception handling
    def addMedicine(self):
        name = input('Enter Medicine Name: ')
        type = input('Enter Medicine Type: ')
        try:
            if len(self.medicines) > 3:
                raise Exception
        except:
            print('Cannot add medicine')
    def dropMedicine(self, name):
        try:
            for i in range(len(self.medicines)):
                if self.medicines[i].name == name:
                    del self.medicines[i]
                    print('Deleted ...')
                    return True
            raise Exception
        except:
            print('Medicine not found ...')
    def display(self):
        print(self.name, self.gender, self.weight)
        for m in self.medicines:
            print(m.name, m.type)

ip = In_Patient('Ahmed', 'male', 80, 4)
ip.display()


op = Out_Patient('Sara', 'female', 60)
op.display()
