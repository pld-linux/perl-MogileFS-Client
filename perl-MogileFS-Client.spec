#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	MogileFS
%define	pnam	Client
Summary:	MogileFS::Client - Client library for the MogileFS distributed file system.
#Summary(pl.UTF-8):	MogileFS::Client - Modu³ klienta dla rozproszonego systemu plików MoglieFS 
Name:		perl-MogileFS-Client
Version:	1.08
Release:	1
# same as perl 
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/B/BR/BRADFITZ/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2d7a6853100566496c408c752408442d
URL:		http://search.cpan.org/dist/MogileFS-Client/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-IO-stringy >= 2.102
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a client library for the MogileFS distributed file system. The
class method 'new' creates a client object against a particular mogilefs
tracker and domain. This object may then be used to store and retrieve content
easily from MogileFS.


#%description -l pl.UTF-8
#Ten modu³ jest klientem dla rozproszonego systemu plików MogileFS. Metoda 'new'
#tworzy obiekt klienta skojarzony z konkretnym sledz±cym mogilefs i domen±. 
#Ten obiekt mo¿e byæ u¿ywany jako interfejs do zapisywania i odtwarzania tre¶ci z
#MogileFS.
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES TODO
%{perl_vendorlib}/MogileFS/*.pm
#%%{perl_vendorlib}/MogileFS/Client
%{_mandir}/man3/*
