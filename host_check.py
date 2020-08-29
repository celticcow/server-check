#!/usr/bin/python3

import csv
import sys
import ipaddress
import socket
import argparse


def extract_data(file):
    debug = 1
    end = "\n"

    ###file = "sample.csv"
    print("In Extract_Data()")

    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            total = len(row)
            
            dst = "127.0.0.1"

            for x in range(total):
                if(x == 0):
                    dst = row[x] ## need to pass to verify is valid IP addr
                else:
                    port_info = row[x]

                    if(port_info == ""):
                        # port is not there ... so skip it.
                        pass
                    else:
                        print("Connect to ", end="")
                        print(dst, end="")
                        print(" port: " + row[x], end=end)
                        #print(row[x] + " port")
            #print(dst, end=end)
            #print(total, end=end)

#end of extract_data

def connection(server, port):
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location = (server, int(port))

    a_socket.settimeout(0.5)

    result = a_socket.connect_ex(location)

    if(result == 0):
        return(True)
    else:
        return(False)
#end of connect



def main():
    print("In Main Function")

    extract_data("sample.csv")

    if(connection("146.18.2.137", "22")):
        print("good")
    else:
        print("failed")

if __name__ == "__main__":
    main()
#end of program