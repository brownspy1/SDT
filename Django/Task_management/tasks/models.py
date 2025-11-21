from django.db import models

# Create your models here.
class task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class tasks_details(models.Model):
    High = 'H'
    Medium = 'M'
    Low = 'L'

    OPTIONS = (
        (High,'High'),
        (Medium,'Medium'),
        (Low,'Low')
    )
    task_id = models.OneToOneField
    priority = models.CharField(max_length=1,choices=OPTIONS,default=Low)