from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TodoList(models.Model):

    PENDING = 1
    COMPLETED = 2
    STATUS_CHOICES = (
		(PENDING, 'pending'),
		(COMPLETED, 'completed'),
	)

    title = models.CharField(max_length=250) 
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return self.title