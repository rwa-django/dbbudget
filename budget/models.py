import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.utils import timezone
from django.conf import settings

# Budget
class Budget(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    login = models.CharField(max_length=200,
                             help_text="Login")
    budget_month = models.PositiveSmallIntegerField(
            default=0,
            validators=[
                MinValueValidator(1),
                MaxValueValidator(12)],
            help_text="Format: <MM>")
    budget_year = models.PositiveSmallIntegerField(
            default=datetime.now().year,
            validators=[
                MinValueValidator(2017),
                MaxValueValidator(2050)],
            help_text="Format: <YYYY>")
    budget_amount = models.DecimalField(max_digits=10,
                                        decimal_places=2)
    budget_info = models.CharField(max_length=200,
                                   help_text="Buchungs Info")
    budget_booked = models.DateTimeField(default=timezone.now,
                                         editable=False)

    def __str__(self):
        return '{0}-{1}/{2}-{3}'.format(self.login, self.budget_year, self.budget_month, self.budget_amount)

    def currend_budget(self):
        return self.budget_amount


# Budget Position
class Budget_Pos(models.Model):
    budget_id = models.ForeignKey(Budget,
                                  on_delete=models.CASCADE)
    pos = models.SmallIntegerField(default=1)
    booking_date = models.DateTimeField(default=datetime.now())
    booking_amount = models.DecimalField(default=0,
                                         max_digits=10,
                                         decimal_places=2)
    booking_info = models.CharField(max_length=200,
                                    help_text="Buchungs Info")
    booking_booked = models.DateTimeField(default=timezone.now,
                                          editable=False)

    class Meta:
        unique_together = (('budget_id', 'pos'),)
        ordering = ["budget_id", "-pos"]           # sortierung mit - dreht die Sortierung

    def __str__(self):
        return '{0} / - / {1} {2}.- {3}'.format(self.budget_id, self.pos, int(self.booking_amount), self.booking_info)


# Budget Base Data
class Budget_Base(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             editable=True)
    budget_amount = models.DecimalField(default=0,
                                        max_digits=10,
                                        decimal_places=2)
    budget_info = models.CharField(max_length=200,
                                   help_text="Buchungs Info")
    budget_start_day = models.PositiveSmallIntegerField(default=0,
                                                        validators=[
                                                            MinValueValidator(1),
                                                            MaxValueValidator(30)],
                                                        help_text="Format: <MM>")

    def __str__(self):
        return '{0} {1}.- {2}'.format(self.user, self.budget_amount, self.budget_info)
