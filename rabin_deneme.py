import math
#çevirme fonksiyonları
def string_bin(string):
    return ''.join(format(ord(c), 'b') for c in string)

def bin_string(binary):
    bingen = (binary[i:i+7] for i in range(0, len(binary), 7))
    return ''.join(chr(eval('0b'+n)) for n in bingen)

#Asal sayılar https://en.wikipedia.org/wiki/Prime_number adresinden alınmıştır.
def anahtar_verileri(x):
    p = 2996863034895*2**1290000+1
    q = 2996863034895*2**1290000-1
    n = p * q
    if x == 1:
        return p
    if x == 2:
        return q
    if x == 3:
        return n


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)



#rabin crypt
def cryptrabin(plaintxt):
    metinbitleri = string_bin(plaintxt)
    sayisal_metin = int(metinbitleri)
    cipher_text = pow(sayisal_metin,2,anahtar_verileri(3))
    print(cipher_text)
    return cipher_text
#rabin decrypt
def decryprabin(binary):
    metin = int(binary)
    p = int(anahtar_verileri(1))
    q = int(anahtar_verileri(2))
    n = int(anahtar_verileri(3))
    yp_yq_hesapla = egcd(p,q)
    mp = math.sqrt(metin)%p
    mq = math.sqrt(metin)%q
    yp = yp_yq_hesapla[1]
    yq = yp_yq_hesapla[2]
    s1 =(yp*mq*p+yq*mp*q)%n
    s2 =(yp*mq*p-yq*mp*q)%n
    r1 =n-(yp*mq*p+yq*mp*q)%n
    r2 =n-(yp*mq*p-yq*mp*q)%n
    print('s1 = ', s1)
    print('s2 = ', s2)
    print('r1 = ', r1)
    print('r2 = ', r2)


plaintext = input("Plain text verin: ")
cipher = cryptrabin(plaintext) #şifreli hali gösteriliyor

print('Şifre çözülüyor. \n')
decryprabin(cipher)
