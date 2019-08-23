from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class CrawlingData(models.Model):
    title = models.TextField()
    category = models.CharField(max_length=10)
    write_date = models.CharField(max_length=10)
    detail_link = models.URLField()
    prod_image = models.URLField(blank=True, null=True)
    crawling_data = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

from .utils.send_mail import send_mails
from keywords.models import Keywords
import re

@receiver(post_save, sender=CrawlingData)
def update_signal(sender, instance, **kwargs):
    if instance.status == True:
        keywords = Keywords.objects.filter(alarm=True)
        for key in keywords:
            keyword = key.keyword
            if re.search(keyword, instance.title):
                send_mails(key, instance)
