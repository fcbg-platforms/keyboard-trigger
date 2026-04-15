# keyboard-trigger
A simple python package to send triggers with key press

# Example

```python
from keyboard_trigger import KeyboardTrigger

    
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

kb_trigger = KeyboardTrigger(key_to_trigger_mapping,
                             key_start='space',
                             key_stop='esc',
                             suppress_propagation=True,
                             trigger_port_type = 'arduino',
                             trigger_port_address = 'COM3',
                             logfile = 'logs.csv',
                             verbose = True
                             )

kb_trigger.start()
```
