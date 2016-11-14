#! /usr/bin/env sh

base=""
if [ $# = 0 ];then
    base=$ROBOTPKG_BASE/share/move3d/assets
elif [ $# = 1 ];then
    base=$1
fi
echo Will link with p3d files found in $base

ln -sf $base/ADREAM/MACROS p3d/
ln -sf $base/urdf/COLLADA p3d/

