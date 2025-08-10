import socket, sys

ART = r"""
    ___           _      __                  
   /   \__ _ _ __| | __ / / _   _ _ __ __  __
  / /\ / _` | '__| |/ // / | | | | '_ \\ \/ /
 / /_// (_| | |  |   </ /__| |_| | | | |>  < 
/___,' \__,_|_|  |_|\_\____/\__, |_| |_/_/\_\
                            |___/            
"""
BANNER = r"""
     B A S 1 C    T C P    $ C 4 N N E R   

    getting blocked by firewalls since 2025 yay!                               
"""

def scan( ip, ports):

    if not ports:
        print(f"Please specify at least one TCP port to scan.")
        return False
    
    try:
        port_list = []
        if "-" in ports:
            start, end = map(int, ports.split('-'))
            port_list = list(range(start, end + 1))
        elif "," in ports:
            port_list = [int(p) for p in ports.split(',')]
        else:
            port_list = [int(ports)]

        for port in port_list:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                result = s.connect_ex((ip, port))
                s.close()
                if result == 0:
                    print(f"[+] TCP port: {port} is open")

            except socket.error as e:
                print(f"[-] Error scanning port {port}: {e}")
            finally:
                if 's' in locals():
                    s.close()
    
    except Exception as e:
        print(f"[!] An error occurred: {e}")
        return False

    return True
    
if __name__ == "__main__":
    print(ART)
    print(BANNER)

    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <IP> <PORTS>")
        print(f"Examples:")
        print(f"  {sys.argv[0]} 192.168.0.10 21,22,80   # Scan ports 21, 22 and 80")
        print(f"  {sys.argv[0]} 192.168.0.10 22          # Scan only port 22")
        print(f"  {sys.argv[0]} 192.168.0.10 21-80      # Scan ports from 21 to 80 \n")
        sys.exit(1)

    scan(sys.argv[1], sys.argv[2])
    print(f"\n-+=+--+=+--+=+--+=+- Finished -+=+--+=+--+=+--+=+-\n")