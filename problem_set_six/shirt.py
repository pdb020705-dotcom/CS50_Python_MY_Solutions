import sys
from PIL import Image, ImageOps

def main():

    valid_images = (".png", ".jpg", ".jpeg")
    word1, extension1 = sys.argv[1].split(".")
    word2, extension2 = sys.argv[2].split(".")



    if len(sys.argv) != 3:
        sys.exit("incorrect amount of arguments")
    elif extension2 != extension1:
        sys.exit("Mismatch of extension")
    elif not sys.argv[1].endswith(valid_images) or not sys.argv[2].endswith(valid_images):
        sys.exit("Invalid file format")

    shirt = Image.open("shirt.png")


    try:
        with Image.open(f"{sys.argv[1]}") as inim:
            photo = ImageOps.fit(inim, shirt.size)
            photo.paste(shirt, (0, 0), shirt)
            photo.save(f"{sys.argv[2]}")
    except FileNotFoundError:
        sys.exit("")
    

if __name__ == "__main__":
    main()


    