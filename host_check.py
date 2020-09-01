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
                        port = str(validate_port(row[x]))

                        if(port != 0):
                            #print("Connect to ", end="")
                            #print(dst, end="")
                            #print(" port: " + row[x], end=" ")
                            #print(" " + port, end=end)

                            if(connection(dst, port)):
                                print("** Valid ", end=" ")
                            else:
                                print("** Not_Found: ", end=" ")
                            
                            print("Connect to ", end="")
                            print(dst, end="")
                            print(" port: " + row[x], end=" ")
                            print(" " + port, end=end)
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

def validate_port(port_str):
    debug = 1

    if(port_str == "http"):
        return("80")
    elif(port_str == "https"):
        return("443")
    elif(port_str == "ftp"):
        return("21")
    elif(port_str == "ssh"):
        return("22")
    elif(port_str == "traceroute"):
        return("0")
    elif(port_str == "smtp"):
        return("25")
    elif("-" in port_str):
        portsplit = port_str.split("-")

        if(portsplit[0].lower() == "udp"):
            return(0)
        else:
            return(portsplit[1])
    elif(port_str.isnumeric()):
        # is number
        return(int(port_str))
    else:
        ##default case ... nothing found return 0
        return(0)

def main():
    print("In Main Function")

    parser = argparse.ArgumentParser(description='Port Check')

    parser.add_argument("-f", required=True, help="name of input file(csv)")

    args = parser.parse_args()

    inputfile = args.f

    extract_data(inputfile)

    """
    if(connection("146.18.2.137", "22")):
        print("good")
    else:
        print("failed")
    
    print(validate_port("http"))
    print(validate_port("https"))
    print(validate_port("http-7040"))
    print(validate_port("TCP-9999"))
    print(validate_port("UdP-9999"))
    """

if __name__ == "__main__":
    main()
#end of program