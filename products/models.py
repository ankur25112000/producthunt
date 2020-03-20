from django.db import models
from django.contrib.auth.models import User
class products(models.Model):
    title = models.CharField(max_length =255)
    pub_date = models.DateTimeField(null=True)
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='image/')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]
    def pub_date_pretty(self):
        return self.pub_date_strftime('%b %e %Y')
