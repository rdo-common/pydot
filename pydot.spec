%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:		pydot
Version:	1.0.2
Release:	5%{?dist}
License:	MIT
Group:		System Environment/Libraries
Summary:	Python interface to Graphviz's Dot language
URL:		http://code.google.com/p/pydot/
Source0:	http://pydot.googlecode.com/files/pydot-%{version}.tar.gz
# Fix bugzilla 481540, sent upstream in Issue 23
# http://code.google.com/p/pydot/issues/detail?id=23
Patch0:		pydot-need-quote.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	pyparsing python-devel
Requires:	graphviz, pyparsing
BuildArch:	noarch

%description
An interface for creating both directed and non directed graphs from Python. 
Currently all attributes implemented in the Dot language are supported (up 
to Graphviz 2.16).

Output can be inlined in Postscript into interactive scientific environments 
like TeXmacs, or output in any of the format's supported by the Graphviz 
tools dot, neato, twopi.

%prep
%setup -q
%patch0 -p1 -b .need-quote

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root=$RPM_BUILD_ROOT

# Why would you do this? :/
rm -rf $RPM_BUILD_ROOT%{_prefix}/ChangeLog $RPM_BUILD_ROOT%{_prefix}/LICENSE $RPM_BUILD_ROOT%{_prefix}/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE ChangeLog PKG-INFO README
%{python_sitelib}/*

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul  6 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.2-4
- fix pydot crash with accented character (bugzilla 481540)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.2-2
- Rebuild for Python 2.6

* Fri Sep 12 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.2-1
- update to 1.0.2

* Thu Dec 14 2006 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.9.10-5
- Rebuild for new Python
- Add BR: python-devel

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.10-4
- bump for fc6

* Thu Oct  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.10-3
- We really do need pyparsing as a BR

* Thu Oct  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.10-2
- change BR to R for graphviz, pyparsing

* Sat Sep 17 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.10-1
- initial package for Fedora Extras
