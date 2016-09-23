from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from.forms import EnterpriseForm, FormsetFormFormset

from simulation.models import Enterprise, SimulationYear
@login_required
def inputs(request, page):
    if not page:
      page = "intro"
    return HttpResponse(render(request,'inputs/'+page+'.html'))

def enterprises(request):
    # if this is a POST request we need to process the form data

    year = SimulationYear(year_ending=1)
    year.save()
    enterprise= Enterprise(year=year)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EnterpriseForm(request.POST, instance=enterprise)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('enterprises/success/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EnterpriseForm()

    return render(request, 'inputs/enterprises.html', {'form': form})

def enterprises_submitted(request):
    return HttpResponse(render(request, "inputs/enterprises_submitted.html"))

def formset_test(request):
    formset = FormsetFormFormset(initial=[{"title":"this is a title", "pages":10},{"title":"this is a book", "pages":1}])
    return render(request, 'inputs/formset.html', {'formset': formset})