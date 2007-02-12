%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	Finance
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}_CreditCard
Summary:	%{_pearname} - Validation class for Credit Cards
Summary(pl.UTF-8):   %{_pearname} - Klasa sprawdzająca poprawność dla kart kredytowych
Name:		php-pear-%{_pearname}
Version:	0.5.2
Release:	2
Epoch:		0
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a4eb8f52783b2f15ea99f0210ab1eda8
URL:		http://pear.php.net/package/Validate_Finance_CreditCard/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(pcre)
Requires:	php-common >= 3:4.2.0
Requires:	php-pear >= 4:1.0-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package to validate Credit Card numbers and types.

Although, still marked in alpha stage, the package is pretty stable.
There is currently no plan to change the API.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności numerów oraz typów kart kredytowych.

Chociaż oznaczony jako alpha, pakiet zachowuje się całkiem stabilnie.
Nie ma też planów zmiany API.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):   Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}/*

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
