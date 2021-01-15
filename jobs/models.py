from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=50, blank=True) # name the job
    image = models.ImageField(upload_to='images/') # send to folder called 'images'
    summary = models.CharField(max_length=200) # description of jobs

    month_completed = models.CharField(max_length=50, blank=True)

    skill_types = [('r', 'R'), ('python', 'Python'), ('scraping', 'Web Scraping'),
     ('django', 'Django'), ('rmd', 'Markdown'), ('tableau','Tableau')]
    skill1 = models.CharField(max_length = 20, blank=True, choices=skill_types)
    skill2 = models.CharField(max_length = 20, blank=True, choices=skill_types)

    extracurricular_or_class = models.CharField(max_length=50, blank=True)

    best_accuracy = models.FloatField(max_length=5, null=True, blank=True)
    takeaway1 = models.CharField(max_length=200, blank=True)
    takeaway2 = models.CharField(max_length=200, blank=True)

    related_title1 = models.CharField(max_length=200, blank=True)
    related_title2 = models.CharField(max_length=200, blank=True)
    related_link1 = models.URLField(max_length=200, blank=True)
    related_link2 = models.URLField(max_length=200, blank=True)
    related_img1 = models.ImageField(upload_to='images/', blank=True)
    related_img2 = models.ImageField(upload_to='images/', blank=True)


    def __str__(self):
        return self.title