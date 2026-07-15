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
/usr/bin/addr2line
%{_bindir}/ar
%{_bindir}/as
%{_bindir}/c++filt
%{_bindir}/elfedit
%{_bindir}/gp-archive
%{_bindir}/gp-collect-app
%{_bindir}/gp-display-html
%{_bindir}/gp-display-src
%{_bindir}/gp-display-text
%{_bindir}/gprof
%{_bindir}/gprofng
%{_bindir}/gprofng-archive
%{_bindir}/gprofng-collect-app
%{_bindir}/gprofng-display-html
%{_bindir}/gprofng-display-src
%{_bindir}/gprofng-display-text
%{_bindir}/gprofng-gmon
%{_bindir}/ld
%{_bindir}/ld.bfd
%{_bindir}/nm
%{_bindir}/objcopy
%{_bindir}/objdump
%{_bindir}/ranlib
%{_bindir}/readelf
%{_bindir}/size
%{_bindir}/strings
%{_bindir}/strip
%{_includedir}/ansidecl.h
%{_includedir}/bfd.h
%{_includedir}/bfdlink.h
%{_includedir}/collectorAPI.h
%{_includedir}/ctf-api.h
%{_includedir}/ctf.h
%{_includedir}/diagnostics.h
%{_includedir}/dis-asm.h
%{_includedir}/libcollector.h
%{_includedir}/libfcollector.h
%{_includedir}/libiberty/ansidecl.h
%{_includedir}/libiberty/demangle.h
%{_includedir}/libiberty/doubly-linked-list.h
%{_includedir}/libiberty/dyn-string.h
%{_includedir}/libiberty/fibheap.h
%{_includedir}/libiberty/floatformat.h
%{_includedir}/libiberty/hashtab.h
%{_includedir}/libiberty/libiberty.h
%{_includedir}/libiberty/objalloc.h
%{_includedir}/libiberty/partition.h
%{_includedir}/libiberty/safe-ctype.h
%{_includedir}/libiberty/sort.h
%{_includedir}/libiberty/splay-tree.h
%{_includedir}/libiberty/timeval-utils.h
%{_includedir}/plugin-api.h
%{_includedir}/sframe-api.h
%{_includedir}/sframe.h
%{_includedir}/symcat.h
/usr/lib/bfd-plugins/libdep.so
/usr/lib/gprofng/libgp-collector.so
/usr/lib/gprofng/libgp-collectorAPI.a
/usr/lib/gprofng/libgp-collectorAPI.so
/usr/lib/gprofng/libgp-heap.so
/usr/lib/gprofng/libgp-iotrace.so
/usr/lib/gprofng/libgp-sync.so
/usr/lib/libbfd-2.46.1.so
/usr/lib/libbfd.a
/usr/lib/libbfd.so
/usr/lib/libctf-nobfd.a
/usr/lib/libctf-nobfd.so
/usr/lib/libctf-nobfd.so.0
/usr/lib/libctf-nobfd.so.0.0.0
/usr/lib/libctf.a
/usr/lib/libctf.so
/usr/lib/libctf.so.0
/usr/lib/libctf.so.0.0.0
/usr/lib/libgprofng.a
/usr/lib/libgprofng.so
/usr/lib/libgprofng.so.0
/usr/lib/libgprofng.so.0.0.0
/usr/lib/libiberty.a
/usr/lib/libopcodes-2.46.1.so
/usr/lib/libopcodes.a
/usr/lib/libopcodes.so
/usr/lib/libsframe.a
/usr/lib/libsframe.so
/usr/lib/libsframe.so.3
/usr/lib/libsframe.so.3.0.0
%{_libdir}/libiberty.a
%{_datadir}/doc/gprofng/examples.tar.gz
%{_infodir}/as.info.gz
%{_infodir}/bfd.info.gz
%{_infodir}/binutils.info.gz
%{_infodir}/ctf-spec.info.gz
%{_infodir}/gprof.info.gz
%{_infodir}/gprofng.info.gz
%{_infodir}/ld.info.gz
%{_infodir}/ldint.info.gz
%{_infodir}/sframe-spec.info.gz
%{_datadir}/locale/ar/LC_MESSAGES/binutils.mo
%{_datadir}/locale/bg/LC_MESSAGES/binutils.mo
%{_datadir}/locale/bg/LC_MESSAGES/gprof.mo
%{_datadir}/locale/bg/LC_MESSAGES/ld.mo
%{_datadir}/locale/ca/LC_MESSAGES/binutils.mo
%{_datadir}/locale/da/LC_MESSAGES/bfd.mo
%{_datadir}/locale/da/LC_MESSAGES/binutils.mo
%{_datadir}/locale/da/LC_MESSAGES/gprof.mo
%{_datadir}/locale/da/LC_MESSAGES/ld.mo
%{_datadir}/locale/da/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/de/LC_MESSAGES/gprof.mo
%{_datadir}/locale/de/LC_MESSAGES/ld.mo
%{_datadir}/locale/de/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/eo/LC_MESSAGES/gprof.mo
%{_datadir}/locale/es/LC_MESSAGES/bfd.mo
%{_datadir}/locale/es/LC_MESSAGES/binutils.mo
%{_datadir}/locale/es/LC_MESSAGES/gas.mo
%{_datadir}/locale/es/LC_MESSAGES/gprof.mo
%{_datadir}/locale/es/LC_MESSAGES/ld.mo
%{_datadir}/locale/es/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/fi/LC_MESSAGES/bfd.mo
%{_datadir}/locale/fi/LC_MESSAGES/binutils.mo
%{_datadir}/locale/fi/LC_MESSAGES/gas.mo
%{_datadir}/locale/fi/LC_MESSAGES/gprof.mo
%{_datadir}/locale/fi/LC_MESSAGES/ld.mo
%{_datadir}/locale/fi/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/fr/LC_MESSAGES/bfd.mo
%{_datadir}/locale/fr/LC_MESSAGES/binutils.mo
%{_datadir}/locale/fr/LC_MESSAGES/gas.mo
%{_datadir}/locale/fr/LC_MESSAGES/gprof.mo
%{_datadir}/locale/fr/LC_MESSAGES/ld.mo
%{_datadir}/locale/fr/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/ga/LC_MESSAGES/gprof.mo
%{_datadir}/locale/ga/LC_MESSAGES/ld.mo
%{_datadir}/locale/ga/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/hr/LC_MESSAGES/bfd.mo
%{_datadir}/locale/hr/LC_MESSAGES/binutils.mo
%{_datadir}/locale/hu/LC_MESSAGES/gprof.mo
%{_datadir}/locale/id/LC_MESSAGES/bfd.mo
%{_datadir}/locale/id/LC_MESSAGES/binutils.mo
%{_datadir}/locale/id/LC_MESSAGES/gas.mo
%{_datadir}/locale/id/LC_MESSAGES/gprof.mo
%{_datadir}/locale/id/LC_MESSAGES/ld.mo
%{_datadir}/locale/id/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/it/LC_MESSAGES/binutils.mo
%{_datadir}/locale/it/LC_MESSAGES/gprof.mo
%{_datadir}/locale/it/LC_MESSAGES/ld.mo
%{_datadir}/locale/it/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/ja/LC_MESSAGES/bfd.mo
%{_datadir}/locale/ja/LC_MESSAGES/binutils.mo
%{_datadir}/locale/ja/LC_MESSAGES/gas.mo
%{_datadir}/locale/ja/LC_MESSAGES/gprof.mo
%{_datadir}/locale/ja/LC_MESSAGES/ld.mo
%{_datadir}/locale/ka/LC_MESSAGES/bfd.mo
%{_datadir}/locale/ka/LC_MESSAGES/binutils.mo
%{_datadir}/locale/ka/LC_MESSAGES/gas.mo
%{_datadir}/locale/ka/LC_MESSAGES/gprof.mo
%{_datadir}/locale/ka/LC_MESSAGES/ld.mo
%{_datadir}/locale/ka/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/ms/LC_MESSAGES/bfd.mo
%{_datadir}/locale/ms/LC_MESSAGES/gprof.mo
%{_datadir}/locale/nl/LC_MESSAGES/gprof.mo
%{_datadir}/locale/nl/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/pt/LC_MESSAGES/bfd.mo
%{_datadir}/locale/pt/LC_MESSAGES/binutils.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/gprof.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/ld.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/ro/LC_MESSAGES/bfd.mo
%{_datadir}/locale/ro/LC_MESSAGES/binutils.mo
%{_datadir}/locale/ro/LC_MESSAGES/gas.mo
%{_datadir}/locale/ro/LC_MESSAGES/gprof.mo
%{_datadir}/locale/ro/LC_MESSAGES/ld.mo
%{_datadir}/locale/ro/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/ru/LC_MESSAGES/bfd.mo
%{_datadir}/locale/ru/LC_MESSAGES/binutils.mo
%{_datadir}/locale/ru/LC_MESSAGES/gas.mo
%{_datadir}/locale/ru/LC_MESSAGES/gprof.mo
%{_datadir}/locale/ru/LC_MESSAGES/ld.mo
%{_datadir}/locale/rw/LC_MESSAGES/bfd.mo
%{_datadir}/locale/rw/LC_MESSAGES/binutils.mo
%{_datadir}/locale/rw/LC_MESSAGES/gas.mo
%{_datadir}/locale/rw/LC_MESSAGES/gprof.mo
%{_datadir}/locale/sk/LC_MESSAGES/binutils.mo
%{_datadir}/locale/sr/LC_MESSAGES/bfd.mo
%{_datadir}/locale/sr/LC_MESSAGES/binutils.mo
%{_datadir}/locale/sr/LC_MESSAGES/gprof.mo
%{_datadir}/locale/sr/LC_MESSAGES/ld.mo
%{_datadir}/locale/sr/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/sv/LC_MESSAGES/bfd.mo
%{_datadir}/locale/sv/LC_MESSAGES/binutils.mo
%{_datadir}/locale/sv/LC_MESSAGES/gas.mo
%{_datadir}/locale/sv/LC_MESSAGES/gprof.mo
%{_datadir}/locale/sv/LC_MESSAGES/ld.mo
%{_datadir}/locale/sv/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/tr/LC_MESSAGES/bfd.mo
%{_datadir}/locale/tr/LC_MESSAGES/binutils.mo
%{_datadir}/locale/tr/LC_MESSAGES/gas.mo
%{_datadir}/locale/tr/LC_MESSAGES/gprof.mo
%{_datadir}/locale/tr/LC_MESSAGES/ld.mo
%{_datadir}/locale/tr/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/uk/LC_MESSAGES/bfd.mo
%{_datadir}/locale/uk/LC_MESSAGES/binutils.mo
%{_datadir}/locale/uk/LC_MESSAGES/gas.mo
%{_datadir}/locale/uk/LC_MESSAGES/gprof.mo
%{_datadir}/locale/uk/LC_MESSAGES/ld.mo
%{_datadir}/locale/uk/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/vi/LC_MESSAGES/bfd.mo
%{_datadir}/locale/vi/LC_MESSAGES/binutils.mo
%{_datadir}/locale/vi/LC_MESSAGES/gprof.mo
%{_datadir}/locale/vi/LC_MESSAGES/ld.mo
%{_datadir}/locale/vi/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/bfd.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/binutils.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/gas.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/ld.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/opcodes.mo
%{_datadir}/locale/zh_TW/LC_MESSAGES/binutils.mo
%{_datadir}/locale/zh_TW/LC_MESSAGES/ld.mo
%{_mandir}/man1/addr2line.1.gz
%{_mandir}/man1/ar.1.gz
%{_mandir}/man1/as.1.gz
%{_mandir}/man1/c++filt.1.gz
%{_mandir}/man1/elfedit.1.gz
%{_mandir}/man1/gprof.1.gz
%{_mandir}/man1/gprofng-archive.1.gz
%{_mandir}/man1/gprofng-collect-app.1.gz
%{_mandir}/man1/gprofng-display-gmon.1.gz
%{_mandir}/man1/gprofng-display-html.1.gz
%{_mandir}/man1/gprofng-display-src.1.gz
%{_mandir}/man1/gprofng-display-text.1.gz
%{_mandir}/man1/gprofng.1.gz
%{_mandir}/man1/ld.1.gz
%{_mandir}/man1/nm.1.gz
%{_mandir}/man1/objcopy.1.gz
%{_mandir}/man1/objdump.1.gz
%{_mandir}/man1/ranlib.1.gz
%{_mandir}/man1/readelf.1.gz
%{_mandir}/man1/size.1.gz
%{_mandir}/man1/strings.1.gz
%{_mandir}/man1/strip.1.gz

%changelog
* Wed Jul 15 2026 Rain Xelelo <rxelelo@outlook.com> - 2.46.1-1
- Initial pacakge binutils with 2.46.1
