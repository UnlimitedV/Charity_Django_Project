from django.db import models
from accounts.models import User


class Benefactor(models.Model):
    choices = (
        (0, 'Biggner'), 
        (1, 'Intermidiate'), 
        (2, 'Advanced')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices=choices, default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        query = self.filter(charity__user = user)
        return query

    def related_tasks_to_benefactor(self, user):
        query = self.filter(assigned_benefactor__user = user)
        return query

    def all_related_tasks_to_user(self, user):
        q = models.Q(charity__user = user) | models.Q(assigned_benefactor__user = user) | models.Q(state = 'P')
        query = self.filter(q)
        return query

class Task(models.Model):
    gchoices = (
        ('F', 'Female'), 
        ('M', 'Male')
    )

    schoices = (
        ('P', 'Pending'),
        ('W', 'Waiting'),
        ('A', 'Assigned'),
        ('D', 'Done')
    )
    assigned_benefactor = models.ForeignKey(Benefactor, null=True, on_delete=models.SET_NULL)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    age_limit_from = models.IntegerField(blank=True, null=True)
    age_limit_to = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender_limit = models.CharField(max_length=1, choices=gchoices, blank=True, null=True)
    state = models.CharField(choices=schoices, max_length=1, default='P')
    title = models.CharField(max_length=60)

    objects = TaskManager()
