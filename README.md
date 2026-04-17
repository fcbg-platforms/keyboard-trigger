# keyboard-trigger
A simple python package to send triggers with key press

## Installation

Install with pip (requires git to be installed):

```bash
pip install git+https://github.com/fcbg-platforms/keyboard-trigger.git
```

## Usage

```python
from keyboard_trigger import KeyboardTrigger

# mapping of keys to trigger values
key_to_trigger_mapping = {'1': 1,
                          '2': 2,
                          '3': 3,
                          '4': 4,
                          '5': 5,
                          '6': 6,
                          '7': 7,
                          '8': 8,
                          '9': 9,
                          '0': 10,
                          'space': 100,
                          'esc': 101
                          }

# init
kb_trigger = KeyboardTrigger(key_to_trigger_mapping,
                             key_start='space', # press space to start
                             key_stop='esc', # press escape to stop
                             suppress_propagation=False,
                             trigger_port_type = 'arduino',
                             trigger_port_address = 'COM3',
                             logfile = 'logs.csv', # log file
                             verbose = True
                             )

# start
kb_trigger.start()
```
