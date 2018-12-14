# PRETty
"PRinter Exploiration Toolkit" LAN automation tool

![alt text](https://github.com/BusesCanFly/PRETty/blob/master/PRETty.png "PRETTy")


# GUIDE:

## Installation
1. Install [PRET](https://github.com/RUB-NDS/PRET) and all required dependencies
2. Install requirements: `sudo pip install os time termcolor`
3. Navigate to [PRET](https://github.com/RUB-NDS/PRET) location: `cd $PRET`
4. Install PRETty into PRET: `git clone https://github.com/BusesCanFly/PRETty`
5. Rename PRETty (because folders have same name \_(._.)_/) `sudo mv ./PREtty ./PRETTY`
6. Navigate to PRETty: `cd PRETTTY`
7. Move PRETty to PRET: `sudo mv PRETty ../`
8. Make PRETty executable: `chmod +x PRETty.py`
* One line variant: `sudo pip install os time termcolor && cd $PRET && git clone https://github.com/BusesCanFly/PRETty && sudo mv ./PREtty ./PRETTY && cd PRETTU && sudo mv PRETty ../ && chmod +x PRETty.py`

## Lists
* PRETty automatically scans the LAN for HP printers and creates an IP list for itself
	* However, you can place custom IP lists in `PRETty/IP/`
* PRETty comes with pre-made command files for PRET located in `PRETty/commands/`
	* However, you can place additional command files in `PRETty/IP/`

## Usage
1. Run PRETty with `./PRETty.py` and follow the prompts

## Disclaimer
### The standard internet fun disclaimer applies. Don't commit crimes, be responsible. 
### I am in no way responsible for any and everything you do with PRETty. 
The code is gross, noob-y and inefficient. But it works, and it's my first "real" project. So i'm prood :D
