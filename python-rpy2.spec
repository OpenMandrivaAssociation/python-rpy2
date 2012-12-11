%define module rpy2
%define r_version 2.8.1
%define _requires_exceptions libR.so

Summary:	A very simple, yet robust, Python interface to the R Programming Language
Name:		python-%{module}
Version:	2.2.5
Release:	%mkrel 1
Group:		Development/Python
License:	AGPLv3+
URL:		http://rpy.sourceforge.net/
Source0:	http://pypi.python.org/packages/source/r/%{module}/%{module}-%{version}.tar.gz
Patch0:		rinterface-readline-2.2.5.patch
Requires:	R-base >= %{r_version}
Requires:	python-numpy
BuildRequires:	R-base >= %{r_version}
BuildRequires:	python-devel
BuildRequires:	python-numpy-devel
BuildRequires:	texlive-latex
BuildRequires:	texinfo
BuildRequires:	lapack-devel
BuildRequires:	readline-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -qn %{module}-%{version}
%patch0 -p0

%build
env CFLAGS="%{optflags}" %{__python} setup.py build

#pushd doc
#make all
#popd

%install
rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= \
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --record=INSTALLED_FILES

# install info
#mkdir -p %{buildroot}%{_datadir}/info
#cp doc/rpy.info %{buildroot}%{_datadir}/info/

%clean
rm -rf %{buildroot}

%post
#%_install_info rpy.info

%preun
#%_remove_install_info rpy.info

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc NEWS README


%changelog
* Thu Jan 19 2012 Lev Givon <lev@mandriva.org> 2.2.5-1
+ Revision: 762809
- Update to 2.2.5.

* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.9-1mdv2011.0
+ Revision: 603073
- update to new version 2.1.9

* Fri Nov 05 2010 Paulo Andrade <pcpa@mandriva.com.br> 2.0.8-1mdv2011.0
+ Revision: 593536
- Rebuild with python 2.7

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.8-1mdv2010.1
+ Revision: 489192
- update to new version 2.0.8

* Fri Sep 25 2009 Frederik Himpe <fhimpe@mandriva.org> 2.0.7-1mdv2010.0
+ Revision: 449213
- Update to new version 2.0.7

* Wed Sep 16 2009 Paulo Andrade <pcpa@mandriva.com.br> 2.0.3-2mdv2010.0
+ Revision: 443339
- Import python-rpy2 version 2.0.3
- This was incorrectly named python-rpy
- python-rpy2

