from gpsModule import ubx, gps_io
from time import sleep, time
gpsio = gps_io(input_speed=38400)
ubxt = ubx.ubx()
ubxt.protver = 26.0
ubxt.io_handle = gpsio

def read_ser():
    out = None
    while out == None:
        out = gpsio.ser.sock.recv(8192)
        print(out, '\n')
    return out

CFG_VALSET = {"class" : 0x06, "id" : 0x8a}



#print(ubxt.send_cfg_valget([0x10730001, 0x10730002, 0x10740001, 0x10740002], 1, 0))

#print(ubxt.send_cfg_valset(["CFG-UART1INPROT-UBX,1", "CFG-UART1INPROT-NMEA,0", "CFG-UART1OUTPROT-UBX,1", "CFG-UART1OUTPROT-NMEA,0"]))

for i in range(15):
    ubxt.decode_msg(read_ser())
    #print(ubxt.decode_msg(read_ser()))















































#file.close()











def bar(file):
    t0=time()
    out = None
    #ubxt.send_able_ned(1, None)
    while out == None:
        out = gpsio.ser.sock.recv(8192)
        print(out)
        res = ubxt.decode_msg(out)
        #file.write(out)
    #print(time() - t0)
    #return out
    #print(res)
