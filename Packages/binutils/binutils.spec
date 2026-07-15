Name:           binutils
Version:        2.46.1
Release:        1%{?dist}
Summary:        A GNU collection of binary utilities (as, ld, objdump, etc.)

License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://www.gnu.org/software/binutils/
Source0:        https://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.gz

Requires:       glibc
Requires:       jansson
Requires:       libelf
Requires:       libgcc
Requires:       libstdc++
Requires:       zlib
Requires:       zstd

BuildRequires:  glibc
BuildRequires:  jansson
BuildRequires:  libelf
BuildRequires:  libgcc
BuildRequires:  zlib
BuildRequires:  zstd
BuildRequires:  libstdc++-devel

%description
The GNU Binutils are a collection of binary tools, the mainstay of
which are "ld" (the GNU linker) and "as" (the GNU assembler). This
package also provides addr2line, ar, c++filt, elfedit, gprof,
nm, objcopy, objdump, ranlib, readelf, size, strings and strip.

Built with gold enabled, shared libbfd/libopcodes, system zlib and
zstd for compressed debug sections, and libctf support (jansson +
libelf) for CTF debug data.

%prep
%setup -q -n binutils-%{version}

%build
mkdir -v build
cd build

../configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --sysconfdir=%{_sysconfdir} \
    --infodir=%{_infodir} \
    --mandir=%{_mandir} \
    --build=%{_build} \
    --host=%{_host} \
    --enable-gold=default \
    --enable-ld=yes \
    --enable-plugins \
    --enable-shared \
    --enable-64-bit-bfd \
    --enable-libctf \
    --enable-default-hash-style=gnu \
    --with-system-zlib \
    --with-zstd \
    --disable-werror \
    --disable-static

%{?_smp_mflags:make %{_smp_mflags} tooldir=%{_prefix}}
%{!?_smp_mflags:make tooldir=%{_prefix}}

%install
cd build
make DESTDIR=%{buildroot} tooldir=%{buildroot}%{_prefix} install

# Remove libtool archives, we ship shared libs instead
find %{buildroot} -name '*.la' -delete

# Some binutils installs drop libiberty.a — not needed at runtime
rm -f %{buildroot}%{_libdir}/libiberty.a

%files
%license COPYING COPYING.LIB COPYING3 COPYING3.LIB
%doc NEWS README

%changelog
* Wed Jul 15 2026 Rain Xelelo <rxelelo@outlook.com> - 2.46.1-1
- Initial pacakge binutils with 2.46.1
