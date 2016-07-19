Name:		pydot
Version:	1.0.28
Release:	12%{?dist}
License:	MIT
Group:		System Environment/Libraries
Summary:	Python interface to Graphviz's Dot language
URL:		http://code.google.com/p/pydot/
Source0:	http://pydot.googlecode.com/files/pydot-%{version}.tar.gz
Patch0:		https://anonscm.debian.org/cgit/python-modules/packages/pydot.git/plain/debian/patches/0002-support-python3.patch
BuildRequires:	pyparsing python3-pyparsing python2-devel python3-devel
BuildArch:	noarch

%description
An interface for creating both directed and non directed graphs from Python. 
Currently all attributes implemented in the Dot language are supported (up 
to Graphviz 2.16).

Output can be inlined in Postscript into interactive scientific environments 
like TeXmacs, or output in any of the format's supported by the Graphviz 
tools dot, neato, twopi.

%package -n python2-pydot
Summary:	Python2 interface to Graphviz's Dot language
Requires:	graphviz, pyparsing
%{?python_provide:%python_provide python2-pydot}
Obsoletes:	pydot < %{version}-%{release}

%description -n python2-pydot
An interface for creating both directed and non directed graphs from Python. 
Currently all attributes implemented in the Dot language are supported (up 
to Graphviz 2.16).

Output can be inlined in Postscript into interactive scientific environments 
like TeXmacs, or output in any of the format's supported by the Graphviz 
tools dot, neato, twopi.

%package -n python3-pydot
Summary:	Python3 interface to Graphviz's Dot language
Requires:	graphviz, python3-pyparsing
Provides:	pydot = %{version}-%{release}
%{?python_provide:%python_provide python3-pydot}

%description -n python3-pydot
An interface for creating both directed and non directed graphs from Python. 
Currently all attributes implemented in the Dot language are supported (up 
to Graphviz 2.16).

Output can be inlined in Postscript into interactive scientific environments 
like TeXmacs, or output in any of the format's supported by the Graphviz 
tools dot, neato, twopi.

%prep
%setup -q
%patch0 -p1 -b .python3

%build
%py2_build
%py3_build

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
%py2_install
%py3_install

# Why would you do this? :/
rm -rf $RPM_BUILD_ROOT%{_prefix}/LICENSE $RPM_BUILD_ROOT%{_prefix}/README

%files -n python2-pydot
%doc PKG-INFO README
%license LICENSE
%{python2_sitelib}/*

%files -n python3-pydot
%doc PKG-INFO README
%license LICENSE
%{python3_sitelib}/*

%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.28-12
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Apr 15 2016 Tom Callaway <spot@fedoraproject.org> - 1.0.28-11
- use debian's python3 fix (tested against bz1312815)

* Fri Apr  8 2016 Tom Callaway <spot@fedoraproject.org> - 1.0.28-10
- properly obsolete old "pydot" packages (bz1323980)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Tom Callaway <spot@fedoraproject.org> - 1.0.28-8
- python 3 support

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec  9 2013 Tom Callaway <spot@fedoraproject.org> - 1.0.28-5
- fix for pyparsing2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar  2 2012 Tom Callaway <spot@fedoraproject.org> - 1.0.28-1
- update to 1.0.28

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Tom Callaway <spot@fedoraproject.org> - 1.0.25-2
- apply fix for pebl relating to catching AttributeError, thanks to Thomas Spura

* Thu Apr 21 2011 Tom Callaway <spot@fedoraproject.org> - 1.0.25-1
- update to 1.0.25

* Thu Mar  3 2011 Tom Callaway <spot@fedoraproject.org> - 1.0.23-1
- update to 1.0.23

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan  4 2011 Tom Callaway <spot@fedoraproject.org> - 1.0.4-1
- update to 1.0.4

* Wed Nov  3 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.3-1
- update to 1.0.3

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 31 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.2-6
- somehow, the egg info didn't make it into the rebuild...

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
