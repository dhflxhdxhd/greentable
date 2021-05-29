from django.db import models

"""
name
explain : 채식지원 0 채식전문 1	
division : 식당 0 카페 1 베이커리 2
country : 한국 0 일본,중국 1 인도 2 남미 3 중동 4 서양 5
call 
locate
break
time
menu
etc
"""

class Place(models.Model):
    name = models.CharField(max_length=20, null=True)
    explain = models.IntegerField(blank=True, null=True)
    division = models.IntegerField(blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    call = models.CharField(max_length=20, blank=True, null=True)
    locate = models.CharField(max_length=50, blank=True, null=True)
    day_break = models.CharField(max_length=30, blank=True, null=True)
    time = models.CharField(max_length=100, blank=True, null=True)
    menu = models.CharField(max_length=20, blank=True, null=True)
    etc = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.id}.{self.name}'