#RSA Cipher
import math
def RSA_Cipher():
    p = int(input("Enter a prime number p: "))
    q = int(input("Enter a prime number q: "))
    n = p * q
    phi = (p - 1) * (q - 1)
    for i in range(2, phi): 
        if math.gcd(i, phi) == 1:
            e = i
            break   
    x = 0 
    y = phi + 1 
    d = 0
    while x % phi != 1: 
        x2 = e * y 
        if x2 % phi == 1: 
            d = y
            x = 1 
        else: 
            y += 1
    print(f"Public key: (e={e}, n={n})")
    print(f"Private key: (d={d}, n={n})")
    message = (input("Enter the message to encrypt: ")).lower() 
    newmessage = ""
    for i in message:  
        if i == " ":  
            newmessage += " "  
            continue
        i = ord(i) - 97  
        ciphertext = pow(i, e) 
        ciphertext = ciphertext % n
        newmessage += chr(ciphertext + 96)
    print(f"Encrypted message: {newmessage}") 
    decrypted_message = ""
    for i in newmessage:    
        if i == " ":  
            decrypted_message += " "  
            continue
        i = ord(i) - 96
        decrypted_text = pow(i, d)  
        decrypted_text = decrypted_text % n 
        decrypted_message += chr(decrypted_text + 97)
    print(f"Decrypted message: {decrypted_message}")
RSA_Cipher()