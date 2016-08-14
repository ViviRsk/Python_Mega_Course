temperatures=[10,-20,-289,100]


def celsius_converter(temperatures):
    with open("C:\Python27\example.txt", 'w') as file:
        rate = 1.8
        suf = 32

        for c in temperatures:
            if c > -273.15:
                f = c * rate + suf
                file.write(str(f)+"\n")

celsius_converter(temperatures)
