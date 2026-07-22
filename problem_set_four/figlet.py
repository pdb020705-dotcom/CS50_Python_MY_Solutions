from pyfiglet import Figlet
import random as r
import sys

def main():

    if len(sys.argv) == 1:
        figlet = Figlet()
        fonts = figlet.getFonts()
        random_font = r.choice(fonts)
        f = Figlet(font=random_font)
        str = input("Input: ")
        print(f.renderText(str))
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        f = Figlet(font=sys.argv[2])
        str = input("Input:: ")
        print(f.renderText(str))
    else:
        sys.exit("Invalid usage")
        
        


    


main()
