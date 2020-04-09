# # imports
# from django.db import models
# from django.conf import settings
# from django.utils import timezone
#
# # End: imports -----------------------------------------------------------------
#
#
# class Workout(models.Model):
#     NOTHING = 0
#     STRENGTH = 1
#     RUNNING = 2
#     CYCLING = 3
#     WALKING = 4
#     SWIMMING = 5
#     SKIING = 6
#     TYPES = [
#         (NOTHING, '------'),
#         (STRENGTH, 'styrke'),
#         (RUNNING, 'løping'),
#         (CYCLING, 'sykling'),
#         (WALKING, 'gåing'),
#         (SWIMMING, 'svømming'),
#         (SKIING, 'ski'),
#     ]
#     POINTS = {
#         NOTHING: 0,
#         STRENGTH: 4,
#         RUNNING: 1,
#         CYCLING: 1/4,
#         WALKING: 1/2,
#         SWIMMING: 2,
#         SKIING: 1/2,
#     }
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=False, related_name="workouts", verbose_name="Bruker")
#     type = models.IntegerField(choices=TYPES, default=0, verbose_name="Treningstype")
#     distance = models.FloatField(default=0, null=False, blank=True, verbose_name="Distanse")
#     comment = models.TextField(null=True, blank=True, verbose_name="Kommentar")
#
#     date = models.DateField(null=True, blank=True, verbose_name="Dato")
#     created = models.DateTimeField(null=True, blank=True, editable=False, verbose_name="Opprettet")
#
#     class Meta:
#         ordering = ["-id"]
#         verbose_name = "Treningsøkt"
#         verbose_name_plural = "Treningsøkter"
#
#     def __str__(self):
#         return f"{self.user}, {self.get_type_display()}, {self.date}"
#
#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.created = timezone.now()
#
#         return super(type(self), self).save(*args, **kwargs)
#
#     @classmethod
#     def NOTHING_P(cls):
#         return cls.POINTS[cls.NOTHING]
#
#     @classmethod
#     def STRENGTH_P(cls):
#         return cls.POINTS[cls.STRENGTH]
#
#     @classmethod
#     def RUNNING_P(cls):
#         return cls.POINTS[cls.RUNNING]
#
#     @classmethod
#     def CYCLING_P(cls):
#         return cls.POINTS[cls.CYCLING]
#
#     @classmethod
#     def WALKING_P(cls):
#         return cls.POINTS[cls.WALKING]
#
#     @classmethod
#     def SWIMMING_P(cls):
#         return cls.POINTS[cls.SWIMMING]
#
#     @classmethod
#     def SKIING_P(cls):
#         return cls.POINTS[cls.SKIING]
#
#
#
# # class Example(models.Model):
# #     title = models.CharField(max_length=140, null=True, blank=False, verbose_name="Tittel")
# #     course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, null=True, blank=True, related_name="sections", verbose_name="Kurs")
# #     description = models.TextField(null=True, blank=True, verbose_name="Beskrivelse")
# #     start = models.TimeField(null=True, blank=True)
# #     # duration = models.FloatField(null=True, blank=False, verbose_name="Varighet")
# #     duration = models.FloatField(default=7.5, null=True, blank=False, verbose_name="Varighet")
# #     song = models.ForeignKey('songs.Song', on_delete=models.SET_NULL, null=True, blank=True, related_name="sections", verbose_name="Sang")
# #     song2 = models.ForeignKey('songs.Song', on_delete=models.SET_NULL, null=True, blank=True, related_name="sections_song2", verbose_name="Sang")
# #     video = models.ForeignKey('videos.Video', on_delete=models.SET_NULL, null=True, blank=True, related_name="sections", verbose_name="Video")
# #     nr = models.IntegerField(null=True, blank=True)
# #
# #     class Meta:
# #         ordering = ['nr']
# #         verbose_name = "Kurs-seksjon"
# #         verbose_name_plural = "Kurs-seksjoner"
# #
# #     def __str__(self):
# #         return "Section ({}) in course: {}".format(self.getNr(), self.getCourse())
# #
# #     def getCourse(self):
# #         return self.course or None
# #
# #     def getNr(self):
# #         return self.nr or None
# #
# #     def getStart(self):
# #         return self.start.strftime("%H:%M")
# #
# #     def getSong(self):
# #         return self.song or None
