# Copyright (c) <year>, <copyright holder>
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import globals
import subtract


globals.initialize()
print(globals.seq)


class T1:
    def get(self):
        subtract.minus()
        print(globals.seq)


class T2:
    def get(self):
        subtract.minus()
        print(globals.seq)
