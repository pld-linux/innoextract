Summary:	Tool to unpack installers created by Inno Setup
Summary(pl.UTF-8):	Narzędzie do rozpakowywania instalatorów tworzonych przez Inno Setup
Name:		innoextract
Version:	1.3
Release:	2
License:	BSD
Group:		Applications/Files
Source0:	http://downloads.sourceforge.net/innoextract/%{name}-%{version}.tar.gz
# Source0-md5:	a6b2662ebc182efa15e09f4281c231df
URL:		http://constexpr.org/innoextract/
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	libstdc++-devel
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inno Setup is a tool to create installers for Microsoft Windows
applications. innoextract allows to extract such installers under
non-windows systems without running the actual installer using WINE.
innoextract currently supports installers created by Inno Setup 1.2.10
to 5.5.3.

%description -l pl.UTF-8
Inno Setup to narzędzie do tworzenia instalatorów dla systemu
Microsoft Windows. innoextract pozwala na rozpakowywanie takich
instalatorów na innych systemach operacyjnych bez uruchamiania samego
instalatora przy użyciu WINE. innoextract obecnie obsługuje
instalatory utworzone przez Inno Setup w wersjach od 1.2.10 do 5.5.3.

%prep
%setup -q

%build
%cmake .

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.md
%attr(755,root,root) %{_bindir}/innoextract
%{_mandir}/man1/innoextract.1*
