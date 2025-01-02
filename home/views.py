from django.shortcuts import render

# Create your views here.
from datetime import date, timedelta, datetime
import calendar
import locale


def calendar_view(request):
    # Obtener la fecha actual
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Establecer la localización a español
    
    today = date.today()
    current_day = today.day
    current_month = today.month
    current_year = today.year

    # Obtener el calendario del mes actual
    cal = calendar.Calendar()
    days_in_month = cal.itermonthdays2(current_year, current_month)  # Devuelve (día, día_semana)
    
    # Crear estructura del calendario
    weeks = []
    week = []

    # Día de la semana en el que empieza el mes (0=lunes, 6=domingo)
    first_weekday = calendar.monthrange(current_year, current_month)[0]

    # Agregar días vacíos al principio del mes (si es necesario)
    for _ in range(first_weekday):
        week.append({"day": None, "class": "prev-month"})  # Días fuera del mes actual al principio

    # Agregar los días del mes actual
    for day, weekday in days_in_month:
        if day == 0:  # Días fuera del mes actual
            continue
        css_class = "current-day" if day == current_day else ""
        week.append({"day": day, "class": css_class})

        # Si la semana tiene 7 días, agregarla a la lista de semanas
        if len(week) == 7:
            weeks.append(week)
            week = []

    # Si la última semana no tiene 7 días, agregar días vacíos al final
    if len(week) < 7:
        for _ in range(7 - len(week)):
            week.append({"day": None, "class": "next-month"})  # Días fuera del mes actual al final
        weeks.append(week)

    # Pasar datos al template
    context = {
        "current_day": current_day,
        "current_month": today.strftime("%B").capitalize(),  # El nombre del mes en español
        "current_year": current_year,
        "weeks": weeks,
    }
    
    return render(request, "home/home.html", context)




def flowers_view(request):
    return render(request, "home/flowers.html")
    

