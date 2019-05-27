from django.db import models

# Create your models here.

class Article(models.Model):
    yazar = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    baslik = models.CharField(max_length=50)
    icerik = models.TextField()
    olusturma_tarihi=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baslik




