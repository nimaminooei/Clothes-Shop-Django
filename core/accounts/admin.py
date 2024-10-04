from django.contrib import admin
from .models import CustomUser, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 1  # تعداد فرم‌های خالی برای افزودن پروفایل

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff', 'is_active', 'date_joined')  # نمایش فیلدها در لیست کاربران
    list_filter = ('is_staff', 'is_active')  # فیلترها در لیست کاربران
    search_fields = ('username',)  # جستجو بر اساس نام کاربری
    inlines = [ProfileInline]  # پروفایل به عنوان فرم داخلی

# ثبت مدل‌ها در پنل مدیریت
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)