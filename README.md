# VTMLiveSyncMoney
This small python script syncs your profile money from http://virtualtruckingmanager.com/ to your ingame money

Tested on Windows10 21H1 and using 
Python 3.7.3 (64bit) with Euro Truck Simulator 2 32 bit v1.40.5.1

The script only works if the game is ran on 32bit mode, the pointer has been found for that mode, it doesnt work on 64bit + ReadWriteMemory has problems reading and writing 64 bit addresses
Future updates might ruin both the pointer and the script

I also inclued a cheat table that has the money pointer

Use:
pip install -r requirements.txt 

to install all the required modules
