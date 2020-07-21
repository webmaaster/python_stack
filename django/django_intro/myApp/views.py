from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print(request.method)
    print(request.POST)
    print(request.GET)
    print(type(request.session))
    request.session['count'] = 1
    return render(request, "index.html")

def show_name(request, name):
    print('_'*50)
    print(f'name is: {name}')
    print('_'*50)
    return redirect('/')

def process_form(request):
    print(request.method)
    print(request.POST)
    print(request.POST['name'])
    print(request.POST['location'])
    print(request.session['count'])
    print(request.GET)

    request.session['name_from_form'] = request.POST['name'],
    request.session['location_from_form'] = request.POST['name']

    context = {
      'name_to_temlate': request.POST['name'], 
      'location_to_template': request.POST['location']

    }

    #return render(request, 'process.html', context )
    return redirect('/success')

def success(request):
    
      print(request.GET),
      print(request.POST)
      if 'name_from_form' in request.POST:
        context = {
          'name_to_template': request.session['name_from_form'],
          'location_to_template': request.session['location_from_form']


     }
      return render(request, 'process.html', context)