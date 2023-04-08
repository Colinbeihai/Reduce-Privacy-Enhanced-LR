class RegressionBase(object):
    def __init__(self):
        self.bias = None
        self.weights = None

class LinearRegression(RegressionBase):
    def __init__(self):
        RegressionBase.__init__(self)

    def _predict(self, Xi):
        return sum(wi * xij for wi, xij in zip(self.weights, Xi))

    def _get_gradient_delta(self, Xi, yi):
        y_hat = self._predict(Xi)
        bias_grad_delta = yi - y_hat
        weights_grad_delta = [bias_grad_delta * Xij for Xij in Xi] #为什么加中括号
        return bias_grad_delta, weights_grad_delta


