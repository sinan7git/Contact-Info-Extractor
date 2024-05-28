from django.db import models


class CompanyRecommendation(models.Model):
    website_url = models.URLField()
    company_name = models.CharField(max_length=200)
    emails = models.TextField()
    contact_link = models.URLField(null=True, blank=True)  # Optional
    phone_number = models.CharField(max_length=50, null=True, blank=True) # Optional


    def __str__(self):
        return self.company_name