from django.db import models
import django.contrib.postgres.search

class Place(models.Model):
    name         = models.CharField(max_length=200)
    description  = models.TextField()
    latitude     = models.DecimalField(max_digits=9,decimal_places=6)
    longitude    = models.DecimalField(max_digits=9,decimal_places=6)
    created_at   = models.DateTimeField(auto_now=True)

    @property
    def full_text(self):
        return django.contrib.postgres.search.SearchVector(
            [self.name, self.description]
        )

    