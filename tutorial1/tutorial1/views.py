from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render
import datetime


def show_index(request):
    t = get_template('index.html')
    html = t.render(Context({'seccion_actual': 'Hola Mundo'}))
    return HttpResponse(html)


def show_course_django(request):
    return render(request, 'courses/django.html', {
        'seccion_actual': 'django',
        'tema_django': 'Generación plantilla',
        'ejem1': 'Texto "escapado", \ejemplo',
        'ejem2': datetime.datetime.now()
    })
