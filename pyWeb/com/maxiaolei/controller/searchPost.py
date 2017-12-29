# -*- coding: utf-8 -*-

from django.http import HttpResponse
import json
from ..models import demoModel,error

# 接收POST请求数据
def search_post(request):
    if not request.POST:
        return HttpResponse(error.Error('not allow method'))
    ctx=demoModel.ResDemo()
    if request.POST:
        ctx.name,ctx.age=request.POST['name'],int(request.POST['age']) or 0
    #return HttpResponse(json.dumps(ctx.__dict__))
    return HttpResponse(ctx.toJSON())
