import socket
import os
import sys
from rich import print
from rich.table import Table
from rich.progress import track
from fsplit.filesplit import Filesplit

fs = Filesplit()

table_commands = Table(title="Commands")
table_commands.add_column("Command", style="cyan", no_wrap=True)
table_commands.add_column("Use", style="magenta")
table_commands.add_column("No", justify="right", style="green")
table_commands.add_row("help", "Get info about the commands.", "1")
table_commands.add_row("upload (filename) (password)", "Upload a file.", "2")
table_commands.add_row("download (filename) (output) ", "Download a file.", "3")
table_commands.add_row("delete (filename) (password) ","Delete a file which is present in the server.","4")
table_commands.add_row("replace (filename) (newfile) (password)","Replace a existing file.","5")

recv_chunks = []
send_chunks = []
max_chunk = 65536
# setting connection to server
port = 19568
add = "3.6.122.107"
print(f"[bold green] You are connecting to : {add} [/bold green]")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    function = sys.argv[1]
except:
    print(f"[bold green] No Commands Provided Type 'uft help' [/bold green]")

try:
    client.connect((add, port))
    print("[green] Got Connected To Server [/green]")
    if function == "help":
        print(table_commands)
    elif function == "download":
        client.send("download".encode())
        client.recv(1024).decode()
        file_name = sys.argv[2]
        new_name = sys.argv[3]
        client.send(file_name.encode())
        res = client.recv(1024).decode()
        if res == "yes":
            client.send(".".encode())
            for step in track(range(15)):
                len_ = int(client.recv(1024).decode())
                client.send(".".encode())
                file_data = client.recv(len_)
                recv_chunks.append(file_data)
                step
            output = b""
            for each in recv_chunks:
                output += each
            recv_chunks = []
            f = open(new_name, "wb")
            f.write(output)
            f.close()
            print("\n")
        else:
            print("[red] File Not Found...[/red]")
    elif function == "upload":
        file_name = sys.argv[2]
        file_password = sys.argv[3]
        client.send("upload".encode())
        client.recv(1024).decode()
        client.send(file_name.encode())
        res = client.recv(1024).decode()
        if res == "__++":
            print("[red] File already exists , Try using other filename. [/red]")
        else:
            client.send(file_password.encode())
            client.recv(1024).decode()
            try:
                os.mkdir("splitting_dir_2")
            except:
                pass
            f = open(file_name,"rb")
            data = f.read()
            f.close()
            len_ = int(len(data)/15)
            fs.split(file=file_name, split_size=len_, output_dir="splitting_dir_2")
            file_name_new = str(file_name).split(".")

            try:
                file_name_extention ="."
                file_name_extention+= file_name_new[1]


            except:
                file_name_extention = ""

            file_name_new = file_name_new[0]

            file = open("splitting_dir_2/" + file_name_new + "_1" + file_name_extention, "rb")

            msg = file.read()
            file.close()

            client.send(str(len_ + 10).encode())
            client.recv(1024).decode()
            client.send(msg)

            file = open("splitting_dir_2/" + file_name_new + "_2" + file_name_extention, "rb")
            msg = file.read()
            file.close()
            client.send(str(len_ + 100).encode())
            client.recv(1024).decode()
            client.send(msg)

            file = open("splitting_dir_2/" + file_name_new + "_3" + file_name_extention, "rb")
            msg = file.read()
            file.close()
            client.send(str(len_ + 100).encode())
            client.recv(1024).decode()
            client.send(msg)

            file = open("splitting_dir_2/" + file_name_new + "_4" + file_name_extention, "rb")
            msg = file.read()
            file.close()
            client.send(str(len_ + 100).encode())
            client.recv(1024).decode()
            client.send(msg)

            file = open("splitting_dir_2/" + file_name_new + "_5" + file_name_extention, "rb")
            msg = file.read()
            file.close()
            client.send(str(len_ + 100).encode())
            client.recv(1024).decode()
            client.send(msg)

            file = open("splitting_dir_2/" + file_name_new + "_6" + file_name_extention, "rb")
            msg = file.read()
            file.close()
            client.send(str(len_ + 100).encode())
            client.recv(1024).decode()
            client.send(msg)

            file = open("splitting_dir_2/" + file_name_new + "_7" + file_name_extention, "rb")
            msg = file.read()
            file.close()
            client.send(str(len_ + 100).encode())
            client.recv(1024).decode()
            client.send(msg)

            file = open("splitting_dir_2/" + file_name_new + "_8" + file_name_extention, "rb")
            msg = file.read()
            file.close()
            client.send(str(len_ + 100).encode())
            client.recv(1024).decode()
            client.send(msg)

            file = open("splitting_dir_2/" + file_name_new + "_9" + file_name_extention, "rb")
            msg = file.read()
            file.close()
            client.send(str(len_ + 100).encode())
            client.recv(1024).decode()
            client.send(msg)

            file = open("splitting_dir_2/" + file_name_new + "_10" + file_name_extention, "rb")
            msg = file.read()
            file.close()
            client.send(str(len_ + 100).encode())
            client.recv(1024).decode()
            client.send(msg)

            file = open("splitting_dir_2/" + file_name_new + "_11" + file_name_extention, "rb")
            msg = file.read()
            file.close()
            client.send(str(len_ + 100).encode())
            client.recv(1024).decode()
            client.send(msg)

            file = open("splitting_dir_2/" + file_name_new + "_12" + file_name_extention, "rb")
            msg = file.read()
            file.close()
            client.send(str(len_ + 100).encode())
            client.recv(1024).decode()
            client.send(msg)

            file = open("splitting_dir_2/" + file_name_new + "_13" + file_name_extention, "rb")
            msg = file.read()
            file.close()
            client.send(str(len_ + 100).encode())
            client.recv(1024).decode()
            client.send(msg)

            file = open("splitting_dir_2/" + file_name_new + "_14" + file_name_extention, "rb")
            msg = file.read()
            file.close()
            client.send(str(len_ + 100).encode())
            client.recv(1024).decode()
            client.send(msg)

            file = open("splitting_dir_2/" + file_name_new + "_15" + file_name_extention, "rb")
            msg = file.read()
            file.close()
            client.send(str(len_ + 100).encode())
            client.recv(1024).decode()
            client.send(msg)

            print("[green] UPLOADED[/green]")
    else:
        print("[red] Command Not Found...[/red]")
    print("[red] Disconnected[/red]")
except:
    print("[red] Connection Error [/red]")


