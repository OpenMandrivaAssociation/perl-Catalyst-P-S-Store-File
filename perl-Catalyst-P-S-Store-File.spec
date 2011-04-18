%define upstream_name    Catalyst-Plugin-Session-Store-File
%define abbrev_name      Catalyst-P-S-Store-File
%define upstream_version 0.18

Name:		perl-%{abbrev_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	File storage backend for session data
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Cache::Cache) >= 1.02
BuildRequires:	perl(Catalyst) >= 5
BuildRequires:	perl(Catalyst::Plugin::Session) >= 0.21
BuildRequires:	perl(Class::Accessor::Fast) >= 0.22
BuildRequires:	perl(Class::Data::Inheritable) >= 0.04
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Catalyst::Plugin::Session::Store::File is an easy to use storage plugin for
Catalyst that uses an simple file to act as a shared memory interprocess cache.
It is based on Cache::FileCache.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*

%clean
rm -rf %{buildroot}

