Summary:	School organizer
Summary(pl):	Terminarz ucznia
Name:		gnutu
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.gnutu.org/dane/download/%{name}-%{version}.tar.gz
# Source0-md5:	66e1fa6636465ae5218a10d573fa9ac9
Patch0:		%{name}-desktop.patch
URL:		http://www.gnu-tu.prv.pl/
BuildRequires:	libgnomeui-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Terminarz Ucznia is equivalent and continuation of Windows program
Terminarz Ucznia. This program will be useful for all students. You
can write here dates of all your tests, your notices and marks. You
can also use it to search for date of your nearest test.

%description -l pl
GNU Terminarz Ucznia jest odpowiednikiem i kontynuacj± windowsowego
programu Terminarz Ucznia. Program przyda siê wszystkim uczniom. S³u¿y
do zapisywania terminów sprawdzianów, notatek, ocen, umo¿liwia
wyszukiwanie najbli¿szych klasówek.

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/%{name}
%{_datadir}/locale/pl/LC_MESSAGES/*
