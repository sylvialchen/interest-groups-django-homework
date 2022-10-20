from django.db import models
from django.urls import reverse

# Create your models here.

PILLARS = (
    ("CU", 'Cultural'),
    ("SI", 'Sisterhood'),
    ("SV", 'Service'),
    ("PH", 'Philanthropy'),
    ("SA", 'RAINN'),
)


class Chapter(models.Model):
    name = models.CharField(max_length=50)
    chapter_school = models.CharField(max_length=50)
    city_state = models.CharField(max_length=50)
    original_founding_date = models.DateField()
    recharter_date = models.DateField(null=True)

    def get_absolute_url(self):
        return reverse('chapter_detail', kwargs={'pk': self.id})


class School(models.Model):
    school_name = models.CharField(max_length=100)
    school_state = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    group_pillars = models.TextField(max_length=200)
    group_social_media = models.URLField()
    contact_emails = models.EmailField()
    can_visit = models.ManyToManyField(Chapter)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'school_id': self.id})


class PlannedEvent(models.Model):
    date = models.DateField()
    type_of_event = models.CharField(
        max_length=50,
        choices=PILLARS,
        default=PILLARS[0][0])
    description = models.TextField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly string value of a Field.choice
        return f"{self.school} hosted {self.type_of_event} event on {self.date}"

    class Meta:
        ordering = ['-date']
