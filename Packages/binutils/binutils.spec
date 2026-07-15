%global debug_package %{nil}

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
mkdir -p binutils-build
%setup -q -n binutils-%{version}

%build
CONFFLAGS=(
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir} \
    --with-lib-path=%{_libdir}:/usr/local/lib64 \
    --with-bugurl= \
    --enable-cet \
    --enable-colored-disassembly \
    --enable-default-execstack=no \
    --enable-deterministic-archives \
    --enable-gold \
    --enable-install-libiberty \
    --enable-jansson \
    --enable-ld=default \
    --enable-new-dtags \
    --enable-plugins \
    --enable-relro \
    --enable-shared \
    --enable-targets=x86_64-pep,bpf-unknown-none \
    --enable-threads \
    --disable-gdb \
    --disable-gdbserver \
    --disable-libdecnumber \
    --disable-readline \
    --disable-sim \
    --disable-werror \
    --with-debuginfod \
    --with-pic \
    --with-system-zlib
)

cd ../binutils-build

../binutils-%{version}/configure \
    "${CONFFLAGS[@]}"

make %{?_smp_mflags}


%install
cd ../binutils-build
%make_install DESTDIR=%{buildroot} tooldir=%{buildroot}%{_prefix}

# Remove libtool archives, we ship shared libs instead
find %{buildroot} -name '*.la' -delete

# install PIC version of libiberty
install -m644 libiberty/pic/libiberty.a %{buildroot}/usr/lib

# Remove unwanted files
rm -f %{buildroot}/usr/share/man/man1/{dlltool,windres,windmc}*

# No shared linking to these files outside binutils
rm -f %{buildroot}/usr/lib/lib{bfd,opcodes}.so
tee %{buildroot}/usr/lib/libbfd.so << EOS
/* GNU ld script */

INPUT( /usr/lib/libbfd.a -lsframe -liberty -lz -lzstd -ldl )
EOS

  tee %{buildroot}/usr/lib/libopcodes.so << EOS
/* GNU ld script */

INPUT( /usr/lib/libopcodes.a -lbfd )
EOS

# Extract the FSF All Permissive License
# <https://www.gnu.org/prep/maintain/html_node/License-Notices-for-Other-Files.html>
# used for some linker scripts.
tail -n 5 ../binutils-%{version}/ld/scripttempl/README > FSFAP

%files
%license ../binutils-build/FSFAP

%changelog
* Wed Jul 15 2026 Rain Xelelo <rxelelo@outlook.com> - 2.46.1-1
- Initial pacakge binutils with 2.46.1
