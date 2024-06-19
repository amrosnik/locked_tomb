import string

cipher = [20,8,5,20,15,23,5,18,8,1,19,18,5,1,3,20,9,22,1,20,5,4]

alphabet = {(n+1):s for n,s in enumerate(string.ascii_lowercase)}

message = ""
for n,c in enumerate(cipher):
    message += alphabet.get(c)

print(message) # the message is: thetowerhasreactivated
