from django.db import models

# Create your models here.


class wa_camp(models.Model):
    camp_name = models.CharField(max_length=50)
    response = models.TextField(null=True, blank=True)
    numbers = models.CharField(max_length=15)

    def __str__(self):
        return self.camp_name