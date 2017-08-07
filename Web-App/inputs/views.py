from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from.forms import FormsetFormFormset, TradesSheetFormset

@login_required
def inputs(request, page):
    if not page:
      page = "intro"
    formset = TradesSheetFormset()
    print(formset.forms)
    for form in formset.forms:
        for field in form:
            print(field)
    return HttpResponse(render(request,'inputs/'+page+'.html', {'formset': formset}))


def enterprises_submitted(request):
    return HttpResponse(render(request, "inputs/enterprises_submitted.html"))


def formset_test(request):
    formset = TradesSheetFormset()
    #formset = FormsetFormFormset(initial=[{"title":"this is a title", "pages":10},{"title":"this is a book", "pages":1}])
    return render(request, 'inputs/formset.html', {'formset': formset})