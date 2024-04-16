# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Coupons(models.Model):
    code = models.CharField(unique=True, max_length=255, blank=True, null=True)
    speaker = models.ForeignKey('Speakers', models.DO_NOTHING)
    discount_percent = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    valid_until = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'coupons'
        verbose_name = 'coupon'
        verbose_name_plural = 'coupons'


class EventSpeakers(models.Model):
    speaker = models.ForeignKey('Speakers', models.DO_NOTHING)
    event = models.ForeignKey('Events', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_speakers'
        verbose_name = 'event speaker'
        verbose_name_plural = 'event speakers'


class Events(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} ({self.start_date.year}-{self.start_date.month}-{self.start_date.day} {self.start_date.hour}:{self.start_date.minute} - {self.end_date.year}-{self.end_date.month}-{self.end_date.day} {self.end_date.hour}:{self.end_date.minute})'

    class Meta:
        managed = False
        db_table = 'events'
        verbose_name = 'event'
        verbose_name_plural = 'events'
        


class Packages(models.Model):
    event = models.ForeignKey(Events, models.DO_NOTHING, blank=True, null=True)
    type = models.TextField()  # This field type is a guess.
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'packages'
        verbose_name = 'price package'
        verbose_name_plural = 'price packages'


class Participants(models.Model):
    role = models.TextField()  # This field type is a guess.
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    doc_no = models.CharField(max_length=120)
    event = models.ForeignKey(Events, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name} ({self.role} - {self.email} | {self.doc_no})'

    class Meta:
        managed = False
        db_table = 'participants'
        verbose_name = 'participant'
        verbose_name_plural = 'participants'


class Payments(models.Model):
    participant = models.ForeignKey(Participants, models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(Events, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    coupon = models.ForeignKey(Coupons, models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey(Packages, models.DO_NOTHING, blank=True, null=True)
    url = models.CharField(max_length=2048, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'payments'
        verbose_name = 'payment'
        verbose_name_plural = 'payments'


class Speakers(models.Model):
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    organization = models.CharField(max_length=255)
    photo_url = models.CharField(max_length=255, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self) -> str:
        return f'{self.name} ({self.email})'

    class Meta:
        managed = False
        db_table = 'speakers'
        verbose_name = 'speaker'
        verbose_name_plural = 'speakers'
