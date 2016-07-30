from django.http import HttpRequest

def get_new_us_request():
    request = HttpRequest()
    request.method = 'POST'
    request.POST['title'] = 'ususus'
    request.POST['estimate_time'] = 2
    return request
