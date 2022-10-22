import socket
import random
#randomly picking an ip from random list
port_nums=["75","45","65","55","62","25"]
flags=["start","continue","end"]
Target_ip='169.254.88.224'
Target_portno='6500'
def Generate() :
    Ip_Addresses=["192.168.1.0","192.168.2.0","192.168.3.0","192.168.4.0","192.168.5.0","192.168.6.0"]
    for x in Ip_Addresses:
        #interface_shuffle=str(random.randrange(255))
        #x=x.replace("0",interface_shuffle)
        #my_dummyIp = x
        my_DummyPortNumber= random.choice(port_nums)
        flag=random.choice(flags)
        byte_message = bytes(x+" " + my_DummyPortNumber+" "+Target_ip+" "+Target_portno+" "+flag, "utf-8")
        opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        opened_socket.sendto(byte_message, (Target_ip, int(Target_portno))) #target ip and port number.
        k=input("Try another one? yes/no ")
        if k=="yes":
            continue
        elif k=="no":
            print("ok..quitting")
            break

while(1):
    x=input("Start Y/N?")
    if x=='Y':
        Generate()
    else:
        print('Quittting...')
        break
