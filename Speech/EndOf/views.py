from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Speech,Speaker
from django.views import generic
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
# Create your views here.


def index(request):
    return render(request,'speech/welcome.html')

def home(request):
    context = {
        'posts': Speech.objects.all()
    }
    return render(request,'speech/home.html',context)

class UserPostListView(ListView):
    model = Speech
    template_name = 'speech/Use_post.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2
    
class PostListView(ListView):
    model = Speech
    template_name = 'speech/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 2
    
    
    def get_query_set(self):
        user = get_object_or_404(User, username =self.kwargs.get('username'))
        return Speech.objects.filter(author = user).order_by('-date_posted')
        





def about(request):
    context = {
        'posts': Speech.objects.all()
    }
    return render(request, 'speech/about.html',context)


def Speakview(request):
    context = {
        'queryset': Speaker.objects.all()
    }
    return render(request, 'speech/speaker.html',context)








