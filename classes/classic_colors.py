class ClassicColor:
    # 37m is the color code for White - setting that as the default
    def __init__(self,name='white',value='37m',text_affect='normal'):
        self.name = name
        self.value = value

        self.text_affects = {}
        self.text_affects['normal'] = ''
        self.text_affects['bold'] = '1;'
        self.text_affects['disabled'] = '2;'
        self.text_affects['italic'] = '3;'
        self.text_affects['underlined'] = '4;'
        self.text_affects['reverse'] = '7;'
        self.text_affects['strike through'] = '8;'
        self.text_affects['invisible'] = '9;'

        self.text_affect = text_affect

        # Default the text affect to normal if an invalid value is passed in
        if(text_affect not in list(self.text_affects.keys())):
            self.text_affect = 'normal'

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_text_affect(self):
        return self.text_affect

    def get_output(self):
        return self.value

    def print_color(self,string='',end='\n'):
        print('\x1b[' + self.value + string + '\x1b[0m',end)

    def colored(self,string):
        return '\x1b[' + self.value + string + '\x1b[0m'

