# TODO:
# - en description
#
Summary:	School organizer
Summary(pl):	Terminarz ucznia
Name:		gnutu
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.mkk.akcja.pl/gnutu/program/%{name}-%{version}.tar.gz
# Source0-md5:	b3a04767c373ba89726578316be5703a
Patch0:		%{name}-desktop.patch
URL:		www.gnu-tu.prv.pl
BuildRequires:	libgnomeui-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl
GNU Terminarz Ucznia jest odpowiednikiem i kontynuacj windowsowego
programu Terminarz Ucznia. Program przyda si wszystkim uczniom. Suy do
zapisywania terminw sprawdzianw, notatek, ocen, umoliwia wyszukiwanie
najbliszych klaswek.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/%{name}
