{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4ff1e416",
   "metadata": {},
   "source": [
    "###Soru 1: Görev Yöneticisi Uygulaması\n",
    "Proje Açıklaması: Bu ödevde, Python programlama dilini kullanarak bir görev yöneticisi uygulaması oluşturacaksınız. Bu uygulama kullanıcıların görevlerini eklemelerine, tamamlamalarına, silmelerine ve listelemelerine olanak tanıyacaktır.\n",
    "\n",
    "Gereksinimler:\n",
    "1- Görevler bir Python listesinde saklanacak ve her görev bir sözlük olarak temsil edilecektir. Her görevin aşağıdaki özelliklere sahip olması gerekir:\n",
    "\n",
    "Sıra Numarası (Otomatik olarak atanır)\n",
    "\n",
    "Görev Adı\n",
    "\n",
    "Durum (Tamamlandı, Bekliyor veya Silindi)\n",
    "\n",
    "2- Kullanıcının yapabileceği işlemler:\n",
    "\n",
    "Yeni bir görev ekle\n",
    "\n",
    "Bir görevi tamamla\n",
    "\n",
    "Bir görevi sil\n",
    "\n",
    "Tamamlanan görevleri listele\n",
    "\n",
    "Tüm görevleri durumlarıyla birlikte listeleyin\n",
    "\n",
    "Çıkış\n",
    "\n",
    "3- Görevler eklenme sırasına göre otomatik olarak sıra numarası almalıdır.\n",
    "\n",
    "4- Silinen görev numaralarının yerine yeni görevler kaydedilmeli.\n",
    "\n",
    "5- Görevler listelenirken sıra numarasına göre sıralanmalıdır.\n",
    "\n",
    "6- Her işlemden sonra kullanıcıya uygun geri bildirim verilmelidir. Örneğin, yeni bir görev eklendiğinde, görevin eklendiğini belirten bir mesaj görmelidir."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f98c7bcc",
   "metadata": {},
   "outputs": [],
   "source": [
    "
gorevler = []
siradaki_numara = 1 

def gorev_ekle(ad):
    global siradaki_numara
    gorev = {
        "sira": siradaki_numara,
        "ad": ad,
        "durum": "Bekliyor"
    }
    gorevler.append(gorev)
    print(f"\n görev eklendi: [{siradaki_numara}] {ad}")
    siradaki_numara += 1

def gorev_tamamla(sira_no):
    for gorev in gorevler:
        if gorev["sira"] == sira_no and gorev["durum"] != "Silindi":
            gorev["durum"] = "Tamamlandi"
            print(f" görev tamamlandi: [{sira_no}] {gorev['ad']}")
            return
    print(" geçerli bir sira numarasi bulunamadi.")

def gorev_sil(sira_no):
    for gorev in gorevler:
        if gorev["sira"] == sira_no and gorev["durum"] != "Silindi":
            gorev["durum"] = "Silindi"
            print(f" görev silindi: [{sira_no}] {gorev['ad']}")
            return
    print(" geçerli bir sira numarasi bulunamadi veya zaten silinmiş.")

def tamamlanan_gorevler():
    print("\n Tamamlanan görevler:")
    tamamlananlar = [j for j in gorevler if j ["durum"] == "Tamamlandi"]
    if not tamamlananlar:
        print("Henüz tamamlanan görev yok.")
    for j in sorted(tamamlananlar, key=lambda x: x["sira"]):
        print(f"[{j['sira']}] {j['ad']}")

def tum_gorevler():
    print("\n Tüm görevler:")
    if not gorevler:
        print("Henüz hiç görev eklenmedi.")
    else:
        for j in sorted(gorevler, key=lambda x: x["sira"]):
            print(f"[{j['sira']}] {j['ad']} - Durum: {j['durum']}")

def menu():
    while True:
        print("""
======= gÖREV YÖNETİCİSİ =======
1. Yeni görev Ekle
2. görevi Tamamla
3. görevi Sil
4. Tamamlanan görevleri Listele
5. Tüm görevleri Listele
6. Çikiş
""")
        secim = input("Bir işlem seçin (1-6): ")

        if secim == "1":
            ad = input("görev adini girin: ")
            gorev_ekle(ad)
        elif secim == "2":
            try:
                sira_no = int(input("Tamamlanacak görev sira numarasi: "))
                gorev_tamamla(sira_no)
            except ValueError:
                print(" Lütfen geçerli bir sayi girin.")
        elif secim == "3":
            try:
                sira_no = int(input("Silinecek görev sira numarasi: "))
                gorev_sil(sira_no)
            except ValueError:
                print(" Lütfen geçerli bir sayi girin.")
        elif secim == "4":
            tamamlanan_gorevler()
        elif secim == "5":
            tum_gorevler()
        elif secim == "6":
            print(" Çikiliyor... İyi günler!")
            break
        else:
            print(" geçerli bir seçenek girin.")


menu()\n",
    "       "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
