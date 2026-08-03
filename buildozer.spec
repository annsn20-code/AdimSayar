[app]

# Uygulamanın adı
title = Adim Sayaci

# Paket adı (Boşluksuz ve küçük harf olmalı)
package.name = adimsayaci

# Paket domaini
package.domain = org.sulo

# Kaynak kod dizini (main.py'nin olduğu yer)
source.dir = .

# Dahil edilecek dosya uzantıları
source.include_exts = py,png,jpg,kv,atlas

# Uygulama versiyonu
version = 0.1

# GEREKSİNİMLER (Sensör için plyer eklendi)
requirements = python3, kivy, plyer

# Ekran yönü (Adım sayacı için dikey - portrait)
orientation = portrait

# Tam ekran modu (0 = Kapalı, üstteki saat ve şarj görünür)
fullscreen = 0

# İZİNLER (İvmeölçer sensör izni)
android.permissions = HIGH_SAMPLING_RATE_SENSORS

# Hedef Android API sürümü
android.api = 33

# Minimum Android API sürümü
android.minapi = 24

# NDK SÜRÜMÜ (Hata almamak için 25b'ye sabitlendi)
android.ndk = 25b

# SDK lisanslarını otomatik kabul et
android.accept_sdk_license = True

# Derlenecek mimariler (Çoğu modern telefon için)
android.archs = arm64-v8a, armeabi-v7a

# Yedeklemeye izin ver
android.allow_backup = True

[buildozer]

# Hata ayıklama log seviyesi (2 = Detaylı çıktı)
log_level = 2

# Root uyarısı
warn_on_root = 1
