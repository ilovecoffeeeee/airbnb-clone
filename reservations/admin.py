from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservastionAdmin(admin.ModelAdmin):
    """Reservastion Admin Definition"""

    pass
