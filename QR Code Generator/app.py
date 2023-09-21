import qrcode

# qr code generator function
def qr_code(text):

    #creating a QRCode instance
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
# version=1: Specifies the QR code version. it's set to 1, which represents the smallest QR code size.
# error_correction=qrcode.constants.
# ERROR_CORRECT_L: Sets the error correction level to "L" (Low), which provides the lowest level of error correction.
# box_size=10: Determines the size of each "box" (pixel) in the QR code.
# border=4: Sets the size of the border around the QR code.



    qr.add_data(text)
    qr.make(fit=True)
    # This line generates the QR code based on the data and configuration provided. The fit=True parameter
    #  ensures that the QR code adjusts its size to fit the data.

    img=qr.make_image()
    # creates an image representation of the QR code

    img.save('qr.png')
    # saves the image as a PNG file in the current working directory.

text=input('Enter the text or link you want to generate QR code for: ')
qr_code(text)
print('QR code generated successfully')
print('QR code saved as qr.png in current working directory.')






