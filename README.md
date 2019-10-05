# PRETty
"PRinter Exploitation Toolkit" LAN automation tool
(It's just a python wrapper for PRET)
![alt text](https://github.com/BusesCanFly/PRETty/blob/master/screenshot.png "Who doesn't love ASCII art?")

PRETty is useful when a large number of printers are present on a network. Instead of scanning, logging, and manually running PRET againt each individual printer, PRETty will automatically discover and run choosen PRET payloads against all printers on the target network.

Additionally, PRETty can be used to automate command/payload delivery to any given list of printers (See the "Lists" section)

# GUIDE:

## Installation
1. Install [PRET](https://github.com/RUB-NDS/PRET) and all required dependencies
2. Install requirements: `sudo pip install -U argparse termcolor` and `sudo apt -y install arp-scan tshark`
3. Navigate to where you installed [PRET](https://github.com/RUB-NDS/PRET): `cd PRET`
4. Install PRETty into [PRET](https://github.com/RUB-NDS/PRET): `git clone https://github.com/BusesCanFly/PRETty`
5. Navigate to PRETty: `cd PRETty`
6. Make PRETty executable: `chmod +x PRETty.py`
* One line variant (from [PRET](https://github.com/RUB-NDS/PRET) folder): `sudo apt -y install arp-scan tshark && sudo pip install -U argparse termcolor && git clone https://github.com/BusesCanFly/PRETty && cd PRETty && chmod +x PRETty.py`
* One line variant w/ [PRET](https://github.com/RUB-NDS/PRET) installation: `sudo apt -y install imagemagick ghostscript arp-scan tshark && sudo pip install -U argparse termcolor colorama pysnmp && git clone https://github.com/RUB-NDS/PRET && cd PRET && git clone https://github.com/BusesCanFly/PRETty && cd PRETty && chmod +x PRETty.py`

## Lists
* PRETty automatically scans the LAN for HP/Brother/Kyocera printers and creates an IP list for itself
	* However, you can place custom IP lists in `PRETty/IP/`
* PRETty comes with pre-made command list files for PRET located in `PRETty/commands/`
	* However, you can place additional command list files in `PRETty/commands/`
	
## Usage
* Run PRETty with `./PRETty.py` and follow the prompts :D
* For more advanced users, run `./PRETty.py -h`
	* `./PRETty.py --cli` enables CLI mode. (No user input required)
	* The default `./PRETty.py --cli` will scan the current LAN, and run `./commands/pret_pagecount.txt` on every printer found
	* (optional) Additional arguments are: `-r [IP range to scan] -c [Name of command list file to use] -s [PRET shell type]`

## Disclaimers
### The standard internet fun disclaimer applies. Don't commit crimes, be responsible. 
### I am in no way responsible for anything and everything you do with PRETty.

## Links
PRETty has been seen in:
* https://www.kitploit.com/2019/01/pretty-printer-exploitation-toolkit-lan.html
* https://www.hack4.net/2019/01/pretty-printer-exploitation-toolkit-lan.html
* https://moretip.com/pretty/
* https://hackertor.com/tag/pretty/
* http://fullcrypters.net/pretty-ferramenta-de-automacao-de-lan-printer-exploitation-toolkit/
* https://www.chainnews.com/articles/860508131277.htm
* https://www.reddit.com/r/blackhat/comments/ad7hre/printer_exploitation_toolkit_lan_automation_tool/
* https://twitter.com/netbiosX/status/1081855584260030464

_Thank you!_

--
VGhlIGNvZGUgaXMgZ3Jvc3MsIG5vb2IteSBhbmQgaW5lZmZpY2llbnQuIEJ1dCBpdCB3b3JrcywgYW5kIGl0J3MgbXkgZmlyc3QgcmVhbCBwcm9qZWN0LiBTbyBJJ20gcHJvdWQgOkQKClRoaXMgaXMgYSBmb3IgbG9vcC4gVGhlIG9ubHkgcGFydCBvZiB0aGlzIGNvZGUgdGhhdCBtYXR0ZXJzIGlzIGF0IHRoZSBib3R0b20uCgpodHRwczovL3R3aXR0ZXIuY29tL0J1c2VzQ2FuRmx5L3N0YXR1cy8xMDgwOTQ5OTkzMTgyMjk0MDE3
--
