#!/bin/bash
# SPDX-FileCopyrightText: 2023 Ryota Ema <rhenium4694@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

cd src/mypkg
# cat inputs.txt | read INPUT
INPUT = cat inputs.txt
cd ../..
(ros2 launch mypkg talk_listen.launch.py < $INPUT ) > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Listen: 1'
