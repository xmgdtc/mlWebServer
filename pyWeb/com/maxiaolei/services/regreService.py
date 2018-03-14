from sklearn.linear_model import LinearRegression,RidgeCV,LassoCV,ElasticNetCV
from sklearn.linear_model.base import LinearModel
import numpy as np
from ..config import regerSettings
defaultAlphas=regerSettings.alphas


class Reger(object):

    def __int__(self,data:np.array,tags:np.array):
        self.data=data
        self.tags=tags
        self.model=LinearRegression()

    model:LinearModel= None
    data = None
    tags = None

    def fitByLinear(self):
        self.model=LinearRegression(
            fit_intercept=True,
            normalize=True,
            copy_X=False,
            n_jobs=-1
        )
        self.model.fit(self.data,self.tags)
        return self

    def fitByRidge(self,alphas:np.array):
        self.model=RidgeCV(
            alphas=alphas,
            fit_intercept=True,
            normalize=True,
            cv=None,
            gcv_mode='auto',
            store_cv_values=False
        )
        self.model.fit(self.data,self.tags)
        return self

    def predict(self,data:np.array)->np.array:
        return self.model.predict(data)

