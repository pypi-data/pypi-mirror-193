import unittest

from elasticai.creator.vhdl.code_files.fp_hard_sigmoid_component import (
    FPHardSigmoidComponent,
)
from elasticai.creator.vhdl.number_representations import FixedPoint
from elasticai.creator.vhdl.translator.abstract.layers.fp_hard_sigmoid_module import (
    FPHardSigmoidModule,
)


class FPHardSigmoidModuleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.fp_factory = FixedPoint.get_factory(total_bits=8, frac_bits=4)
        self.module = FPHardSigmoidModule(
            layer_id="0", fixed_point_factory=self.fp_factory
        )

    def test_components_return_only_one_component(self) -> None:
        components = list(self.module.files)
        self.assertEqual(len(components), 1)
        self.assertEqual(type(components[0]), FPHardSigmoidComponent)

    def test_components_component_args_are_correctly_set(self) -> None:
        component = list(self.module.files)[0]
        self.assertEqual(component.zero_threshold, self.fp_factory(-3))  # type: ignore
        self.assertEqual(component.one_threshold, self.fp_factory(3))  # type: ignore
        self.assertEqual(component.slope, self.fp_factory(0.125))  # type: ignore
        self.assertEqual(component.y_intercept, self.fp_factory(0.5))  # type: ignore
