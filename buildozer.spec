[app]

title = Calendar App
package.name = calendarapp
package.domain = org.calendar

source.dir = .
source.include_exts = py,json

version = 1.0.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.api = 35
android.minapi = 23
android.archs = arm64-v8a

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1