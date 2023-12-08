
import os,sys

if(sys.platform.lower().startswith('linux')):
    OS_TYPE = 'linux'
elif(sys.platform.lower().startswith('mac')):
    OS_TYPE = 'macintosh'
elif(sys.platform.lower().startswith('win')):
    OS_TYPE = 'windows'
else:
    OS_TYPE = 'invalid'

# Get our current directory
OUTPUT_FILE_DIRECTORY = os.getcwd()

def find_all(a_str, sub):
    """
    Returns the indexes of {sub} where they were found in {a_str}.  The values
    returned from this function should be made into a list() before they can
    be easily used.
    Last Update: 03/01/2017
    By: LB023593
    """

    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1

# Create variables for all the paths
if((OS_TYPE == 'windows')):
    # Clear Screen Windows
    os.system('cls')
    directories = list(find_all(OUTPUT_FILE_DIRECTORY,'\\'))
    OUTPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\outputs\\'
    INPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\inputs\\'
    SCRIPTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\scripts\\'
    MODULES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\modules\\'
    CLASSES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\classes\\'
elif((OS_TYPE == 'linux') or (OS_TYPE == 'macintosh')):
    # Clear Screen Linux / Mac
    os.system('clear')
    directories = list(find_all(OUTPUT_FILE_DIRECTORY,'/'))
    OUTPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/outputs/'
    INPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/inputs/'
    SCRIPTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/scripts/'
    MODULES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/modules/'
    CLASSES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/classes/'

# OS Compatibility for importing Class Files
if((OS_TYPE == 'linux')):
    sys.path.insert(0,'../classes/')
elif((OS_TYPE == 'windows')):
    sys.path.insert(0,'..\\classes\\')

from everything_datatype import EverythingDataType
from constants import *

##a = EverythingDataType(['A'])
##a.add_value('B')

a = EverythingDataType([white.colored(' Tableau 10:')])
a.add_value(white.colored(' Tableau 20:'))
a.add_value(white.colored(' Earthtone:'))
a.add_value(white.colored(' Minecraft:'))
a.add_value(white.colored(' Minecraft:'))

a.add_value(tableau_10_blue.colored('Blue'))
a.add_value(tableau_20_blue.colored(tableau_20_blue.get_name().replace('Tableau 20 ','')))
a.add_value(earthtone_brown_grey.colored(earthtone_brown_grey.get_name().replace('Earthtone ','')))
a.add_value(minecraft_pink.colored(minecraft_pink.get_name().replace('Minecraft ','')))
a.add_value(minecraft_darker_grey.colored(minecraft_darker_grey.get_name().replace('Minecraft ','')))

a.add_value(tableau_10_brown.colored('Brown'))
a.add_value(tableau_20_light_green.colored(tableau_20_light_green.get_name().replace('Tableau 20 ','')))
a.add_value(earthtone_light_brown_grey.colored(earthtone_light_brown_grey.get_name().replace('Earthtone ','')))
a.add_value(minecraft_red.colored(minecraft_red.get_name().replace('Minecraft ','')))
a.add_value(minecraft_light_grey.colored(minecraft_light_grey.get_name().replace('Minecraft ','')))

a.add_value(tableau_10_orange.colored('Orange'))
a.add_value(tableau_20_brown.colored(tableau_20_brown.get_name().replace('Tableau 20 ','')))
a.add_value(earthtone_light_grey.colored(earthtone_light_grey.get_name().replace('Earthtone ','')))
a.add_value(minecraft_dark_red.colored(minecraft_dark_red.get_name().replace('Minecraft ','')))
a.add_value(minecraft_dark_grey.colored(minecraft_dark_grey.get_name().replace('Minecraft ','')))

a.add_value(tableau_10_pink.colored('Pink'))
a.add_value(tableau_20_grey.colored(tableau_20_grey.get_name().replace('Tableau 20 ','')))
a.add_value(earthtone_dark_brown.colored(earthtone_dark_brown.get_name().replace('Earthtone ','')))
a.add_value(minecraft_orange.colored(minecraft_orange.get_name().replace('Minecraft ','')))
a.add_value(minecraft_grey.colored(minecraft_grey.get_name().replace('Minecraft ','')))

