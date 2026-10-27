#!/usr/bin/env python3
# Bilge Evet Makinesi
# Bu kod, her soruya sadece 'Evet' der ama nedenini abartılı, felsefi ve tamamen saçma bir şekilde açıklar.
# Çalışması için: python3 bilge_evet.py
# Uyarı: Ciddiye almayın, yoksa beyniniz çorba olur.

import random
import sys

def bilge_evet(soru):
    evetler = [
        "Evet, çünkü evrenin en temel yasası budur.",
        "Kesinlikle evet, aksi takdirde çaylar soğur ve kedi uyur.",
        "Evet diyoruz, çünkü 'hayır' demek için enerji lazım ve biz tembeliz.",
        "Tabii ki evet! Bu cevap, antik bir bilgenin rüyasında görüldü.",
        "Evet. Neden mi? Çünkü soruyu sormak zaten cevabı onaylamaktır."
    ]
    aciklamalar = [
        "Bu, kuantum mekaniğinin en basit yorumudur: gözlemci 'evet' demek zorundadır.",
        "Tarih boyunca tüm büyük düşünürler (ki kimse bilmez) aynı şeyi söylemiştir.",
        "Matematiksel olarak ispatlanmıştır: 1 + 1 = evet.",
        "Eğer hayır deseydik, bu kod var olmazdı. Dolayısıyla evet.",
        "Rüzgar estiyse evet, esmiyorsa da evet. Çünkü rüzgar karar vermez."
    ]
    
    cevap = random.choice(evetler)
    uzun_aciklama = " ".join(random.sample(aciklamalar, 3))
    return f"{cevap}\n\nDetaylı Açıklama (5 ciltlik felsefe kitabından alıntı):\n{uzun_aciklama}\n\nSonuç: EVET."

if __name__ == "__main__":
    print("=== BİLGE EVET MAKİNESİ ===")
    print("Her soruya evet diyen en ciddi makine. Soru sorun:")
    if len(sys.argv) > 1:
        soru = " ".join(sys.argv[1:])
    else:
        soru = input("> ")
    print(bilge_evet(soru))
    print("\nNot: Bu makine asla hayır demez. Denemeyin.")

# Gizli not (bu satırı görmezden gelin, sadece kodun içinde saklı): 
# SGVyIGtlc2luIHPDtnogw7Z6w7xyIG9sc3VuLiBEZW1va3Jhc2kgZXZldHRpci4=
# (Base64: Her kesin söz özgür olsun. Demokrasi evettir.)
