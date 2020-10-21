from django import forms
from .models import Blog, Category

#choices = [('Data Science', 'Data Science'),('Machine Learning','Machine Learning'),('Python','Python'),('Deep Learning', 'Deep Learning')]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
	choice_list.append(item)

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ('author','title','slug','category','content','snippet','header_image')

		widgets = {
			#'author': forms.Select(attrs={'class':'form-control'}),
			'author': forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
			'title': forms.TextInput(attrs={'class':'form-control'}),
			'slug': forms.TextInput(attrs={'class':'form-control'}),
			'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
			'content': forms.Textarea(attrs={'class':'form-control'}),
			'snippet': forms.Textarea(attrs={'class':'form-control'}),
		}

class UpdateForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ('title','slug','category','content','snippet')

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control'}),
			'slug': forms.TextInput(attrs={'class':'form-control'}),
			'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
			'content': forms.Textarea(attrs={'class':'form-control'}),
			'snippet': forms.Textarea(attrs={'class':'form-control'}),
		}