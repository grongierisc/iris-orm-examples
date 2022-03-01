from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import person
from django.http import HttpResponseRedirect

class IndexView(generic.ListView):
    template_name = 'persons/index.html'
    context_object_name = 'person_list'

    def get_queryset(self):
        """Return all the latest persons."""
        return person.objects.order_by('name')

def add(request):
    title = request.POST['title']
    person.objects.create(title=title)

    return redirect('persons:index')

def delete(request, person_id):
    person = get_object_or_404(person, pk=person_id)
    person.delete()

    return redirect('persons:index')

def update(request, person_id):
    person = get_object_or_404(person, pk=person_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    person.isCompleted = isCompleted

    person.save()
    return redirect('persons:index')