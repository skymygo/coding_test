import numpy as np

class NormBase:
    """Base class of normalizations.
    """

    def __init__(self, num_channels, gamma=None, beta=None, eps=1e-5):
        """Initialization.
        `gamma` and `beta` are learnable parameters which are denoted as
        `gamma` and `beta` in the equation.
        """
        self.C = num_channels
        self.eps = eps

        self.gamma = gamma if gamma is not None else np.random.uniform(size=self.C)
        self.beta = beta if beta is not None else np.random.uniform(size=self.C)

    def forward(self, input):
        raise NotImplementedError


class InstanceNorm(NormBase):
    def forward(self, input):
        b, c, h, w = input.shape
        input = input.reshape([b, c, h*w])
        # out_arr = np.zeros([b, c, h*w])
        out_arr = []
        for i in range(b):
            for j in range(c):
                c_val = input[i, j, :]
                mean = c_val.mean()
                std = self._std(c_val)
                c_norm = (c_val - mean) / std
                c_norm = (self.gamma[j] * c_norm) + self.beta[j]
                # out_arr[i, j, :] = c_norm
                out_arr.append(c_norm)
        out_arr = np.array(out_arr)
        out_arr = out_arr.reshape([b, c, h, w])
        return out_arr

    def _std(self, x):
        m = x.shape[0]
        mean = x.mean()
        std = (1 / m) * np.power((x - mean), 2).sum() + self.eps
        std = np.sqrt(std)

        return std

inn = InstanceNorm(num_channels=3, eps=1e-5)
input = np.ones([10, 3, 224, 224])
output =  inn.forward(input)
print(output.shape)