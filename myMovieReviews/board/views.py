from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Board

def board_create(request):

    GENRE_CHOICES=Board.MOVIE_GENRE_CHOICES
    AGE_CHOICES=Board.AGE_CHOICES

    if request.method == 'POST':
        board = Board.objects.create(
            title=request.POST['title'],
            release=request.POST['release'],
            genre=request.POST['genre'],
            age=request.POST['age'],
            rate=request.POST['rate'],
            runningtime=request.POST['runningtime'],
            review=request.POST['review'],
            director=request.POST['director'],
            actor=request.POST['actor'],
        )
        return redirect(reverse('board:board_list'))
    context = {
        "genre_choices": GENRE_CHOICES,
        "age_choices": AGE_CHOICES,
    }
    return render(request,'board/create.html', context)

def board_detail(request, pk):
    boards=Board.objects.get(id=pk)
    try:
        runningtime_minutes = int(boards.runningtime)
        if runningtime_minutes >= 60:
            hours = runningtime_minutes // 60
            minutes = runningtime_minutes % 60
            boards.runningtime = f"{hours}시간 {minutes}분"
        else:
            boards.runningtime = f"{runningtime_minutes}분"
    except ValueError:
        pass

    age_dict = {
        'G': '전체 관람',
        'PG': '12세 관람',
        'F15': '15세 이상 관람',
        'R': '청소년 관람불가'
    }
    boards.age_display = age_dict.get(boards.age, boards.age)

    context={
        'board':boards
    }
    return render(request, 'board/read.html', context)

def board_list(request):
    boards=Board.objects.all()
    context={'boards': boards}
    return render(request,'board/list.html',context)

def board_update(request, pk):
    board = Board.objects.get(id=pk)

    GENRE_CHOICES=Board.MOVIE_GENRE_CHOICES
    AGE_CHOICES=Board.AGE_CHOICES

    if request.method=="POST":
        board.title = request.POST.get('title')
        board.release = request.POST.get('release')
        board.genre = request.POST.get('genre')
        board.age = request.POST.get('age')
        board.rate = request.POST.get('rate')
        board.runningtime = request.POST.get('runningtime')
        board.review = request.POST.get('review')
        board.director = request.POST.get('director')
        board.actor = request.POST.get('actor')
        board.save()
        return redirect('board:board_detail', pk=board.pk)

    context = {
        "board": board,
        "genre_choices": GENRE_CHOICES,
        "age_choices": AGE_CHOICES,
    }
    return render(request, 'board/update.html', context)

def board_delete(request, pk):
    if request.method == "POST":
        board = Board.objects.get(id=pk)
        board.delete()
        return redirect('board:board_list')
    return redirect('home:main') 