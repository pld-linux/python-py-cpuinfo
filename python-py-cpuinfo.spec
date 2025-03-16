#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Get CPU info with pure Python 2
Summary(pl.UTF-8):	Pobieranie informacji o CPU w czystym Pythonie 2
Name:		python-py-cpuinfo
Version:	8.0.0
Release:	8
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/py-cpuinfo/
Source0:	https://files.pythonhosted.org/packages/source/p/py-cpuinfo/py-cpuinfo-%{version}.tar.gz
# Source0-md5:	cf3bec89839a0bf18c5f6c1c18aaee10
URL:		https://github.com/workhorsy/py-cpuinfo
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Py-cpuinfo gets CPU info with pure Python. Py-cpuinfo should work
without any extra programs or libraries, beyond what your OS provides.
It does not require any compilation (C/C++, assembly, et cetera) to
use. It works with Python 2 and 3.

%description -l pl.UTF-8
Py-cpuinfo pobiera informacje o CPU z poziomu czystego Pythona.
Powinien działać bez dodatkowych programów czy bibliotek, tylko z tym,
co udostępnia system operacyjny. Nie wymaga żadnej kompilacji (C/C++,
asemblera itp.). Działa z Pythonem 2 i 3.

%prep
%setup -q -n py-cpuinfo-%{version}

%build
%py_build

%if %{with tests}
%{__python} test_suite.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/cpuinfo{,-py2}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.rst
%attr(755,root,root) %{_bindir}/cpuinfo-py2
%{py_sitescriptdir}/cpuinfo
%{py_sitescriptdir}/py_cpuinfo-%{version}-py*.egg-info
