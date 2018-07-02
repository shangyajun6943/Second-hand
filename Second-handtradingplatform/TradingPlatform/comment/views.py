from django.shortcuts import render

# Create your views here.

def comment(request):
    return render(request,'comment/comment_index.html')
