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

@receiver(post_save, sender=CrawlingData)
def updata_signal(sender, instance, **kwargs):
    print('---signal-----')
    print(instance)
# send_mails('abmu333@hanmail.net')
