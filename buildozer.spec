[app]

# (str) Uygulama başlığı
title = Step Pro

# (str) Paket adı ve domain
package.name = steppro
package.domain = org.steppro

# (str) Kaynak kod dizini
source.dir = .

# (list) Dahil edilecek dosya uzantıları
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Uygulama sürümü
version = 0.1

# (list) Uygulama bağımlılıkları (Kivy, Plyer ve Android kütüphaneleri)
requirements = python3,kivy,plyer,android

# (list) İvmeölçer ve fiziksel aktivite izinleri
android.permissions = ACTIVITY_RECOGNITION, HIGH_SAMPLING_RATE_SENSORS, INTERNET

# (int) Hedef Android API sürümü
android.api = 33

# (int) Minimum Android API sürümü (Android 7.0+)
android.minapi = 24

# (str) Desteklenen ekran yönü
orientation = portrait

# (bool) Tam ekran modu (0: Kapalı, 1: Açık)
fullscreen = 0

# (list) Desteklenen mimariler
android.archs = arm64-v8a, armeabi-v7a

# (bool) Android Otomatik Yedekleme
android.allow_backup = True

[buildozer]

# (int) Log detay seviyesi (2 = Detaylı loglama)
log_level = 2

# (int) Root yetkisiyle çalıştırma uyarısı
warn_on_root = 1
