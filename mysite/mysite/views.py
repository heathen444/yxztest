from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is %s now</body></html>" % now
    return HttpResponse(html)

def time_plus(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>in %s hours, It will be %s</body></html>"  % (offset, dt)
    return HttpResponse(html)