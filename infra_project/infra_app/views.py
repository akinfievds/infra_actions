from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Не так ли...')


def second_page(request):
    return HttpResponse('А это вторая страница')
