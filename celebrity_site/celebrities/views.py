from django.shortcuts import render, redirect
from .models import Celebrity

def home_celeb(requet):
   return render(requet, 'home.html')

def celebrity_list(request):
    celebs = Celebrity.objects.all()
    return render(request, 'celebrities/list.html', {'celebs': celebs})
def detayl_celeb(request, id ):
    celeb = Celebrity.objects.get(id=id)
    return render(request, "celebrities/detail.html", {"celeb":celeb})


def create_celeb(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get("name")
        bio = request.POST.get("bio")
        birth_date = request.POST.get("birth_date")
        image = request.FILES.get("image")
        content = request.POST.get("content")
        Celebrity.objects.create(name=name, bio=bio, image=image, content=content, birth_date=birth_date)
        return redirect(f"/celebs/")
    elif request.method == "GET":
        return render(request=request, template_name="celebrities/create_celeb.html")
    return


