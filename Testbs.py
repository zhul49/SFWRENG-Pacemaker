import serial
import struct
from time import sleep
from serial.tools.list_ports import comports

data = b"\x16\x22" + b"\x00"*25

for port in comports():
    print(port)

mode = 0
LRL=120
URL=1
A_Amp=5
A_pw=5
V_Amp=5
V_pw=10
ARP=1
VRP=1
Duty=60
AVdelay = 0

mode_b = struct.pack("B", mode)
LRL_b = struct.pack("B", LRL)
URL_b = struct.pack("B", URL)
A_Amp_b = struct.pack("f", A_Amp)
A_pw_b=struct.pack("f", A_pw)
V_Amp_b=struct.pack("f", V_Amp)
V_pw_b=struct.pack("f", V_pw)
ARP_b=struct.pack("H", ARP)
VRP_b=struct.pack("H", VRP)
Duty_b=struct.pack("B", Duty)
AVdelay_b = struct.pack("b", AVdelay)

data = b"\x16\x55" + mode_b + LRL_b + URL_b + A_Amp_b + A_pw_b + V_Amp_b + V_pw_b + ARP_b + VRP_b + Duty_b + AVdelay_b

with serial.Serial(port = "COM3", baudrate=115200) as ser:
    ser.write(data)
    sleep(0.1)
    ser.write(b"\x16\x22" + b"\x00"*25)
    sleep(0.1)
    data_r = ser.read(25)

    mode = data_r[0]
    LRL = data_r[1]
    URL = data_r[2]

    A_Amp = struct.unpack("f", data_r[3:7])[0]
    A_pw = struct.unpack("f", data_r[7:11])[0]
    V_Amp = struct.unpack("f", data_r[11:15])[0]
    V_pw = struct.unpack("f", data_r[15:19])[0]

    ARP = struct.unpack("H", data_r[19:21])[0]
    VRP = struct.unpack("H", data_r[21:23])[0]

    Duty = data_r[23]
    AVdelay = data_r[24]

    print(f"Mode: {mode}")
    print(f"LRL: {LRL}, URL: {URL}")
    print(f"A_Amp: {A_Amp}, A_pw: {A_pw}, V_Amp: {V_Amp}, V_pw: {V_pw}")
    print(f"ARP: {ARP}, VRP: {VRP}")

    print(f"Duty: {Duty}, AVdelay: {AVdelay}")
    ser.close()