from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return reverse('detail', kwargs={'slug':self.slug})
		return reverse('home')

class Profile(models.Model):
	user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(null=True,blank=True,upload_to='images/profile/')
	fb_url = models.CharField(max_length=200,null=True,blank=True)
	twitter_url = models.CharField(max_length=200,null=True,blank=True)
	linkedin_url = models.CharField(max_length=200,null=True,blank=True)

	def __str__(self):
		return str(self.user)

	

class Blog(models.Model):
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=200,unique=True)
	slug = models.SlugField(max_length=200,unique=True)
	content = RichTextField(blank=True, null=True)
	header_image = models.ImageField(null=True,blank=True,upload_to="images/")
	#content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	category = models.CharField(max_length=200,default='programming')
	snippet = models.CharField(max_length=200)
	likes = models.ManyToManyField(User,related_name='blog_posts')

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		#return reverse('detail', kwargs={'slug':self.slug})
		return reverse('home')

