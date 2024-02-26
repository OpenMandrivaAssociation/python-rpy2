%define module rpy2
%define r_version %(pkg-config --modversion libR || echo 0)
%define __noautoreq 'libR.so\\(.*'
%define _files_listed_twice_terminate_build 0

Name:		python-%{module}
Version:	3.5.15
Release:	1
Group:		Development/Python
Summary:	A very simple, yet robust, Python interface to the R Programming Language
License:	AGPLv3+
URL: http://rpy.sourceforge.net/
Source0:	http://pypi.python.org/packages/source/r/rpy2/rpy2-%{version}.tar.gz
Requires:	python-numpy
Requires:	R-core = %{r_version}
BuildRequires:	lapack-devel
BuildRequires:	python3-devel
BuildRequires:	python-numpy-devel
BuildRequires:	pkgconfig(libR)
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(icu-i18n)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	python-setuptools

Provides:	rpy = %{EVRD}

%description
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary R
functions (including the graphic functions). All errors from the R language
areconverted to Python exceptions. Any module installed for the R system can
be used from within Python. 

This code is inspired by RSPython from the Omegahat project. The main goals of
RPy are: 
 + to have a very robust interface for using R from Python 
 + the interface should be as transparent and easy to use as possible 
 + it should be usable for real scientific and statistical computations
 
%prep
%autosetup -n %{module}-%{version}

%build
env CFLAGS="%{optflags}" python setup.py build build_ext -lreadline

%install
PYTHONDONTWRITEBYTECODE=1 \
python setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc NEWS README.md
%py3_platsitedir/%{module}*.egg-info
%py3_platsitedir/%module
%py3_platsitedir/_rinterface_cffi_*
