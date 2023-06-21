import qrcode

if __name__ == '__main__':
    print("""
Welcome to QR code generator!
You can generate any vaild URL you want.""")
    data = input(("URL to generate: "))
    qr_image = qrcode.make(data)

    while True:
        confirm = input(("Are you sure to generate the following URL '{}' ?(Y/N): ".format(data)))

        if confirm.lower() == 'y':
            #put the name you want to save
            qr_image.save("C:/Users/USER/Desktop/qr.png")
            print("QR code save successfully.")
            break
        elif confirm.lower() == 'n':
            print("Thank you for using.")
            break
        else:
            print("I don't understand that.")