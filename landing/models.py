from django.db import models
import uuid 
from django.core.validators import FileExtensionValidator


class Team(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=500)
    cv = models.FileField(upload_to="team/pdf/%Y/%m/", validators=[FileExtensionValidator(["pdf"], "Wrong extension")], blank=True)
    biography = models.TextField()
    pic = models.ImageField(upload_to="team/pic/%Y/%m/%d")
    contact = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["-add_date"]

class Research(models.Model):
    pass