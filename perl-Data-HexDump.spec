#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	HexDump
Summary:	Data::HexDump - a simple hexadecial dumper
Summary(pl):	Data::HexDump - proste zrzucanie danych w formacie szesnastkowym
Name:		perl-Data-HexDump
Version:	0.02
Release:	2
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dump in hexadecimal the content of a scalar. The result is returned in
a string. Each line of the result consists of the offset in the source
in the leftmost column of each line, followed by one or more columns
of data from the source in hexadecimal. The rightmost column of each
line shows the printable characters (all others are shown as single
dots).

%description -l pl
Data::HexDump wyrzuca szesnastkowo zawarto¶æ skalara. Wynik jest
zwracany jako ³añcuch. Ka¿da linia wyniku sk³ada siê z offsetu w
¼ródle w lewej kolumnie ka¿dej linii, po którym nastêpuje jedna lub
wiêcej kolumn szesnastkowych danych ze ¼ród³a. Prawa kolumna ka¿dej
linii pokazuje znaki drukowalne (wszystkie inne s± pokazywane jako
pojedyncze kropki).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Data/*.pm
%{_mandir}/man3/*
