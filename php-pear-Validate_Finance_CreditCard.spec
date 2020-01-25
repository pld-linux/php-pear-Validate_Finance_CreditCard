%define		_status		alpha
%define		_pearname	Validate_Finance_CreditCard
Summary:	%{_pearname} - Validation class for Credit Cards
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla kart kredytowych
Name:		php-pear-%{_pearname}
Version:	0.6.0
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	be20c565a7ecfbfdc71337e03be1be2c
URL:		http://pear.php.net/package/Validate_Finance_CreditCard/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php(pcre)
Requires:	php-pear >= 4:1.0-4
Obsoletes:	php-pear-Validate_Finance_CreditCard-tests
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
%{php_pear_dir}/Validate/Finance/*
