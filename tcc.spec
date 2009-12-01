Summary:	Tiny C Compiler
Name:		tcc
Version:	0.9.25
Release:	%mkrel 1
License:	GPL
Group:		Development/C
URL:		http://bellard.org/tcc/
Source0:	http://download.savannah.nongnu.org/releases/tinycc/%{name}-%{version}.tar.bz2
Patch0:		tcc-0.9.23-DESTDIR.diff
# http://www.mail-archive.com/tinycc-devel%40nongnu.org/msg00297.html
Patch1:		tcc-0.9.23-binutils_fix.diff
Patch2:		tcc_0.9.23-2.diff
ExclusiveArch:	%{ix86}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Tiny C Compiler - C Scripting Everywhere - The Smallest ANSI C 
compiler

%prep

%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1

# path fix
find -type f | xargs perl -pi -e "s|^#\!/usr/local/bin|#\!%{_bindir}|g"

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
%{_libdir}/*.a
%{_includedir}/*.h
%{_mandir}/man1/tcc.1*