a.add_value(tableau_10_green.colored('Green'))
a.add_value(tableau_20_light_blue.colored(tableau_20_light_blue.get_name().replace('Tableau 20 ','')))
a.add_value(earthtone_medium_brown.colored(earthtone_medium_brown.get_name().replace('Earthtone ','')))
a.add_value(minecraft_orange_2.colored(minecraft_orange_2.get_name().replace('Minecraft ','')))
a.add_value(minecraft_grey_brown.colored(minecraft_grey_brown.get_name().replace('Minecraft ','')))

a.add_value(tableau_10_grey.colored('Grey'))
a.add_value(tableau_20_red.colored(tableau_20_red.get_name().replace('Tableau 20 ','')))
a.add_value(earthtone_light_brown.colored(earthtone_light_brown.get_name().replace('Earthtone ','')))
a.add_value(minecraft_sand.colored(minecraft_sand.get_name().replace('Minecraft ','')))
a.add_value(minecraft_brown.colored(minecraft_brown.get_name().replace('Minecraft ','')))

#a.add_value(white.colored('uncoloredzzzzzzzzzz'))
#a.add_value('uncoloredzzzzzzzzzzzz')
a.add_value(tableau_10_red.colored('Red'))
a.add_value(tableau_20_light_baby_blue.colored(tableau_20_light_baby_blue.get_name().replace('Tableau 20 ','')))
a.add_value(earthtone_mauroon.colored(earthtone_mauroon.get_name().replace('Earthtone ','')))
a.add_value(minecraft_yellow.colored(minecraft_yellow.get_name().replace('Minecraft ','')))
a.add_value(minecraft_light_brown.colored(minecraft_light_brown.get_name().replace('Minecraft ','')))

a.add_value(tableau_10_yellow.colored('Yellow'))
a.add_value(tableau_20_light_brown.colored(tableau_20_light_brown.get_name().replace('Tableau 20 ','')))
a.add_value(earthtone_orange.colored(earthtone_orange.get_name().replace('Earthtone ','')))
a.add_value(minecraft_yellow_2.colored(minecraft_yellow_2.get_name().replace('Minecraft ','')))
a.add_value(minecraft_light_brown.colored(minecraft_light_brown.get_name().replace('Minecraft ','')))

a.add_value(tableau_10_purple.colored('Purple'))
a.add_value(tableau_20_yellow.colored(tableau_20_yellow.get_name().replace('Tableau 20 ','')))
a.add_value(earthtone_yellow.colored(earthtone_yellow.get_name().replace('Earthtone ','')))
a.add_value(minecraft_dark_green.colored(minecraft_dark_green.get_name().replace('Minecraft ','')))
a.add_value(minecraft_dark_grey_blue.colored(minecraft_dark_grey_blue.get_name().replace('Minecraft ','')))

a.add_value(tableau_10_teal.colored('Teal'))
a.add_value(tableau_20_orange.colored(tableau_20_orange.get_name().replace('Tableau 20 ','')))
a.add_value(earthtone_dark_green.colored(earthtone_dark_green.get_name().replace('Earthtone ','')))
a.add_value(minecraft_grey_green.colored(minecraft_grey_green.get_name().replace('Minecraft ','')))
a.add_value(minecraft_dark_purple.colored(minecraft_dark_purple.get_name().replace('Minecraft ','')))

a.add_value(tableau_10_teal.colored(''))
a.add_value(tableau_20_light_red.colored(tableau_20_light_red.get_name().replace('Tableau 20 ','')))
a.add_value(earthtone_green.colored(earthtone_green.get_name().replace('Earthtone ','')))
a.add_value(minecraft_green.colored(minecraft_green.get_name().replace('Minecraft ','')))
a.add_value(minecraft_purple.colored(minecraft_purple.get_name().replace('Minecraft ','')))

