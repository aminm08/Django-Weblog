from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.translation import gettext as _

from .models import BlogPost, Comment
from .forms import PostForm, CommentForm


class PostListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return BlogPost.objects.filter(status='p').order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_message = _('your Blog post is now submitted')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_message = _('your Blog Post Successfully updated')

    def test_func(self):
        return self.get_object().author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.DeleteView):
    model = BlogPost
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog_list')
    success_message = _('your Blog Post successfully deleted')

    def test_func(self):
        return self.get_object().author == self.request.user


class CommentCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    success_message = _('your comment successfully submitted')

    def form_valid(self, form):
        obj = form.save(commit=False)

        blog_id = int(self.kwargs['blog_id'])
        blogpost = get_object_or_404(BlogPost, pk=blog_id)

        obj.author = self.request.user
        obj.Blog = blogpost

        return super().form_valid(form)
