from django.shortcuts import render, redirect
from .models import Idea
from .forms import IdeaForm
from django.http import JsonResponse
from apps.devtool.models import DevTool
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'idealist/list.html')

def create(request):
    if request.method == 'GET':
        form = IdeaForm()
        ctx = {'form': form}
        return render(request, 'idealist/create.html', context=ctx)
    else:
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('idealist:list')

def list(request):
    sort = request.GET.get('sort', 'id')
    page = request.GET.get('page', 1)

    if not sort:
        sort = 'id'

    ideas = Idea.objects.all().order_by(sort)
    paginator = Paginator(ideas, 4) 
    paginated_ideas = paginator.get_page(page)

    ctx = {
        'ideas': paginated_ideas, 
        'sort': sort,
    }
    return render(request, 'idealist/list.html', ctx)

def startoggle(request, idea_id):
    idea = Idea.objects.get(id=idea_id)
    idea.star = not idea.star
    idea.save()
    return JsonResponse({'success': True, 'star': idea.star})


def detail(request, pk):
    idea = Idea.objects.get(id=pk)
    ctx = {
        'idea': idea
    }
    return render(request, 'idealist/detail.html', ctx)

def update(request, pk):
    idea = Idea.objects.get(id=pk)
    if request.method == 'GET':
        form = IdeaForm(instance=idea)
        ctx = {'form': form, 'idea': idea, 'pk': pk}
        return render(request, 'idealist/update.html', context=ctx)
    else:
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idealist:detail', pk=idea.pk)

def delete(request, pk):
    idea = Idea.objects.get(id=pk)
    idea.delete()
    return redirect('idealist:list')

def update_interest(request, pk, action):
    try:
        idea = Idea.objects.get(id=pk)
    except Idea.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Idea not found'}, status=404)

    if action == 'increase':
        idea.interest += 1
    elif action == 'decrease':
        idea.interest -= 1
    idea.save()

    return JsonResponse({
        'success': True,
        'new_interest': idea.interest  
    })

def devtool_detail(request, pk):
    devtool = DevTool.objects(id=pk)
    ideas = Idea.objects.filter(devtool=devtool)
    ctx = {
        'devtool' : devtool,
        'ideas' : ideas
    }
    return render(request, 'devtool/detail.html', ctx)