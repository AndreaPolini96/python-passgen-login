import random
import qrcode

def genera_password():
    vocali = 'aeiou'
    consonanti = 'bcdfghlmnpqrstvz'
    caratteri= '!?-_+^'
    password = []
    lunghezza = int(input("Quanti caratteri deve presentare ogni password? "))
    n=int(input("Quante password vuoi generare? "))

    if(lunghezza<4):
        print("ERRORE: lunghezza minima 4 caratteri!")
    else:
        for j in range(n):
            passwordTemp = f"{random.choice(caratteri)}"
            for i in range(lunghezza-2):
                if i % 2 == 0:
                    passwordTemp += random.choice(consonanti)
                else:
                    passwordTemp += random.choice(vocali) 
                i=i+1
            passwordTemp += f"{random.randint(0,10)}"
            password.append(passwordTemp)
    
    return password

if __name__ == "__main__":
    passwords = genera_password()
    for i, password in enumerate(passwords):
        print(password)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(password)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        #img.show() #qualora volessi aprire immediatamente l'immagine
        img.save(f"password_{i+1}.png")
