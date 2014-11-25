#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Data
%define		pnam	HexDump
%include	/usr/lib/rpm/macros.perl
Summary:	Data::HexDump - a simple hexadecial dumper
Summary(pl.UTF-8):	Data::HexDump - proste zrzucanie danych w formacie szesnastkowym
Name:		perl-Data-HexDump
Version:	0.02
Release:	4
# sa,e as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	467b7183d1062ab4a502b50c34e7d67f
URL:		http://search.cpan.org/dist/Data-HexDump/
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Data::HexDump wyrzuca szesnastkowo zawartość skalara. Wynik jest
zwracany jako łańcuch. Każda linia wyniku składa się z offsetu w
źródle w lewej kolumnie każdej linii, po którym następuje jedna lub
więcej kolumn szesnastkowych danych ze źródła. Prawa kolumna każdej
linii pokazuje znaki drukowalne (wszystkie inne są pokazywane jako
pojedyncze kropki).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT%{_bindir}/hexdump $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Data/*.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/hexdump
