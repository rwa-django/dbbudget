from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):

    template = loader.get_template('budget/index.html')
    context = {
        'db_data': 'Dickbüch Budget',
    }
    return HttpResponse(template.render(context, request))