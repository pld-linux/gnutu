Summary:	Student's Timetable
Summary(pl):	Terminarz ucznia
Name:		gnutu
Version:	1.1
%define		_beta	beta1
Release:	0.%{_beta}.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.gnutu.org/dane/download/%{name}-%{version}-%{_beta}.tar.gz
# Source0-md5:	cc805614be62209bc88c14f68650a04f
Patch0:		%{name}-desktop.patch
URL:		http://www.gnutu.org/
BuildRequires:	libgnomeui-devel
BuildRequires:	pkgconfig
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
GNU Terminarz Ucznia jest odpowiednikiem i kontynuacj� windowsowego
programu Terminarz Ucznia. Program przyda si� wszystkim uczniom. S�u�y
do zapisywania termin�w sprawdzian�w, notatek, ocen, umo�liwia
wyszukiwanie najbli�szych klas�wek.

%prep
%setup -q -n %{name}-%{version}-%{_beta}
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
%{_desktopdir}/*
%{_pixmapsdir}/%{name}
