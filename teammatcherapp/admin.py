from telnetlib import SE
from django.contrib import admin
from .models import User, LeaderBoardPosition, shopInfo
# Register your models here.
admin.site.register(User)
admin.site.register(LeaderBoardPosition)
admin.site.register(shopInfo)
