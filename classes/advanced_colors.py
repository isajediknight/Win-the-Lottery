class AdvancedColor:

    # 0 is the RGB color code for White - setting that as the default
    def __init__(self,name='white',red='0',green='0',blue='0',ansi_1='0',ansi_2='38',ansi_3='2'):
        self.name = str(name)
        self.ansi_1 = str(ansi_1)
        self.ansi_2 = str(ansi_2)
        self.ansi_3 = str(ansi_3)
        self.red = str(red)
        self.green = str(green)
        self.blue = str(blue)

    def get_name(self):
        return self.name

    def get_red(self):
        return self.red

    def get_green(self):
        return self.green

    def get_blue(self):
        return self.blue

    def get_output(self):
        return ''

    def print_color(self,string='',end='\n'):
        print('\x1b[' + self.ansi_1 + ';'+ self.ansi_2 + ';' + self.ansi_3 + ';' + self.red + ';' + self.green + ';' + self.blue +'m' + string + '\x1b[0m',end)

    def colored(self,string=''):
        return '\x1b[' + self.ansi_1 + ';'+ self.ansi_2 + ';' + self.ansi_3 + ';' + self.red + ';' + self.green + ';' + self.blue +'m' + string + '\x1b[0m'
