%define fedir root/usr/share/nethserver/sogo-frontends
Name:		sogo-frontends
Version: 1.4.1
Release: 1%{?dist}
Summary:	SOGo Thunderbird frontends bundle
License:	GPL
URL:		%{url_prefix}/%{name}
BuildArch:	noarch
Source0: %{name}-%{version}.tar.gz
Source1: http://packages.inverse.ca/SOGo/thunderbird/nightly/sogo-connector-31.0.4-693129fa0d.xpi
Source2: http://packages.inverse.ca/SOGo/thunderbird/nightly/sogo-integrator-31.0.4-f4f08aa3f2-sogo-demo.xpi

BuildRequires: nethserver-devtools

%description
SOGo Thunderbird frontends bundle

%prep
%setup


%build
perl createlinks

%install
mkdir -p %{fedir}
mv -v MANIFEST-sogo-frontends.tsv %{fedir}
mv -v %{SOURCE1} %{fedir}/sogo-connector-31.0.4.xpi
mv -v %{SOURCE2} %{fedir}/sogo-integrator-31.0.4-sogo-demo.xpi
(cd root; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%post

%changelog
* Thu May 25 2017 Davide Principi <davide.principi@nethesis.it> - 1.4.1-1
- Thunderbird 52 extensions for SOGo - #3441

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




