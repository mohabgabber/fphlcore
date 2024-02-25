from django.db import models
import uuid
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField


class Team(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=500)
    cv = models.FileField(upload_to="team/pdf/%Y/%m/", validators=[
                          FileExtensionValidator(["pdf"], "Wrong extension")], blank=True)
    biography = models.TextField()
    pic = models.ImageField(upload_to="team/pic/%Y/%m/%d", blank=True)
    contact = models.TextField(blank=True)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["add_date"]


class Research(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=500)
    file = models.FileField(upload_to="research/pdfs/%Y", validators=[
                            FileExtensionValidator(["pdf"], "Wrong Extension")], blank=True)
    description = RichTextField()
    image = models.ImageField(upload_to="research/img/%Y", blank=True)
    publish_date = models.DateField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["-date"]


class Faq(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    q = models.CharField(max_length=500)
    a = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.q}"

    class Meta:
        ordering = ["-date"]


class Data(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)


class Subject(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=500)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    home = models.BooleanField(default=False)
    year = models.IntegerField(default=0)
    term = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["-date"]


class Road(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    pub_date = models.DateField()
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        ordering = ["-date"]


class Apply(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    text = RichTextField()


class Event(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    img = models.ImageField(upload_to="event/img/%Y", blank=True)
    show = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    adddate = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    link = models.CharField(max_length=100)
