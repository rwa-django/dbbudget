from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Budget
from datetime import datetime

from django.template.defaultfilters import date


@login_required(login_url='/accounts/login/')
def index(request):

    year = datetime.now().year
    month = datetime.now().month
    actuel_budget = Budget.objects.filter(budget_month=month).filter(budget_year=year).values()

    template = loader.get_template('budget/index.html')
    context = {
        'db_data': actuel_budget[0]['budget_amount'],
        'year': year,
        'month': month,
        'month_desc' : date(datetime.now(), 'F')
    }
    return HttpResponse(template.render(context, request))