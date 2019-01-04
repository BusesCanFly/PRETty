#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from time import sleep
from termcolor import colored, cprint
main_color = str('green')
sub_color = str('blue')

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
cprint("  BusesCanFly   		  			50 52 45 54 74 79       ", sub_color)
cprint("--------------------------------------------------------------------------------", 'red')
cprint("              \"PRinter Exploitation Toolkit\" LAN automation tool              ", 'white')
cprint("--------------------------------------------------------------------------------", 'red')
cprint("Step 1: Generate IP list", 'yellow')
cprint("Step 2: Select IP list", 'yellow')
cprint("Step 3: Select PRET command input file", 'yellow')
cprint("Step 4: Select shell type", 'yellow')
cprint("Step 5: Observe all laws and ethical/moral codes :D", 'yellow')
cprint("Step 6: >:)", 'yellow')

gen_new= str(raw_input("Generate new IP list? [y/N] "))
if gen_new == str('y'):
	interface= raw_input("Wireless interface name: [ex. wlan0/wlp58s0] ")

	set_ip_range = raw_input("Set IP range for scanning? [y/N] ")
	if set_ip_range == str('y'):
		ip_range = str("-r ") + str(raw_input("IP range: [ex. 192.168.0.0/16] "))
	else:
		ip_range = ''
	cprint("Ctrl+C after 10-30 seconds to finish scanning (more time for larger networks)", 'green')
        sleep(2.5)
	os.system('sudo netdiscover ' + ip_range + ' -i '+ interface +' '+ ' | grep -wi \'Hewlett\|Brother\|Keyocera\' > ./IP/list')
	cprint('Received '+ str(sum(1 for line in open ('./IP/list'))) + ' ARP requests', 'yellow')
	sleep(1.5)
	cprint('Successfully collected IP\'s', 'green')
	os.system('awk \'{print $1}\' ./IP/list | sort -u > ./IP/HP_list')
	sleep(1.5)
        cprint('Successfully processed raw data', 'green')
        os.system('rm ./IP/list')
        sleep(1.5)
	cprint('\nLocated '+ str(sum(1 for line in open ('./IP/HP_list'))) +' printers, storing as ./IP/HP_list\n', 'yellow')

list_answer = str(raw_input("Use default IP list? [Y/n] "))
if list_answer == str('n'):
	cprint('Example IP lists can be found in in ./IP', 'green')
	list = './IP/' + str(raw_input("Which list? ./IP/"))
	cprint('\nLoaded '+ str(sum(1 for line in open (list))) +' IP\'s\n', 'yellow')
else:
        cprint('Using "./IP/HP_list" as IP range', 'green')
        list = str('./IP/HP_list')
	cprint('\nLoaded '+ str(sum(1 for line in open ('./IP/HP_list'))) +' IP\'s\n', 'yellow')

commands_list = str(raw_input("Use default ./commands/pret_pagecount.txt command file? [Y/n] "))
if commands_list == str('n'):
	cprint('Example command lists: ( ./commands)', 'green')
	os.system('ls ./commands/')
	print('\n')
	commands_list = './commands/' + str(raw_input("Which command list? "+'./commands/'))
	cprint('Commands: ', 'green')
	os.system('cat '+commands_list)
	print('\n')
else:
        cprint('Using "./commands/pret_pagecount.txt" as commands', 'green')
        commands_list = str('./commands/pret_pagecount.txt')
	cprint('Commands: ', 'green')
	os.system('cat ./commands/pret_pagecount.txt')
	print('\n')

debug = raw_input('Enable PRET debug mode? [y/N]')
if debug == str('y'):
        debug_enabled = str('-d')
else:
        debug_enabled = ''

shell_type = raw_input("Shell Type: [ps, pjl, pcl] ")

with open(list) as inf:
        lines = [line.strip() for line in inf]

i=0
while i < len(lines):
	os.system('../pret.py '+debug_enabled+' -i '+commands_list+' -q '+lines[i]+' '+ shell_type)
	#print('../pret.py '+debug_enabled+' -i '+commands_list+' -q '+lines[i]+' '+ shell_type)
	i+=1
