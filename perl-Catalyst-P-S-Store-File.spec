%define realname Catalyst-Plugin-Session-Store-File
%define abbrevname Catalyst-P-S-Store-File
%define name	perl-%{abbrevname}
%define	modprefix Catalyst

%define version	0.09
%define release	%mkrel 4

Summary:	File storage backend for session data
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Cache::Cache) >= 1.02
BuildRequires:	perl(Catalyst) >= 5
BuildRequires:	perl(Catalyst::Plugin::Session) >= 0.01
BuildRequires:	perl(Class::Accessor::Fast) >= 0.22
BuildRequires:	perl(Class::Data::Inheritable) >= 0.04
BuildRequires:	perl(Module::Build)
Provides:	perl-%{realname}
Obsoletes:	perl-%{realname}
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Catalyst::Plugin::Session::Store::File is an easy to use storage plugin for
Catalyst that uses an simple file to act as a shared memory interprocess cache.
It is based on Cache::FileCache.

%prep
%setup -q -n %{realname}-%{version}
sed -i.DOS -e 's/\r//g' CHANGES
sed -i.DOS -e 's/\r//g' README

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

%clean
rm -rf %{buildroot}

