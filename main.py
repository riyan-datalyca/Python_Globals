# Copyright (c) <year>, <copyright holder>
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from classes import T1, T2
import time


def exec_func():
    t1 = T1()

    t2 = T2()

    t1.get()
    time.sleep(1)
    t2.get()
    time.sleep(1)
    t1.get()
    time.sleep(2)
    t2.get()


if __name__ == '__main__':
    exec_func()
