from elasticai.creator.tests.unit.vhdl.vhdl_file_testcase import GeneratedVHDLCodeTest
from elasticai.creator.vhdl.code_files.rom_component import RomFile
from elasticai.creator.vhdl.number_representations import float_values_to_fixed_point


class GenerateROMVhdTest(GeneratedVHDLCodeTest):
    def test_compare_files(self) -> None:
        # biases for the input gate
        bi = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]

        rom = RomFile(
            rom_name="rom_bi",
            layer_id="0",
            values=float_values_to_fixed_point(bi, total_bits=12, frac_bits=4),
            resource_option="auto",
        )
        generated_code = list(rom.code())

        expected_code = [
            "library ieee;",
            "    use ieee.std_logic_1164.all;",
            "    use ieee.std_logic_unsigned.all;",
            "entity rom_bi_0 is",
            "    port (",
            "        clk : in std_logic;",
            "        en : in std_logic;",
            "        addr : in std_logic_vector(3-1 downto 0);",
            "        data : out std_logic_vector(12-1 downto 0)",
            "    );",
            "end entity rom_bi_0;",
            "architecture rtl of rom_bi_0 is",
            (
                "    type rom_bi_0_array_t is array (0 to 2**3-1) of"
                " std_logic_vector(12-1 downto 0);"
            ),
            (
                "    signal ROM :"
                ' rom_bi_0_array_t:=(x"011",x"023",x"034",x"046",x"058",x"069",x"000",x"000");'
            ),
            "    attribute rom_style : string;",
            '    attribute rom_style of ROM : signal is "auto";',
            "begin",
            "    ROM_process: process(clk)",
            "    begin",
            "        if rising_edge(clk) then",
            "            if (en = '1') then",
            "                data <= ROM(conv_integer(addr));",
            "            end if;",
            "        end if;",
            "    end process ROM_process;",
            "end architecture rtl;",
        ]

        self.assertEqual(expected_code, generated_code)
