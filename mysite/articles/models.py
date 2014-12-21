from django.db import models

YEARS = (
    ("2010", "2010"),
    ("2011", "2011"),
    ("2012", "2012"),
    ("2013", "2013"),
    ("2014", "2014"),
    ("2015", "2015")
)


class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='static/uploads/', blank=True)
    description = models.TextField()
    year = models.CharField(max_length=4, choices=YEARS, default="2014")
    slug = models.SlugField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title







