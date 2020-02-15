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
#rm -rf %{buildroot}



%pre
echo "running pre-install instructions..."
exit 0

%post
echo "running post-install instructions..."
exit 0

%preun
echo "running pre-uninstall instructions..."
exit 0

%postun
echo "running post-uninstall instructions..."
exit 0


%files
%defattr(-,root,root,-)
%{_bindir}/*
%config(noreplace) %{_datadir}%{_sysconfdir}/%{name}/%{name}.conf
%doc %{_docdir}/%{name}/COPYRIGHT
%license %{_docdir}/%{name}/LICENSE
%{_infodir}/rust-pkg-rpm.info.gz
