Summary:	Tiny C Compiler
Name:		tcc
Version:	0.9.25
Release:	%mkrel 2
License:	GPL
Group:		Development/C
URL:		http://bellard.org/tcc/
Source0:	http://download.savannah.nongnu.org/releases/tinycc/%{name}-%{version}.tar.bz2
# (tv) fix tccdir on x86_64:
Patch3:		tcc-0.9.25-tccdif.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Tiny C Compiler - C Scripting Everywhere - The Smallest ANSI C 
compiler

%prep

%setup -q
%patch3 -p0

# (tv) use DESTDIR:
perl -pi -e 's!(\$\((bin|doc|include|lib|man|tcc)dir)!\$(DESTDIR)\1!' Makefile

# path fix
find -type f | xargs perl -pi -e "s|^#\!/usr/local/bin|#\!%{_bindir}|g"

# (tv) fix path on x86_64:
%ifarch x86_64
perl -pi -e 's!/usr/lib!/usr/lib64!' libtcc.c tcc.h
%endif

# fix attribs
chmod 644 examples/*

%build

%configure2_5x

make CFLAGS="%{optflags}"
#make test

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_includedir}
install -d %{buildroot}%{_mandir}/man1

%makeinstall_std


# cleanup
rm -rf %{buildroot}%{_docdir}/tcc

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc Changelog README TODO *.html examples
%defattr(-,root,root)
%{_bindir}/tcc
%{_libdir}/tcc/include/*.h
%{_libdir}/tcc/*.a
%ifarch %{ix86}
%{_libdir}/tcc/*.o
%endif
%{_libdir}/*.a
%{_includedir}/*.h
%{_mandir}/man1/tcc.1*




%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.25-2mdv2011.0
+ Revision: 615165
- the mass rebuild of 2010.1 packages

* Tue Dec 01 2009 Thierry Vignaud <tv@mandriva.org> 0.9.25-1mdv2010.1
+ Revision: 472432
- adjust file list for both x86_64 and ia32
- enable build on x86_64 and fix path (patch 3)
- drop patches 1 & 2 (uneeded)
- replace patch 0 by a one-liner perl command
- fix installing
- use %%configure2_5x
- adjust file list
- new release
- new URL
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.9.23-6mdv2009.0
+ Revision: 242855
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 10 2007 Pascal Terjan <pterjan@mandriva.org> 0.9.23-4mdv2008.0
+ Revision: 61306
- Rebuild to sync x86_64


* Mon Feb 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.9.23-3mdv2007.0
+ Revision: 122783
- rebuild in order to get the same extension on x86_64
- Import tcc

* Mon Jun 05 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.23-2mdv2007.0
- fix #22862 (P1)
- added debian patches

* Fri Jun 02 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.23-1mdv2007.0
- 0.9.23

* Wed May 24 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.9.22-2mdk
- use %%mkrel 2
- rebuild with new toolchain

* Fri May 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.22-1mdk
- 0.9.22
- added P0 by Paul Furber to make is somewhat work under x86_64

* Sat Apr 24 2004 Michael Scherer <misc@mandrake.org> 0.9.20-1mdk
- New release 0.9.20

