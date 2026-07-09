%global type binary
%global utype manual

Name:           glibc
Version:        2.43
Release:        1%{?dist}
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Summary:        GNU C Library
URL:            https://www.gnu.org/software/libc

Source0:        https://ftp.gnu.org/gnu/libc/glibc-%{version}.tar.gz
Source1:        https://varclen.nohi.click/Packages/Main/raw/branch/main/Packages/glibc/locale.gen.txt
Source2:        https://varclen.nohi.click/Packages/Main/raw/branch/main/Packages/glibc/locale-gen
Source3:        https://varclen.nohi.click/Packages/Main/raw/branch/main/Packages/glibc/lib32-glibc.conf
Source4:        https://varclen.nohi.click/Packages/Main/raw/branch/main/Packages/glibc/sdt.h
Source5:        https://varclen.nohi.click/Packages/Main/raw/branch/main/Packages/glibc/sdt-config.h

BuildRequires:  gd
BuildRequires:  python

%ifarch x86_64
BuildRequires:  lib32-gcc-libs
%endif

# -------- GLIBC --------

Requires:       linux-api-headers >= 4.10
Requires:       tzdata
#Not yet done
#Requires:       filesystem

Suggests:       gd
Suggests:       perl

%post
if [ $1 -eq 2 ]; then
  locale-gen

  ldconfig -r .

  iconvconfig
fi

# -------- LIB32-GLIBC --------

%package -n lib32-glibc
Summary:        GNU C Library (32-bit)

Requires:       glibc = %{version}

%post
iconvconfig --nostdlib -o /usr/lib32/gconv/gconv-modules.cache /usr/lib32/gconv

%postun
rm -f /usr/lib32/gconv/gconv-modules.cache

# -------- GLIBC-LOCALES --------

%package locales
Summary:        Pregenerated locales for GNU C Library

Requires:       glibc = %{version}