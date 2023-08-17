print("""
                                                    **************************

                                                    ATM MAKİNESİNE HOŞGELDİNİZ

                                                    **************************

      GİRİŞ YAPMAK İÇİN "G" TUŞUNA BASIN

        İŞLEMLER:

            1.BAKİYE SORGULAMA

                 2.PARA YATIRMA

                   3.PARA ÇEKME

       PROGRAMDAN ÇIKMAK İÇİN "q" TUŞUNA BASIN

                                                  """)
bakiye = 1000
sys_isim = "Furkan"
sys_parola = "12345"
while True:
        
        isim = input("İsminiz:")
        parola = input("Parolaniz:")

        if( isim != sys_isim and parola == sys_parola):
            print("İsim Hatali")
        elif( isim == sys_isim and parola != sys_parola):
            print("Parola Hatali")
        elif(isim != sys_isim and parola != sys_parola):
            print("İsim ve Parola Hatali")        
        else:
             print("Başariyla Giriş Yaptiniz  \n  Hoşgeldin {}".format(isim))
             break
while True:               
        işlem = input("İşlemi Seçin:")

        if (işlem == "q"):
            print("İyi Günler Dileriz")
            break
        elif (işlem == "1"):
             print("Bakiyeniz {} TL dir.".format(bakiye))

        elif (işlem == "2"):
             miktar = int(input("Miktari Girin:"))
             bakiye += miktar
        
        elif (işlem == "3"):
              miktar = int(input("Miktari Girin:"))
              if (bakiye - miktar < 0):
                  print("Bakiyeniz yetersiz bakiyeniz {} ".format(bakiye))
                  continue
              bakiye -= miktar
        
        else:
         print("Geçersiz İşlem")