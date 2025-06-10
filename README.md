# MathGame

MathGame, bir Python konsol uygulaması olarak tasarlanmış, kullanıcıların matematik sorularını çözerek puan kazandığı bir oyun simülasyonudur. Oyuncular, kolay, normal veya zor seviyelerden birini seçerek oyuna başlayabilir.

## Özellikler

- **Seviye Seçimi**: Oyuncular, kolay (`e`), normal (`n`) veya zor (`h`) seviyelerden birini seçebilir.
- **Dinamik Soru Üretimi**: Rastgele sayılar ve işlemlerle matematik soruları oluşturulur.
- **Puanlama Sistemi**: Doğru cevaplar için puan kazanılır, yanlış cevaplar için puan kaybedilir.
- **Farklı Zorluk Seviyeleri**:
  - **Kolay**: Toplamda 5 soru, 1 ile 50 arasında sayılar.
  - **Normal**: Toplamda 10 soru, 1 ile 100 arasında sayılar.
  - **Zor**: Toplamda 10 soru, 50 ile 500 arasında sayılar ve çarpma işlemi dahil.

## Nasıl Kullanılır?

1. Depoyu klonlayın veya `MathGame.py` dosyasını yerel makinenize kopyalayın.
2. Programı bir Python yorumlayıcısı kullanarak çalıştırın (örneğin, `python3`).
   ```bash
   python3 MathGame.py
   ```
3. Oyuncu, kolay (`e`), normal (`n`) veya zor (`h`) seviyelerden birini seçer.
4. Oyuncu, soruları çözerek puan kazanmaya çalışır.
5. Oyun sonunda toplam puan görüntülenir.

## Örnek

```plaintext
Please select your destination (Easy: e, Normal: n, Hard: h): e
You have chosen the LOSERS path you idiot. We are starting with 5 questions.
Quesiton  0 
 25 + 15
Your Answer: 40
Correct! Here is +1 point for you.
Quesiton  1 
 30 - 10
Your Answer: 25
Wrong! I'll take one of your points.
Your last point is:  0
```

## Gereksinimler

- Python 3.x yüklü bir ortam.
- Terminal veya komut satırı bilgisi.

## Notlar

- Program, kullanıcı girdilerini doğrular ve yalnızca geçerli cevapları kabul eder.
- Zor seviyede çarpma işlemi de dahil olmak üzere daha karmaşık matematik işlemleri bulunur.
- Puanlama sistemi, oyuncunun performansını ölçmek için tasarlanmıştır.

## Lisans

Bu proje açık kaynaklıdır ve [MIT Lisansı](https://opensource.org/licenses/MIT) altında sunulmaktadır.
