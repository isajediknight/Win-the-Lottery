import datetime

class EverythingDataType:
    """
    The purpose of this class is to be able to handle
    a wide range of needs
    """
    def __init__(self,value = ''):
        # Record all the changes
        self.history = []

        # Record when changes happened
        self.timestamp = []

        # Record the datatypes
        self.base_types = []

        # Capture the base type
        if(type('') == type(value)):
            self.base_type = 'string'
        elif(type(0) == type(value)):
            self.base_type = 'integer'
        elif(type(1.1) == type(value)):
            self.base_type = 'float'
        elif(type([]) == type(value)):
            self.base_type = 'list'
        elif(type({}) == type(value)):
            self.base_type = 'dictionary'
        elif(type((0,1)) == type(value)):
            self.base_type = 'tuple'
        else:
            self.base_type = 'unknown'
        
        # Save the value
        self.value = value
        self.timestamp.append(datetime.datetime.now())
        self.history.append(value)
        self.base_types.append(self.base_type)

        self.prepend_spaces = 0
        self.postpend_spaces = 0

    def print_as_columns(self,number_of_columns):
        counter = 0

        column_spaces = []

        for column in range(0,number_of_columns):
            column_spaces.append(0)

        counter = 0
        for value in self.value:
            remainder = counter % number_of_columns

            temp_length = 0
            if('\x1b[' in value[0:4] and '\x1b[0m' in value):
                #print("front: " + str(value[0:4].index('\x1b[')) + "\tend: " + str(value.index('\x1b[0m')) + "\t value:" + value[value.index('m')+1:value.index('\x1b[0m')])
                temp_length = value.index('\x1b[0m') - value.index('m') + 1

                if(column_spaces[remainder] < temp_length):
                    column_spaces[remainder] = temp_length
                    #print("Updating remainder " + str(remainder) + " length to be " + str())
                
            else:
                if(column_spaces[remainder] < len(value)):
                    column_spaces[remainder] = len(value)

            counter += 1

        counter = 0
        for value in self.value:
            remainder = counter % number_of_columns

            if('\x1b[' in value[0:4] and '\x1b[0m' in value):
                temp_len = value.index('\x1b[0m') - value.index('m') - 1# + 1
            else:
                temp_len = len(str(value))
            ans = ''

            while(len(ans) < (column_spaces[remainder]) - temp_len):
                ans += ' '

            print(ans + value + "\t",end="")

            #print("|" + str(counter) + "|",end= "")

            if(counter % number_of_columns == (number_of_columns - 1)):
                print("")

            counter += 1

    def set_prepend_spaces(self,prepend_spaces):
        self.prepend_spaces = prepend_spaces

    def set_postpend_spaces(self,postpend_spaces):
        self.postpend_spaces = postpend_spaces

    def set_value(self,value):

        # Capture the base type
        if(type('') == type(value)):
            self.base_type = 'string'
        elif(type(0) == type(value)):
            self.base_type = 'integer'
        elif(type(1.1) == type(value)):
            self.base_type = 'float'
        elif(type([]) == type(value)):
            self.base_type = 'list'
        elif(type({}) == type(value)):
            self.base_type = 'dictionary'
        elif(type((0,1)) == type(value)):
            self.base_type = 'tuple'
        else:
            self.base_type = 'unknown'
        
        # Save the value
        self.value = value
        self.timestamp.append(datetime.datetime.now())
        self.history.append(value)
        self.base_types.append(self.base_type)

    def add_value(self,value):
        if(self.base_type != 'list'):
            print(" Datatype is " + self.base_type + " not list.  Only lists are supported to be printed as columns.")
        else:
            self.value.append(value)

    def get_printstring(self):
        temp_len = len(str(self.value))

        while(len(ans) < (len(str(self.value)) - self.prepend_spaces)):
            ans += ' '

        return ans + str(self.value)

    def get_value(self):
        return value
