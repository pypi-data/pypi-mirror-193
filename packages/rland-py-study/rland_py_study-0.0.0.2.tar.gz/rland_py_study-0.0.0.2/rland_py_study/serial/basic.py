#-*-coding:utf-8-*-
import sys
import time
import serial
import serial.tools.list_ports

class SerialBasic:
    def __init__(self):
        self.robot = None
        self.process = None
    def port_search(self):
        available_port_list = list()
        ports = serial.tools.list_ports.comports()
        for p in ports:
            available_port_list.append(p.device)
        print(available_port_list)
            
    def port_open(self, port):
        if type(port) != str: 
            print("Port name is string(ex.COM3, tty/devUSB0)")
            return
        self.robot = serial.serial_for_url(str(port), baudrate=115200, timeout=1)
        print("Opening port...")
        if self.robot.is_open:
            print("self.robot connected : " + str(port))
            print("Start reading self.process")
            
            print("Start data calculation self.process")

        else:
            port_close()

    def port_close(self):
        while(self.robot.is_open):
            print("Disconnecting self.robot")
            self.robot.close()
            if self.robot.is_open:
                time.sleep(1)
        print("Port closed")    


    

