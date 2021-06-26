# from django.db import models
# from graveyards.models import CustomModel
# from django.contrib.auth import get_user_model
# from django.utils.translation import gettext_lazy as _
#
# AuthUserModel = get_user_model()
#
#
# # Create your models here.
# class Cemetery(CustomModel):
#     class Meta:
#         verbose_name = 'cemetery'
#         verbose_name_plural = 'cemetery'
#
#     name = models.CharField(max_length=255, null=False)
#     address = models.CharField(max_length=255, null=False)
#     administrator = models.ForeignKey(AuthUserModel, null=False, on_delete=models.CASCADE, related_name='users')
#
#     # image = models.ImageField(upload_to='graveyards')
#
#
# class Parcel(CustomModel):
#     class Meta:
#         verbose_name = 'parcel'
#         verbose_name_plural = 'parcels'
#
#     graveyard = models.ForeignKey(Cemetery, null=False, on_delete=models.CASCADE, related_name='cemetery')
#
#     class Type(models.TextChoices):
#         LOT = '1', _('Lot')
#         TOMB = '2', _('Tomb')
#
#     type = models.CharField(
#         max_length=2,
#         choices=Type.choices,
#     )
#
#     class Status(models.TextChoices):
#         FREE = '1', _('Free')
#         RESERVED = '2', _('Reserved')
#
#     status = models.CharField(
#         max_length=2,
#         choices=Status.choices,
#     )
#
#     location = models.CharField(max_length=255, null=False)  # location_id?
