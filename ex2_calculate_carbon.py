portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
    [0, 8943, 8019, 3652, 10545],
    [8943, 0, 2619, 6317, 2078],
    [8019, 2619, 0, 5836, 4939],
    [3652, 6317, 5836, 0, 7825],
    [10545, 2078, 4939, 7825, 0],
]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]


def permutations(route, ports):
    global smallest
    global bestroute
    if ports:
        for port in ports:
            new_ports = [p for p in ports if p != port]
            permutations(route + [port], new_ports)
    else:
        carbon_emission = get_carbon_emission_from_route(route)
        print(carbon_emission)
        if carbon_emission < smallest:
            smallest = carbon_emission
            bestroute = route


def get_carbon_emission_from_route(route):
    total_emission = 0
    for (stop1, stop2) in zip(route, route[1:]):
        total_emission = total_emission + D[stop1][stop2] * co2
    return total_emission


def main():
    # Do not edit any (global) variables using this function, as it will mess up the testing

    # this will start the recursion
    permutations([0], list(range(1, len(portnames))))

    # print the best route and its emissions
    print(" ".join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)


main()


# Facit
# portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# D = [
#         [0,8943,8019,3652,10545],
#         [8943,0,2619,6317,2078],
#         [8019,2619,0,5836,4939],
#         [3652,6317,5836,0,7825],
#         [10545,2078,4939,7825,0]
#     ]

# co2 = 0.020

# smallest = 1000000
# bestroute = None

# def permutations(route, ports):
#     global smallest, bestroute
#     if len(ports) < 1:
#         score = co2 * sum(D[i][j] for i, j in zip(route[:-1], route[1:]))
#         if score < smallest:
#             smallest = score
#             bestroute = route
#     else:
#         for i in range(len(ports)):
#             permutations(route+[ports[i]], ports[:i]+ports[i+1:])

# def main():
#     permutations([0], list(range(1, len(portnames))))

#     print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

# main()
