import socket
import websocket
import program_ACO as runACO

ws = websocket.WebSocket()
ws.connect("ws://192.168.43.137/ws")
s = socket.socket()
 
s.bind(('0.0.0.0', 8090))
s.listen(0)
print("waiting...")

while True:

    data_agen = 0
    data_task = 0
    data_caps = 0
    i=0

    get_data = "not found"
    client, addr = s.accept()
    while True:
        content = client.recv(1024)
 
        if len(content) == 0:
           break
 
        else:
            if i==0 :
                data_agen = int(float(content.decode()))
                i += 1
            elif i==1 :
                data_task = int(float(content.decode()))
                i += 1
            elif i==2 :
                data_caps =int(float(content.decode()))
                print("Input data\t: "+str(data_agen)+", "+str(data_task)+", "+ str(data_caps))
                get_data = runACO.solveTA(jmlh_ant=80,jmlh_iterasi=60,jmlh_agent=data_agen,jmlh_caps=data_caps,jmlh_task=data_task,w2=0.1,rho=0.1,alpha=1,beta=1,seed=1403)
                ws.send(get_data)

    print("Data sent\t: \n", get_data)
    print("\nClosing connection")
    client.close()

ws.close()
