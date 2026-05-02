# Import Required Libraries
import qrcode
from PIL import Image #PIL(Python Library Image)
import datetime

# Take Input from the user (url or text)
data=input("Enter the URL or Text: ")

# Basic validation to check empty input
if data=="":
    print("Invalid Input")
    exit()   # stop the program if input is empty 


# Take QR color and the background color from the user
fill_qr_color=input("Enter the QR color: ")
background_color=input("Enter the background color: ")

# Image Save 
image_save=input("Enter the your save image name: ")

qr=qrcode.QRCode(version=1  # Controls the size of the QR code (1=smallest)
                 , error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction level
                   box_size=20, # Size of each box in the QR code
                   border=10,   # Thickness of the border (white space)   
                )


# Add data to the QR code
qr.add_data(data)

# Generate the QR code 
qr.make(fit=True)

# Convert QR code into an image with custom colors
try:
    image=qr.make_image(fill_color=fill_qr_color, back_color=background_color)

except:
    print("Invalid color! Using default colors")
    image=qr.make_image(fill_color="black", back_color="white")
    

#Print success message
print("QR Generated Sucessfully")

# Print the current time  (basic tracking feature)
print("Time: ", datetime.datetime.now())

image.save(image_save + ".png")