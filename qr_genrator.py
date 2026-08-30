import qrcode
data =input("enter the link: ")
img=qrcode.make(data)
img.save("img.png")
img.show()
print("QR code genrated successfully!!")