from functools import partial

from elasticai.creator.tests.integration.vhdl.vhdl_file_test_case import (
    VHDLFileTestCase,
)
from elasticai.creator.vhdl.lstm_testbench_generator import LSTMCellTestBench
from elasticai.creator.vhdl.number_representations import (
    float_values_to_fixed_point,
    unsigned_int_values_to_fixed_point,
)


class LSTMCellTestBenchTest(VHDLFileTestCase):
    maxDiff = None

    def test_compare_files(self) -> None:
        fp_args = dict(total_bits=16, frac_bits=8)
        ints_to_fp = partial(unsigned_int_values_to_fixed_point, **fp_args)
        floats_to_fp = partial(float_values_to_fixed_point, **fp_args)

        lstm_cell = LSTMCellTestBench(
            input_size=5,
            hidden_size=20,
            component_name="lstm_cell",
            test_x_h_data=ints_to_fp(
                [
                    0x018A,
                    0xFFB5,
                    0xFDD3,
                    0x0091,
                    0xFEEB,
                    0x0099,
                    0xFE72,
                    0xFFA9,
                    0x01DA,
                    0xFFC9,
                    0xFF42,
                    0x0090,
                    0x0042,
                    0xFFD4,
                    0xFF53,
                    0x00F0,
                    0x007D,
                    0x0134,
                    0x0015,
                    0xFECD,
                    0xFFFF,
                    0xFF7C,
                    0xFFB2,
                    0xFE6C,
                    0x01B4,
                    0x0000,
                    0x0000,
                    0x0000,
                    0x0000,
                    0x0000,
                    0x0000,
                    0x0000,
                ]
            ),
            test_c_data=ints_to_fp(
                [
                    0x0034,
                    0xFF8D,
                    0xFF6E,
                    0xFF72,
                    0xFEE0,
                    0xFFAF,
                    0xFEE9,
                    0xFFEB,
                    0xFFE9,
                    0x00AF,
                    0xFF2A,
                    0x0000,
                    0xFF40,
                    0x002F,
                    0x009F,
                    0x00A3,
                    0xFFC2,
                    0x024D,
                    0xFE1F,
                    0xFFF4,
                    0x0000,
                    0x0000,
                    0x0000,
                    0x0000,
                    0x0000,
                    0x0000,
                    0x0000,
                    0x0000,
                    0x0000,
                    0x0000,
                    0x0000,
                    0x0000,
                ]
            ),
            h_out=floats_to_fp(
                [
                    34,
                    -80,
                    -32,
                    -28,
                    -88,
                    11,
                    -60,
                    6,
                    -16,
                    18,
                    -32,
                    46,
                    -77,
                    15,
                    70,
                    27,
                    13,
                    112,
                    -126,
                    3,
                ]
            ),
        )
        lstm_cell_code = lstm_cell.code()
        self.compareToFile("expected_lstm_cell_testbench.vhd", lstm_cell_code)
