"""mod doc"""
def main():
    """doc"""  
    path = input()
    empty = input()
    server = input()
    packet1 = input()
    packet2 = input()
    packet3 = input()
    packet4 = input()
    all_packet = f"{packet1}{packet2}{packet3}{packet4}"

    path = empty
    empty = path

    # find ip server
    ip = ""
    if "[" in server:
        for j in range(server.find("[") + 1, server.find("]")):
            ip += server[j]
    else:
        for j in range(server.find("with") - 2, 1,-1):
            if server[j] == " ":
                break
            ip += server[j]
        ip = ip[-1::-1]


    # find packet sent
    packet_sent = all_packet.count("ms")
    received = 4 - (4 - packet_sent)
    lost = 100 - (received/4) * 100


    if not received:
        print(f"Ping statistics for {ip}:")
        print(f"    Packets: Sent = 4, Received = {received}, \
Lost = {4 - packet_sent} ({int(lost)}% loss),")
    else:
        # fine time
        num1 = ""
        num2 = ""
        num3 = ""
        num4 = ""
        most = 0
        mini = 0
        lost = 0
        div = 0
        if packet1.find("time") != -1:
            for k in range(packet1.find("time") + 4,packet1.find("ms")):
                if packet1[k].isnumeric():
                    num1 +=  packet1[k]
                elif packet1[k] == "<":
                    num1 = "0"
                    break
            div += 1
        else:
            num1 = "0"
        if packet2.find("time") != -1:
            for m in range(packet2.find("time") + 4,packet2.find("ms")):
                if packet2[m].isnumeric():
                    num2 +=  packet2[m]
                elif packet2[m] == "<":
                    num2 = "0"
                    break
            div += 1
        else:
            num2 = "0"
        if packet3.find("time") != -1:
            for n in range(packet3.find("time") + 4,packet3.find("ms")):
                if packet3[n].isnumeric():
                    num3 +=  packet3[n]
                elif packet3[n] == "<":
                    num3 = "0"
                    break
            div += 1
        else:
            num3 = "0"
        if packet4.find("time") != -1:
            for o in range(packet4.find("time") + 4,packet4.find("ms")):
                if packet4[o].isnumeric():
                    num4 +=  packet4[o]
                elif packet4[o] == "<":
                    num4 = "0"
                    break
            div += 1
        else:
            num4 = "0"


        average = (int(num1) + int(num2) + int(num3) + int(num4))/div
        mini = min(int(num1), int(num1), int(num2),int(num3))
        most = max(int(num1), int(num1), int(num2),int(num3))

        print(f"Ping statistics for {ip}:")
        print(f"    Packets: Sent = 4, Received = {received}, \
Lost = {4 - packet_sent} ({int(lost)}% loss),")
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {mini}ms, Maximum = {most}ms, Average = {int(average)}ms")
main()
