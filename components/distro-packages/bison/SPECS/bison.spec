# Look for TODOs.

#----------------------------------------------------------------------------bh-
# This RPM .spec file is part of the ATSE project.
#
# It may have been modified from the default version supplied by the underlying
# release package (if available) in order to apply patches, perform customized
# build/install configurations, and supply additional files to support
# desired integration conventions.
#
#----------------------------------------------------------------------------eh-

%include %{_sourcedir}/OHPC_macros

%define pname bison

%define major_version 3.0
%define minor_version 5

Summary: Bison is a general-purpose parser generator
Name:    %{pname}%{PROJ_DELIM}
Version: %{major_version}.%{minor_version}
Release: 1%{?dist}
License: GNU GPL v3 or later
Group:   %{PROJ_NAME}/dist-packages
URL:     https://www.gnu.org/software/bison/
Source0: http://ftp.gnu.org/gnu/bison/bison-%{version}.tar.gz
Source1: OHPC_macros
BuildRequires: gcc-c++
BuildRequires: pkgconfig

%define install_path %{OHPC_UTILS}/%{pname}/%version

%description
Bison is a general-purpose parser generator that converts an annotated context-free grammar into a deterministic LR or generalized LR (GLR) parser employing LALR(1) parser tables. As an experimental feature, Bison can also generate IELR(1) or canonical LR(1) parser tables. Once you are proficient with Bison, you can use it to develop a wide range of language parsers, from those used in simple desk calculators to complex programming languages.

%prep
%setup -q -n %{pname}-%{version}

./configure --prefix=%{install_path}/bin

%build
%{__make} %{?mflags}

%install
%{__make} install

# Module file
%{__mkdir_p} %{buildroot}%{OHPC_MODULES}/%{pname}
%{__cat} << EOF > %{buildroot}/%{OHPC_MODULES}/%{pname}/%{version}
#%Module1.0#####################################################################

proc ModulesHelp { } {

        puts stderr " "
        puts stderr "This module loads the %{pname} utility"
        puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname}"
module-whatis "Version: %{version}"
module-whatis "Category: utility, developer support"
module-whatis "Keywords: System, Utility"
module-whatis "Description: %{summary}"
module-whatis "URL %{url}"

set     version             %{version}

prepend-path    PATH                %{install_path}/bin

EOF

%{__cat} << EOF > %{buildroot}/%{OHPC_MODULES}/%{pname}/.version.%{version}
#%Module1.0#####################################################################
##
## version file for %{pname}-%{version}
##
set     ModulesVersion      "%{version}"
EOF

%files
%defattr(-,root,root,-)
%dir %{OHPC_UTILS}
%{OHPC_UTILS}/%{pname}
%{OHPC_MODULES}/%{pname}
