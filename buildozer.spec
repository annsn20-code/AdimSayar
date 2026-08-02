[app]

title = Adim Sayar
package.name = adimsayar
package.domain = org.gamertilki

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,atlas

version = 1.0

requirements = python3,kivy,pyjnius

orientation = portrait

fullscreen = 0

android.permissions = ACTIVITY_RECOGNITION

android.api = 35
android.minapi = 21
android.ndk = 28c

android.archs = arm64-v8a

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
