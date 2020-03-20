from django import forms
from django.contrib.auth.models import User
class products(forms.Form):
    title = forms.CharField(max_length =255)
    pub_date = forms.DateTimeField(
    body = forms.TextField()
    url = forms.TextField()
    image = forms.ImageField(upload_to='images/')
    icon = forms.ImageField(upload_to='image/')
    votes_total = forms.IntegerField(default=1)
    hunter = forms.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]
    def pub_date_pretty(self):
        return self.pub_date_strftime('%b %e %Y')
