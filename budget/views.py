from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('budget/index.html')
    context = {
        'db_data': 'Dickbüch Budget',
    }
    return HttpResponse(template.render(context, request))