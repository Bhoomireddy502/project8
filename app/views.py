from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='this is my assumption data'
    d={'key':data,'age':22}

    return render(request,'data_render.html',context=d)