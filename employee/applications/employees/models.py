from django.db import models

from ckeditor.fields import RichTextField

from applications.departments.models import Department

class Skill(models.Model):
    skill = models.CharField('skill', max_length=50)

    class Meta:
        verbose_name = 'Habilidades'
        verbose_name_plural = 'Habilidades empleado'
    
    def __str__(self) -> str:
        return str(self.id) + ' ' +  self.skill

class Employee(models.Model):
    """Employee model for table on bd"""
    JOB_CHOICES =(
        ('0', 'Engineer'),
        ('1', 'Accounter'),
        ('2', 'Salesman'),
        ('3', 'Others'),
    )
    first_name = models.CharField('name', max_length=60)
    last_name = models.CharField('last name', max_length=60)
    full_name = models.CharField('full name', max_length=120, blank=True)
    job = models.CharField('job', max_length=1, choices=JOB_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='employee', height_field=None, blank=True, null=True)
    skills = models.ManyToManyField(Skill)
    cv = RichTextField()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['first_name', 'last_name'] 

    def __str__(self) -> str:
        return str(self.id) + ' ' +  self.first_name + ' ' + self.last_name