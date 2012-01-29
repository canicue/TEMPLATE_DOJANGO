import sys 
import socket 
import string 
import os #No es necesario pero despues vamos a usar algunas caracteristicas de este

HOST = 'mesa.az.us.undernet.org' #El server al que queremos conectar
PORT = 6667 #El puerto para conectar que normalmente es el 6667
NICK = 'pybotv000' #El nick del bot
IDENT = 'pybot' 
REALNAME = 's1ash' 
OWNER = 'ne0n-' #El nombre del propietario del bot
CHANNELINIT = '#test198' #El canal predeterminado del bot
readbuffer = '' #Aqui se almacena todos los mensajes del server

s = socket.socket() #Creamos el socket
s.connect((HOST, PORT)) #Conectamos al server
s.send('NICK ' + NICK + 'n') #Enviamos el nick al server 
s.send('USER ' + IDENT + ' ' + HOST + ' bla :' + REALNAME + 'n') #Identificamos al server

while 1: 

    line = s.recv(500) #recibe los mensajes del server 
    print line #mensaje de server de salida
    if line.find('Welcome to the UnderNet IRC Network') != -1: 
        s.send('JOIN ' + CHANNELINIT + 'n') #entramos al canal 
    if line.find('PRIVMSG') != -1: #llamar a una funci
        parsemsg(line) 
        line = line.rstrip() #eliminar al final 'rn' 
        line = line.split() 
        if(line[0] == 'PING'): #si hace ping al servidor
            s.send('PONG ' + line[1] + 'n')
            
def parsemsg(msg): 
    complete = msg[1:].split(':', 1) #Analizar el mensaje en datos utiles
    info = complete[0].split(' ') 
    msgpart = complete[1] 
    sender = info[0].split('!') 
    if msgpart[0] == '`' and sender[0] == OWNER: #Tratar a todos los mensajes que comiencen por '`' como comando
        cmd = msgpart[1:].split(' ') 
        if cmd[0] == 'op': 
            s.send('MODE ' + info[2] + ' +o ' + cmd[1] + 'n') 
        if cmd[0] == 'deop': 
            s.send('MODE ' + info[2] + ' -o ' + cmd[1] + 'n') 
        if cmd[0] == 'voice': 
            s.send('MODE ' + info[2] + ' +v ' + cmd[1] + 'n') 
        if cmd[0] == 'devoice': 
            s.send('MODE ' + info[2] + ' -v ' + cmd[1] + 'n') 
        if cmd[0] == 'sys': 
            syscmd(msgpart[1:], info[2]) 
         
    if msgpart[0] == '-' and sender[0] == OWNER : #Tratar con mens - como mandato explcito para enviar al servidor
        cmd = msgpart[1:] 
        s.send(cmd + 'n') 
        print 'cmd=' + cmd
        
def syscmd(commandline, channel): 
    cmd = commandline.replace('sys ', '') 
    cmd = cmd.rstrip() 
    os.system(cmd + ' >temp.txt') 
    a = open('temp.txt') 
    ot = a.read() 
    ot.replace('n', '|') 
    a.close() 
    s.send('PRIVMSG ' + channel + ' :' + ot + 'n') 
    return 0
