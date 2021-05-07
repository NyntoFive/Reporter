import json, fnmatch

from django.db import models
# from .utils import get_filtered_image
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

ACTION_CHOICES = (
    ('NO_FILTER', 'no filter'),
    ('COLORIZED', 'colorized'),
    ('GRAYSCALE', 'grayscale'),
    ('BLURRED', 'blurred'),
    ('BINARY', 'binary'),
    ('INVERT', 'invert'),
)

class Upload(models.Model):
    image = models.ImageField(upload_to='images')
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    def save(self, *args, **kwargs):
        pil_img = Image.open(self.image)

        # convert to an array and do some processing
        cv_img = np.array(pil_img)
        img = get_filtered_image(cv_img, self.action)

        # convert back to pil image
        im_pil = Image.fromarray(img)

        #save
        buffer = BytesIO()
        im_pil.save(buffer, format='png')
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save=False)
        
        super().save(*args, **kwargs)


class CKKItem(models.Model):
    sku = models.CharField(max_length=255, blank=True)
    all_images = models.TextField()
    cannonical_url = models.URLField(max_length=255, blank=True)
    video_url = models.URLField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    keywords = models.CharField(max_length=255, blank=True)
    link = models.URLField(max_length=255, blank=True)
    products_id = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    discount_tiers = models.CharField(max_length=255, blank=True)
    discount_amount = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.sku

    def set_all_images(self, x):
        self.all_images = json.dumps(x)
    def get_all_images(self):
        return json.loads(self.all_images)
    
    def set_description(self, x):
        tmp = json.dumps(x)
        new = []
        for line in tmp:
            if line:
                new.append(line.strip())        
        self.description = new

    def get_description(self):
        return json.loads(self.description)

class CKKImage(models.Model):
    item = models.ForeignKey(CKKItem, on_delete=models.CASCADE)
    source = models.URLField(blank=True, max_length=255)
    position = models.PositiveIntegerField(blank=True)
    fname = models.CharField(max_length=200)
    
    local = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return self.fname
    