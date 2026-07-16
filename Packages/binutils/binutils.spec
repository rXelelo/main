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
    --libdir=%{_libdir} \
    --sysconfdir=%{_sysconfdir} \
    --with-lib-path=%{_libdir}:%{_prefix}/local/lib64 \
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
%make_install tooldir=%{_prefix}

#mv %{buildroot}/github/home/rpmbuild/BUILD/binutils-2.46.1-build/BUILDROOT/usr/lib64/* %{buildroot}/usr/lib64

# Remove libtool archives, we ship shared libs instead
find %{buildroot} -name '*.la' -delete

# install PIC version of libiberty
install -m644 libiberty/pic/libiberty.a %{buildroot}%{_libdir}

# Remove unwanted files
rm -f %{buildroot}%{_datadir}/man/man1/{dlltool,windres,windmc}*

# No shared linking to these files outside binutils
rm -f %{buildroot}%{_libdir}/lib{bfd,opcodes}.so
tee %{buildroot}%{_libdir}/libbfd.so << EOS
/* GNU ld script */

INPUT( %{_libdir}/libbfd.a -lsframe -liberty -lz -lzstd -ldl )
EOS

  tee %{buildroot}%{_libdir}/libopcodes.so << EOS
/* GNU ld script */

INPUT( %{_libdir}/libopcodes.a -lbfd )
EOS

find %{buildroot} -type f \( -perm -0100 -o -perm -0010 -o -perm -0001 \) \
    -exec sh -c '
        for f; do
            if head -c4 "$f" 2>/dev/null | grep -q ELF; then
                chrpath --delete "$f" >/dev/null 2>&1 || :
            fi
        done
    ' _ {} + 2>/dev/null || :

# Extract the FSF All Permissive License
# <https://www.gnu.org/prep/maintain/html_node/License-Notices-for-Other-Files.html>
# used for some linker scripts.
tail -n 5 ../binutils-%{version}/ld/scripttempl/README > FSFAP

