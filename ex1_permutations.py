# Assignment - calculate all combinations of ports always starting with PAN(index=0)
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


def permutations(route, ports):
    # Built in method:
    # import itertools
    # port_permutations = list(itertools.permutations(ports))
    # Write your recursive code here
    print("1. route=" + str(route) + " ports=" + str(ports))
    if ports:
        for port in ports:
            print("2. port=" + str(port) + " ports=" + str(ports))
            new_ports = [p for p in ports if p != port]
            print("3. route=" + str(route) + " new_ports = " + str(new_ports))
            permutations(route + [port], new_ports)
    else:
        print(" ".join([portnames[i] for i in route]))


# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))

# Facit
# def permutations(route, ports):
#     if len(ports) < 1:
#         print(' '.join([portnames[i] for i in route]))
#     else:
#         for i in range(len(ports)):
#             permutations(route+[ports[i]], ports[:i]+ports[i+1:])

# permutations([0], list(range(1, len(portnames))))
