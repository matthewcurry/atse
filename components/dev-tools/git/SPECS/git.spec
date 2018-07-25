#----------------------------------------------------------------------------bh-
# This RPM .spec file is part of the ATSE project.
#----------------------------------------------------------------------------eh-

%include %{_sourcedir}/OHPC_macros

%define pname git
%define PNAME %(echo %{pname} | tr [a-z] [A-Z])
%define install_path %{OHPC_UTILS}/git

Summary:   Git distributed revision control system
Name:      %{pname}%{PROJ_DELIM}
Version:   2.18.0
Release:   1%{?dist}
License:   GPLv2
Group:     %{PROJ_NAME}/dev-tools
URL:       https://git-scm.com/
Source0:   https://mirrors.edge.kernel.org/pub/software/scm/git/git-%{version}.tar.gz

BuildRequires: autoconf, automake, libtool, m4
BuildRequires: asciidoc
BuildRequires: emacs
BuildRequires: expat-devel
BuildRequires: gettext
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: perl-devel
BuildRequires: tk-devel
BuildRequires: xmlto
BuildRequires: zlib-devel

Requires: expat
Requires: gettext
Requires: libcurl
Requires: less
Requires: openssl
Requires: openssh-clients
Requires: pcre
Requires: perl(Error)
Requires: rsync
Requires: tk
Requires: zlib

%description
Git distributed revision control system

%prep
%setup -n %{pname}-%{version}

%build
./configure --prefix=%{install_path}

%install
make %{?_smp_mflags} DESTDIR=$RPM_BUILD_ROOT install install-doc

# OpenHPC module file
%{__mkdir_p} %{buildroot}%{OHPC_MODULES}/%{pname}
%{__cat} << EOF > %{buildroot}/%{OHPC_MODULES}/%{pname}/%{version}
#%Module1.0#####################################################################

proc ModulesHelp { } {

        puts stderr " "
        puts stderr "This module loads the %{pname} library"
        puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname}"
module-whatis "Version: %{version}"
module-whatis "Category: utility, developer support"
module-whatis "Description: %{summary}"
module-whatis "URL %{url}"

prepend-path    PATH                %{install_path}/bin
prepend-path    MANPATH             %{install_path}/share/man
EOF

%{__cat} << EOF > %{buildroot}/%{OHPC_MODULES}/%{pname}/.version.%{version}
#%Module1.0#####################################################################
##
## version file for %{pname}-%{version}
##
set     ModulesVersion      "%{version}"
EOF

%{__mkdir_p} ${RPM_BUILD_ROOT}/%{_docdir}

%files
%{OHPC_PUB}
%doc COPYING
%doc README.md