%files
%license ../binutils-build/FSFAP
%{_sysconfdir}/gprofng.rc
%{_bindir}/addr2line
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
%{_prefix}/lib/ldscripts/elf32_x86_64.x
%{_prefix}/lib/ldscripts/elf32_x86_64.xbn
%{_prefix}/lib/ldscripts/elf32_x86_64.xc
%{_prefix}/lib/ldscripts/elf32_x86_64.xce
%{_prefix}/lib/ldscripts/elf32_x86_64.xcer
%{_prefix}/lib/ldscripts/elf32_x86_64.xd
%{_prefix}/lib/ldscripts/elf32_x86_64.xdc
%{_prefix}/lib/ldscripts/elf32_x86_64.xdce
%{_prefix}/lib/ldscripts/elf32_x86_64.xdcer
%{_prefix}/lib/ldscripts/elf32_x86_64.xde
%{_prefix}/lib/ldscripts/elf32_x86_64.xder
%{_prefix}/lib/ldscripts/elf32_x86_64.xdw
%{_prefix}/lib/ldscripts/elf32_x86_64.xdwe
%{_prefix}/lib/ldscripts/elf32_x86_64.xdwer
%{_prefix}/lib/ldscripts/elf32_x86_64.xe
%{_prefix}/lib/ldscripts/elf32_x86_64.xer
%{_prefix}/lib/ldscripts/elf32_x86_64.xn
%{_prefix}/lib/ldscripts/elf32_x86_64.xr
%{_prefix}/lib/ldscripts/elf32_x86_64.xs
%{_prefix}/lib/ldscripts/elf32_x86_64.xsc
%{_prefix}/lib/ldscripts/elf32_x86_64.xsce
%{_prefix}/lib/ldscripts/elf32_x86_64.xscer
%{_prefix}/lib/ldscripts/elf32_x86_64.xse
%{_prefix}/lib/ldscripts/elf32_x86_64.xser
%{_prefix}/lib/ldscripts/elf32_x86_64.xsw
%{_prefix}/lib/ldscripts/elf32_x86_64.xswe
%{_prefix}/lib/ldscripts/elf32_x86_64.xswer
%{_prefix}/lib/ldscripts/elf32_x86_64.xu
%{_prefix}/lib/ldscripts/elf32_x86_64.xw
%{_prefix}/lib/ldscripts/elf32_x86_64.xwe
%{_prefix}/lib/ldscripts/elf32_x86_64.xwer
%{_prefix}/lib/ldscripts/elf64bpf.x
%{_prefix}/lib/ldscripts/elf64bpf.xbn
%{_prefix}/lib/ldscripts/elf64bpf.xe
%{_prefix}/lib/ldscripts/elf64bpf.xer
%{_prefix}/lib/ldscripts/elf64bpf.xn
%{_prefix}/lib/ldscripts/elf64bpf.xr
%{_prefix}/lib/ldscripts/elf64bpf.xu
%{_prefix}/lib/ldscripts/elf_i386.x
%{_prefix}/lib/ldscripts/elf_i386.xbn
%{_prefix}/lib/ldscripts/elf_i386.xc
%{_prefix}/lib/ldscripts/elf_i386.xce
%{_prefix}/lib/ldscripts/elf_i386.xcer
%{_prefix}/lib/ldscripts/elf_i386.xd
%{_prefix}/lib/ldscripts/elf_i386.xdc
%{_prefix}/lib/ldscripts/elf_i386.xdce
%{_prefix}/lib/ldscripts/elf_i386.xdcer
%{_prefix}/lib/ldscripts/elf_i386.xde
%{_prefix}/lib/ldscripts/elf_i386.xder
%{_prefix}/lib/ldscripts/elf_i386.xdw
%{_prefix}/lib/ldscripts/elf_i386.xdwe
%{_prefix}/lib/ldscripts/elf_i386.xdwer
%{_prefix}/lib/ldscripts/elf_i386.xe
%{_prefix}/lib/ldscripts/elf_i386.xer
%{_prefix}/lib/ldscripts/elf_i386.xn
%{_prefix}/lib/ldscripts/elf_i386.xr
%{_prefix}/lib/ldscripts/elf_i386.xs
%{_prefix}/lib/ldscripts/elf_x86_64.xdce
%{_prefix}/lib/ldscripts/elf_x86_64.xdcer
%{_prefix}/lib/ldscripts/elf_x86_64.xde
%{_prefix}/lib/ldscripts/elf_x86_64.xder
%{_prefix}/lib/ldscripts/elf_x86_64.xdw
%{_prefix}/lib/ldscripts/elf_x86_64.xdwe
%{_prefix}/lib/ldscripts/elf_x86_64.xdwer
%{_prefix}/lib/ldscripts/elf_x86_64.xe
%{_prefix}/lib/ldscripts/elf_x86_64.xer
%{_prefix}/lib/ldscripts/elf_x86_64.xn
%{_prefix}/lib/ldscripts/elf_x86_64.xr
%{_prefix}/lib/ldscripts/elf_x86_64.xs
%{_prefix}/lib/ldscripts/elf_x86_64.xsc
%{_prefix}/lib/ldscripts/elf_x86_64.xsce
%{_prefix}/lib/ldscripts/elf_x86_64.xscer
%{_prefix}/lib/ldscripts/elf_x86_64.xse
%{_prefix}/lib/ldscripts/elf_x86_64.xser
%{_prefix}/lib/ldscripts/elf_x86_64.xsw
%{_prefix}/lib/ldscripts/elf_x86_64.xswe
%{_prefix}/lib/ldscripts/elf_x86_64.xswer
%{_prefix}/lib/ldscripts/elf_x86_64.xu
%{_prefix}/lib/ldscripts/elf_x86_64.xw
%{_prefix}/lib/ldscripts/elf_x86_64.xwe
%{_prefix}/lib/ldscripts/elf_x86_64.xwer
%{_prefix}/lib/ldscripts/i386pe.x
%{_prefix}/lib/ldscripts/i386pe.xa
%{_prefix}/lib/ldscripts/i386pe.xbn
%{_prefix}/lib/ldscripts/i386pe.xe
%{_prefix}/lib/ldscripts/i386pe.xer
%{_prefix}/lib/ldscripts/i386pe.xn
%{_prefix}/lib/ldscripts/i386pe.xr
%{_prefix}/lib/ldscripts/i386pe.xu
%{_prefix}/lib/ldscripts/i386pep.x
%{_prefix}/lib/ldscripts/i386pep.xa
%{_prefix}/lib/ldscripts/i386pep.xbn
%{_prefix}/lib/ldscripts/i386pep.xe
%{_prefix}/lib/ldscripts/i386pep.xer
%{_prefix}/lib/ldscripts/i386pep.xn
%{_prefix}/lib/ldscripts/i386pep.xr
%{_prefix}/lib/ldscripts/i386pep.xu
%{_prefix}/lib/ldscripts/stamp
%{_libdir}/bfd-plugins/libdep.so
%{_libdir}/gprofng/libgp-collector.so
%{_libdir}/gprofng/libgp-collectorAPI.a
%{_libdir}/gprofng/libgp-collectorAPI.so
%{_libdir}/gprofng/libgp-heap.so
%{_libdir}/gprofng/libgp-iotrace.so
%{_libdir}/gprofng/libgp-sync.so
%{_libdir}/libbfd-2.46.1.so
%{_libdir}/libbfd.a
%{_libdir}/libbfd.so
%{_libdir}/libctf-nobfd.a
%{_libdir}/libctf-nobfd.so
%{_libdir}/libctf-nobfd.so.0
%{_libdir}/libctf-nobfd.so.0.0.0
%{_libdir}/libctf.a
%{_libdir}/libctf.so
%{_libdir}/libctf.so.0
%{_libdir}/libctf.so.0.0.0
%{_libdir}/libgprofng.a
%{_libdir}/libgprofng.so
%{_libdir}/libgprofng.so.0
%{_libdir}/libgprofng.so.0.0.0
%{_libdir}/libiberty.a
%{_libdir}/libopcodes-2.46.1.so
%{_libdir}/libopcodes.a
%{_libdir}/libopcodes.so
%{_libdir}/libsframe.a
%{_libdir}/libsframe.so
%{_libdir}/libsframe.so.3
%{_libdir}/libsframe.so.3.0.0
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
