from django.http import HttpResponse


def execute(request, **kwargs):
    return HttpResponse('result=' + kwargs.get('response'))

