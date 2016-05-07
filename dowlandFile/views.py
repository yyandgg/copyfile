from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .forms import NameForm
import shutil
# Create your views here.
def index(request):

    return render(request,'dowlandFile/index.html',{})
	
def results(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            file_dir=str((form.cleaned_data['your_file']))
            move_to_dir='E:'+file_dir[2:]
            shutil.copy(file_dir,move_to_dir)
            return render(request,'dowlandFile/results.html',{})
    else:
        form = NameForm()
    return render(request,'dowlandFile/index.html',{'form':form})


    