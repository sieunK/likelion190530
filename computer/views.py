from django.shortcuts import render

# Create your views here.
def index(request):
    text = request.POST.get('text','')
    context = {'text':text}
    return render(request,'index.html',context)