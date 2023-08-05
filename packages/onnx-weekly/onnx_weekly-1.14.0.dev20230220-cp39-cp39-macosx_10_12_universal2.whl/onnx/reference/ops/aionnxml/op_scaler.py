# SPDX-License-Identifier: Apache-2.0
# pylint: disable=R0913,R0914,W0221

from ._op_run_aionnxml import OpRunAiOnnxMl


class Scaler(OpRunAiOnnxMl):
    def _run(self, x, offset=None, scale=None):  # type: ignore
        dx = x - offset
        return ((dx * scale).astype(x.dtype),)
