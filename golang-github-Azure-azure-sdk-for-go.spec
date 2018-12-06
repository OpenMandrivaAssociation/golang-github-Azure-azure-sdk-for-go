# https://github.com/Azure/azure-sdk-for-go
%global goipath         github.com/Azure/azure-sdk-for-go
Version:                15.2.0

%gometa

Name:           golang-github-Azure-azure-sdk-for-go
Release:        2%{?dist}
Summary:        Microsoft Azure SDK for Go
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/Azure/go-autorest/autorest)
BuildRequires: golang(github.com/Azure/go-autorest/autorest/adal)
BuildRequires: golang(github.com/Azure/go-autorest/autorest/azure)
BuildRequires: golang(github.com/Azure/go-autorest/autorest/date)
BuildRequires: golang(github.com/Azure/go-autorest/autorest/to)
BuildRequires: golang(github.com/Azure/go-autorest/autorest/validation)
BuildRequires: golang(github.com/globalsign/mgo)
BuildRequires: golang(github.com/marstr/collection)
BuildRequires: golang(github.com/marstr/goalias/model)
BuildRequires: golang(github.com/marstr/guid)
BuildRequires: golang(github.com/marstr/randname)
BuildRequires: golang(github.com/mitchellh/go-homedir)
BuildRequires: golang(github.com/satori/go.uuid)
BuildRequires: golang(github.com/shopspring/decimal)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/spf13/viper)
BuildRequires: golang(golang.org/x/crypto/pkcs12)
BuildRequires: golang(golang.org/x/tools/imports)

# tests
BuildRequires: golang(github.com/dnaeon/go-vcr/cassette)
BuildRequires: golang(github.com/dnaeon/go-vcr/recorder)
BuildRequires: golang(gopkg.in/check.v1)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gobaseipath} prefix.

%prep
%gosetup

%install
%goinstall

%check
%gochecks -d storage

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 15.2.0-1
- Upstream release v15.2.0

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.2-0.10.20150612git97d9593
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.9.git97d9593
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.8.git97d9593
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.7.git97d9593
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.6.git97d9593
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 jchaloup <jchaloup@redhat.com> - 1.2-0.5.git97d9593
- Enable devel and unit-test for epel7
  resolves: #1365467

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.4.git97d9593
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.3.git97d9593
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.2.git97d9593
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 14 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git97d9593
- First package for Fedora
  resolves: #1262716
