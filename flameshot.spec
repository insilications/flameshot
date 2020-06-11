#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : flameshot
Version  : 1
Release  : 3
URL      : file:///insilications/build/clearlinux/packages/flameshot/flameshot.zip
Source0  : file:///insilications/build/clearlinux/packages/flameshot/flameshot.zip
Summary  : Powerful yet simple to use screenshot software
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0
Requires: flameshot-bin = %{version}-%{release}
Requires: flameshot-data = %{version}-%{release}
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : ca-certs
BuildRequires : ca-certs-static
BuildRequires : openssl-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : qttools
BuildRequires : qttools-dev
Patch1: 0001-Fix-compile-on-Qt-5.15.0.patch

%description
Flameshot is a screenshot software, it's
powerful yet simple to use for GNU/Linux

%package bin
Summary: bin components for the flameshot package.
Group: Binaries
Requires: flameshot-data = %{version}-%{release}

%description bin
bin components for the flameshot package.


%package data
Summary: data components for the flameshot package.
Group: Data

%description data
data components for the flameshot package.


%prep
%setup -q -n flameshot
cd %{_builddir}/flameshot
%patch1 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=12 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fno-common -pipe"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=12 -fno-common -Wno-error -Wp,-D_REENTRANT
export CXXFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=12 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -fno-common -pipe"
#
export FCFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=12 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fno-common -pipe"
export FFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=12 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fno-common -pipe"
export CFFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=12 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fno-common -pipe"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=12 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fno-common -pipe"
#
export QMAKE_CFLAGS_RELEASE="-config ltcg"
export QMAKE_CXXFLAGS_RELEASE="-config ltcg"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags1 end
%qmake -config ltcg
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1591569041
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flameshot

%files data
%defattr(-,root,root,-)
/usr/share/applications/flameshot.desktop
/usr/share/bash-completion/completions/flameshot
/usr/share/dbus-1/interfaces/org.dharkael.Flameshot.xml
/usr/share/dbus-1/services/org.dharkael.Flameshot.service
/usr/share/flameshot/translations/Internationalization_ca.qm
/usr/share/flameshot/translations/Internationalization_de_DE.qm
/usr/share/flameshot/translations/Internationalization_es.qm
/usr/share/flameshot/translations/Internationalization_fr.qm
/usr/share/flameshot/translations/Internationalization_ja.qm
/usr/share/flameshot/translations/Internationalization_ka.qm
/usr/share/flameshot/translations/Internationalization_pl.qm
/usr/share/flameshot/translations/Internationalization_pt_br.qm
/usr/share/flameshot/translations/Internationalization_ru.qm
/usr/share/flameshot/translations/Internationalization_sk.qm
/usr/share/flameshot/translations/Internationalization_sr.qm
/usr/share/flameshot/translations/Internationalization_tr.qm
/usr/share/flameshot/translations/Internationalization_uk.qm
/usr/share/flameshot/translations/Internationalization_zh_CN.qm
/usr/share/flameshot/translations/Internationalization_zh_TW.qm
/usr/share/icons/hicolor/128x128/apps/flameshot.png
/usr/share/icons/hicolor/48x48/apps/flameshot.png
/usr/share/icons/hicolor/scalable/apps/flameshot.svg
/usr/share/metainfo/flameshot.appdata.xml
