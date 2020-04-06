# imports
from django.db import models
from django.conf import settings
from django.utils import timezone

# End: imports -----------------------------------------------------------------


class Registrering(models.Model):
    TYPES = [
        (0, '------'),
        (1, 'styrke'),
        (2, 'løping'),
        (3, 'sykling'),
        (4, 'gåing'),
        (5, 'svømming'),
        (6, 'ski'),
    ]

    first_name = models.CharField(max_length=140, null=True, blank=False, verbose_name="Fornavn")
    last_name = models.CharField(max_length=140, null=True, blank=False, verbose_name="Etternavn")
    department = models.CharField(max_length=140, null=True, blank=False, verbose_name="Avdeling")
    type = models.IntegerField(choices=TYPES, default=0, verbose_name="Treningstype")
    distance = models.FloatField(null=True, blank=True, verbose_name="Distanse")
    comment = models.TextField(null=True, blank=True)


    class Meta:
        ordering = ['first_name']
        verbose_name = "Registrering"
        verbose_name_plural = "Registreringer"

    def __str__(self):
        return f"ID: {self.id}"




# class Example(models.Model):
#     title = models.CharField(max_length=140, null=True, blank=False, verbose_name="Tittel")
#     course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, null=True, blank=True, related_name="sections", verbose_name="Kurs")
#     description = models.TextField(null=True, blank=True, verbose_name="Beskrivelse")
#     start = models.TimeField(null=True, blank=True)
#     # duration = models.FloatField(null=True, blank=False, verbose_name="Varighet")
#     duration = models.FloatField(default=7.5, null=True, blank=False, verbose_name="Varighet")
#     song = models.ForeignKey('songs.Song', on_delete=models.SET_NULL, null=True, blank=True, related_name="sections", verbose_name="Sang")
#     song2 = models.ForeignKey('songs.Song', on_delete=models.SET_NULL, null=True, blank=True, related_name="sections_song2", verbose_name="Sang")
#     video = models.ForeignKey('videos.Video', on_delete=models.SET_NULL, null=True, blank=True, related_name="sections", verbose_name="Video")
#     nr = models.IntegerField(null=True, blank=True)
#
#     class Meta:
#         ordering = ['nr']
#         verbose_name = "Kurs-seksjon"
#         verbose_name_plural = "Kurs-seksjoner"
#
#     def __str__(self):
#         return "Section ({}) in course: {}".format(self.getNr(), self.getCourse())
#
#     def getCourse(self):
#         return self.course or None
#
#     def getNr(self):
#         return self.nr or None
#
#     def getStart(self):
#         return self.start.strftime("%H:%M")
#
#     def getSong(self):
#         return self.song or None
