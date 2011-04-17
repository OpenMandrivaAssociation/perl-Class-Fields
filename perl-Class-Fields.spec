%define upstream_name    Class-Fields
%define upstream_version 0.204

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Inspect the fields of a class
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Carp::Assert)
BuildRequires: perl(Test::More)
BuildRequires: perl(base)
BuildRequires: perl(constant)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


