#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-selectors34
Version  : 1.2
Release  : 4
URL      : https://files.pythonhosted.org/packages/7a/5e/fb5491a0295ee9d018d046ecffc30cec26075cb925f35bd24d40036aa95a/selectors34-1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/7a/5e/fb5491a0295ee9d018d046ecffc30cec26075cb925f35bd24d40036aa95a/selectors34-1.2.tar.gz
Summary  : Backport of the selectors module from Python 3.4.
Group    : Development/Tools
License  : Python-2.0
Requires: pypi-selectors34-python = %{version}-%{release}
Requires: pypi-selectors34-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(six)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
selectors34
        ===========
        
        *selectors34* is a backport of the selectors module from Python 3.4. The
        selectors module written by Charles-François Natali. This port is based on
        Victor Stinner's ``trollius/selectors.py`` port.
        
        Installation and Usage
        ----------------------

%package python
Summary: python components for the pypi-selectors34 package.
Group: Default
Requires: pypi-selectors34-python3 = %{version}-%{release}

%description python
python components for the pypi-selectors34 package.


%package python3
Summary: python3 components for the pypi-selectors34 package.
Group: Default
Requires: python3-core
Provides: pypi(selectors34)
Requires: pypi(six)

%description python3
python3 components for the pypi-selectors34 package.


%prep
%setup -q -n selectors34-1.2
cd %{_builddir}/selectors34-1.2
pushd ..
cp -a selectors34-1.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656374169
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
