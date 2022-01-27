from datetime import datetime


def year(request):
    year_now = datetime.now().year
    return {'year': year_now}
