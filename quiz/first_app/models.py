from django.db import models
from django.contrib.auth.models import User


# Create your models here.Status
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    Status_Draft = 0
    Status_Voting = 1
    Status_End = 2
    Status_Deleted = 3
    Status_Choice = (
        (Status_Draft,'Draft'),
        (Status_Voting,'Voting'),
        (Status_End,'End'),
        (Status_Deleted,'Deleted'),
    )
    # created_time = models.DateTimeField(default= now, auto_now=False, auto_now_add=False)
    status = models.IntegerField(choices=Status_Choice, default=Status_Draft)
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    question = models.ForeignKey(Question,on_delete=models.CASCADE, related_name='choice_in_question')
    voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='choice_in_user')
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text


class VoteReason(models.Model):
    reason = models.CharField(max_length=200)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE,  related_name='create_reason')
    voter = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='voter_of_reason')

    def __str__(self):
        return self.reason