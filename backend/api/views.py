from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)  # json => dictionary
    except:
        pass
    data["headers"] = dict(request.headers)
    data["params"] = dict(request.GET)
    return JsonResponse({
        "message": "this is repsonse",
        "data": data
    })
