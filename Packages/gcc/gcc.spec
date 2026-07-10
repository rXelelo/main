%global type binary
%global utype manual

Name:           gcc
Version:        16.1.0
Release:        1%{?dist}
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1) AND (GPL-3.0-or-later WITH Texinfo-exception) AND (LGPL-2.1-or-later WITH GCC-exception-2.0) AND (GPL-2.0-or-later WITH GCC-exception-2.0) AND BSD-3-Clause AND MIT AND Apache-2.0
Summary:        The GNU Compiler Collection - C and C++ frontends
URL:            https://gcc.gnu.org

Source0:        https://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.gz
Source1:        https://varclen.nohi.click/Packages/Main/raw/branch/main/Packages/gcc/c89
Source2:        https://varclen.nohi.click/Packages/Main/raw/branch/main/Packages/gcc/c99

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

# -------- GCC (base) --------

Requires:       libasan = %{version}-%{release}
Requires:       libgcc = %{version}-%{release}
Requires:       libhwasan = %{version}-%{release}
Requires:       liblsan = %{version}-%{release}
Requires:       libstdc++ = %{version}-%{release}
Requires:       libubsan = %{version}-%{release}
Requires:       binutils >= 2.28
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

Suggests:       lib32-gcc-libs

Obsoletes:      %{name}-multilib

%description
The gcc package contains the GNU Compiler Collection C and C++
front ends, needed to compile C and C++ source code into
executables or libraries.

# -------- GCC-ADA --------

%package ada
Summary:        Ada front-end for GCC (GNAT)

