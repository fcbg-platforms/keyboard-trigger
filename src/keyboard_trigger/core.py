from datetime import datetime
from pynput import keyboard
import csv
from stimuli.trigger import ParallelPortTrigger

class KeyboardTrigger():
    
    def __init__(self, key_mapping,
                 key_start='space',
                 key_stop='esc',
                 suppress_propagation=False,
                 trigger_port_type = None,
                 trigger_port_address = None,
                 logfile = 'logs.csv',
                 verbose = True
                 ):
        self._key_mapping = key_mapping
        self._key_start = key_start
        self._key_stop = key_stop
        self._suppress_propagation = suppress_propagation
        self._trigger_port_type = trigger_port_type
        self._verbose = verbose
        self._logfile = logfile
        self._file = None
        self._writer = None
        self._is_running = False
        
        if self._logfile is not None:
            self._file = open(self._logfile, "a", newline="")
            self._writer = csv.writer(self._file)
        else:
            self._writer = None
        
        if self._trigger_port_type is not None:
            self._trigger = ParallelPortTrigger(trigger_port_address,
                                                port_type=self._trigger_port_type)
        else:
            self._trigger = None
        
    def _normalize_key(self,key):
        try:
            return key.char.lower() if key.char else None
        except AttributeError:
            special = {
                keyboard.Key.space: 'space',
                keyboard.Key.enter: 'enter',
                keyboard.Key.shift: 'shift',
                keyboard.Key.ctrl_l: 'ctrl',
                keyboard.Key.ctrl_r: 'ctrl',
                keyboard.Key.alt_l: 'alt',
                keyboard.Key.alt_r: 'alt',
                keyboard.Key.esc: 'esc'
            }
            return special.get(key, str(key))
    
    def _add_row(self, row):
        if self._writer is not None:
            self._writer.writerow(row)
    
    def _on_press(self, key):        
        t = datetime.now()
        k = self._normalize_key(key)
        if k is None:
            return
        
        if k == self._key_start:
            self._is_running = True
           
        if self._is_running:
            if self._verbose:
                print(f'{t}: keypress {k}')
            self._add_row([t, k])
    
            if self._trigger is not None:
                if k in self._key_mapping:
                    self._trigger.signal(self._key_mapping[k])
                    if self._verbose:
                        print(f'{t}: trigger {self._key_mapping[k]}')
        if k == self._key_stop:
            self._close()
            return False
        
    def _on_release(key):
        pass
    
    def _close(self):
        if self._file is not None:
            self._file.close()
            
        if self._trigger is not None:
            self._trigger.close()
        
    
    def start(self):
        
        print(f'Press {self._key_start} key to start logging.')
        print(f'Press {self._key_stop} to stop logging.')
        with keyboard.Listener(on_press=self._on_press,
                               on_release=self._on_release,
                               suppress=self._suppress_propagation) as listener:
            listener.join()
        



    
