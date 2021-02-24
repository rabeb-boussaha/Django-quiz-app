from django.db import 

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
