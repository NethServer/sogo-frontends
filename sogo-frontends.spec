%define destdir root%{_datadir}/nethserver/sogo-frontends
%define templatedir root%{_nstemplatesdir}/sogo-frontends

Name:		sogo-frontends
Version:	1.4.0
Release:	1%{dist}
Summary:	SOGo Thunderbird frontends bundle
License:	GPL
URL:		%{url_prefix}/%{name}
BuildArch:	noarch
Source0:	%{name}-%{version}.tar.gz
Source1:        http://www.sogo.nu/files/downloads/SOGo/Thunderbird/sogo-integrator-31.0.1-sogo-demo.xpi
Source2:        http://www.sogo.nu/files/downloads/SOGo/Thunderbird/sogo-connector-31.0.1.xpi

BuildRequires: nethserver-devtools

%description
SOGo Thunderbird frontends bundle

%prep
%setup

%build
%__install -d %{destdir} %{templatedir}
%__install -m 0644 %_sourcedir/*.xpi %{destdir}
%__install -m 0644 MANIFEST* %{destdir}
%__install -m 0644 *.patch %{templatedir}
./createlinks

%install
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Tue Mar 10 2015 Stefano Fancello <stefano.fancello@nethesis.it> - 1.4.0-1.ns6
- Thunderbird 31 add-ons. Refs #2961
- Fix sogo-connector not downloaded automatically with Thunderbird 31 - Bug #2961 [NethServer]

* Wed Feb 26 2014 Davide Principi <davide.principi@nethesis.it> - 1.3.0-1.ns6
- TimeZone with unknown format blocks Mozilla Lightning - Bug #2632 [NethServer]
- Drop old TB plugins. Only TB24 is supported.

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.2.0-1.ns6
- Thunderbird 24 support - Enhancement #2535 [NethServer]
- Upgrade SOGo to release 2.1.1b - Enhancement #2457 [NethServer]

* Wed Dec 18 2013 Davide Principi <davide.principi@nethesis.it> - 1.1.1-1.ns6
- Removed %post scriptlet. Refs #2029

* Tue Apr 30 2013 Davide Principi <davide.principi@nethesis.it> - 1.1.0-1.ns6
- Added support for TB17

* Fri Feb  8 2013 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1.ns6
- Initial version




