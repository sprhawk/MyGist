#!/bin/sh

# change something like 612_hd_motion_tracking_with_the_core_motion_framework.mov-, attachment to 612_hd_motion_tracking_with_the_core_motion_framework.mov
a=`basename "$1"`
#echo $a
 mv "$a" "${a%*-, *}"


