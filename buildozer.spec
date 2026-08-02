[app]

title = Adım Sayar
package.name = adimsayar
package.domain = org.adimsayar

source.dir = .
source.include_exts = py,json,png,jpg,jpeg,kv,atlas

version = 1.0

requirements = python3,kivy,pyjnius

orientation = portrait

fullscreen = 0

android.permissions = ACTIVITY_RECOGNITION

android.api = 35
android.minapi = 21
android.ndk = 26c

android.archs = arm64-v8a

android.accept_sdk_license = True

android.allow_backup = False

[buildozer]

log_level = 2
warn_on_root = 1
