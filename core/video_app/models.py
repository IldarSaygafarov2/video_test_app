from django.db import models
from django.core.validators import FileExtensionValidator


class Video(models.Model):
    title = models.CharField(verbose_name="Название видео", max_length=150)
    file = models.FileField(upload_to="videos/", validators=[FileExtensionValidator(allowed_extensions=['mp4'])])

    def __str__(self):
        return self.title

