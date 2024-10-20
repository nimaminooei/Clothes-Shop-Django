from django.contrib import admin
from .models import CustomUser, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 1  

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff', 'is_active', 'date_joined') 
    list_filter = ('is_staff', 'is_active')  
    search_fields = ('username',)  
    inlines = [ProfileInline] 


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)