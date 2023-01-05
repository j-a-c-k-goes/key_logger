# ⌨️ keylogger

## 👀 context

the keylogger is a background running process which listens for input from the keyboard, an input device. 
	   
this was an exploration in experiencing how a digital device ( the computer ) receives input from an input device ( a keyboard ), and how this connection stores, passes, and processes the data as information.

also, having a better awarenees of how a keylogger works.

## 🚀 launch sequence
* open a terminal window
* clone this repository
	- ( using github cli tools)
		+ `gh repo clone j-a-c-k-goes/key_logger`
	- ( download the .zip file )
* navigate to the directory
	- `cd ~/key_logger`
* activate virtual environment ( using poetry, in this case )
	- `poetry shell`
* run the script
	- `python3 main.py`
		+ *note: changing .py to .pyw to prevent a terminal window from opening when the script is run*
	- *you may receive a notification to allow for input monitoring. accepting this is neccessary for the logger to work.*
		+ you accepted, now you can type type anything...
		+ you declined, the program stops.

## 👀 where to find log file
* windows
	- `<os.environ['TEMP']>\keys.log`
* everwhere else
	- `/tmp/keys.log`
	
## 📣 disclaimer
it is known that keyloggers could reveal passwords or other sensitive information. 

however, this is not a keylogger for any nefarious purpose(s). 

*challenge: use the keylogger for a non-theft-or-syping purpose.*

## 👋 attributions / references
* (python logging documentation)[https://docs.python.org/3/library/logging.html)]
* (pynput documentation)[https://pynput.readthedocs.io/en/latest/]

## 🚧 future builds
* make log file text readable
	- currently output is very vertical. it needs to be horizontal.

* listen for specific combinations of characters during input
* create a menu
	- options would be:
		+ keylogger
		+ clipboardrecorder