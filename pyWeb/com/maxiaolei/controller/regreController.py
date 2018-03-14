from django.http import HttpResponse,HttpRequest
from ..models import error
import json
import numpy as np
from ..services import regreService
from ..config import regerSettings
defaultAlphas=regerSettings.alphas


def regre(request:HttpRequest):
    if not request.method=='POST':
        return HttpResponse(error.Error(406,'http method not allow '))

    body=json.loads(request.body.decode('utf-8'))
    data=np.array(body['data'])
    tags=np.array(body['tags'])
    pData=np.array(body['pdata'])
    alphas=np.array(body.get('alphas',defaultAlphas))

    regreModel=regreService.Reger()
    regreModel.data=data
    regreModel.tags=tags
    regreModel.fitByRidge(alphas)
    tag=regreModel.predict(pData)

    return HttpResponse(tag)
