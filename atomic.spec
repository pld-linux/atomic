Summary:	Atomic operations implementation
Name:		atomic
Version:	1.0.0
Release:	1
License:	GPL v2+
Group:		Development/Libraries
Source0:	http://www.ioremap.net/archive/libatomic/%{name}-%{version}.tar.gz
# Source0-md5:	e615316852011269e26f4cea8b1f0c8d
URL:		http://www.ioremap.net/projects/libatomic
BuildRequires:	gcc >= 4.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libatomic provides arch-independant API for the low-level atomic
implementation. Library supports x86 (both i386 and x86_64), PPC64,
Sparc64 (v9 and higher) and with modern gcc (version higher than
4.1.0) and its __sync extensions all its supported platforms.

%package devel
Summary:	Header files and develpment documentation for atomic
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and develpment documentation for atomic.

%package static
Summary:	Static atomic library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static atomic library.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libatomic.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libatomic.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/atomic
%attr(755,root,root) %{_libdir}/libatomic.so
%{_libdir}/libatomic.la

%files static
%defattr(644,root,root,755)
%{_libdir}/libatomic.a
