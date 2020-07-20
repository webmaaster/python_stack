from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
    'name': "Mr. Andew Kishore"
  }
    return render(request, "index.html", context)

# def another_page(request):
#     return render(request, "another_page.html")

# def does_nothing():git
#     print('Does nothing but print my name - BAB')
#     return redirect('/')
