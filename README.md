# Mon Topology Rutini Otomasyonu

### Giriş
Bu repo BİDB tarihinde bir milat niteliği taşıyabilir. Nöbet kavramını oluşturan **mon ve topoloji** rutinini otomatize edilmiş bir sisteme indirgeyip C nöbetlerinin amacını ortadan kaldırabilir.

### Neden yapıyorum?

> Üşengeçlik
<br>

> Bide CVye falan yazarız python biliyoz diye. :)


### Kurulum (Windows)
[Buradan indirebilirsiniz.](https://github.com/the-src/mon-and-topology/releases/tag/v1.0)

<br>

### Kaynak koddan kullanım

[Chrome](https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B4B77B947-B1C7-F937-671D-C61FBD15373E%7D%26lang%3Dtr%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DFKPE%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe) ve [Python](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe) yüklü olmalıdır. Üstlerine tıklayarak indirebilirsiniz.

Python indirdikten sonra aşağıdaki komutu açtığınız zip dosyasının içinde çalıştırmanız gerekmektedir.

```pip install requirements.txt```

### Fonksiyonlar

<!-- Topology sisteminde değişiklik olursa kodda bazı kısımların güncellenmesi gerekebilir. -->
<!-- Mon için şu anda süper bir rutin alıyor, test edilmedi (artık edildi) ama text formatlaması çok iyi oldu; kendimi aştım orda. -->

Şu anda cihazların durumunu ve bilgilerini bir dosyaya çekip, up-down durumlarını kontrol eder. Bunun sonucunda rutin mesajını size yansıtmakla kalmaz, bunu mercekteki rutin alma bölümüne kaydeder. İleride talep olursa saat ayarı getirilebilir. Kullanım hakkında sorularınız ve önerileriniz olursa pull request atabilir veya [mail adresimden](mailto:saraclioglu@itu.edu.tr) bana ulaşabilirsiniz.

**!!!! Yeni Fonksiyon eklendi !!!!**
Artık tek kaldığınız nöbetlerde `timed_mercek.py` dosyasını çalıştırarak her saat başı 20 geçe <!-- çaktırmadan --> rutin alabilirsiniz.

<br>

![](https://media.giphy.com/media/F6L3rTYMhBJL6D0qDL/giphy.gif)
