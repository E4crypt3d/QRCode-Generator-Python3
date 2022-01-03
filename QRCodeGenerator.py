import pyqrcode

print("Enter text to convert")
user_text=input(": ")

print("Save as")
filename=input(": ")

full_filename=filename+".png"
url=pyqrcode.create(user_text)

url.png(full_filename, scale =9)
url.show()