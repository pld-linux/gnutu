%include	/usr/lib/rpm/macros.mono
Summary:	Student's Timetable
Summary(pl):	Terminarz ucznia
Name:		gnutu
Version:	2.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://gnutu.org/download/sources/%{name}-%{version}.tar.gz
# Source0-md5:	428cb15223884d67b35e4225293cc69f
Patch0:		%{name}-desktop.patch
URL:		http://www.gnutu.org/
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.4.0
BuildRequires:	mono-csharp
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Student's Timetable is a Polish program. It is designed for
students from primary and secondary schools - using it, you can note
various information (like marks, tests' dates and important school
events). It also can create various statistics, calculate your
average; it can also serve as a journal and many, many more... This
program is a continuation of a windows program with similar name -
Terminarz Ucznia (Student's Timetable), which's author is also Marcin
Krzywonos.

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/gnutu.png
