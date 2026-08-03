[app]

# Uygulama Başlığı
title = Step Pro

# Paket Adı (Küçük harf ve boşluksuz)
package.name = steppro

# Paket Domaini
package.domain = org.sulo

# Kaynak kod dizini (main.py'nin olduğu dizin)
source.dir = .

# Kodun dahil edeceği dosya uzantıları (JSON verisini ve ikonları kapsar)
source.include_exts = py,png,jpg,kv,atlas,json

# Uygulama Versiyonu
version = 0.1

# GEREKSİNİMLER
# Kodundaki 'from android.permissions import ...' yapısı için 'android' kütüphanesi eklendi.
requirements = python3, kivy, android

# Ekran Yönü (Dikey)
orientation = portrait

# Tam Ekran Modu (0 = Üstteki durum çubuğu görünür)
fullscreen = 0

# İZİNLER
# Kodunda istediğin ACTIVITY_RECOGNITION ve ivmeölçer için gerekli izinler:
android.permissions = ACTIVITY_RECOGNITION, HIGH_SAMPLING_RATE_SENSORS

# Hedef Android API Sürümü
android.api = 33

# Minimum Android API Sürümü (ACTIVITY_RECOGNITION izni için en az 29 önerilir)
android.minapi = 29

# NDK SÜRÜMÜ (Derleme hatası almamak için 25b'ye sabitlendi)
android.ndk = 25b

# SDK Lisanslarını Otomatik Kabul Et
android.accept_sdk_license = True

# Desteklenen İşlemci Mimarileri
android.archs = arm64-v8a, armeabi-v7a

# Android Otomatik Yedekleme
android.allow_backup = True

[buildozer]

# Detaylı Hata Log Seviyesi
log_level = 2

# Root Uyarısı
warn_on_root = 1
