from django.contrib import admin
from .models import Coupons, EventSpeakers, Events, Packages, Participants, Payments, Speakers

# Optional: Define a custom admin interface
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'start_date', 'end_date', 'created_at', 'modified_at')
    list_filter = ('location', 'start_date')
    search_fields = ('name', 'description')

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'organization', 'photo_url', 'organization', 'biography', 'created_at', 'modified_at')
    search_fields = ('name', 'email', 'organization')

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'event', 'created_at')
    list_filter = ('role', 'event')
    search_fields = ('name', 'email')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('participant', 'event', 'amount', 'status', 'transaction_id', 'created_at', 'modified_at')
    list_filter = ('status', 'event')
    search_fields = ('participant__name', 'event__name', 'transaction_id')

class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percent', 'valid_until', 'speaker', 'created_at', 'modified_at')
    list_filter = ('discount_percent', 'valid_until')
    search_fields = ('code', 'description')
    date_hierarchy = 'valid_until'


class EventSpeakerAdmin(admin.ModelAdmin):
    list_display = ('speaker', 'event')
    list_filter = ('speaker__name', 'event__name')
    search_fields = ('speaker__name', 'event__name')
    raw_id_fields = ('speaker', 'event')

class PackageAdmin(admin.ModelAdmin):
    list_display = ('event', 'type', 'price', 'description', 'created_at', 'modified_at')
    list_filter = ('event', 'type', 'price')
    search_fields = ('description',)
    raw_id_fields = ('event',)


# Register your models here.
admin.site.register(Events, EventAdmin)
admin.site.register(Speakers, SpeakerAdmin)
admin.site.register(Participants, ParticipantAdmin)
admin.site.register(Payments, PaymentAdmin)
admin.site.register(Coupons, CouponAdmin)
admin.site.register(EventSpeakers, EventSpeakerAdmin)
admin.site.register(Packages, PackageAdmin)