a.add_value(tableau_10_teal.colored(''))
a.add_value(tableau_20_pink.colored(tableau_20_pink.get_name().replace('Tableau 20 ','')))
a.add_value(earthtone_light_green.colored(earthtone_light_green.get_name().replace('Earthtone ','')))
a.add_value(minecraft_light_green.colored(minecraft_light_green.get_name().replace('Minecraft ','')))
a.add_value(minecraft_dark_magenta.colored(minecraft_dark_magenta.get_name().replace('Minecraft ','')))

a.add_value(tableau_10_teal.colored(''))
a.add_value(tableau_20_light_yellow.colored(tableau_20_light_yellow.get_name().replace('Tableau 20 ','')))
a.add_value(earthtone_dark_grey_blue.colored(earthtone_dark_grey_blue.get_name().replace('Earthtone ','')))
a.add_value(minecraft_blue.colored(minecraft_blue.get_name().replace('Minecraft ','')))
a.add_value(minecraft_light_magenta.colored(minecraft_light_magenta.get_name().replace('Minecraft ','')))

a.add_value(tableau_10_teal.colored(''))
a.add_value(tableau_20_light_orange.colored(tableau_20_light_orange.get_name().replace('Tableau 20 ','')))
a.add_value(earthtone_grey_blue.colored(earthtone_grey_blue.get_name().replace('Earthtone ','')))
a.add_value(minecraft_teal.colored(minecraft_teal.get_name().replace('Minecraft ','')))
a.add_value(minecraft_light_grey_purple.colored(minecraft_light_grey_purple.get_name().replace('Minecraft ','')))

a.add_value(tableau_10_teal.colored(''))
a.add_value(tableau_20_purple.colored(tableau_20_purple.get_name().replace('Tableau 20 ','')))
a.add_value(earthtone_light_grey_blue.colored(earthtone_light_grey_blue.get_name().replace('Earthtone ','')))
a.add_value(minecraft_dark_teal.colored(minecraft_dark_teal.get_name().replace('Minecraft ','')))
a.add_value(minecraft_grey_purple.colored(minecraft_grey_purple.get_name().replace('Minecraft ','')))

a.add_value('')
a.add_value(tableau_20_light_pink.colored(tableau_20_light_pink.get_name().replace('Tableau 20 ','')))
a.add_value('')
a.add_value(minecraft_light_teal.colored(minecraft_light_teal.get_name().replace('Minecraft ','')))
a.add_value('')

a.add_value('')
a.add_value(tableau_20_baby_blue.colored(tableau_20_baby_blue.get_name().replace('Tableau 20 ','')))
a.add_value('')
a.add_value('')
a.add_value('')

a.add_value('')
a.add_value(tableau_20_green.colored(tableau_20_green.get_name().replace('Tableau 20 ','')))
a.add_value('')
a.add_value('')
a.add_value('')

a.add_value('')
a.add_value(tableau_20_light_purple.colored(tableau_20_light_purple.get_name().replace('Tableau 20 ','')))
a.add_value('')
a.add_value('')
a.add_value('')

a.add_value('')
a.add_value(tableau_20_dark_grey.colored(tableau_20_dark_grey.get_name().replace('Tableau 20 ','')))
a.add_value('')
a.add_value('')
a.add_value('')

a.add_value('')
a.add_value(tableau_20_light_baby_blue.colored(tableau_20_light_baby_blue.get_name().replace('Tableau 20 ','')))
a.add_value('')
a.add_value('')
a.add_value('')
#a.add_value(tableau_10_blue.colored('blue'))

a.print_as_columns(5)
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()
##a.add_value()

print("")

b = EverythingDataType(['Column 1'])
b.add_value('Column 2')
b.add_value('Column 3')
b.add_value('Column 4')

b.add_value('')
b.add_value('')
b.add_value('Luke')
b.add_value('')

b.add_value('Eleanor Jenavieve Brady')
b.add_value('')
b.add_value('')
b.add_value('')

b.add_value('')
b.add_value('')
b.add_value('')
b.add_value('James')

b.add_value('')
b.add_value('Bonnie Jean')
b.add_value('')
b.add_value('')

b.print_as_columns(4)
