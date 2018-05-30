# -*- coding: utf-8 -*-

import uuid
import tempfile
from django.http import HttpResponse
from captcha_identify.tf_for_identify import identify
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def identifying(request):
    """ 接收请求数据 """
    if 'image' not in request.FILES.keys():
        return HttpResponse('can not get image.')
    file = request.FILES.get('image')
    filename = '%s/%s.png' % (str(tempfile.gettempdir()), str(uuid.uuid1()))
    with open(filename, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)

    try:
        code = identify(filename)
    except Exception as e:
        print(e)
        return HttpResponse('')
    return HttpResponse(code)
