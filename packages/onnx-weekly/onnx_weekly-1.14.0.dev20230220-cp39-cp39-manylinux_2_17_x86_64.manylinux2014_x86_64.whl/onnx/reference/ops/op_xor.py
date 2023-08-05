# SPDX-License-Identifier: Apache-2.0
# pylint: disable=W0221

import numpy as np

from ._op import OpRunBinary


class Xor(OpRunBinary):
    def _run(self, x, y):  # type: ignore
        return (np.logical_xor(x, y),)
