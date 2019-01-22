#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import argparse
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
cprint("  BusesCanFly   		  			    76 33 2e 30        ", sub_color)
cprint("-------------------------------------------------------------------------------", line_color)
cprint("              \"PRinter Exploitation Toolkit\" LAN automation tool             ", 'white')
cprint("-------------------------------------------------------------------------------", line_color)
cprint("Step 1: Generate IP list", 'yellow')
cprint("Step 2: Select IP list", 'yellow')
cprint("Step 3: Select PRET command input file", 'yellow')
cprint("Step 4: Select shell type", 'yellow')
cprint("Step 5: Observe all laws and ethical/moral codes :D", 'yellow')
cprint("Step 6: >:)\n", 'yellow')

parser = argparse.ArgumentParser()
parser.add_argument('--cli', dest='cli', action='store_true',
                    help='Enable CLI mode (No user input)')
parser.add_argument('-r', '--ip_range', type=str, default='--localnet',
                    help='IP range to scan')
parser.add_argument('-c', '--commands_list', type=str, default='./commands/pret_pagecount.txt',
                    help='File for PRET commands')
parser.add_argument('-s', '--shell_type', type=str, default='ps',
                    help='Printer shell type for PRET')

args = parser.parse_args()

sleep_time=1.5
def PrinterLogSort():
	os.system('tshark -r ./IP/scan.pcap > ./IP/pcap.txt')
        os.system('cat ./IP/pcap.txt | grep -iE "Hewlett|Brother|Kyocera|Laserjet" > ./IP/raw_list')
        os.system('awk \'{print $8}\' ./IP/raw_list > ./IP/Printer_list')
        sleep(sleep_time)
        cprint('Successfully processed raw data', 'green')
        os.system('rm -rf ./IP/scan.pcap && rm -rf ./IP/pcap.txt && rm -rf ./IP/raw_list')
        sleep(sleep_time)
        cprint('Cleaned raw data', 'green')
        sleep(sleep_time)
        cprint('\nLocated '+ str(sum(1 for line in open ('./IP/Printer_list'))) +' printers, storing as ./IP/Printer_list\n', 'yellow')

def PRETty_Interactive():
	sleep_time=1.5
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

		PrinterLogSort()

	list_answer = str(raw_input("Use default IP list? [Y/n] "))
	if list_answer == str('n'):
		cprint('An example IP list can be found at ./IP/example', 'green')
		cprint('Available IP lists: ', 'green')
	        os.system('ls ./IP/')
	        print('\n')
		list = './IP/' + str(raw_input("Which list? ./IP/"))
		cprint('\nLoaded '+ str(sum(1 for line in open (list))) +' IP\'s\n', 'yellow')
	else:
	        cprint('Using "./IP/Printer_list" as IP range', 'green')
	        list = str('./IP/Printer_list')
		cprint('\nLoaded '+ str(sum(1 for line in open ('./IP/Printer_list'))) +' IP\'s\n', 'yellow')

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

def PRETty_cli():
	sleep_time=0.5
        os.system('sudo arp-scan -g '+args.ip_range+' -W ./IP/scan.pcap')
	PrinterLogSort()
	sleep(1)
	list = './IP/Printer_list'
        with open(list) as inf:
                lines = [line.strip() for line in inf]
        i=0
        while i < len(lines):
                os.system('../pret.py -i ./commands/'+args.commands_list+' -q '+lines[i]+' '+ args.shell_type)
                i+=1

if args.cli:
	PRETty_cli()
else:
	PRETty_Interactive()
