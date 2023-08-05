# SPDX-License-Identifier: Apache-2.0
# pylint: disable=W0221

import numpy as np

from ._op import OpRunUnary


class IsNaN(OpRunUnary):
    def _run(self, data):  # type: ignore
        return (np.isnan(data),)
