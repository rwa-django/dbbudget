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
        info = request.POST['info']
    except:
        amount = 0
        info = ''

    year = datetime.now().year
    month = datetime.now().month
    actuel_budget = Budget.objects.filter(login=request.user,budget_month=month).filter(budget_year=year)
    ID_B = actuel_budget[0].pk

    Q_Budget_Pos = Budget_Pos.objects.filter(budget_id=ID_B)

    val = 0
    last_pos = 1
    for pos in Q_Budget_Pos.order_by('pos'):
        val += pos.booking_amount
        last_pos = pos.pos

    value = actuel_budget[0].budget_amount - val

    print('----lastpos-- %s val %s am %s' % (last_pos, value, amount))

    if amount != 0:
        # create Q_Budget_pos
        print('--Create Pos %s' % (last_pos + 1))

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

