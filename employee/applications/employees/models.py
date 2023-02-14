from django.db import models

from applications.departments.models import Department

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
    job = models.CharField('job', max_length=1, choices=JOB_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self) -> str:
        return str(self.id) + ' ' +  self.first_name + ' ' + self.last_name