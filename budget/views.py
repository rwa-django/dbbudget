from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Budget, Budget_Pos, Budget_Base
from datetime import datetime
from django.conf import settings

from django.template.defaultfilters import date

@login_required(login_url='/accounts/login/')
def index(request):

    try:
        amount = int(request.POST['amount'])
        info = request.POST['info']
    except:
        amount = 0
        info = ''

    value = 0
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    Q_Budget_Pos = []

    if day > 26:
        month += 1
        if month > 12:
            month = 1
            year += 1

    actuel_budget = Budget.objects.filter(login=request.user,budget_month=month).filter(budget_year=year)
    if actuel_budget:
        ID_B = actuel_budget[0].pk

        Q_Budget_Pos = Budget_Pos.objects.filter(budget_id=ID_B)

        val = 0
        last_pos = 1
        for pos in Q_Budget_Pos.order_by('pos'):
            val += pos.booking_amount
            last_pos = pos.pos

        value = actuel_budget[0].budget_amount - val

        if amount != 0:
            # create Q_Budget_pos
            print('--Create Budget Pos %s M %s Y %s' % (last_pos + 1, month, year))

            bp = Budget_Pos(budget_id=actuel_budget[0],pos=last_pos + 1,booking_amount=amount,booking_info=info)
            bp.save()

            Q_Budget_Pos = Budget_Pos.objects.filter(budget_id=actuel_budget[0])

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


def Profile(request):
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day

    Q_data = Budget_Base.objects.filter(user=request.user)
    print('======%s %s' % (Q_data.__dict__,request.user))

    template = loader.get_template('budget/profile.html')
    context = {
        'day': Q_data[0].budget_start_day,
        'amount': Q_data[0].budget_amount,
    }
    return HttpResponse(template.render(context, request))
