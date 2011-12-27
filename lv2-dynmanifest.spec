Summary:	LV2 Dynamic Manifest extension - support for dynamic data generation
Summary(pl.UTF-8):	Rozszerzenie LV2 Dynamic Manifest - obsługa dynamicznego generowania danych
Name:		lv2-dynmanifest
Version:	1.2
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
# Source0-md5:	5c4e4b9a717dbbb253602a137fda910d
URL:		http://lv2plug.in/ns/ext/dynmanifest/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
Requires:	lv2core >= 6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The LV2 API, on its own, cannot be used to write plugin libraries
where data is dynamically generated at runtime (e.g. API wrappers),
since LV2 requires needed information to be provided in one or more
static data (RDF) files. This API addresses this limitation by
extending the LV2 API.

%description -l pl.UTF-8
API LV2 jako takie nie może być używane do pisania bibliotek wtyczek,
w których dane są dynamicznie generowane w czasie działania (np.
obudowań API), ponieważ LV2 wymaga dostarczenia potrzebnych informacji
w jednym lub większej liczbie plików danych statycznych (RDF). To API
wychodzi naprzeciw temu ograniczeniu rozszerzając API LV2.

%package devel
Summary:	Header file for LV2 Dynamic Manifest extension
Summary(pl.UTF-8):	Plik nagłówkowy rozszerzenia LV2 Dynamic Manifest
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lv2core-devel >= 6.0

%description devel
Header file for LV2 Dynamic Manifest extension.

%description devel -l pl.UTF-8
Plik nagłówkowy rozszerzenia LV2 Dynamic Manifest.

%prep
%setup -q

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

./waf

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%dir %{_libdir}/lv2/dynmanifest.lv2
%{_libdir}/lv2/dynmanifest.lv2/dynmanifest.ttl
%{_libdir}/lv2/dynmanifest.lv2/lv2-dynmanifest.doap.ttl
%{_libdir}/lv2/dynmanifest.lv2/manifest.ttl

%files devel
%defattr(644,root,root,755)
%{_libdir}/lv2/dynmanifest.lv2/dynmanifest.h
%{_includedir}/lv2/lv2plug.in/ns/ext/dynmanifest
%{_pkgconfigdir}/lv2-lv2plug.in-ns-ext-dynmanifest.pc
