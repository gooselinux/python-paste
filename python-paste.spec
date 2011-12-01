%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-paste
Version:        1.7.4
Release:        1%{?dist}
Summary:        Tools for using a Web Server Gateway Interface stack
Group:          System Environment/Libraries
# Most of the code is MIT
# paste/exceptions/collector.py is ZPLv2.0
# paste/evalexception/mochikit/MochiKit.js AFL or MIT
# paste/lint.py MIT or Apache v2
# subproccess24.py PySourceColor.py, Python
# doctest24.py, Public Domain
License: MIT and ZPLv2.0 and Python and Public Domain and (AFL or MIT) and (MIT or ASL 2.0)
URL:            http://pythonpaste.org
Source0:        http://cheeseshop.python.org/packages/source/P/Paste/Paste-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel

Requires:       pyOpenSSL


%description
These provide several pieces of "middleware" (or filters) that can be nested
to build web applications.  Each piece of middleware uses the WSGI (PEP 333)
interface, and should be compatible with other middleware based on those
interfaces.


%prep
%setup -q -n Paste-%{version}

# Strip #! lines that make these seem like scripts
%{__sed} -i -e '/^#!.*/,1 d' paste/util/scgiserver.py paste/debug/doctest_webapp.py

# clean docs directory
pushd docs
rm StyleGuide.txt
popd


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc docs/*
%{python_sitelib}/*


%changelog
* Wed Jul 14 2010 David Malcolm <dmalcolm@redhat.com> - 1.7.4-1
- rebase to 1.7.4; drop SSL patch (present in that tarball)
- fix license tag
- add requirement on pyOpenSSL
- specfile cleanups
Resolves: rhbz#613191

* Tue May  4 2010 David Malcolm <dmalcolm@redhat.com> - 1.7.2-5
- add patch from http://trac.pythonpaste.org/pythonpaste/ticket/314 to fix SSL
support on Python 2.6 (rhbz:588546)

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.7.2-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Kyle VanderBeek <kylev@kylev.com> - 1.7.2-3
- Package formerly ghost'ed .pyo files
- Update to current python package methods

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 1.7.2-1
- Update to 1.7.2

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.7.1-2
- Rebuild for Python 2.6

* Sat Jun 14 2008 Luke Macken <lmacken@redhat.com> - 1.7.1-1
- Update to Paste 1.7.1

* Thu Feb 28 2008 Luke Macken <lmacken@redhat.com> - 1.6-1
- Update to 1.6

* Wed Oct  3 2007 Luke Macken <lmacken@redhat.com> - 1.4.2-1
- 1.4.2

* Sun Sep  2 2007 Luke Macken <lmacken@redhat.com> - 1.4-2
- Update for python-setuptools changes in rawhide

* Sat Jul  8 2007 Luke Macken <lmacken@redhat.com> - 1.4-1
- 1.4

* Sat Mar  3 2007 Luke Macken <lmacken@redhat.com> - 1.2.1-1
- 1.2.1

* Sat Dec  9 2006 Luke Macken <lmacken@redhat.com> - 1.0-2
- Add python-devel to BuildRequires
- 1.0

* Sun Sep 17 2006 Luke Macken <lmacken@redhat.com> - 0.9.8.1-1
- 0.9.8.1

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> - 0.9.3-5
- Rebuild for FC6

* Wed Jul 19 2006 Luke Macken <lmacken@redhat.com> - 0.9.3-4
- Use a smarter shebang removal expression

* Wed Jul 19 2006 Luke Macken <lmacken@redhat.com> - 0.9.3-3
- Fix doc inclusion

* Sat Jul 15 2006 Luke Macken <lmacken@redhat.com> - 0.9.3-2
- Clean up docs directory
- Remove shebang from from non-executable scripts
- Use consistent build root variables

* Mon Jul 10 2006 Luke Macken <lmacken@redhat.com> - 0.9.3-1
- Initial package
