from django.shortcuts import render
from .models import Celebrity

def celebrity_list(request):
    celebs = Celebrity.objects.all()
    return render(request, 'celebrities/list.html', {'celebs': celebs})

# Create your views here.
