from django.urls import path
from .views import HomeView, ArticleDetailView, AddBlogView, UpdateBlogView, DeleteBlogView,AddCategoryView, CategoryView

urlpatterns = [
	path('',HomeView.as_view(),name='home'),
	path('add_blog/',AddBlogView.as_view(),name='add_blog'),
	path('add_category/',AddCategoryView.as_view(),name='add_category'),
	path('<str:slug>/',ArticleDetailView.as_view(),name='detail'),
	path('category/<str:cats>/',CategoryView,name='category'),
	path('update/<str:slug>/',UpdateBlogView.as_view(),name='update'),
	path('delete/<str:slug>/',DeleteBlogView.as_view(),name='delete'),
]