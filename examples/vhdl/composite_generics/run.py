# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014-2019, Lars Asplund lars.anders.asplund@gmail.com

"""
Composite generics
------------------

See `Enable Your Simulator to Handle Complex Top-Level Generics <https://vunit.github.io/posts/2017_06_03_enable_your_simulator_to_handle_complex_top_level_generics/post.html>`_.
"""

from os.path import join, dirname
from vunit import VUnit


def encode(tb_cfg):
    return ", ".join(["%s:%s" % (key, str(tb_cfg[key])) for key in tb_cfg])


vu = VUnit.from_argv()

tb_lib = vu.add_library("tb_lib")
tb_lib.add_source_files(join(dirname(__file__), "test", "*.vhd"))

test_1 = tb_lib.test_bench("tb_composite_generics").test("Test 1")

vga_tb_cfg = dict(image_width=640, image_height=480, dump_debug_data=False)
test_1.add_config(name="VGA", generics=dict(encoded_tb_cfg=encode(vga_tb_cfg)))

tiny_tb_cfg = dict(image_width=4, image_height=3, dump_debug_data=True)
test_1.add_config(name="tiny", generics=dict(encoded_tb_cfg=encode(tiny_tb_cfg)))

vu.main()
