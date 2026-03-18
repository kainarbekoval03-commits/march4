from django.shortcuts import render, redirect
from .models import Celebrity
from django.db.models import Q
from celebrities.forms import CreateCelebForm, SearchForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home_celeb(request):
    if request.method == "GET":
        return render(request, 'home.html')

def celebrity_list(request):
    if request.method == "GET":
        all_celebs = Celebrity.objects.all()
        limit = 3
        page = int(request.GET.get("page", 1)) 
        max_page = all_celebs.count() // limit + 1
        list_pages = range(1, max_page + 1)
        start = (page - 1) * limit
        end = page * limit
        all_celebs = all_celebs[start:end]
        form = SearchForm(request.GET)
        
        if form.is_valid():
            search = form.cleaned_data.get("search")
            category = form.cleaned_data.get("category")
            author = form.cleaned_data.get("author")
            tags = form.cleaned_data.get("tags")
        else:
            search = category = author = tags = None
        if search:
            all_celebs = all_celebs.filter(Q(title__icontains=search) | Q(description__icontains=search))
        if category:
            all_celebs = all_celebs.filter(category=category)
        if author:
            print(author)
        if tags:
            all_celebs = all_celebs.filter(tags__in=tags)
        return render(request, template_name="celebrities/list.html", context={"celebs": all_celebs, "form": form, "list": list})
def detayl_celeb(request, id ):
    if request.method == "GET":
        celeb = Celebrity.objects.get(id=id)
        return render(request, "celebrities/detail.html", {"celeb":celeb})

@login_required(login_url="/users/sign-in/")
def create_celeb(request):
    if request.method == "POST":
        print(request.POST)
        form = CreateCelebForm(request.POST, request.FILES)
        if not form.is_valid():
            return HttpResponse("Error data")
        name = form.cleaned_data.get("title")
        bio = form.cleaned_data.get("author")
        birth_date  = form.cleaned_data.get("description")
        image = form.cleaned_data.get("image")
        content = form.cleaned_data.get("content")
        Celebrity.objects.create(name=name, bio=bio, image=image, content=content, birth_date=birth_date)
        return redirect(f"/celebs/")
    elif request.method == "GET":
        form = CreateCelebForm()
        return render(request=request, template_name="celebrities/create_celeb.html", context={"form": form})
    return


