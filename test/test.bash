#!/bin/bash
# SPDX-FileCopyrightText: 2023 Ryota Ema <rhenium4694@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws/src/mypkg
colcon build
source $dir/.bashrc

# cd src/mypkg
while read INPUT
do
	(ros2 launch mypkg talk_listen.launch.py < $INPUT ) >/tmp/mypkg.log
done < ./inputs.txt 

cat /tmp/mypkg.log |
grep 'Listen: 1'
