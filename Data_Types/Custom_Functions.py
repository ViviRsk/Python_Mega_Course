temperatures=[10,-20,-289,100]


def celsius_converter(c):

    rate = 1.8
    suf = 32
    f = c*rate+suf

    if c < -273.15:
        return str(f)+": "+"The lowest possible temperature that physical matter can reach is -273.15 C. Keep that in mind."
    return f

for celsius in temperatures:
    print(celsius_converter(celsius))
