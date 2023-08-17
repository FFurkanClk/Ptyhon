print("""
      ******************************************************
      Kulanici Girisi Programi
      ***************************************************""")
sys_kullaici_adi = "Furkan"
sys_kullanici_parola ="12345"

giris_hakki = 3

while True:
    kullaici_adi = input("Kullanici Adi:")
    parola = input("Parola:")
    
    if (kullaici_adi != sys_kullaici_adi and parola == sys_kullanici_parola):
        print("Kullanci Adi Hatali...")
        giris_hakki -= 1
    elif(kullaici_adi == sys_kullaici_adi and parola != sys_kullanici_parola):   
        print("Parola Hatali...")
        giris_hakki -= 1
    elif(kullaici_adi != sys_kullaici_adi and parola != sys_kullanici_parola):   
        print("Kullanici Adi ve Parola Hatali...")
        giris_hakki -= 1
    else:
        print("Sisteme Basariyle Girildi")   
        break
    if (giris_hakki == 0):
        print("Giris Hakiniz bitti")
        break