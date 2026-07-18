file = input("Input your file ")
if file.__contains__("."):
    fileName, fileType = file.split(".")

    image = ("gif", "jpg", "jpeg", "png")
    application = ("pdf", "txt", "zip")

    if fileType in image:
        print("image/", fileType, sep="")
    elif fileType in application:
        print("application/", fileType, sep="")
else:
    print("application/octet-stream")







