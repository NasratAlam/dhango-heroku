import datetime

from django.db import models
from django.utils import timezone

# As I understand it, models are "templates" for particular pieces of data in the database table.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self): # For the database object representation
        return self.question_text
    def was_published_recently(self):
        # This makes it so dates in the future can be considered "recent"
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    # Used for tracking on the admin page
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# Now for my own model, oh boy...
class Thoughts(models.Model):
    title = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)
    def __str__(self):
        return self.title