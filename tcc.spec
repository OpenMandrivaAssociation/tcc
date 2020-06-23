%define snapshot 20200623

Summary:	Tiny C Compiler
Name:		tcc
Version:	0.9.28
Release:	%{?snapshot:0.%{snapshot}.}1
License:	GPL
Group:		Development/C
URL:		https://repo.or.cz/w/tinycc.git
Source0:	http://download.savannah.nongnu.org/releases/tinycc/%{name}-%{version}%{?snapshot:-%{snapshot}}.tar.zst
BuildRequires:	texinfo
BuildRequires:	make

%description
Tiny C Compiler - C Scripting Everywhere - The Smallest ANSI C 
compiler

%prep
%autosetup -p1

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
# Looks and acts a lot like autoconf, but isn't
mkdir build
cd build
../configure \
	--cc=%{__cc} \
	--extra-cflags="%{optflags}" \
	--extra-ldflags="%{optflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--triplet=%{_target_platform} \
	--libpaths="%{_libdir}:/%{_lib}:%{_prefix}/local/%{_lib}" \
	--crtprefix=%{_libdir}

sed -i -e 's,\$(DESTDIR),,g' config.mak
sed -i -e 's,\$(infodir),$(DESTDIR)$(infodir),g' Makefile

%make_build

%install
%make_install DESTDIR="%{buildroot}" -C build

%files
%defattr(-, root, root)
%{_bindir}/tcc
%{_includedir}/libtcc.h
%{_libdir}/libtcc.a
%{_libdir}/tcc
%doc %{_docdir}/tcc-doc.html
%{_infodir}/tcc-doc.info*
%{_mandir}/man1/tcc.1*
