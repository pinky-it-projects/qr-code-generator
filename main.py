import qrcode
website = input("Wat is uw websitesadres?")
website = website.strip()

while website == "":
    print("ERROR")
    website = input("Nog een keer proberen")
    website = website.strip()
    
print(f"Websiteadres ontvangen: {website}")


#Generate our first QR code
qr = qrcode.make(website)        # website is a variable
qr.save("mijn_qrcode.png")  # filename is a string