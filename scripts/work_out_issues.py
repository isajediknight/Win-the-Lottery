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
    SAVES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\saves\\'
elif((OS_TYPE == 'linux') or (OS_TYPE == 'macintosh')):
    # Clear Screen Linux / Mac
    os.system('clear')
    directories = list(find_all(OUTPUT_FILE_DIRECTORY,'/'))
    OUTPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/outputs/'
    INPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/inputs/'
    SCRIPTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/scripts/'
    MODULES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/modules/'
    CLASSES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/classes/'
    SAVES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '/saves/'

# OS Compatibility for importing Class Files
if((OS_TYPE == 'linux')):
    sys.path.insert(0,'../classes/')
    sys.path.insert(0,'../modules/')
elif((OS_TYPE == 'windows')):
    sys.path.insert(0,'..\\classes\\')
    sys.path.insert(0,'..\\modules\\')

from benchmark import Benchmark

from bitcoinaddress2 import Wallet

maintime = Benchmark()

##print(wallet.address.get_public_key())
##print(wallet.address.get_public_key_compressed())
##print(wallet.address.get_mainnet_public_address_1())
##print(wallet.address.get_mainnet_public_address_1_compressed())
##print(wallet.address.get_mainnet_public_address_3())
##print(wallet.address.get_mainnet_public_P2WPKH())
##print(wallet.address.get_mainnet_public_P2WSH())

read_in_addresses = Benchmark()
readfile = open('D:\\BTC_Addresses\\Balances\\08-11-2017.csv','r')
counter = 0
address_list = []
for line in readfile:
    #if(counter % 100000 == 0):
    #    print(str(counter)+" "+maintime.current_benchmark_without_stopping())
    address_list.append(line.split(';')[0])
    counter += 1
readfile.close()
read_in_addresses.stop()
print(str(counter)+" Addresses read in " + read_in_addresses.human_readable_string_without_microseconds())
address_set = set(address_list)
for runner in range(0,10000):
    wallet = Wallet()
    if(wallet.address.get_mainnet_public_address_1() in address_set or wallet.address.get_mainnet_public_address_1_compressed() in address_set or wallet.address.get_mainnet_public_address_3() in address_set):
        print(wallet)
        print(wallet.address.get_public_key())
        print(wallet.address.get_mainnet_public_address_1())
    del wallet
maintime.stop()
print("Total runtime: "+maintime.human_readable_string_without_microseconds())
