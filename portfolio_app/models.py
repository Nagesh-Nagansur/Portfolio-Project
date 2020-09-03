from django.db import models

# Create your models here.
class Home(models.Model):
	title=models.CharField(max_length=50)
	discription=models.TextField()
	image=models.ImageField(upload_to="portfolio_app/images/")
	link=models.URLField()


	def __str__(self):
		return self.title

# class Blog(models.Model):
