from django.contrib import admin
from collecjv.models import Company, Collection, Platform, Game, GameCompany, GameCollection, GameUser

# Register your models here.
admin.site.register(Company)
admin.site.register(Collection)
admin.site.register(Platform)
admin.site.register(Game)
admin.site.register(GameCompany)
admin.site.register(GameCollection)
admin.site.register(GameUser)
