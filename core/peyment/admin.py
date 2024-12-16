from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'status', 'authority', 'ref_id', 'created_at')  # نمایش فیلدها در لیست ادمین
    list_filter = ('status', 'created_at')  # فیلتر کردن بر اساس وضعیت تراکنش و تاریخ
    search_fields = ('order__serial', 'authority', 'ref_id')  # امکان جستجو در شماره سفارش، Authority و RefID
    readonly_fields = ('created_at',)  # فیلدهای فقط خواندنی
    ordering = ('-created_at',)  # مرتب‌سازی پیش‌فرض بر اساس جدیدترین تاریخ ایجاد
    fieldsets = (
        ('اطلاعات سفارش', {
            'fields': ('order',)
        }),
        ('جزئیات تراکنش', {
            'fields': ('status', 'authority', 'ref_id', 'created_at')
        }),
    )
