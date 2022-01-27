from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservastionAdmin(admin.ModelAdmin):
    """Reservastion Admin Definition"""

    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)


@admin.register(models.BookedDay)
class BookedDayAdmin(admin.ModelAdmin):
    list_display = (
        "day",
        "reservation",
    )