Requires:       gcc = %{version}-%{release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libgcc
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

Obsoletes:      %{name}-ada-multilib

%description ada
The GNAT Ada 83/95/2005/2012 front end for GCC, providing gnat,
gnatmake, gnatbind, and related tools.

# -------- GCC-D --------

%package d
Summary:        D frontend for GCC

Requires:       gcc = %{version}-%{release}
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

%description d
The D programming language front end for GCC (gdc).

# -------- GCC-FORTRAN --------

%package fortran
Summary:        Fortran front-end for GCC

Requires:       gcc = %{version}-%{release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libgfortran
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

Provides:       %{name}-fortran-multilib
Obsoletes:      %{name}-fortran-multilib

%description fortran
The Fortran front end for GCC (gfortran).

# -------- GCC-GCOBOL --------

%package gcobol
Summary:        Cobol frontend for GCC

Requires:       gcc = %{version}-%{release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libgcobol
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

%description gcobol
The COBOL front end for GCC (gcobol / gcobc).

# -------- GCC-GO --------

%package go
Summary:        Go front-end for GCC

Requires:       gcc = %{version}-%{release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libgo
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

Provides:       %{name}-go-multilib
Provides:       go = 1.17
Obsoletes:      %{name}-go-multilib
Conflicts:      go

%description go
The Go front end for GCC (gccgo).

# -------- GCC-LIBs --------

%package libs
Summary:        Runtime libraries shipped by GCC

Requires:       gcc = %{version}-%{release}
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

Provides:       %{name}-libs-multilib

%description libs
Metapackage pulling in the full set of GCC runtime libraries.

# -------- GCC-M2 --------

%package m2
Summary:        Modula-2 frontend for GCC

Requires:       gcc = %{version}-%{release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libgm2
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

%description m2
The Modula-2 front end for GCC (gm2).

# -------- GCC-OBJC --------

%package objc
Summary:        Objective-C front-end for GCC

Requires:       gcc = %{version}-%{release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libobjc
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

Provides:       %{name}-objc-multilib
Obsoletes:      %{name}-objc-multilib

%description objc
The Objective-C front end for GCC.

# -------- GCC-RUST --------

%package rust
Summary:        Rust frontend for GCC

Requires:       gcc = %{version}-%{release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

%description rust
The Rust front end for GCC (gccrs).

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

%description -n lib32-gcc-libs
32-bit (multilib) versions of the GCC runtime libraries, for
running/compiling 32-bit binaries on a 64-bit system.

# -------- LIBASAN --------

%package -n libasan
Summary:        Address Sanitizer runtime library shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc
Requires:       libstdc++

Provides:       libasan.so

%description -n libasan
The AddressSanitizer (ASan) runtime library.

# -------- LIBATOMIC --------

%package -n libatomic
Summary:        GNU Atomic library shipped by GCC

Requires:       glibc >= 2.27

Provides:       libatomic.so

%description -n libatomic
The GNU Atomic runtime library.

# -------- LIBGCC --------

%package -n libgcc
Summary:        Low-level runtime library shipped by GCC

Requires:       glibc >= 2.27

Provides:       libgcc_s.so

%description -n libgcc
The low-level GCC support runtime library.

# -------- LIBGCCJIT --------

%package -n libgccjit
Summary:        Just-In-Time Compilation with GCC backend

Requires:       gcc = %{version}-%{release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

Provides:       libgccjit.so

%description -n libgccjit
Embeddable just-in-time compilation library backed by GCC.

# -------- LIBGCOBOL --------

%package -n libgcobol
Summary:        Cobol runtime libraries shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc
Requires:       libstdc++

Provides:       libgcobol.so

%description -n libgcobol
Runtime library for GCC-compiled COBOL programs.

# -------- LIBGFORTRAN --------

%package -n libgfortran
Summary:        Runtime libraries shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc

Provides:       libgfortran.so

%description -n libgfortran
Runtime library for GCC-compiled Fortran programs.

# -------- LIBGM2 --------

%package -n libgm2
Summary:        Modula-2 runtime libraries shipped by GCC

Requires:       glibc >= 2.27

Provides:       libm2cor.so
Provides:       libm2iso.so
Provides:       libm2log.so
Provides:       libm2min.so
Provides:       libm2pim.so

%description -n libgm2
Runtime libraries for GCC-compiled Modula-2 programs.

# -------- LIBGO --------

%package -n libgo
Summary:        Go runtime libraries shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc

Provides:       libgo.so

%description -n libgo
Runtime library for GCC-compiled Go programs.

# -------- LIBGOMP --------

%package -n libgomp
Summary:        OpenMP library shipped by GCC

Requires:       glibc >= 2.27

Provides:       libgomp.so

%description -n libgomp
The GNU OpenMP runtime library.

# -------- LIBGPHOBOS --------

%package -n libgphobos
Summary:        D runtime libraries shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc

Provides:       libgdruntime.so
Provides:       libgphobos.so

%description -n libgphobos
Runtime libraries for GCC-compiled D programs.

# -------- LIBHWASAN --------

%package -n libhwasan
Summary:        Hardware-assisted Address Sanitizer runtime library shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc
Requires:       libstdc++

Provides:       libhwasan.so

%description -n libhwasan
The Hardware-assisted AddressSanitizer (HWASan) runtime library.

# -------- LIBITM --------

%package -n libitm
Summary:        GNU Transactional Memory library shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc

Provides:       libitm.so

%description -n libitm
The GNU Transactional Memory runtime library.

# -------- LIBLSAN --------

%package -n liblsan
Summary:        Leak Sanitizer runtime library shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc
Requires:       libstdc++

Provides:       liblsan.so

%description -n liblsan
The LeakSanitizer (LSan) runtime library.

# -------- LIBOBJC --------

%package -n libobjc
Summary:        Objective-C runtime libraries shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc

Provides:       libobjc.so

%description -n libobjc
Runtime library for GCC-compiled Objective-C programs.

# -------- LIBQUADMATH --------

%package -n libquadmath
Summary:        GCC __float128 library
Requires:       glibc >= 2.27
Requires:       libgcc

Provides:       libquadmath.so

%description -n libquadmath
The GCC quad-precision math (__float128) runtime library.

# -------- LIBSTDC++ --------

%package -n libstdc++
Summary:        C++ runtime libraries shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc

Provides:       libstdc++.so

%description -n libstdc++
The GNU Standard C++ Library runtime.

# -------- LIBTSAN --------

%package -n libtsan
Summary:        Thread Sanitizer runtime library shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc
Requires:       libstdc++

Provides:       libtsan.so

%description -n libtsan
The ThreadSanitizer (TSan) runtime library.

# -------- LIBUBSAN --------

%package -n libubsan
Summary:        Undefined Behavior Sanitizer runtime library shipped by GCC

Requires:       glibc >= 2.27
Requires:       libgcc
Requires:       libstdc++

Provides:       libubsan.so

%description -n libubsan
The UndefinedBehaviorSanitizer (UBSan) runtime library.

# -------- LTO-DUMP --------

%package -n lto-dump
Summary:        Dump link time optimization object files

Requires:       gcc = %{version}-%{release}
Requires:       glibc >= 2.27
Requires:       gmp
Requires:       libisl.so
Requires:       libmpc
Requires:       mpfr
Requires:       zlib
Requires:       zstd

%description -n lto-dump
Diagnostic tool for dumping LTO (link time optimization) object
file contents.


%prep
%setup -q
# Set up build environments relative to the source tree root
mkdir -p ../gcc-build ../libgccjit-build


%build
CONFFLAGS="
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libexecdir} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir} \
    --with-bugurl=https://varclen.nohi.click/Packages/Main/issues \
    --with-build-config=bootstrap-lto \
    --with-gcc-major-version-only \
    --with-linker-hash-style=gnu \
    --with-system-zlib \
    --enable-cet=auto \
    --enable-checking=release \
    --enable-clocale=gnu \
    --enable-default-pie \
    --enable-default-ssp \
    --enable-gnu-indirect-function \
    --enable-gnu-unique-object \
    --enable-libstdcxx-backtrace \
    --enable-link-serialization=1 \
    --enable-linker-build-id \
    --enable-lto \
    --enable-multilib \
    --enable-plugin \
    --enable-shared \
    --enable-threads=posix \
    --disable-fixincludes \
    --disable-libssp \
    --disable-libstdcxx-pch \
    --disable-werror
"

CFLAGS="${CFLAGS/-Werror=format-security/}"
CXXFLAGS="${CXXFLAGS/-Werror=format-security/}"
export CFLAGS CXXFLAGS

# Navigate up and build from the explicit build tree sibling directories
cd ../gcc-build

../gcc-%{version}/configure \
    --enable-languages=ada,c,c++,d,fortran,go,lto,m2,objc,obj-c++,rust,cobol \
    --enable-bootstrap \
    $CONFFLAGS

make %{?_smp_mflags} -O \
    STAGE1_CFLAGS="-O2" \
    BOOT_CFLAGS="$CFLAGS" \
    BOOT_LDFLAGS="$LDFLAGS" \
    LDFLAGS_FOR_TARGET="$LDFLAGS" \
    bootstrap

make -O -C %{_target_platform}/libstdc++-v3/doc doc-man-doxygen

# --- STAGE 2: Build libgccjit separately ---
cd ../libgccjit-build

../gcc-%{version}/configure \
    --enable-languages=jit \
    --disable-bootstrap \
    --enable-host-shared \
    $CONFFLAGS

make %{?_smp_mflags} -O all-gcc

cp -a gcc/libgccjit.so* ../gcc-build/gcc/

%install
cd ../gcc-build
%make_install DESTDIR=%{buildroot}
cd ../libgccjit-build
install -m755 gcc/libgccjit.so* %{buildroot}%{_libdir}/ 2>/dev/null || :
cd -

# c89 / c99 convenience wrapper scripts (Source1/Source2)
install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}/c89
install -Dm755 %{SOURCE2} %{buildroot}%{_bindir}/c99

# Drop the generated libtool archives - not shipped downstream
find %{buildroot} -name '*.la' -delete

# Fix any stray info dir index (regenerated at post/postun via install-info)
rm -f %{buildroot}%{_infodir}/dir


%post
/sbin/install-info %{_infodir}/gcc.info %{_infodir}/dir || :
/sbin/install-info %{_infodir}/cpp.info %{_infodir}/dir || :

%preun
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/gcc.info %{_infodir}/dir || :
    /sbin/install-info --delete %{_infodir}/cpp.info %{_infodir}/dir || :
fi

%post ada
/sbin/install-info %{_infodir}/gnat-style.info %{_infodir}/dir || :
/sbin/install-info %{_infodir}/gnat_rm.info %{_infodir}/dir || :
/sbin/install-info %{_infodir}/gnat_ugn.info %{_infodir}/dir || :

%preun ada
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/gnat-style.info %{_infodir}/dir || :
    /sbin/install-info --delete %{_infodir}/gnat_rm.info %{_infodir}/dir || :
    /sbin/install-info --delete %{_infodir}/gnat_ugn.info %{_infodir}/dir || :
fi

%post d
/sbin/install-info %{_infodir}/gdc.info %{_infodir}/dir || :

%preun d
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/gdc.info %{_infodir}/dir || :
fi

%post fortran
/sbin/install-info %{_infodir}/gfortran.info %{_infodir}/dir || :

%preun fortran
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/gfortran.info %{_infodir}/dir || :
fi

%post go
/sbin/install-info %{_infodir}/gccgo.info %{_infodir}/dir || :

%preun go
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/gccgo.info %{_infodir}/dir || :
fi

%post m2
/sbin/install-info %{_infodir}/m2.info %{_infodir}/dir || :

%preun m2
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/m2.info %{_infodir}/dir || :
fi

%post -n libgccjit
/sbin/install-info %{_infodir}/libgccjit.info %{_infodir}/dir || :
/sbin/ldconfig

%preun -n libgccjit
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/libgccjit.info %{_infodir}/dir || :
fi

%postun -n libgccjit
/sbin/ldconfig

%post -n libgomp
/sbin/install-info %{_infodir}/libgomp.info %{_infodir}/dir || :
/sbin/ldconfig

%preun -n libgomp
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/libgomp.info %{_infodir}/dir || :
fi

%postun -n libgomp
/sbin/ldconfig

%post -n libitm
/sbin/install-info %{_infodir}/libitm.info %{_infodir}/dir || :
/sbin/ldconfig

%preun -n libitm
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/libitm.info %{_infodir}/dir || :
fi

%postun -n libitm
/sbin/ldconfig

%post -n libquadmath
/sbin/install-info %{_infodir}/libquadmath.info %{_infodir}/dir || :
/sbin/ldconfig

%preun -n libquadmath
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/libquadmath.info %{_infodir}/dir || :
fi

%postun -n libquadmath
/sbin/ldconfig

%post -n libgcc
/sbin/ldconfig

%postun -n libgcc
/sbin/ldconfig

%post -n libstdc++
/sbin/ldconfig

%postun -n libstdc++
/sbin/ldconfig

%post -n libasan
/sbin/ldconfig

%postun -n libasan
/sbin/ldconfig

%post -n libatomic
/sbin/ldconfig

%postun -n libatomic
/sbin/ldconfig

%post -n libhwasan
/sbin/ldconfig

%postun -n libhwasan
/sbin/ldconfig

%post -n liblsan
/sbin/ldconfig

%postun -n liblsan
/sbin/ldconfig

%post -n libtsan
/sbin/ldconfig

%postun -n libtsan
/sbin/ldconfig

%post -n libubsan
/sbin/ldconfig

%postun -n libubsan
/sbin/ldconfig

%post -n libgfortran
/sbin/ldconfig

%postun -n libgfortran
/sbin/ldconfig

%post -n libgo
/sbin/ldconfig

%postun -n libgo
/sbin/ldconfig

%post -n libgphobos
/sbin/ldconfig

%postun -n libgphobos
/sbin/ldconfig

%post -n libobjc
/sbin/ldconfig

%postun -n libobjc
/sbin/ldconfig

%post -n libgcobol
/sbin/ldconfig

%postun -n libgcobol
/sbin/ldconfig

%post -n libgm2
/sbin/ldconfig

%postun -n libgm2
/sbin/ldconfig

%post -n lib32-gcc-libs
/sbin/ldconfig

%postun -n lib32-gcc-libs
/sbin/ldconfig


# ==========================================================================
# %files sections
# 64-bit libs use %{_libdir} (-> /usr/lib64 on this filesystem layout).
# 32-bit libs are hardcoded to /usr/lib since %{_libdir} means 64-bit here.
# ==========================================================================

%files
%license gcc-%{version}/COPYING gcc-%{version}/COPYING3 gcc-%{version}/COPYING.RUNTIME
%doc gcc-%{version}/README
%{_bindir}/gcc
%{_bindir}/gcc-%{version}
%{_bindir}/%{_target_platform}-gcc
%{_bindir}/cpp
%{_bindir}/c89
%{_bindir}/c99
%{_mandir}/man1/gcc.1*
%{_mandir}/man1/cpp.1*
%{_infodir}/cpp.info*
%{_infodir}/gcc.info*

%files ada
%{_bindir}/gnat
%{_bindir}/gnatbind
%{_bindir}/gnatchop
%{_bindir}/gnatclean
%{_bindir}/gnatkr
%{_bindir}/gnatlink
%{_bindir}/gnatls
%{_bindir}/gnatmake
%{_bindir}/gnatname
%{_bindir}/gnatprep
%{_libdir}/ada_target_properties
%{_libdir}/32/ada_target_properties
%{_libdir}/adainclude/
%{_libdir}/adalib/
%{_libdir}/32/adainclude/
%{_libdir}/32/adalib/
%{_libdir}/gnat1
%{_infodir}/gnat-style.info*
%{_infodir}/gnat_rm.info*
%{_infodir}/gnat_ugn.info*

%files d
%{_bindir}/gdc
%{_bindir}/%{_target_platform}-gdc
%{_libdir}/d21
%{_libdir}/include/d/
/usr/lib/libgdruntime.a
/usr/lib32/libgdruntime.a
/usr/lib/libgphobos.a
/usr/lib32/libgphobos.a
/usr/lib/libgphobos.spec
/usr/lib32/libgphobos.spec
%{_infodir}/gdc.info*
%{_mandir}/man1/gdc.1*

%files fortran
%{_bindir}/gfortran
%{_bindir}/%{_target_platform}-gfortran
%{_libdir}/finclude/
%{_libdir}/32/finclude/
%{_libdir}/libcaf_shmem.a
%{_libdir}/libcaf_single.a
%{_libdir}/32/libcaf_shmem.a
%{_libdir}/32/libcaf_single.a
%{_libdir}/f951
%{_libdir}/include/ISO_Fortran_binding.h
/usr/lib/libgfortran.spec
/usr/lib32/libgfortran.spec
%{_infodir}/gfortran.info*
%{_mandir}/man1/gfortran.1*

%files gcobol
%{_bindir}/gcobc
%{_bindir}/gcobol
%{_bindir}/%{_target_platform}-gcobc
%{_bindir}/%{_target_platform}-gcobol
%{_libdir}/cobol/
%{_libdir}/cobol1
/usr/lib/libgcobol.spec
%{_mandir}/man1/gcobol.1*
%{_mandir}/man3/gcobol-io.3*

%files go
%{_bindir}/gccgo
%{_bindir}/go
%{_bindir}/gofmt
%{_bindir}/%{_target_platform}-gccgo
%{_libdir}/buildid
%{_libdir}/cgo
%{_libdir}/go1
%{_libdir}/test2json
%{_libdir}/vet
/usr/lib/go/
/usr/lib32/go/
/usr/lib/libgo.a
/usr/lib32/libgo.a
/usr/lib/libgobegin.a
/usr/lib32/libgobegin.a
/usr/lib/libgolibbegin.a
/usr/lib32/libgolibbegin.a
%{_infodir}/gccgo.info*
%{_mandir}/man1/gccgo.1*
%{_mandir}/man1/go.1*
%{_mandir}/man1/gofmt.1*

%files libs
# metapackage - no files of its own, just pulls in the runtime libs

%files m2
%{_bindir}/gm2
%{_bindir}/%{_target_platform}-gm2
%{_libdir}/cc1gm2
%{_infodir}/m2.info*
%{_mandir}/man1/gm2.1*

%files objc
%{_libdir}/include/objc/
%{_libdir}/cc1obj*

%files rust
%{_bindir}/gccrs
%{_bindir}/%{_target_platform}-gccrs
%{_libdir}/crab1

%files -n lib32-gcc-libs
/usr/lib/libasan.a
/usr/lib/libasan.so*
/usr/lib/libatomic.so*
/usr/lib/libgcc_s.so.*
/usr/lib/libgdruntime.so*
/usr/lib/libgfortran.a
/usr/lib/libgfortran.so*
/usr/lib/libgo.so*
/usr/lib/libgomp.a
/usr/lib/libgomp.so*
/usr/lib/libgphobos.so*
/usr/lib/libitm.a
/usr/lib/libitm.so*
/usr/lib/libobjc.a
/usr/lib/libobjc.so*
/usr/lib/libquadmath.a
/usr/lib/libquadmath.so*
/usr/lib/libstdc++.so*
/usr/lib/libubsan.a
/usr/lib/libubsan.so*

%files -n libasan
%{_libdir}/libasan.a
%{_libdir}/libasan.so*

%files -n libatomic
%{_libdir}/libatomic.so*

%files -n libgcc
%{_libdir}/libgcc_s.so.*

%files -n libgccjit
%{_includedir}/libgccjit*
%{_libdir}/libgccjit.so*
%{_infodir}/libgccjit.info*

%files -n libgcobol
%{_libdir}/libgcobol.a
%{_libdir}/libgcobol.so*

%files -n libgfortran
%{_libdir}/libgfortran.a
%{_libdir}/libgfortran.so*

%files -n libgm2
%{_libdir}/m2/
%{_libdir}/32/m2/
%{_libdir}/libm2cor.a
%{_libdir}/libm2cor.so*
%{_libdir}/libm2iso.a
%{_libdir}/libm2iso.so*
%{_libdir}/libm2log.a
%{_libdir}/libm2log.so*
%{_libdir}/libm2min.a
%{_libdir}/libm2min.so*
%{_libdir}/libm2pim.a
%{_libdir}/libm2pim.so*
/usr/lib32/libm2cor.a
/usr/lib32/libm2cor.so*
/usr/lib32/libm2iso.a
/usr/lib32/libm2iso.so*
/usr/lib32/libm2log.a
/usr/lib32/libm2log.so*
/usr/lib32/libm2min.a
/usr/lib32/libm2min.so*
/usr/lib32/libm2pim.a
/usr/lib32/libm2pim.so*

%files -n libgo
%{_libdir}/libgo.so*

%files -n libgomp
%{_libdir}/libgomp.a
%{_libdir}/libgomp.so*
%{_infodir}/libgomp.info*

%files -n libgphobos
%{_libdir}/libgdruntime.so*
%{_libdir}/libgphobos.so*

%files -n libhwasan
%{_libdir}/libhwasan.a
%{_libdir}/libhwasan.so*

%files -n libitm
%{_libdir}/libitm.a
%{_libdir}/libitm.so*
%{_infodir}/libitm.info*

%files -n liblsan
%{_libdir}/liblsan.a
%{_libdir}/liblsan.so*

%files -n libobjc
%{_libdir}/libobjc.a
%{_libdir}/libobjc.so*

%files -n libquadmath
%{_libdir}/libquadmath.a
%{_libdir}/libquadmath.so*
%{_infodir}/libquadmath.info*

%files -n libstdc++
%{_libdir}/libstdc++.so*
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/libstdc++.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/libstdc++.mo

%files -n libtsan
%{_libdir}/libtsan.a
%{_libdir}/libtsan.so*

%files -n libubsan
%{_libdir}/libubsan.a
%{_libdir}/libubsan.so*

%files -n lto-dump
%{_bindir}/lto-dump
%{_mandir}/man1/lto-dump.1*


%changelog
* Wed Jul 08 2026 Rain Xelelo <rxelelo@outlook.com> - 16.1.0-1
- Initial packaging of gcc 16.1.0 with full frontend/runtime split
