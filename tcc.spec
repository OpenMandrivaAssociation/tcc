Summary:	Tiny C Compiler
Name:		tcc
Version:	0.9.25
Release:	%mkrel 1
License:	GPL
Group:		Development/C
URL:		http://bellard.org/tcc/
Source0:	http://download.savannah.nongnu.org/releases/tinycc/%{name}-%{version}.tar.bz2
ExclusiveArch:	%{ix86}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Tiny C Compiler - C Scripting Everywhere - The Smallest ANSI C 
compiler

%prep

%setup -q

# (tv) use DESTDIR:
perl -pi -e 's!(\$\((bin|doc|include|lib|man|tcc)dir)!\$(DESTDIR)\1!' Makefile

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


