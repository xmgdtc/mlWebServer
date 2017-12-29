from sklearn.linear_model import LinearRegression,RidgeCV,LassoCV,ElasticNetCV
from sklearn.linear_model.base import LinearModel
import numpy as np

class Reger(object):

    model=LinearRegression()
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

    def predict(self,data:np.array)->np.array:
        return self.model.predict(data)
