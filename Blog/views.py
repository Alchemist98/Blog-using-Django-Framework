from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Blog, Category
from .forms import BlogForm, UpdateForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.

class HomeView(ListView):
	model = Blog
	template_name = "Blog/home.html"

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView,self).get_context_data(*args,**kwargs)
		context["cat_menu"] = cat_menu
		return context

def CategoryView(request,cats):
	categories = Category.objects.all()
	category_blogs = Blog.objects.filter(category=cats)
	return render(request,"Blog/categories.html",{'cats':cats.title(), 'category_blogs':category_blogs, 'categories':categories})

class ArticleDetailView(DetailView):
	model = Blog
	template_name = "Blog/details.html"

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)
		context["cat_menu"] = cat_menu
		return context

class AddBlogView(CreateView):
	model = Blog
	form_class = BlogForm
	template_name = "Blog/add_blog.html"
	#fields = '__all__'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(AddBlogView,self).get_context_data(*args,**kwargs)
		context["cat_menu"] = cat_menu
		return context


class AddCategoryView(CreateView):
	model = Category
	template_name = 'Blog/add_category.html'
	fields = '__all__'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(AddCategoryView,self).get_context_data(*args,**kwargs)
		context["cat_menu"] = cat_menu
		return context
	
class UpdateBlogView(UpdateView):
	model = Blog
	form_class = UpdateForm
	template_name = "Blog/update_blog.html"
	#fields = ['title','content']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(UpdateBlogView,self).get_context_data(*args,**kwargs)
		context["cat_menu"] = cat_menu
		return context

class DeleteBlogView(DeleteView):
	model = Blog
	template_name = "Blog/delete_blog.html"
	success_url = reverse_lazy('home')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(DeleteBlogView,self).get_context_data(*args,**kwargs)
		context["cat_menu"] = cat_menu
		return context