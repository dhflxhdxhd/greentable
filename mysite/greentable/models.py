from django.db import models

class Question(models.Model):
    number = models.IntegerField(unique=True)
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.number}' #f-string

class Choice(models.Model):
    content = models.CharField(max_length=100)
    question_id = models.ForeignKey(to='greentable.Question',on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.question_id}-{self.content}'

class Place(models.Model):
    name = models.CharField(max_length=20, blank=True)
    explain = models.IntegerField(blank=True)
    division = models.IntegerField(blank=True)
    country = models.IntegerField(blank=True)
    call = models.CharField(max_length=20, blank=True)
    locate = models.CharField(max_length=50, blank=True)
    time = models.CharField(max_length=100,  blank=True)
    day_break = models.CharField(max_length=30, blank=True)
    menu = models.CharField(max_length=20, blank=True)
    etc = models.CharField(max_length=50, blank=True)


