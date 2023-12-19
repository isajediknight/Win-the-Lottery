import os,sys

from multiprocessing import Lock, Process, Queue, current_process
import time
import queue # imported for using queue.Empty exception

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
    #os.system('cls')
    directories = list(find_all(OUTPUT_FILE_DIRECTORY,'\\'))
    OUTPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\outputs\\'
    INPUTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\inputs\\'
    SCRIPTS_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\scripts\\'
    MODULES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\modules\\'
    CLASSES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\classes\\'
    SAVES_DIR = OUTPUT_FILE_DIRECTORY[:directories[-1]] + '\\saves\\'
elif((OS_TYPE == 'linux') or (OS_TYPE == 'macintosh')):
    # Clear Screen Linux / Mac
    #os.system('clear')
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

class FindBitcoins:
    def __init__(self,processes=2,tasks=5):
        self.processes = processes
        self.tasks = tasks

        self.tasks_to_accomplish = Queue()
        self.tasks_that_are_done = Queue()

        self.processes = []

        self.list_of_addresses = []

        self.list_of_1 = []
        self.list_of_3 = []
        self.list_of_bc1 = []
        self.list_of_others = []

        self.list_of_public_P2WPKH = []
        self.list_of_public_P2WSH = []
        

        counter = 0
        readfile = open('D:\\GitHub_Repos\\Win-the-Lottery\\inputs\\blockchair_bitcoin_addresses_latest.tsv','r')
        for line in readfile:
            address = line.strip().split('\t')[0]

            if(address[0] == '1'):
                self.list_of_1.append(address)
            elif(address[0] == '3'):
                self.list_of_3.append(address)
            elif(address[0:3] == 'bc1'):
                self.list_of_bc1.append(address)
            else:
                self.list_of_others.append(address)
            counter += 1

##            if(counter > 1000):
##                break
            
        readfile.close()

        self.set_of_1 = set(self.list_of_1)
        self.set_of_3 = set(self.list_of_3)
        self.set_of_bc1 = set(self.list_of_bc1)
        self.set_of_others = set(self.list_of_others)

    def gen_addr(self):
        list_of_1 = []
        list_of_1_compressed = []
        list_of_3 = []
        list_of_bc1 = []
        list_of_others = []
        list_of_public_P2WSH = []
        list_of_public_P2WPKH = []
        
        list_of_private_hex = []
        list_of_private_wif = []
        list_of_private_wifc = []
        for runner in range(0,2000):
            wallet = Wallet()
            list_of_1.append(wallet.address.get_mainnet_public_address_1())
            list_of_1_compressed.append(wallet.address.get_mainnet_public_address_1_compressed())
            list_of_3.append(wallet.address.get_mainnet_public_address_3())
            list_of_public_P2WPKH.append(wallet.address.get_mainnet_public_P2WPKH())
            list_of_public_P2WSH.append(wallet.address.get_mainnet_public_P2WSH())
            list_of_private_hex.append(wallet.address.key.get_hex())
            list_of_private_wif.append(wallet.address.key.get_mainnet_wif())
            list_of_private_wifc.append(wallet.address.key.get_mainnet_wifc())

        set_of_1 = set(list_of_1)
        set_of_1_compressed = set(list_of_1_compressed)
        set_of_3 = set(list_of_3)
        set_of_bc1_P2WPKH = set(list_of_public_P2WPKH)
        set_of_bc1_P2WSH = set(list_of_public_P2WSH)
        print("Comparing")
        condition_1 = len(self.set_of_1) > len(set(self.set_of_1 - set_of_1))
        print("1 Addresses")
        condition_2 = len(self.set_of_1) > len(set(self.set_of_1 - set_of_1_compressed))
        print("1 Addresses Compressed")
        condition_3 = len(self.set_of_3) > len(set(self.set_of_3 - set_of_3))
        print(" 3 Addresses")
        condition_4 = len(self.set_of_bc1) > len(set(self.set_of_bc1 - set_of_bc1_P2WPKH))
        print(" bc1 Addresses P2WPKH")
        condition_5 = len(self.set_of_bc1) > len(set(self.set_of_bc1 - set_of_bc1_P2WSH))
        print(" bc1 Addresses P2WSH")
        if(condition_1):
            for i in range(0,len(list_of_1)):
                if(list_of_1[i] in self.list_of_1):
                    try:
                        print(list_of_1[i])
                        print(list_of_1_compressed[i])
                        print(list_of_3[i])
                        print(list_of_public_P2WPKH[i])
                        print(list_of_public_P2WSH[i])
                        print(list_of_private_hex[i])
                        print(list_of_private_wif[i])
                        print(list_of_private_wifc[i])
                    except:
                        print("Error")
                        print(list_of_private_hex[i])
                        print(list_of_private_wif[i])
                        print(list_of_private_wifc[i])
        
        if(condition_2):
            for i in range(0,len(list_of_1_compressed)):
                if(list_of_1_compressed[i] in self.list_of_1_compressed):
                    try:
                        print(list_of_1[i])
                        print(list_of_1_compressed[i])
                        print(list_of_3[i])
                        print(list_of_public_P2WPKH[i])
                        print(list_of_public_P2WSH[i])
                        print(list_of_private_hex[i])
                        print(list_of_private_wif[i])
                        print(list_of_private_wifc[i])
                    except:
                        print("Error")
                        print(list_of_private_hex[i])
                        print(list_of_private_wif[i])
                        print(list_of_private_wifc[i])
        
        if(condition_3):
            for i in range(0,len(list_of_3)):
                if(list_of_3[i] in self.list_of_3):
                    try:
                        print(list_of_1[i])
                        print(list_of_1_compressed[i])
                        print(list_of_3[i])
                        print(list_of_public_P2WPKH[i])
                        print(list_of_public_P2WSH[i])
                        print(list_of_private_hex[i])
                        print(list_of_private_wif[i])
                        print(list_of_private_wifc[i])
                    except:
                        print("Error")
                        print(list_of_private_hex[i])
                        print(list_of_private_wif[i])
                        print(list_of_private_wifc[i])
        
        if(condition_4):
            for i in range(0,len(list_of_public_P2WPKH)):
                if(list_of_public_P2WPKH[i] in self.list_of_public_P2WPKH):
                    try:
                        print(list_of_1[i])
                        print(list_of_1_compressed[i])
                        print(list_of_3[i])
                        print(list_of_public_P2WPKH[i])
                        print(list_of_public_P2WSH[i])
                        print(list_of_private_hex[i])
                        print(list_of_private_wif[i])
                        print(list_of_private_wifc[i])
                    except:
                        print("Error")
                        print(list_of_private_hex[i])
                        print(list_of_private_wif[i])
                        print(list_of_private_wifc[i])
        
        if(condition_5):
            for i in range(0,len(list_of_public_P2WSH)):
                if(list_of_public_P2WSH[i] in self.list_of_public_P2WSH):
                    try:
                        print(list_of_1[i])
                        print(list_of_1_compressed[i])
                        print(list_of_3[i])
                        print(list_of_public_P2WPKH[i])
                        print(list_of_public_P2WSH[i])
                        print(list_of_private_hex[i])
                        print(list_of_private_wif[i])
                        print(list_of_private_wifc[i])
                    except:
                        print("Error")
                        print(list_of_private_hex[i])
                        print(list_of_private_wif[i])
                        print(list_of_private_wifc[i])

    def one_wallet(self):
        wallet = Wallet()
