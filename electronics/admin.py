from django.contrib import admin

from electronics.models import Smartphone, SmartphoneImage, Laptop, LaptopImage

admin.site.register(Smartphone)
admin.site.register(SmartphoneImage)
admin.site.register(Laptop)
admin.site.register(LaptopImage)
