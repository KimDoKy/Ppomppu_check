from django.db import models

class Keywords(models.Model):
    keyword = models.CharField(max_length=100)
    owner = models.ForeignKey('users.CustomUser', related_name='keywords', on_delete=models.CASCADE)
    alarm = models.BooleanField(default=True)
    update_link = models.ForeignKey('crawling_data.CrawlingData', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.keyword}'
