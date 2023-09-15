from django.db import models 

from django.contrib.auth import get_user_model 

import datetime

class Task(models.Model):
    description = models.CharField(max_length = 200)
    owner = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    deadline = models.DateField()
    done = models.IntegerField(default = -1)
    
    def has_chance(self):
        if self.done == -1 and datetime.date.today() > self.deadline:
            self.done = 0
        return self.done == -1
        
    def __str__(self):
        text = 'Muddatgacha imkoniyat bor: '
        if self.done == 0: 
            text = 'Muddatida bajarilmadi: '
        elif self.done == 1:
            text = 'Muddatida bajarildi: '
        return text + self.description             
