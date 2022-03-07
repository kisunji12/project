from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, ApplicationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Naming convention for the template while creating view
# <app>/<model>_<viewtype>.html

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-post_date']


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'job_description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'job_description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostApplyView(LoginRequiredMixin, CreateView):
    model = ApplicationForm
    fields = ['job_post', 'full_name', 'address', 'age', 'qualification', 'contact']

    def form_valid(self, form):
        form.instance.applicant = self.request.user
        return super().form_valid(form)



    success_url = '/blog/'
