
musteriler = []

def evet_hayir_sorusu(soru):
    while True:
        cevap = input(soru).lower()
        if cevap == 'evet' or cevap == 'hayır':
            return cevap
        else:
            print("Lütfen sadece 'evet' veya 'hayır' yazınız.")

# Müşteri Bilgilerini Alan Fonksiyon
def musteri_bilgisi_al():
    musteri = {}
    print("Spor Salonumuza Hoş Geldiniz!")
    
    sigara = evet_hayir_sorusu("Sigara içiyor musunuz? (evet/hayır): ")
    if sigara == 'evet':
        print("Üzgünüz, müşteri kriterlerimize uymuyorsunuz.")
        return None
    musteri['sigara'] = sigara
    
    musteri['isim'] = input("Adınız nedir? ")

    musteri['yaş'] = int(input("Yaşınız kaç? "))

    musteri['üyelik_türü'] = input("Üyelik türünüz nedir? (Altın, Gümüş, Bronz): ")
    
    musteri['hedefler'] = input("Spor salonundaki hedefleriniz nelerdir? ")

    musteriler.append(musteri)
    return musteri

while True:
    musteri = musteri_bilgisi_al()
    
    if musteri is None:
        break
    else:
        baska = evet_hayir_sorusu("Başka bir müşteri bilgisi girmek ister misiniz? (evet/hayır): ")
        if baska != 'evet':
            break

# Tüm müşteri bilgilerini yazdır

print("\nMüşteri Bilgileri:")
for idx, musteri in enumerate(musteriler, start=1):
    print(f"\nMüşteri {idx}:")
    for key, value in musteri.items():
        print(f"{key.capitalize()}: {value}")

#Kaydolan Kişiyi Txt Dosyasına Aktarıyor

with open('musteri_bilgileri.txt', 'w') as dosya:
    dosya.write("Müşteri Bilgileri:\n")
    for idx, musteri in enumerate(musteriler, start=1):
        dosya.write(f"\nMüşteri {idx}:\n")
        for key, value in musteri.items():
            dosya.write(f"{key.capitalize()}: {value}\n")
