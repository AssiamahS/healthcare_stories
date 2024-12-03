from django.shortcuts import render, redirect
from .models import Story

def index(request):
    stories = Story.objects.all()
    return render(request, 'stories/index.html', {'stories': stories})

def submit_story(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        location = request.POST['location']
        category = request.POST['category']
        Story.objects.create(title=title, content=content, location=location, category=category)
        return redirect('index')
    return render(request, 'stories/submit_story.html')
