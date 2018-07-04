#----------------------------------------------------------------------------bh-
# This RPM .spec file is part of the OpenHPC project.
#
# It may have been modified from the default version supplied by the underlying
# release package (if available) in order to apply patches, perform customized
# build/install configurations, and supply additional files to support
# desired integration conventions.
#
#----------------------------------------------------------------------------eh-

%include %{_sourcedir}/OHPC_macros

Name: atse-filesystem
Version: 1.3
Release: 1.atse
Summary: Common top-level ATSE directories

Group: atse/admin
License: ASL 2.0
Source0: ATSE_setup_compiler
Source1: ATSE_setup_mpi
Source2: atse-find-requires
Source3: atse-find-provides
Source4: OHPC_macros

BuildArch: noarch

%description
This administrative package is used to define top level ATSE installation
directories. It is utilized by most packages that do not install into system
default paths.

%package -n atse-buildroot
Summary: Common build scripts used in ATSE packaging
Group: atse/admin
Requires: lmod%{PROJ_DELIM}
Requires: atse-filesystem

%description -n atse-buildroot

This administrative package is used to provide RPM dependency analysis tools
and common compiler and MPI family convenience scripts used during ATSE
builds.

%install
# The atse-filesystems owns all the common directories
mkdir -p $RPM_BUILD_ROOT/opt/atse/pub/{apps,doc,compiler,libs,moduledeps,modulefiles,mpi}
mkdir -p $RPM_BUILD_ROOT/opt/atse/admin/atse
mkdir -p $RPM_BUILD_ROOT/usr/lib/rpm/fileattrs

install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT/opt/atse/admin/atse
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT/opt/atse/admin/atse

# rpm dependency plugins
install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT/usr/lib/rpm
install -p -m 755 %{SOURCE3} $RPM_BUILD_ROOT/usr/lib/rpm

%{__mkdir_p} %{buildroot}/usr/lib/rpm/fileattrs/
%{__cat} <<EOF > %{buildroot}//usr/lib/rpm/fileattrs/atse.attr
%%__atse_provides        /usr/lib/rpm/atse-find-provides
%%__atse_requires        /usr/lib/rpm/atse-find-requires %%{buildroot} %{OHPC_HOME}

%%__atse_path            ^%{OHPC_HOME}
%%__elf_exclude_path     ^%{OHPC_HOME}

%%__atse_magic           ^ELF (32|64)-bit.*$
%%__atse_flags           magic_and_path
EOF

%if 0%{?sles_version} || 0%{?suse_version}
%{__cat} <<EOF >> %{buildroot}//usr/lib/rpm/fileattrs/atse.attr
%%__elflib_exclude_path  ^%{OHPC_HOME}
EOF
%endif


%files
%dir /opt/atse/
%dir /opt/atse/admin/
%dir /opt/atse/pub/
%dir /opt/atse/pub/apps/
%dir /opt/atse/pub/doc/
%dir /opt/atse/pub/compiler/
%dir /opt/atse/pub/libs/
%dir /opt/atse/pub/moduledeps/
%dir /opt/atse/pub/modulefiles/
%dir /opt/atse/pub/mpi/

%files -n atse-buildroot
%dir /opt/atse/admin/atse/
%dir /usr/lib/rpm/
%dir /usr/lib/rpm/fileattrs/
/opt/atse/admin/atse/ATSE_setup_compiler
/opt/atse/admin/atse/ATSE_setup_mpi
/usr/lib/rpm/atse-find-provides
/usr/lib/rpm/atse-find-requires
/usr/lib/rpm/fileattrs/atse.attr
