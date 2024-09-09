import socket
while True:
    target_ip = input("Enter your target ip : ")

    start_port = int(input("Enter start range port scan : "))
    end_port = int(input("Enter end range port scan : "))

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for port in range(start_port, end_port + 1):
        try:
            socket.connect((target_ip, port))
            print(f"Port {port} is open")
        except:
            print(f"Port {port} is closed")

    socket.close()

    repeat = input("Do you want to scan again ? (y/n) : ").lower()
    if repeat != 'y':
        break
