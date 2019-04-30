from django.contrib import admin
from .models import UserProfile,UserInfo

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','phone','birth')

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(UserInfo,UserInfoAdmin)