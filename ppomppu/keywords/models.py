from django.db import models

class Keywords(models.Model):
    keyword = models.CharField(max_length=100)
    owner = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    alarm = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.keyword}'
