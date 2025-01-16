from django.shortcuts import render, redirect
from .models import DevTool
from .forms import DevToolForm
from apps.idealist.models import Idea

# Create your views here.

def create(request):
    if request.method == 'GET':
        form = DevToolForm()
        ctx = {'form':form}
        return render(request, 'devtool/create.html', context=ctx)
    else:
        form = DevToolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('devtool:list')

def list(request):
    devtools=DevTool.objects.all()
    ctx = {'devtools' : devtools}
    return render(request, 'devtool/list.html', ctx)

def detail(request, pk):
    devtool = DevTool.objects.get(id=pk)
    ideas = Idea.objects.filter(devtool=devtool)

    ctx = {
        'devtool' : devtool,
        'ideas' : ideas
    }
    return render(request, 'devtool/detail.html', ctx)

def update(request, pk):
    devtool = DevTool.objects.get(id=pk)
    if request.method == 'GET':
        form = DevToolForm(instance=devtool)
        ctx = {'form': form, 'devtool': devtool, 'pk': pk}
        return render(request, 'devtool/update.html', context=ctx)
    else:
        form = DevToolForm(request.POST, request.FILES, instance=devtool)
        if form.is_valid():
            form.save()
            return redirect('devtool:detail', pk=devtool.pk)

def delete(request, pk):
  devtool = DevTool.objects.get(id=pk)
  devtool.delete()
  return redirect('/')
