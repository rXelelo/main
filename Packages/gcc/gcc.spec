%global type binary
%global utype manual

Name:           gcc
Version:        16.1.0
Release:        1%{?dist}
License:        GPLv3
Summary:        The GNU Compiler Collection - C and C++ frontends
URL:            https://gcc.gnu.org
BuildArch:      x86_64

Source0:        https://ftp.gnu.org/gnu/gcc/gcc-%{Version}/gcc-%{Version}.tar.gz

BuildRequires:  binutils
BuildRequires:  doxygen
BuildRequires:  gcc-ada
BuildRequires:  gcc-d
BuildRequires:  lib32-gcc-libs
BuildRequires:  lib32-glibc
BuildRequires:  libisl
BuildRequires:  libmpc
BuildRequires:  python
BuildRequires:  rust
BuildRequires:  zstd

Requires:       libasan = %{Version}-%{Release}
Requires:       libgcc = %{Version}-%{Release}
Requires:       libhwasan = %{Version}-%{Release}
Requires:       liblsan = %{Version}-%{Release}
Requires:       libstdc++ = %{Version}-%{Release}
Requires:       libubsan = %{Version}-%{Release}
Requires:       binutils >= 2.28
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

Recommends:     lib32-gcc-libs

Provides:       %{Name}-multilib
Obsoletes:      %{Name}-multilib

# -------- GCC-ADA --------

%package ada
Summary:        Ada front-end for GCC (GNAT)

Requires:       gcc = %{Version}-%{Release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libgcc
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

Provides:       %{Name}-multilib
Obsoletes:      %{Name}-multilib

# -------- GCC-D --------

%package d
Summary:        D frontend for GCC

Requires:       gcc = %{Version}-%{Release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libgphobos
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

Provides:       gdc
Obsoletes:      gdc

# -------- GCC-FORTRAN --------

%package fortran
Summary:        Fortran front-end for GCC

Requires:       gcc = %{Version}-%{Release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libgfortran
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

Provides:       %{Name}-multilib
Obsoletes:      %{Name}-multilib

# -------- GCC-GCOBOL --------

%package gcobol
Summary:        Cobol frontend for GCC

Requires:       gcc = %{Version}-%{Release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libgcobol
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

# -------- GCC-GO --------

%package go
Summary:        Go front-end for GCC

Requires:       gcc = %{Version}-%{Release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libgo
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

Provides:       %{Name}-multilib
Provides:       go = 1.17
Obsoletes:      %{Name}-multilib
Conflicts:      go

# -------- GCC-LIBs --------

%package libs
Summary:        Runtime libraries shipped by GCC

Requires:       gcc = %{Version}-%{Release}
Requires:       libasan
Requires:       libatomic
Requires:       libgcc
Requires:       libgfortran
Requires:       libgomp
Requires:       libhwasan
Requires:       liblsan
Requires:       libobjc
Requires:       libquadmath
Requires:       libstdc++
Requires:       libtsan
Requires:       libubsan

Provides:       %{Name}-multilib

# -------- GCC-M2 --------

%package m2
Summary:        Modula-2 frontend for GCC

Requires:       gcc = %{Version}-%{Release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libgm2
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

# -------- GCC-OBJC --------

%package objc
Summary:        Objective-C front-end for GCC

Requires:       gcc = %{Version}-%{Release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libobjc
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

Provides:       %{Name}-multilib
Obsoletes:      %{Name}-multilib

# -------- GCC-RUST --------

%package rust
Summary:        Rust frontend for GCC

Requires:       gcc = %{Version}-%{Release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

# -------- LIB32-GCC-LIBs --------

%package -n lib32-gcc-libs
Summary:        32-bit runtime libraries shipped by GCC

Requires:       lib32-glibc >= 2.27

Provides:       libasan.so
Provides:       libatomic.so
Provides:       libgdruntime.so
Provides:       libgfortran.so
Provides:       libgo.so
Provides:       libgomp.so
Provides:       libgphobos.so
Provides:       libitm.so
Provides:       libobjc.so
Provides:       libquadmath.so
Provides:       libubsan.so

# -------- LIBASAN --------

%package -n libasan
Summary:        Address Sanitizer runtime library shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc
Requires:       libstdc++

Provides:       libasan.so

# -------- LIBATOMIC --------

%package -n libatomic
Summary:        GNU Atomic library shipped by GCC

Requires:       glibc >= 2.27

Provides:       libatomic.so

# -------- LIBGCC --------

%package -n libgcc
Summary:        Low-level runtime library shipped by GCC

Requires:       glibc >= 2.27

Provides:       libgcc_s.so

# -------- LIBGCCJIT --------

%package -n libgccjit
Summary:        Just-In-Time Compilation with GCC backend

Requires:       gcc = %{Version}-%{Release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

Provides:       libgccjit.so

# -------- LIBGCOBOL --------

%package -n libgcobol
Summary:        Cobol runtime libraries shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc
Requires:       libstdc++

Provides:       libgcobol.so

# -------- LIBGFORTRAN --------

%package -n libgfortran
Summary:        Runtime libraries shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc

Provides:       libgfortran.so

# -------- LIBGM2 --------

%package -n libgm2
Summary:        Modula-2 runtime libraries shipped by GCC

Requires:       glibc >= 2.27

Provides:       libm2cor.so
Provides:       libm2iso.so
Provides:       libm2log.so
Provides:       libm2min.so
Provides:       libm2pim.so

# -------- LIBGO --------

%package -n libgo
Summary:        Go runtime libraries shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc

Provides:       libgo.so

# -------- LIBGOMP --------

%package -n libgomp
Summary:        OpenMP library shipped by GCC

Requires:       glibc >= 2.27

Provides:       libgomp.so

# -------- LIBGPHOBOS --------

%package -n libgphobos
Summary:        D runtime libraries shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc

Provides:       libgdruntime.so
Provides:       libgphobos.so

# -------- LIBHWASAN --------

%package -n libhwasan
Summary:        Hardware-assisted Address Sanitizer runtime library shipped by GCCs

Requires:       glibc >= 2.27
Requires:       libgcc
Requires:       libstdc++

Provides:       libhwasan.so

# -------- LIBITM --------

%package -n libitm
Summary:        GNU Transactional Memory library shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc

Provides:       libitm.so

# -------- LIBLSAN --------

%package -n liblsan
Summary:        Leak Sanitizer runtime library shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc
Requires:       libstdc++

Provides:       liblsan.so

# -------- LIBOBJC --------

%package -n libobjc
Summary:        Ojective-C runtime libraries shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc

Provides:       libobjc.so

# -------- LIBQUADMATH --------

%package -n libquadmath
Summary:        GCC __float128 library
Requires:       glibc >= 2.27
Requires:       libgcc

Provides:       libquadmath.so

# -------- LIBSTC++ --------

%package -n libstdc++
Summary:        C++ runtime libraries shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc

Provides:       libstc++.so

# -------- LIBTSAN --------

%package -n libtsan
Summary:        Thread Sanitizer runtime library shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc
Requires:       libstdc++

Provides:       libtsan.so

# -------- LIBUBSAN --------

%package -n libubsan
Summary:        Undefined Behavior Sanitizer runtime library shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc
Requires:       libstdc++

Provides:       libubsan.so 

# -------- LTO-DUMP --------

%package -n lto-dump
Summary:        Dump link time optimization object files

Requires:       gcc = %{Version}-%{Release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd


%prep
%setup -q

%build

