%define upstream_name    Catalyst-Plugin-Session-Store-File
%define abbrev_name      Catalyst-P-S-Store-File
%define upstream_version 0.18

Name:		perl-%{abbrev_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	File storage backend for session data
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Cache::Cache) >= 1.02
BuildRequires:	perl(Catalyst) >= 5
BuildRequires:	perl(Catalyst::Plugin::Session) >= 0.21
BuildRequires:	perl(Class::Accessor::Fast) >= 0.22
BuildRequires:	perl(Class::Data::Inheritable) >= 0.04
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
Catalyst::Plugin::Session::Store::File is an easy to use storage plugin for
Catalyst that uses an simple file to act as a shared memory interprocess cache.
It is based on Cache::FileCache.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.180.0-2mdv2011.0
+ Revision: 654824
- rebuild

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.180.0-1mdv2011.0
+ Revision: 461724
- update to 0.18

* Fri Jun 12 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 385468
- adding missing buildrequires:
- adding missing buildrequires:
- update to 0.17
- using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.09-4mdv2009.0
+ Revision: 255585
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.09-2mdv2008.1
+ Revision: 136678
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-2mdv2008.0
+ Revision: 85976
- rebuild


* Sat Aug 05 2006 Scott Karns <scottk@mandriva.org> 0.09-1mdv2007.0
- 0.09
- Updated spec to use Module::Build
- Renamed from Catalyst-Plugin-Session-Store-File to meet joliet
  filename length constraint

* Fri May 05 2006 Scott Karns <scottk@mandriva.org> 0.07-2mdk
- Updated BuildRequires
- Updated to comply with Mandriva perl packaging policies

* Tue Jan 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.07-1mdk
- 0.07

* Tue Dec 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.05-2mdk
- Add BuildRequires

* Fri Dec 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.05-1mdk
- Initial MDV RPM

