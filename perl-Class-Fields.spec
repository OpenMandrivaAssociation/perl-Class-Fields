%define upstream_name    Class-Fields
%define upstream_version 0.204

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Inspect the fields of a class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Carp::Assert)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(base)
BuildArch:	noarch

%description
* _Public member._

  Externally visible data or functionality. An attribute or method that is
  directly accessable from scopes outside the class. In Perl, most members
  are, by their standard semantics, public. By convention, attributes of
  Perl classes are regarded as private, as are methods whose names begin
  with an underscore.

  From *"Object Oriented Perl"* by Damian Conway

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.204.0-2mdv2011.0
+ Revision: 654274
- rebuild for updated spec-helper

* Mon Feb 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.204.0-1
+ Revision: 636578
- update to new version 0.204

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.203.0-1mdv2011.0
+ Revision: 399311
- import perl-Class-Fields


* Fri Jul 24 2009 cpan2dist 0.203-1mdv
- initial mdv release, generated with cpan2dist
