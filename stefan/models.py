# from django.db import models
#
# # Create your models here.
#
# class Registrering(models.Model):
#
#     firstName = models.CharField(max_length=140, null=True, blank=False, verbose_name="Fornavn")
#     lastName = models.CharField(max_length=140, null=True, blank=False, verbose_name="Etternavn")
#     department = models.CharField(max_length=140, null=True, blank=False, verbose_name="Avdeling")
#     TYPES = [
#     (0, '--------'),
#     (1, 'Løping'),
#     (2, 'Styrke'),
#     (3, 'Sykling'),
#     (4, 'Gåing'),
#     (5, 'Ski'),
#     (6, 'Svømming'),
#     ]
#
#     type = models.IntegerField(choices=TYPES, default=0)
#     distance = models.FloatField(null=True, blank=True, verbose_name="Distanse")
#     comment= models.TextField(null=True, blank=True, verbose_name="Kommentar")
#
#
#     class Meta:
#         ordering = ['firstName']
#         verbose_name = "Registrering"
#         verbose_name_plural = "Registreringer"
#
#     def __str__(self):
#         return f"ID: {self.id}"
