from ReadWriteMemory import ReadWriteMemory
import win32process
import win32api
import psutil
import time
from bs4 import BeautifulSoup 
import requests

print("          -----------ETS2 MONEY SYNC WITH VTM LIVE-----------")
print("----This script will sync ets 2 money with the money on your vtm live profile----")
print("----In order for this script to work you need to start ets2 in 32bit----")
url = input("Please insert your profile link:")
source = requests.get(url).text
soup =  BeautifulSoup(source, "lxml")
bank = soup.find("tr")
money =  bank.find("td").find_next_sibling("td").text
numbers = money.translate({ord(i): None for i in "€$£"})
print("Value to set is:" + numbers)
value = int(float(numbers))
my_pid = None
pids = psutil.pids()
for pid in pids:
    ps = psutil.Process(pid)
    if "eurotrucks2.exe" in ps.name():
        my_pid = ps.pid
        print("Process pid:")
        print(my_pid)
PROCESS_ALL_ACCESS = 0x1F0FFF
processHandle = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, my_pid)
modules = win32process.EnumProcessModules(processHandle)
processHandle.close()
base_addr = modules[0] # first item on the list 
#print(hex(base_addr))
def main():
    base_address = hex(base_addr)  #base address of the exe (find out with pymem)
    u = int(base_address, 0)
    static_address_offset =  0x0001338C90
    pointer_static_address =  u + static_address_offset  #eurotrucks2.exe + .....
    offsets = [0x0C, 0x10] #list offsets
   

    rmw = ReadWriteMemory()
    process = rmw.get_process_by_name("eurotrucks2.exe")
    process.open()
    my_pointer = process.get_pointer(pointer_static_address, offsets=offsets)
    pointer_value = process.read(my_pointer)
    #print(pointer_value)
    process.write(my_pointer, value)
    #time.sleep(5)
    #print(pointer_value)
    print("Value set, try opening the bank or progress history, to refresh the value")
    
main()
