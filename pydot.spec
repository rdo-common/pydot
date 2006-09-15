%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:		pydot
Version:	0.9.10
Release:	4%{?dist}
License:	MIT
Group:		System Environment/Libraries
Summary:	Python interface to Graphviz's Dot language
URL:		http://dkbza.org/pydot.html
Source0:	http://dkbza.org/data/pydot-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	pyparsing
Requires:	graphviz, pyparsing
BuildArch:	noarch

%description
An interface for creating both directed and non directed graphs from Python. 
Currently all attributes implemented in the Dot language are supported (up 
to Graphviz 1.16).

Output can be inlined in Postscript into interactive scientific environments 
like TeXmacs, or output in any of the format's supported by the Graphviz 
tools dot, neato, twopi.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE ChangeLog PKG-INFO README
%{python_sitelib}/*

%changelog
* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.10-4
- bump for fc6

* Thu Oct  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.10-3
- We really do need pyparsing as a BR

* Thu Oct  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.10-2
- change BR to R for graphviz, pyparsing

* Sat Sep 17 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.10-1
- initial package for Fedora Extras
