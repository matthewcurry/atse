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

%define pname zlib

Summary:   A lossless data-compression library
Name:      %{pname}%{PROJ_DELIM}
Version:   1.2.11
Release:   1%{?dist}
License:   zlib and Boost
Group:     %{PROJ_NAME}/libs
DocDir:    %{OHPC_PUB}/doc/contrib
URL:       http://www.zlib.net/
Source0:   https://www.zlib.net/zlib-%{version}.tar.xz
Source1:   OHPC_macros
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-root

BuildRequires: automake, autoconf, libtool

%define install_path %{OHPC_LIBS}/zlib

%description
zlib is designed to be a free, general-purpose, legally unencumbered -- that
is, not covered by any patents -- lossless data-compression library for use on
virtually any computer hardware and operating system.

%prep
%setup -n %{pname}-%{version}

%build
CFLAGS="-fPIC -O3 -g" CXXFLAGS="-fPIC -O3 -g" ./configure --prefix=%{install_path}

%install
make %{?_smp_mflags} DESTDIR=$RPM_BUILD_ROOT install
%{__mkdir_p} ${RPM_BUILD_ROOT}/%{_docdir}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{OHPC_HOME}
%{OHPC_LIBS}
%doc README
%doc ChangeLog
%doc FAQ
