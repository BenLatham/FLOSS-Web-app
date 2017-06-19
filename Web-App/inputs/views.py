from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from.forms import FormsetFormFormset

@login_required
def inputs(request, page):
    if not page:
      page = "intro"
    return HttpResponse(render(request,'inputs/'+page+'.html'))


def enterprises_submitted(request):
    return HttpResponse(render(request, "inputs/enterprises_submitted.html"))

def formset_test(request):
    formset = FormsetFormFormset(initial=[{"title":"this is a title", "pages":10},{"title":"this is a book", "pages":1}])
    return render(request, 'inputs/formset.html', {'formset': formset})