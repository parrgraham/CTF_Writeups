"""
    with open('binary.bin','wb') as f:  with open('binary.bin','wb') as f:  with open()
    with open('binary.bin','wb') as f:  with open('binary.bin','wb') as f:  with open('binary.bin','wb') as f:
    
        text = u'this is a test string'
        






"""

# 
# Define a string containing some non-ASCII characters
test_str = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽"

# Convert the string to a byte array using UTF-16 encoding
bytes = test_str.encode('utf-16')

# Print the original string and the encoded bytes
print("Original string: " + test_str)
print("Encoded bytes: " + str(bytes))

# Convert the encoded bytes back to a string
decoded_str = bytes.decode('utf-16')

# Print the decoded string
print("Decoded string: " + decoded_str)
