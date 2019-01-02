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
	interface= raw_input("Wireless interface name: [wlan0/wlp58s0] ")
	set_ip_range = raw_input("Set IP range for scanning? [y/N] ")

	if set_ip_range == str('y'):
		ip_range = str("-r ") + str(raw_input("IP range: [ex. 192.168.0.0/16] "))
	else:
		ip_range = ''

	cprint("Ctrl+C when scan is ready (more time for larger networks)", 'green')
	sleep(2.5)
	print('sudo netdiscover ' + ip_range + ' -i '+ interface +' '+ ' | grep "Hewlett Packard" > ./IP/list')
	cprint('Successfully processed IP\'s', 'green')
	os.system('cat ./IP/list | sort -u > ./IP/uniq_list &&  awk \'{print $1}\' ./IP/uniq_list > ./IP/HP_list')
	sleep(2.5)
	cprint('Successfully cleaned raw data', 'green')
	os.system('rm ./IP/list && rm ./IP/uniq_list')

list_answer = str(raw_input("Use default IP list? [Y/n] "))
if list_answer == str('n'):
	cprint('Example IP lists can be found in in ./IP', 'green')
	list = './IP/' + str(raw_input("Which list? ./IP/"))
else:
        cprint('Using "./IP/HP_list" as IP range', 'green')
        list = str('./IP/HP_list')


commands_list = str(raw_input("Use default command list? [Y/n] "))
if commands_list == str('n'):
	cprint('Example command lists can be found in ./commands', 'green')
        commands_list = './commands/' + str(raw_input("Which command list? "+'./commands/'))
else:
        cprint('Using "./commands/pret_pagecount.txt" as commands', 'green')
        commands_list = str('./commands/pret_pagecount.txt')

debug = raw_input('Enable PRET debug mode? [y/N]')
if debug == str('y'):
        debug_enabled = str('-d')
else:
        debug_enabled = ''

shell_type = raw_input("Shell Type: [ps, pjl, pcl] ")

with open(list) as inf:
        lines = [line.strip() for line in inf]
#print(lines)

i=0
while i < len(lines):
	os.system('../pret.py '+debug_enabled+' -i '+commands_list+' -q '+lines[i]+' '+ shell_type)
	#print('../pret.py '+debug_enabled+' -i '+commands_list+' -q '+lines[i]+' '+ shell_type)
	i+=1
