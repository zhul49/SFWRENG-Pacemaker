import serial
import struct
from time import sleep
from serial.tools.list_ports import comports


for port in comports():
    print(port)


with serial.Serial(port = "COM3", baudrate=115200) as ser:
    for x in range(50):
        ser.write(b"\x16\x47" + b"\x00"*50)
        sleep(0.1)
        
        data_r = ser.read(50)

        aSignal = struct.unpack("d", data_r[0:8])[0] * 3.3
        vSignal = struct.unpack("d", data_r[8:16])[0] * 3.3
        print(aSignal, "    ", vSignal)

    ser.write(b"\x16\x62" + b"\x00"*50)
    sleep(0.1)
    ser.write(b"\x16\x22" + b"\x00"*50)
    sleep(0.1)
    data_r = ser.read(50)
        
    LRL = data_r[0]
    URL = data_r[1]

    A_Amp = struct.unpack("f", data_r[2:6])[0]
    A_pw = data_r[6]
    V_Amp = struct.unpack("f", data_r[7:11])[0]
    V_pw = data_r[11]

    ARP = struct.unpack("H", data_r[12:14])[0]
    VRP = struct.unpack("H", data_r[14:16])[0]
    aSens = struct.unpack("f", data_r[16:20])[0]
    vSens = struct.unpack("f", data_r[20:24])[0]

    mode = data_r[24]
    AVdelay = struct.unpack("H", data_r[25:27])[0]

    actThresh = struct.unpack("f", data_r[27:31])[0]
    reactTime = struct.unpack("d", data_r[31:39])[0]
    recTime = struct.unpack("d", data_r[39:47])[0]
    MSR = data_r[47]
    rateAdapt = data_r[48]
    resFactor = data_r[49]
        
    parameters = [mode, LRL, URL, A_Amp, A_pw, V_Amp, V_pw, VRP, ARP, aSens, vSens, rateAdapt, MSR, actThresh, reactTime, resFactor, recTime, AVdelay]

    print(parameters)
    ser.close()