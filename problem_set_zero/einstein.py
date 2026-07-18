def main():
    mass = int(input("Input the mass to be converted "))
    massToEnergyConverter(mass)

def massToEnergyConverter(mass):
    joules = mass * (300000000**2)
    print(joules)

main()
