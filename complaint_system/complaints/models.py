
from django.db import models

class Complaint(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    complaint_text = models.TextField()
    sentiment = models.CharField(max_length=100,default='none')
    image_classification = models.CharField(max_length=100,default='none')
    pnr_number = models.CharField(max_length=50, default='UNKNOWN')  # Added PNR number field
    complaint_image = models.ImageField(upload_to='complaint_images/', blank=True, null=True,default='Not Classified')  # Image field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    rating = models.IntegerField()
    feedback_quality = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
