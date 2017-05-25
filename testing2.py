#!/usr/bin/env python3 
#-*- coding:utf-8 -*-
import sqlite3
from tkinter import *
vt=sqlite3.connect('defter3.sqlite3')#Veritabanı bağlantısı
im=vt.cursor() #İmleç oluşturmak
#Tablo oluşturmak
im.execute("CREATE TABLE IF NOT EXISTS kayitlar2(sehir TEXT,plaka TEXT)")
def kaydet():
  sehrin_ismi=giris.get().upper()
  plaka_kodu=giris2.get()
  im.execute("SELECT * FROM kayitlar2")
  cities=im.fetchall()
  for i in range(0,len(cities)):
    if plaka_kodu==cities[i][1]:
      mesaj1=Label(text="Bu şehir zaten kayıtlı !")
      mesaj1.pack()
      break
  else:
    im.execute("INSERT INTO kayitlar2 VALUES (?,?)",(sehrin_ismi,plaka_kodu))
    mesaj2=Label(text="Başarılı bir şekilde ekleme yaptınız.")
    mesaj2.pack()
  vt.commit()
def plaka_ekle():
  global giris
  global giris2
  etiket=Label(text="Şehrin ismini giriniz : ")
  etiket.pack()

  giris=Entry()
  giris.pack()

  etiket2=Label(text="Şehre ait plaka kodu giriniz : ")
  etiket2.pack()

  giris2=Entry()
  giris2.pack()

  kaydet_butonu=Button(text="Ekle", command=kaydet)
  kaydet_butonu.pack()
  cikis_butonu=Button(text="Çıkış",command=pencere.quit)
  cikis_butonu.pack()
def listele():
  mesaj3=Label(text="Sistemde Kayıtlı Şehirler")
  mesaj3.pack()
  cities2=im.execute("SELECT * FROM kayitlar2")
  listbox=Listbox(pencere)
  listbox.pack()
  for i in cities2:
    listbox.insert(END, i)
  ekle_butonu=Button(text="Şehir&Plaka Ekle",command=plaka_ekle)
  ekle_butonu.pack()
  cikis_butonu=Button(text="Çıkış",command=pencere.quit)
  cikis_butonu.pack()
def sil():
  silinecek_plaka=giris3.get()
  im.execute("SELECT * FROM kayitlar2")
  cities3=im.fetchall()
  for i in range(0,len(cities3)):
    if silinecek_plaka==cities3[i][1]:
      im.execute("DELETE FROM kayitlar2 WHERE plaka=(?)",(silinecek_plaka,))
      mesaj2=Label(text="Başarılı bir şekilde silindi.")
      mesaj2.pack()
      break
  else:
    mesaj1=Label(text="Bu plaka kodu zaten kayıtlı değil!")
    mesaj1.pack()
  vt.commit()
def plaka_sil():
  global giris3
  mesaj4=Label(text="Silinecek Şehrin Plaka Kodunu Giriniz : ")
  mesaj4.pack()

  giris3=Entry()
  giris3.pack()
  
  sil_butonu=Button(text="Sil",command=sil)
  sil_butonu.pack()
  ekle_butonu=Button(text="Şehir&Plaka Ekle",command=plaka_ekle)
  ekle_butonu.pack()
  cikis_butonu=Button(text="Çıkış",command=pencere.quit)
  cikis_butonu.pack()
def bul():
  bulunacak_sehir=giris4.get().upper()
  im.execute("SELECT * FROM kayitlar2 WHERE sehir=(?)",(bulunacak_sehir, ))
  sonuc=im.fetchall()
  sonuc2=Label(text=bulunacak_sehir+" ilinin plaka kodu="+sonuc[0][1])
  sonuc2.pack()
def plaka_bul():
  global giris4

  mesaj5=Label(text="Hangi Şehrin Plakasını Öğrenmek İstiyorsunuz?")
  mesaj5.pack()
  
  giris4=Entry()
  giris4.pack()
  
  bul_butonu=Button(text="Bul",command=bul)
  bul_butonu.pack()

#---------------------------PENCERE--------------------------------
#Pencere oluşturmak
pencere=Tk()
pencere.geometry("450x800")

mesaj1=Label(text="TÜRKİYE PLAKA UYGULAMASI")
mesaj1.pack()
#Bu kodları internetten buldum.
#Mac'te sıkıntısız çalışıyor.Windows'ta deneyelim.
#Windows'ta da çalıştığı test edilmiştir.
#Sorunsuz bir şekilde çalışıyor.
mb=  Menubutton (pencere, text="İşlem Seçiniz", relief=RAISED )
mb.pack()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu


mb.menu.add_command ( label="Plaka Ekle",command=plaka_ekle)
mb.menu.add_command ( label="Tüm Plakaları Listele",command=listele)
mb.menu.add_command ( label="Şehir/Plaka Sil",command=plaka_sil)
mb.menu.add_command ( command=plaka_bul())
mb.pack()




mainloop()