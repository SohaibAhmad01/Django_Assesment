from django.contrib import admin

# Register your models here.

from .models import Profile,Hobby,Person,Address,Interest,City

admin.site.register(Profile)
admin.site.register(Hobby)
admin.site.register(Person)
admin.site.register(Interest)
admin.site.register(Address)
admin.site.register(City)
