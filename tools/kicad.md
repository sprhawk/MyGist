# KiCAD #
====

## directories ##
kicad
bin
wx-bin
wx-src
build

## wxWidgets ##
sh kicad/scripts/osx_build_wx.sh wx-src wx-bin kicad "-j4"

## build scripts: ##

```shell
cd build

# build with scripts support
cmake ../kicad -DKICAD_BUILD_DYNAMIC=ON \
            -DCMAKE_C_COMPILER=/usr/bin/clang \
            -DCMAKE_CXX_COMPILER=/usr/bin/clang++ \
            -DwxWidgets_CONFIG_EXECUTABLE=../wx-bin/bin/wx-config \
            -DPYTHON_EXECUTABLE=`which python` \
            -DPYTHON_SITE_PACKAGE_PATH=`pwd`/../wx-bin/lib/python2.7/site-packages \
            -DCMAKE_BUILD_TYPE=Release
make swig

cmake ../kicad \
            -DCMAKE_C_COMPILER=/usr/bin/clang \
            -DCMAKE_CXX_COMPILER=/usr/bin/clang++ \
            -DwxWidgets_CONFIG_EXECUTABLE=../wx-bin/bin/wx-config \
            -DPYTHON_EXECUTABLE=`which python` \
            -DPYTHON_SITE_PACKAGE_PATH=`pwd`/../wx-bin/lib/python2.7/site-packages \
            -DBUILD_GITHUB_PLUGIN=ON \
            -DKICAD_SCRIPTING=ON \
            -DKICAD_SCRIPTING_MODULES=ON \
            -DKICAD_SCRIPTING_WXPYTHON=ON \
            -DCMAKE_INSTALL_PREFIX=../bin \
            -DCMAKE_BUILD_TYPE=Release

# build without scripts support
# cmake ../kicad \
#             -DCMAKE_C_COMPILER=clang \
#             -DCMAKE_CXX_COMPILER=clang++ \
#             -DwxWidgets_CONFIG_EXECUTABLE=../wx-bin/bin/wx-config \
#             -DKICAD_SCRIPTING=OFF \
#             -DKICAD_SCRIPTING_MODULES=OFF \
#             -DKICAD_SCRIPTING_WXPYTHON=OFF \
#             -DBUILD_GITHUB_PLUGIN=ON \
#             -DCMAKE_INSTALL_PREFIX=../bin \
#             -DCMAKE_BUILD_TYPE=Release

make
make install
```

## libraries ##

https://github.com/KiCad/kicad-library

