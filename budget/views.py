from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Budget, Budget_Pos
from datetime import datetime

from django.template.defaultfilters import date

@login_required(login_url='/accounts/login/')
def index(request):

    try:
        amount = int(request.POST['amount'])
    except:
        amount = 0

    year = datetime.now().year
    month = datetime.now().month
    actuel_budget = Budget.objects.filter(budget_month=month).filter(budget_year=year).values()

    Q_Budget_Pos = Budget_Pos.objects.filter(id=actuel_budget[0]['id'])

    val = 0
    last_pos = 1
    for pos in Q_Budget_Pos:
        val += pos.booking_amount
        last_pos = pos.pos

    value = actuel_budget[0]['budget_amount'] - val

    if amount != 0:
        # create Q_Budget_pos
        print('--Create Pos %s' % (last_pos + 1))

    value = value - amount

    template = loader.get_template('budget/index.html')
    context = {
        'db_data': value,
        'year': year,
        'month': month,
        'month_desc' : date(datetime.now(), 'F'),
        'Q_Budget_Pos': Q_Budget_Pos,
    }
    return HttpResponse(template.render(context, request))

