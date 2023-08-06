import socket

class SocketConnection:
    def __init__(self,host,port): 
        self.host = host
        self.port = port
        self.unique_data = {}
    
    def connect(self): 
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            return True
        except socket.error as e:
            print('connection error')
            return False

    def receive_data(self):
        LSB = '30'
        MSB = '00'
        ETX = '03'
        lastData = ''
        PC = ''
        EPC = ''
        RSSI = ''
        count = 1
        data = (self.socket.recv(1)).hex()
        if data != "":
            if data == '02':
                data1 = data            
                while data != '0d':
                    data = (self.socket.recv(1)).hex()
                    if count == 5:
                        RSSI = RSSI + data
                    if count == 6:
                        RSSI = RSSI + data
                        RSSI = self.twos_complement(int(RSSI,16),16) 
                    if lastData == LSB and data == MSB:
                        PC = lastData + data
                        data1 = data1 + data
                        while data != ETX:
                            data = (self.socket.recv(1)).hex()
                            if data != ETX:
                                EPC = EPC + data
                                data1 = data1 + data 
                    lastData = data
                    data1 = data1 + data
                    count += 1
            if len(EPC) == 24:
                if EPC not in self.unique_data:
                    self.times = 1
                    self.unique_data[EPC] = [self.times]
                    self.unique_data[EPC].append(PC)
                    self.unique_data[EPC].append(EPC)
                    self.unique_data[EPC].append(RSSI)
                    self.unique_data[EPC].append(RSSI)
                    self.unique_data[EPC].append(RSSI)            
                else:
                    for key in self.unique_data:
                        if key == EPC:
                            self.unique_data[key][0] += 1
                            self.unique_data[key][3] = RSSI
                            if self.unique_data[key][4] == None:
                                self.unique_data[key][4] = RSSI
                            elif self.unique_data[key][4] < RSSI:
                                self.unique_data[key][4] = RSSI
                            if self.unique_data[key][5] == None:
                                self.unique_data[key][5] = RSSI
                            elif self.unique_data[key][5] > RSSI:
                                self.unique_data[key][5] = RSSI
        
        if self.unique_data != None:
            return self.unique_data

    def twos_complement(self,n, w):
        if n & (1 << (w - 1)): 
            n = n - (1 << w)
            n = n/10
        return n       

