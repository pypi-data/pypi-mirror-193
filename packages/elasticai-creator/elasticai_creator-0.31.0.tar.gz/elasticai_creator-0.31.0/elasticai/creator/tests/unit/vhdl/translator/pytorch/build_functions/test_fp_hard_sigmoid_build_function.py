import unittest

from elasticai.creator.nn.hard_sigmoid import HardSigmoid
from elasticai.creator.vhdl.number_representations import FixedPoint
from elasticai.creator.vhdl.translator.abstract.layers.fp_hard_sigmoid_module import (
    FPHardSigmoidModule,
)
from elasticai.creator.vhdl.translator.pytorch.build_functions.fp_hard_sigmoid_build_function import (
    build_fp_hard_sigmoid,
)


class FPHardSigmoidBuildFunctionTest(unittest.TestCase):
    def test_build_function_returns_correct_type(self) -> None:
        fp_factory = FixedPoint.get_factory(total_bits=8, frac_bits=4)
        layer = HardSigmoid()
        layer_module = build_fp_hard_sigmoid(
            layer, layer_id="hs1", fixed_point_factory=fp_factory
        )
        self.assertEqual(type(layer_module), FPHardSigmoidModule)
