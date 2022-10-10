from django.http import HttpResponse
from django.template import loader


def show_blank_page(request):
    template = loader.get_template('template.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)