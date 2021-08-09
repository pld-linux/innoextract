Summary:	Tool to unpack installers created by Inno Setup
Summary(pl.UTF-8):	Narzędzie do rozpakowywania instalatorów tworzonych przez Inno Setup
Name:		innoextract
Version:	1.9
Release:	2
License:	Zlib (BSD-like)
Group:		Applications/Files
Source0:	https://constexpr.org/innoextract/files/innoextract-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	964f39bb3f8fd2313629e69ffd3dab9f
URL:		https://constexpr.org/innoextract/
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	libstdc++-devel
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inno Setup is a tool to create installers for Microsoft Windows
applications. innoextract allows to extract such installers under
non-windows systems without running the actual installer using WINE.
innoextract currently supports installers created by Inno Setup 1.2.10
to 6.0.5.

%description -l pl.UTF-8
Inno Setup to narzędzie do tworzenia instalatorów dla systemu
Microsoft Windows. innoextract pozwala na rozpakowywanie takich
instalatorów na innych systemach operacyjnych bez uruchamiania samego
instalatora przy użyciu WINE. innoextract obecnie obsługuje
instalatory utworzone przez Inno Setup w wersjach od 1.2.10 do 6.0.5.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.md
%attr(755,root,root) %{_bindir}/innoextract
%{_mandir}/man1/innoextract.1*
