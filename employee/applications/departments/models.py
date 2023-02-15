from django.db import models

class Department(models.Model):
    name = models.CharField('name', max_length=50, blank=True)
    short_name = models.CharField('short name', max_length=20, unique=True)
    is_activate = models.BooleanField('activate?', default=False)
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['-name'] # ordernar de manera descendente
        unique_together = ('name', 'short_name') # que no se repita los registros con respecto a estos dos campos

    def __str__(self) -> str:
        return str(self.id) + ' ' +  self.name