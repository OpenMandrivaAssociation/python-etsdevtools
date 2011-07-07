%define	module	etsdevtools
%define name	python-%{module}
%define version	4.0.0
%define release	%mkrel 1

Summary:	Enthought Tool Suite - etsdevtools project
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.enthought.com/repo/ETS/%{module}-%{version}.tar.gz
License:	BSD
Group: 		Development/Python
Url:		http://code.enthought.com/projects/dev_tools.php
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Obsoletes:	python-enthought-etsdevtools
Requires:	python-docutils
Requires: 	python-numpy >= 1.1.0
Requires:	python-traitsui >= 4.0.0
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	python-numpy-devel >= 1.1.0
BuildRequires:	python-sphinx

%description
The etsdevtools project includes a set of packages that can be used
during the development of a software project, for understanding,
debugging, testing, and inspecting code.

* etsdevtools.debug: A collection of debugging tools, not to be
  included in production code.  NOTE: These tools are functional, but
  are not being developed or supported. They have been mainly superceded
  by the tools in the Enthought Developer Tool Suite.
* etsdevtools.developer: A collection of utilities, designed to ease
  the development and debugging of Traits-based programs. They can be
  used as plug-ins to your Envisage application while you are
  developing it, and then removed when you are ready to release it.
* etsdevtools.endo: A Traits-aware tool for processing API
  documentation of Python code. It extracts not only docstrings, but
  also plain comments that immediately precede variable assignments
  (both module-scope variables and class attributes).

%prep 
%setup -q -n %{module}-%{version}

%build

%__python setup.py build
pushd docs
make html
popd

%install
%__rm -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt *.rst examples/ docs/build/html

