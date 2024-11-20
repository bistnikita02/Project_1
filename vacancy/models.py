from django.db import models
from django.utils import timezone
from django .contrib.auth.models import User
from users.models import Skill
from django.urls import reverse

class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    skill = models.ManyToManyField(Skill)

    class Meta:
        verbose_name_plural='vacancies'
        ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse('vacancy-detail', kwargs={"pk": self.pk})


    def short_description(self):
        return self.content[0:300]

    def get_skill_list(self):
        data = list(self.skill.values_list('name', flat=True))
        return data

    def is_more_than_10_days(self):
        date_diff = timezone.now() - self.date_posted
        return date_diff
    