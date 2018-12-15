from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import pyttsx3
import tkinter
import webbrowser


def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            fetch(msg)
            msg_list.insert(tkinter.END, msg)
            msg_list.see(tkinter.END)
        except OSError:  
            break


def send(event=None):  # event is passed by binders.
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()

def openweb():
    webbrowser.open(url,new=new)

def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()


def fetch(mytext):
    engine = pyttsx3.init()
    engine.say(mytext)
    engine.runAndWait()

top = tkinter.Tk()
top.title("Chatz")
top.config(bg='gray')
w = tkinter.Label(top, text="Welcome to Chatz",background="light blue",height="1")
w.pack()


new = 1
url = "http://127.0.0.1:3000"





messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  # To see through previous messages.
# this will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=30, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg,)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()
but1 = tkinter.Button(top, text='-', command=fetch('a'))
but1.pack()
Btn = tkinter.Button(top, text = "Web Chatz",command=openweb)
Btn.pack()


top.protocol("WM_DELETE_WINDOW", on_closing)

#Socket partlocalhost
HOST = input('Enter host: ')
PORT = 5001
BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # for start of GUI  Interface
