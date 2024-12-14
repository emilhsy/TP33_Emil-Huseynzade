# This module is for making requests to get a specific object from database
from django.shortcuts import get_object_or_404

# Using mixins instead of decorators for Login checks and checking if the post belongs to the user
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Importing User model from Django's authentication system models
from django.contrib.auth.models import User

# Using Django's generic views for Post functions
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Importing our own Post model
from .models import Post

# Listing Posts
class PostListView(ListView):
    model = Post # This line will tell view that "Use this model for listing"
    template_name = 'blog/home.html' # Our view will use this template for listing
    context_object_name = 'posts' # Accessing the database data with this name
    ordering = ['-date_posted'] # This will help to order posts with chronological order
    paginate_by = 5 # We don't want to list more than 5 posts in the homepage

# Listing Posts by username
class UserPostListView(ListView):
    model = Post # This line will tell view that "Use this model for listing"
    template_name = 'blog/user_posts.html' # Our view will use this template for listing
    context_object_name = 'posts' # Accessing the database data with this name
    paginate_by = 5 # We don't want to list more than 5 posts in the homepage

    # Gettting specific data to display
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) # Picking the requested user from User database
        return Post.objects.filter(author=user).order_by('-date_posted')  # This will fetch only posts with the specific author and display with chronological order

# Individual Post Details
class PostDetailView(DetailView):
    model = Post # This line will tell view that "Use this model for listing"

# Creating new posts
class PostCreateView(LoginRequiredMixin, CreateView): # Adding mixins to check if user is logged in
    model = Post # This line will tell view that "Use this model for listing"
    fields = ['title', 'content'] # Fields that can be created in form

    # Form validation
    def form_valid(self, form):
        form.instance.author = self.request.user # Setting author
        return super().form_valid(form) # Calling parent class function to save the form data to the database

# Updating specific post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # Adding mixins to check if user is logged in and owns the post that is tried to be changed
    model = Post # This line will tell view that "Use this model for listing"
    fields = ['title', 'content'] # Fields that can be updated in form

    # Form validation
    def form_valid(self, form):
        form.instance.author = self.request.user # Setting author
        return super().form_valid(form) # Calling parent class function to save the form data to the database

    # User validation
    def test_func(self):
        post = self.get_object() # Getting the post that is wanted to be updated
        if self.request.user == post.author: # Checking if the user is the author of the posts
            return True # If so, updating the post
        return False # If not, Django raises a PermissionDenied error (HTTP 403)

# Deleting specific post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # Adding mixins to check if user is logged in and owns the post that is tried to be deleted
    model = Post # This line will tell view that "Use this model for listing"
    success_url = '/' # Redirected url after deleting the post successfully

    # User validation
    def test_func(self):
        post = self.get_object() # Getting the post that is wanted to be deleted
        if self.request.user == post.author: # Checking if the user is the author of the posts
            return True # If so, updating the post
        return False # If not, Django raises a PermissionDenied error (HTTP 403)