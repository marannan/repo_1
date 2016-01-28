import collections

ship = (("NAME", "Albatross"),
        ("HP", 50),
        ("BLASTERS",13),
        ("THRUSTERS",18),
        ("PRICE",250))
ship = collections.OrderedDict(ship)

if __name__ == "__main__":
    ship.update({'c':'3'})
    for item in ship:
        print ship[item]
    #print ship