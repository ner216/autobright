Name:           autobright
Version:        1.0
Release:        1%{?dist}
Summary:        Automate screen and keyboard brightness using a webcam
License:        MIT
URL:            https://github.com/ner216/autobright
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       python3
Requires:       python3-numpy
Requires:       python3-opencv
Conflicts: proj-data-ar proj-data-at proj-data-au proj-data-be proj-data-br
Conflicts: proj-data-ca proj-data-ch proj-data-cz proj-data-de proj-data-dk
Conflicts: proj-data-es proj-data-eur proj-data-fi proj-data-fo proj-data-fr
Conflicts: proj-data-hu proj-data-is proj-data-jp proj-data-lv proj-data-mx
Conflicts: proj-data-nc proj-data-nl proj-data-no proj-data-nz proj-data-pl
Conflicts: proj-data-pt proj-data-se proj-data-si proj-data-sk proj-data-uk
Conflicts: proj-data-us proj-data-za
%{?systemd_requires}

%description
Autobright adjusts display and keyboard backlight levels based on the
ambient brightness measured using a webcam.

%prep
%autosetup

%build

%install
install -Dpm 0755 src/autobright %{buildroot}%{_bindir}/autobright
install -Dpm 0644 debian/autobright.service \
    %{buildroot}%{_unitdir}/autobright.service

%post
%systemd_post autobright.service
if [ "$1" -eq 1 ]; then
    systemctl enable --now autobright.service >/dev/null 2>&1 || :
fi

%preun
%systemd_preun autobright.service

%postun
%systemd_postun_with_restart autobright.service

%files
%license LICENSE
%doc README.md
%{_bindir}/autobright
%{_unitdir}/autobright.service