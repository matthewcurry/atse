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

%define pname binutils

Summary:   The GNU Binary Utilities
Name:      %{pname}%{PROJ_DELIM}
Version:   2.30
Release:   1%{?dist}
License:   GPLv3+
Group:     %{PROJ_NAME}/dev-tools
URL:       https://www.gnu.org/software/binutils/
DocDir:    %{OHPC_PUB}/doc/contrib
Source0:   https://ftp.gnu.org/gnu/binutils/%{pname}-%{version}.tar.gz
Source1:   OHPC_macros
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-root

BuildRequires: autoconf%{PROJ_DELIM} >= 2.69
BuildRequires: automake%{PROJ_DELIM} >= 1.15
BuildRequires: libtool%{PROJ_DELIM}  >= 2.4.6
BuildRequires: m4
BuildRequires: flex
BuildRequires: bison
BuildRequires: gettext

%define install_path %{OHPC_UTILS}/%{pname}/%{version}

%description
The GNU Binary Utilities.

%prep
%setup -n %{pname}-%{version}

%build
module load autotools
./configure --prefix=%{install_path} --disable-dependency-tracking --disable-werror --enable-interwork --enable-multilib --enable-shared --enable-64-bit-bfd --enable-targets=all --with-sysroot=/ --enable-gold --enable-plugins

%install
module load autotools
make %{?_smp_mflags} DESTDIR=$RPM_BUILD_ROOT install

# OpenHPC module file
%{__mkdir_p} %{buildroot}/%{OHPC_MODULES}/%{pname}
%{__cat} << EOF > %{buildroot}/%{OHPC_MODULES}/%{pname}/%{version}
#%Module1.0#####################################################################

proc ModulesHelp { } {
puts stderr "This module loads the GNU binary utilities."
puts stderr " "
}

module-whatis "Name: GNU binutils"
module-whatis "Version: %{version}"
module-whatis "Category: utility, developer tools"
module-whatis "Keywords: System, Utility, Toolchain"
module-whatis "Description: GNU binary utilities"

prepend-path    PATH            %{install_path}/bin
prepend-path    LD_LIBRARY_PATH %{install_path}/lib
prepend-path    MANPATH         %{install_path}/share/man

setenv          %{PNAME}_DIR        %{install_path}
setenv          %{PNAME}_BIN        %{install_path}/bin
setenv          %{PNAME}_INC        %{install_path}/include
setenv          %{PNAME}_LIB        %{install_path}/lib

EOF

%{__mkdir_p} ${RPM_BUILD_ROOT}/%{_docdir}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{OHPC_PUB}
%doc ChangeLog
%doc MAINTAINERS
%doc NEWS
%doc README
