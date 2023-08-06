import numpy as np
import pandas as pd
import sklearn
from typing import Union

from . import nn


class PreprocessorEstimatorPipeline(sklearn.base.BaseEstimator):
    """Wraps preprocessor and estimator into a single sklearn Pipeline.

    Parameters
    ----------
    estimator : Estimator
        Fitted estimator (implementing `fit`/`predict`).

    preprocessor : Transformer
        Fitted transformer (implementing `fit`/`transform`).


    Attributes
    ----------
    pipeline_ : sklearn.pipeline.Pipeline
        Fitted sklearn Pipeline.
    """

    def __init__(
            self,
            preprocessor: nn.base.Transformer,
            estimator: sklearn.base.BaseEstimator,
            **predict_kwargs
    ):
        self.preprocessor = preprocessor
        self.estimator = estimator
        self.predict_kwargs = predict_kwargs

    def fit(self, X: pd.DataFrame, y=None):
        """Fits pipeline composed by both the preprocessor and estimator on X.

        Parameters
        ----------
        X : pd.DataFrame
            Input data

        y : None
            Compatibility purposes.

        Returns
        -------
        self (object)
        """
        self.pipeline_ = self.make_pipeline()
        self.pipeline_.fit(X)
        return self

    def predict(
            self,
            X: pd.DataFrame,
            **kwargs
    ) -> Union[pd.DataFrame, np.array]:
        sklearn.utils.validation.check_is_fitted(self)

        kwargs = kwargs.update(self.predict_kwargs)
        output = self.pipeline_.predict(X, **kwargs)
        return self.inverse_transform(output)

    def inverse_transform(self, X):
        return self.pipeline_.preprocessor.inverse_transform(X)

    def make_pipeline(self):
        steps = [
            ('preprocessor', self.preprocessor),
            ('estimator', self.estimator)
        ]
        return sklearn.pipeline.Pipeline(steps)
