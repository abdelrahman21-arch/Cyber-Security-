import socket
from tkinter import *
import tkinter
port=6500
server_ip="169.254.88.224"
ADDR=(server_ip,port)
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(ADDR)
BLOCED_MESSAGE="!BLOCKED"
count=0

f1=open('Config.txt','r')
a=True
allowed_flag1=0
allowed_flag2=0
allowed_flag3=0
blocked_flag1=0
blocked_flag2=0
blocked_flag3=0
established_flag_allowed=0
established_flag_blocked=0
lines=[]
message_sliced=[]
prefix_list_allowed=[]
prefix_list_blocked=[]
special_ports_allowed=[]
special_ips_allowed=[]
special_ports_blocked=[]
special_ips_blocked=[]

port_number_allowed=[]

port_number_blocked=[]
for line in f1:



    lst=line.split()
    print(lst)
    if lst[0] == "allow":
    #    print("hamda")
    #    print(prefix)
        if len(lst[1]) in range(10,19):
            prefix_list_allowed.append(lst[1])
        if len(lst[2]) in range(2,6):
            port_number_allowed.append(lst[2])
        for y in range(len(prefix_list_blocked)):
            if lst[1]==prefix_list_blocked[y]:
                del prefix_list_blocked[y]
        if len(lst)==4:
            if lst[3] =='established':
                established_flag_allowed=1

                print('hamada')
        if  (lst[1]=='*') and (lst[2]!='*'):
            allowed_flag1=1
            special_ports_allowed.append(lst[2])
            print('allowed_flag1 is set')


        if (lst[1]!='*') and (lst[2]=='*'):
            allowed_flag2=1
            special_ips_allowed.append(lst[1])
            print(f'allowed_flag2 is set')

        if (lst[1] == '*')and (lst[2]== '*'):




            print(f'all ips and port numbers are allowed ')
            port_number_blocked.clear()
            prefix_list_blocked.clear()







    elif lst[0] == "block":
        if len(lst[1]) in range(10,19):

            prefix_list_blocked.append(lst[1])
            print(*prefix_list_blocked)

        if len(lst[2]) in range(2,6):
            port_number_blocked.append(lst[2])
        for y in range(len(prefix_list_allowed)):
            if lst[1]==prefix_list_allowed[y]:
                del prefix_list_allowed[y]

        if len(lst)==4:

            if lst[3]=='established':
                    established_flag_blocked=1

        else:
            pass
        if lst[1]=='*'and lst[2]!='*':
            blocked_flag1=1
            special_ports_blocked.append(lst[2])
            print('blocked_flag1 is set')

        if lst[2]=='*'and lst[1]!='*':
            blocked_flag2=1
            special_ips_blocked.append(lst[1])
            print(f'blocked_flag2  is set')
        elif (lst[1]=='*') and( lst[2]=='*'):
            print('all ips and port numbers are blocked ')

            prefix_list_allowed.clear()
            port_number_allowed.clear()

















