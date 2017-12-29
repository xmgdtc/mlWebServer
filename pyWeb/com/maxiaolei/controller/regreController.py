from django.http import HttpResponse,HttpRequest
from ..models import error
import json
import numpy as np
from ..services import regreService
def regre(request:HttpRequest):
   # if not request.POST:
        #return HttpResponse(error.Error(406,'not allow method'))

   # if request.POST:
        print(request.body)
        body=json.loads(request.body.decode('utf-8'))

        print(body)
        data=body['data']
        data=np.array(data)

        tags=body['tags']
        tags=np.array(tags)

        pData=body['pdata']
        pData=np.array(pData)

        regreModel=regreService.Reger()
        regreModel.data=data
        regreModel.tags=tags
        regreModel.fitByLinear()
        tag=regreModel.predict(pData)

    #return HttpResponse(json.dumps(ctx.__dict__))
        return HttpResponse(tag)
