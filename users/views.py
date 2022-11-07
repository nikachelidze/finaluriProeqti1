from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse, Http404 
from django.views import View
from django.views.generic import CreateView
from users.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from users.models import car,User,comment
from django.urls import reverse_lazy
# Create your views here.

def home_viwe(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')

def mtavari_viwe(request: HttpRequest) -> HttpResponse:
    return render(request, 'mtavari.html', context={
        'cars': car.objects.all()
    })

def fulluser_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'fulluser.html', context={
        'users': User.objects.all()
    })

def delete_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return redirect('users:fulluser')

    pk: int = request.POST.get('pk')
    print(request.POST)
    try:
        post = User.objects.get(pk=pk)
    except:
        raise Http404('მოხდა შეცდომა')

    post.delete()

    return redirect('users:home')

class Register(View):
    template_name = 'registration/registracia.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            # login(request, user)
            return redirect('home')
        context ={
            'form': form
        }
        return render(request, self.template_name, context)

class commentview(CreateView):
    class Meta:
        model = comment
        fields = "__all__"

    template_name = 'mtavari.html'
    success_url = reverse_lazy('comment')
    
    def post(self, request):
        form = UserCreationForm(request.POST)
    
    def form_valid(self, form):
        self.object: comment = form.save

        self.object.user = self.request.user              
        self.object.save()
        
        form.save_m2m()

        redirect(self.get_success_url())
