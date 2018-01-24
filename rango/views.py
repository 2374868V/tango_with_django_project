from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'boldmessage':"cruncy, creamy, cookie, candy, cupcake"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'tutorialmessage':"this tutorial has been put together by Guus van der Ham"}
    return render(request, 'rango/about.html', context=context_dict)