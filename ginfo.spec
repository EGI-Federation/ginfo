Name: ginfo
Version: 1.9.0
Release: 1%{?dist}
Summary: A versatile tool for discovering Grid services
Group: Applications/Internet
License: ASL 2.0
URL: https://github.com/EGI-Federation/ginfo

Source: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: rsync
BuildRequires: make
Requires: python3-ldap

%description
A versatile tool for discovering Grid services by querying either
LDAP-based Grid information services or the EMI Registry.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/ginfo
%{_mandir}/man1/ginfo.1*
%doc %{_docdir}/%{name}-%{version}/README.md
%doc %{_docdir}/%{name}-%{version}/AUTHORS.md
%license %{_datadir}/licenses/%{name}-%{version}/COPYRIGHT
%license %{_datadir}/licenses/%{name}-%{version}/LICENSE.txt

%changelog
* Mon Mar 20 2023 Baptiste Grenier <baptiste.grenier@egi.eu> - 1.10.0-1
- Update source URL information, package additional documentation, build using AlmaLinux. (#3) (Baptiste Grenier)

* Fri Aug 29 2014 Ivan Calvet <ivan.calvet@cern.ch> - 1.9.0-1
- Beta version for the version 2 of ginfo which allow requests on multiple objects

* Wed Oct 2 2013 Laurence Field <laurence.field@cern.ch> - 1.0.3-1
- Added support for Storage Shares

* Thu May 23 2013 Laurence Field <laurence.field@cern.ch> - 1.0.2-1
- Minor cosmetic improvements

* Thu Apr 25 2013 Laurence Field <laurence.field@cern.ch> - 1.0.1-1
- Refactored version enabling general GLUE 2.0 queries

* Thu Oct 25 2012 Laurence Field <laurence.field@cern.ch> - 0.2.4-1
- Added -b --bind option.

* Wed Aug 29 2012 Laurence Field <laurence.field@cern.ch> - 0.2.3-1
- Improved the EMI output.

* Thu Jul 19 2012 Laurence Field <laurence.field@cern.ch> - 0.2.2-1
- Added a timeout for the queries. 

* Fri Jul 13 2012 Laurence Field <laurence.field@cern.ch> - 0.2.1-2
- Initial version
