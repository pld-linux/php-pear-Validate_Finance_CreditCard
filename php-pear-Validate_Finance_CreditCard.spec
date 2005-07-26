%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	Finance
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}_CreditCard

Summary:	%{_pearname} - Validation class for Credit Cards
Summary(pl):	%{_pearname} -
Name:		php-pear-%{_pearname}
Version:	0.5.1
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f64fb3e71e561cbcde700c171dcbc422
URL:		http://pear.php.net/package/Validate_Finance_CreditCard/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear >= 4:1.0-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package to validate Credit Card numbers and types.

Although, still marked in alpha stage, the package is pretty stable.
There is currently no plan to change the API.

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet do sprawdzania poprawno¶ci numerów oraz typów kart kredytowych.

Chocia¿ oznaczony jako alpha, pakiet zachowuje siê ca³kiem stabilnie.
Nie ma te¿ planów do zmiany API.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/%{_class}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests/
%{php_pear_dir}/%{_class}/%{_subclass}/*
