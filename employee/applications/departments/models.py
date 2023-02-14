from django.db import models

class Department(models.Model):
    name = models.CharField('name', max_length=50, blank=True)
    short_name = models.CharField('short name', max_length=20, unique=True)
    is_activate = models.BooleanField('activate?', default=False)
    

    def __str__(self) -> str:
        return str(self.id) + ' ' +  self.name