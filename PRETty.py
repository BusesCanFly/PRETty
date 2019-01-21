#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from time import sleep
from termcolor import colored, cprint
main_color = str('green')
sub_color = str('blue')
line_color = str('red')

cprint(" ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ", main_color)
cprint("▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌ ", main_color)
cprint("▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌ ", main_color)
cprint("▐░▌       ▐░▌▐░▌       ▐░▌▐░▌               ▐░▌          ▐░▌     ▐░▌       ▐░▌ ", main_color)
cprint("▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌          ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌ ", main_color)
cprint("▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌          ▐░▌     ▐░░░░░░░░░░░▌ ", main_color)
cprint("▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌          ▐░▌      ▀▀▀▀█░█▀▀▀▀  ", main_color)
cprint("▐░▌          ▐░▌     ▐░▌  ▐░▌               ▐░▌          ▐░▌          ▐░▌      ", main_color)
cprint("▐░▌          ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌          ▐░▌          ▐░▌      ", main_color)
cprint("▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌          ▐░▌          ▐░▌      ", main_color)
cprint(" ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀            ▀            ▀       ", main_color)
cprint("  BusesCanFly   		  			50 52 45 54 74 79      ", sub_color)
cprint("-------------------------------------------------------------------------------", line_color)
cprint("              \"PRinter Exploitation Toolkit\" LAN automation tool             ", 'white')
cprint("-------------------------------------------------------------------------------", line_color)
cprint("Step 1: Generate IP list", 'yellow')
cprint("Step 2: Select IP list", 'yellow')
cprint("Step 3: Select PRET command input file", 'yellow')
cprint("Step 4: Select shell type", 'yellow')
cprint("Step 5: Observe all laws and ethical/moral codes :D", 'yellow')
cprint("Step 6: >:)\n", 'yellow')

gen_new= str(raw_input("Generate new IP list? [y/N] "))
if gen_new == str('y'):

	set_ip_range = raw_input("Set IP range for scanning? [y/N] ")
	if set_ip_range == str('y'):
		ip_range = str(raw_input("IP range: [ex. 192.168.0.0/16] "))
	else:
		ip_range = '--localnet'

	cprint("ARP scanning LAN for devices...", 'green')
        sleep(1.5)
	os.system('sudo arp-scan -g '+ip_range+' -W ./IP/scan.pcap')
	cprint('Successfully collected IP\'s', 'green')
	os.system('tshark -r ./IP/scan.pcap > ./IP/pcap.txt')
	os.system('cat ./IP/pcap.txt | grep -iE "Hewlett|Brother|Kyocera|Laserjet" > ./IP/printer_list')
	os.system('awk \'{print $8}\' ./IP/printer_list > ./IP/HP_list')
	sleep(1.5)
	cprint('Successfully processed raw data', 'green')
        os.system('rm -rf ./IP/scan.pcap && rm -rf ./IP/pcap.txt && rm -rf ./IP/printer_list')
	sleep(1.5)
	cprint('Cleaned raw data', 'green')
	sleep(1.5)
	cprint('\nLocated '+ str(sum(1 for line in open ('./IP/HP_list'))) +' printers, storing as ./IP/HP_list\n', 'yellow')

list_answer = str(raw_input("Use default IP list? [Y/n] "))
if list_answer == str('n'):
	cprint('An example IP list can be found at ./IP/example', 'green')
	cprint('Available IP lists: ', 'green')
        os.system('ls ./IP/')
        print('\n')
	list = './IP/' + str(raw_input("Which list? ./IP/"))
	cprint('\nLoaded '+ str(sum(1 for line in open (list))) +' IP\'s\n', 'yellow')
else:
        cprint('Using "./IP/HP_list" as IP range', 'green')
        list = str('./IP/HP_list')
	cprint('\nLoaded '+ str(sum(1 for line in open ('./IP/HP_list'))) +' IP\'s\n', 'yellow')

commands_list = str(raw_input("Use default ./commands/pret_pagecount.txt command file? [Y/n] "))
if commands_list == str('n'):
	cprint('Example command lists: (./commands)', 'green')
	os.system('ls ./commands/')
	print('\n')
	commands_list = './commands/' + str(raw_input("Which command list? "+'./commands/'))
	cprint('Commands: ', 'green')
	os.system('cat '+commands_list)
	print('\n')
else:
        cprint('Using "./commands/pret_pagecount.txt" as PRET commands', 'green')
        commands_list = str('./commands/pret_pagecount.txt')
	cprint('Commands: ', 'yellow')
	os.system('cat ./commands/pret_pagecount.txt')
	print('\n')

shell_type = raw_input("Shell Type: [ps, pjl, pcl] ")

debug = raw_input('Enable PRET debug mode? [y/N] ')
if debug == str('y'):
        debug_enabled = str('-d')
else:
        debug_enabled = ''
print('')

with open(list) as inf:
        lines = [line.strip() for line in inf]

i=0
while i < len(lines):
	os.system('../pret.py '+debug_enabled+' -i '+commands_list+' -q '+lines[i]+' '+ shell_type)
	i+=1
