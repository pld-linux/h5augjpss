Summary:	Modify JPSS files to allow use in netCDF-based applications
Summary(pl.UTF-8):	Modyfikowanie plików JPSS dla kompatybilności z aplikacjami opartymi na netCDF
Name:		h5augjpss
Version:	1.0.0
Release:	5
Group:		Applications/File
License:	BSD-like, changed sources must be marked
Source0:	http://www.hdfgroup.org/ftp/HDF5/projects/jpss/h5augjpss/%{name}-%{version}.tar.gz
# Source0-md5:	5435f4dee00fcc8bbe30d9bed421c812
Patch0:		%{name}-cmake.patch
Patch1:		libdir.patch
URL:		http://www.hdfgroup.org/projects/npoess/h5augjpss_index.html
BuildRequires:	hdf5-devel >= 1.8
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The h5augjpss tool has options to make modifications to JPSS files
that will aid in allowing some common "netCDF-based" applications to
use or display them. Certain options will hide unsupported HDF5
elements that block access to the files. These should at least allow
access with ncdump and other netCDF-4 tools. Other options will
incorporate information from the XML product and geolocation files.
Additional metadata required for specific applications can then be
added using h5edit or HDFView.

%description -l pl.UTF-8
Narzędzie h5augjpss pozwala dokonać modyfikacji w plikach JPSS, które
pozwalają korzystać z nich lub wyświetlać je w aplikacjach opartych na
netCDF. Pewne opcje ukrywają nie obsługiwane elementy HDF5 blokujące
dostęp do tych plików. Powinno to pozwolić przynajmniej na dostęp przy
użyciu ncdumpa i innych narzędzi netCDF-4. Inne opcje włączają
informacje z produktu XML i plików geolokalizacji. Dodatkowe metadane,
wymagane dla określonych aplikacji, można potem dodać przy użyciu
programu h5edit lub HDFView.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake .

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D bin/h5augjpss $RPM_BUILD_ROOT%{_bindir}/h5augjpss

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING docs/{RELEASE.txt,h5augjpssReferenceManual1.0-1.htm}
%attr(755,root,root) %{_bindir}/h5augjpss
