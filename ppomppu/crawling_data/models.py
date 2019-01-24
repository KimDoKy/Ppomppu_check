from django.db import models

class CrawlingData(models.Model):
    title = models.TextField()
    category = models.CharField(max_length=10)
    write_date = models.CharField(max_length=10)
    detail_link = models.URLField()
    prod_image = models.URLField(blank=True, null=True)
    crawling_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
