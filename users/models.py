from django.db import models
from django.db.models.fields import DateTimeCheckMixin
import datetime

# Create your models here.
class User(models.Model):
    first_name = models.CharField("el nombre de la persona", max_length=30)
    last_name = models.CharField("el apellido de la persona", max_length=30)
    cars = models.ManyToManyField('Car', verbose_name="los autos de la persona")

STATUS_CHOICES = (
    ('R', 'Reviewed'),
    ('N', 'Not Reviewed'),
    ('E', 'Error'),
    ('A', 'Accepted')
)

class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(unique=True)
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

#    class Meta:
#        ordering = ['rating']
#        db_table = 'website_custom_table_name'
#        verbose_name = 'La pagina web'
#        verbose_name_plural = 'Las paginas'

    def was_released_last_week(self):
        if self.release_date < datetime.date(2021,9,25):
            return "Released before last week"
        else:
            return "Released this week" 

    @property
    def get_full_name(self):
        return f"Este es el nombre completo del Sitio Web: {self.name}" 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/websites/{self.id}"

    def save(self, *args, **kwargs):
        print("Estamos guardando")
        super().save(*args, **kwargs)
    

class Car(models.Model):
    name = models.CharField(max_length=40, primary_key=True)