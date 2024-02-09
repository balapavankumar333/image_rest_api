from django.db import models

# Create your models here.



from django.db import models

class CatPicture(models.Model):
    image = models.ImageField(upload_to='pictures/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cat Picture {self.id}'
