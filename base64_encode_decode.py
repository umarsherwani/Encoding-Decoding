
import base64 
# For Encoding th text
Text = input('Enter The text Here : ')
intial_encoded = Text.encode("ascii") 

base64_bytes = base64.b64encode(intial_encoded) 
base64_string = base64_bytes.decode("ascii") 

print(f"Encoded string: {base64_string}") 

# For Decoding the text

_Text = input("Enter the Encoded text : ")
intial = _Text.encode("ascii") 

sample_string_bytes = base64.b64decode(intial) 
sample_string = sample_string_bytes.decode("ascii") 

print(f"Decoded string: {sample_string}") 

#*********************************** Sample text of base85 ************************
# text = input('enter : ')
# your_text = text.encode('ascii')
# main = base64.b85encode(your_text)
# yess = main.decode('ascii')
# print(f"Encoded string: {yess}")