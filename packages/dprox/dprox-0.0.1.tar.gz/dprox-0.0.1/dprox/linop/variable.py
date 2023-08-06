from .lin_op import LinOp
import numpy as np
import uuid
import torch


class Variable(LinOp):
    """A variable.
    """

    def __init__(self, shape=None, name=None):
        super(Variable, self).__init__([])
        self.uuid = uuid.uuid1()
        self._value = None
        self.shape = shape
        self.varname = name
        self.initval = None

    def forward(self, inputs):
        """The forward operator.

        Reads from inputs and writes to outputs.
        """
        return inputs

    def adjoint(self, inputs):
        """The adjoint operator.

        Reads from inputs and writes to outputs.
        """
        return inputs

    def variables(self):
        return [self]

    def is_diag(self, freq=False):
        """Is the lin op diagonal (in the frequency domain)?
        """
        return True

    def get_diag(self, ref, freq=False):
        """Returns the diagonal representation (A^TA)^(1/2).

        Parameters
        ----------
        freq : bool
            Is the diagonal representation in the frequency domain?
        Returns
        -------
        dict of variable to ndarray
            The diagonal operator acting on each variable.
        """
        return torch.ones(ref.shape)

    @property
    def value(self):
        return self._value.to(self.device)

    @value.setter
    def value(self, val):
        """Assign a value to the variable.
        """
        self._value = val

    def norm_bound(self, input_mags):
        """Gives an upper bound on the magnitudes of the outputs given inputs.

        Parameters
        ----------
        input_mags : list
            List of magnitudes of inputs.

        Returns
        -------
        float
            Magnitude of outputs.
        """
        return 1.0
