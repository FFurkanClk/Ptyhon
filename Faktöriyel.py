print("""
      ******************************************************
      Faktoriyel Hesaplama Programi
        Çikiş Yapmak İçin "q" Tuşuna Basin
      ***************************************************""")
while True:
    sayi = input("Sayi:")
    if (sayi == "q"):
        print("Programdan Çikildi")
        break
    else:
        sayi = int(sayi)

        faktoriyel = 1

        for i in range(2,sayi+1):
            print("Faktoriyel",faktoriyel,"i:",i)
            faktoriyel *= i
            print("Faktöriyel: ",faktoriyel)