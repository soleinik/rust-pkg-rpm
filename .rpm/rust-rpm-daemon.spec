%define __spec_install_post %{nil}
%define __os_install_post %{_dbpath}/brp-compress
%define debug_package %{nil}

Name: rust-rpm-daemon
Summary: Rust daemon, RPM packaged
Version: @@VERSION@@
Release: @@RELEASE@@
License: MIT or ASL 2.0
Group: System Environment/Daemons
Source0: %{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: systemd

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
%{summary}

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp -a * %{buildroot}
gzip -9 %{buildroot}%{_infodir}/rust-pkg-rpm.info

%clean
rm -rf %{buildroot}

%systemd_post rust-rpm-daemon.service

%preun
%systemd_preun rust-rpm-daemon.service

%postun
%systemd_postun_with_restart rust-rpm-daemon.service

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_unitdir}/rust-rpm-daemon.service
%config(noreplace) %{_datadir}%{_sysconfdir}/%{name}/%{name}.conf
%doc %{_docdir}/%{name}/COPYRIGHT
%license %{_docdir}/%{name}/LICENSE
%{_infodir}/rust-pkg-rpm.info.gz
