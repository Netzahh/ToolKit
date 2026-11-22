#!/bin/python3

import socket
import sys
from datetime import datetime as dt
import os


# ==================== FONCTIONS ====================

def myNetwork():

    host = "127.0.0.1"
    port = 80

    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        destination_ip = socket.gethostbyname(host)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        result = s.connect_ex((destination_ip, port))

        if result == 0:
            connection_statut = "Successful !"
        else:
            connection_statut = "Failed.."

        s.close()

        print("== == == == == == ==")
        print("[Network Information]")
        print("== == == == == == ==")
        print("\n")
        print("-----------------------------")
        print("Hostname: ", hostname)
        print("Local Ip: ", local_ip)
        print("Destination_Ip: ", destination_ip)
        print(f"Port: ", port)
        print("-----------------------------")

        # File Saving Process (dans le try, sinon les variables n'existent pas en cas d'erreur)

        file = open("Scan_Result", "a")

        file.write(f"Saving Hostname: {hostname}\n")
        file.write(f"Saving Local Ip: {local_ip}\n")
        file.write(f"Saving Destination Ip: {destination_ip}\n")
        file.write(f"Saving Port: {port}\n")

        file.close()

    except socket.gaierror:
        print("Hostname couldn't be reach.")

    except socket.error as error:
        print(f"Error {error}")


def mySaving():

    try:
        file = open("Scan_Result", "r")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("error")


def myIpCalculator():

    try:
        address_ip = input("Insert the adress ip (192.168.1.0): ")
        cidr = int(input("Insert the cidr (24): "))

        if cidr < 0 or cidr > 32:
            print("The cidr should be between 0 and 32.")
            return

        total_address = 2 ** (32 - cidr)
        usable_host = total_address - 2 if cidr < 31 else total_address

        mask = (0xffffffff >> (32 - cidr) << (32 - cidr))
        subnet_mask = f"{(mask >> 24) & 0xff}.{(mask >> 16) & 0xff}.{(mask >> 8) & 0xff}.{mask & 0xff}"

        print("\n")
        print("== == == == == == ")
        print("Ip Calculator")
        print("== == == == == == ")
        print("\n")
        print("--------------- ! RESULT ! ----------------")
        print(f"Address ip: {address_ip}.")
        print(f"The CIDR: /{cidr}.")
        print(f"Total Address: {total_address}.")
        print(f"Usable Host: {usable_host}.")
        print(f"Subnet Mask: {subnet_mask}.")
        print("---------------------------------")

    except ValueError:
        print("The argument is invalid.")

    except Exception as e:
        print(f"The error is {e}")


def port_scanner():

    host = input("Enter the target (IP or hostname): ")

    try:
        target = socket.gethostbyname(host)

        print("-" * 50)
        print("Scanning target... " + target)
        print("Time started: " + str(dt.now()))
        print("-" * 50)

        for port in range(80, 445):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open !")
            s.close()

    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

    except socket.gaierror:
        print("Hostname couldn't be found.")
        sys.exit()

    except socket.error:
        print("Server is not available.")
        sys.exit()


# ==================== MENU ====================

print("\n")
print("== == == == == == == == == == == == == == ==")
print("\n")
print("NETWORK SECURITY TOOL")
print("\n")
print("== == == == == == == == == == == == == == ==")

sytem_info = "System Information"
network_info = "Network Information"
ip_calcul = "Ip Calculator"
local_port_scan = "Local Port Scan"
view_result = "View Result"
print("\n")

print("--------------------------------------------")
print(sytem_info)
print("--------------------------------------------")
print(network_info)
print("--------------------------------------------")
print(ip_calcul)
print("--------------------------------------------")
print(local_port_scan)
print("--------------------------------------------")
print(view_result)
print("--------------------------------------------")
print("\n")
print("-- --")
print("Exit")
print("-- --")
print("\n")

option_picker = input("Choose an option: ")
print("\n")

if option_picker == "System Information":

    print("== == == == == == ==")
    print("[System Information]")
    print("== == == == == == ==")
    print("\n")
    print("Netzahh was here ;) ")
    print("\n")
    print("--------------------------")
    print("Welcome " + str(os.getlogin()) + " !")
    print("--------------------------")
    print("\n")
    print("------------------------------------------------------------------------------")
    print("Curent date: " + str(dt.now()))
    print("The version of the system is " + sys.version)
    print("The machine name is " + socket.gethostname())
    print("------------------------------------------------------------------------------")


elif option_picker == "Network Information":

    myNetwork()


elif option_picker == "View Result":

    while True:

        print("[----------------------]")
        print("Network Security Tool)")
        print("[----------------------]")
        print("\n")
        print("1 = Network Info")
        print("2 = Check The Result")
        print("3 =  Exit")

        viewResult = input("Choose between: ")

        if viewResult == "1":
            myNetwork()
        elif viewResult == "2":
            mySaving()
        elif viewResult == "3":
            print("\n" "exciting program")
            sys.exit()
        else:
            print("Error")


elif option_picker == "Ip Calculator":

    myIpCalculator()


elif option_picker == "Local Port Scan":

    port_scanner()
			