def start():
    global established_flag_allowed
    global established_flag_blocked
    global count




    connected=True

    while connected:
        clear_flag = 1

        bytesAddressPair = server.recvfrom(1024)
        message=bytesAddressPair[0].decode('utf-8')
        #print("message from client:{}".format(message))
        print(message)

        List_spltmsg=message.split()
        Client_prefix=List_spltmsg[0]
        print(Client_prefix)
        flag=List_spltmsg[4]
        Client_portno=List_spltmsg[1]


        if (Client_prefix in prefix_list_allowed) and (Client_portno in port_number_allowed):
            print('identified cllient\nconnection established')
            clear_flag=0



        if Client_prefix in prefix_list_blocked  and Client_portno in port_number_blocked :
            print('identified blocked client\nConnection Blocked')
            clear_flag=0


        if (Client_portno in special_ports_allowed):
            print('identified client\nConnection Accepted for all ips')
            clear_flag=0
        if Client_prefix in special_ips_allowed:
            print('identified client\nConnection Accepted for all ports')
            clear_flag=0






        for y in prefix_list_allowed:
            for z in port_number_allowed:
                if Client_prefix == y and established_flag_allowed==1 and Client_portno not in special_ports_allowed:
                    if flag == 'continue':
                        print('connection allowed for all ports on this ip ')
                        clear_flag=0
                        established_flag_allowed=0




                    if flag == 'start':
                            print('non established connection...connection blocked!')
                            while count < len(prefix_list_allowed):
                                if Client_prefix==prefix_list_allowed[count]:
                                    del prefix_list_allowed[count]
                                count+=1
                            count=0
                            while count <len(port_number_allowed):
                                if Client_portno==port_number_allowed[count]:
                                    del port_number_allowed[count]
                                count+=1
                            count=0
                            clear_flag=0
                            established_flag_allowed=0


                    if flag == 'end':
                        print('non established connection...connection blocked!')
                        while count < len(prefix_list_allowed):
                            if Client_prefix==prefix_list_allowed[count]:
                                del prefix_list_allowed[count]
                            count+=1
                        count=0
                        while count < len(port_number_allowed):
                            if  Client_portno==port_number_allowed[count]:
                                del port_number_allowed[count]
                            count+=1
                        count=0
                        clear_flag=0
                        established_flag_allowed=0

                if Client_prefix == y and Client_portno==z and established_flag_allowed==1:
                    print('ay haga')
                    if flag=='continue':
                        print('connection allowed')
                        clear_flag=0
                        established_flag_allowed=0
                    elif flag=='start':
                        print('non established connection...connection blocked!')
                        while count < len(prefix_list_allowed):
                            if Client_prefix==prefix_list_allowed[count]:
                                del prefix_list_allowed[count]
                            count +=1
                        count=0
                        while count < len(port_number_allowed):
                            if Client_portno==port_number_allowed[count]:
                                del port_number_allowed[count]
                            count+=1
                        count=0
                        clear_flag=0
                        established_flag_allowed=0
                    elif flag=='end':
                        print('non established connection...connection blocked!')
                        while count < len(prefix_list_allowed):
                            if Client_prefix==prefix_list_allowed[count]:
                                del prefix_list_allowed[count]
                            count +=1
                        count=0


                        while count < len(port_number_allowed):
                            if Client_portno==port_number_allowed[count]:
                                del port_number_allowed[count]
                            count+=1
                        count=0
                        clear_flag=0
                        established_flag_allowed=0




        for y in prefix_list_blocked:
            for z in port_number_blocked:
                if Client_prefix==y and Client_portno==z and established_flag_blocked==1:
                    if flag=='continue':
                        print('connection blocked')
                        clear_flag=0
                        established_flag_blocked=0


                    elif flag=='start':
                        print('non established connection...connection allowed!')
                        while count < len(prefix_list_blocked):
                            if Client_prefix==prefix_list_blocked[count]:
                                del prefix_list_blocked[count]
                            count +=1
                        count=0

                        while count < len(port_number_blocked):
                            if  Client_portno==port_number_blocked[count]:
                                del port_number_blocked[count]
                            count+=1
                        count=0
                        clear_flag=0
                        established_flag_blocked=0

                    elif flag=='end':
                        print('non established connection...connection allowed!')
                        while count < len(prefix_list_blocked):
                            if Client_prefix==prefix_list_blocked[count]:
                                del prefix_list_blocked[count]
                            count +=1
                        count=0


                        while count < len(port_number_blocked):
                            if  Client_portno==port_number_blocked[count]:
                                del port_number_blocked[count]
                            count+=1
                        count=0
                        clear_flag=0
                        established_flag_blocked=0

                    elif established_flag_blocked==1:
                        established_flag_blocked=0
        print(f'this is clear flag {clear_flag}')
        if clear_flag==1:
            print('Unidentified Connection\nconnection Blocked')


        k=input('Exit? y/n ')
        if k=='y':

            connected=False


        else:
            pass



    server.close()
    pass



def Writetomenu():
    root= Tk()
    text=Text(root)
    for y in prefix_list_allowed:
        text.insert(INSERT,y+"\n")
        text.tag_config(y, background="black", foreground="green")


    text.pack()
    root.mainloop()




print("Initiating...")
start()
root = tkinter.Tk()
root.geometry('250x250')
B=tkinter.Button(root,activeforeground='blue',activebackground='cyan',padx='25',pady='25',text='Show Configuration list',command=Writetomenu)
B.pack()
root.mainloop()


    #    print("hamo")
#for y in prefix_list_allowed:

    #print(y)
#for z in port_number_allowed:
    #print(z)
