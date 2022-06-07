from datetime import datetime
from django.shortcuts import render


def base(request):

    date = datetime.today()

    return render(request, "Platformnut/base.html", context={"date": date})
