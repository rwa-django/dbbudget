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

    print('-----user-name', request.user.username)

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

    Q_Base = Budget_Base.objects.filter(user=request.user)
    if Q_Base:
        startDay = Q_Base[0].budget_start_day
    else:
        startDay = 31

    if day >= startDay:
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
    else:
        b = Budget(login=request.user.username,budget_month=month,budget_year=year,budget_amount=Q_Base[0].budget_amount,budget_info='Init {0}'.format(date(datetime.now(), 'F')))
        b.save()

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

    day = 0
    amount = 0
    Q_data = Budget_Base.objects.filter(user=request.user)
    if Q_data:
        day = Q_data[0].budget_start_day
        amount = Q_data[0].budget_amount


    template = loader.get_template('budget/profile.html')
    context = {
        'day': day,
        'amount': amount,
    }
    return HttpResponse(template.render(context, request))
