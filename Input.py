from pynput import keyboard
import socket
import math

##Create Socket
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((socket.gethostname(), 5556))
s.listen(8)
Speed =0

##Accept Connections
while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    conn.send(bytes("Welcome to the Server!","utf-8"))
   
    def on_press(key):  
        ##Make Speed variable global
        global Speed
        ## Convert Speed value to PWM
        if str(key) == "'1'" or str(key) == "'2'"  or str(key) == "'3'"  or str(key) == "'4'"  or str(key) == "'5'":  
            Speed = (int(key.char)/5)*(255)
            Speed = math.trunc(Speed)
            ## Output Speed along with arrow key/direction
        elif key == keyboard.Key.up:
            conn.send(bytes("[f"+ str(Speed) +"][f"+ str(Speed) +"][f"+ str(Speed) +"][f"+ str(Speed) +"]","utf-8"))
        elif key == keyboard.Key.left:
            conn.send(bytes("[r"+ str(Speed) +"][r"+ str(Speed) +"][f"+ str(Speed) +"][f"+ str(Speed) +"]","utf-8"))
        elif key == keyboard.Key.right:
            conn.send(bytes("[f"+ str(Speed) +"][f"+ str(Speed) +"][r"+ str(Speed) +"][r"+ str(Speed) +"]","utf-8"))
        elif key == keyboard.Key.down:\
            conn.send(bytes("[r"+ str(Speed) +"][r"+ str(Speed) +"][r"+ str(Speed) +"][r"+ str(Speed) +"]","utf-8"))
        else:
            pass

    def on_release(key):
        print('{0} released'.format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False


    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
