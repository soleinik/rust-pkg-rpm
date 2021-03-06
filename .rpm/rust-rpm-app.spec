%define __spec_install_post %{nil}
%define __os_install_post %{_dbpath}/brp-compress
%define debug_package %{nil}

Name: rust-rpm-app
Summary: Rust app, RPM packaged
Version: @@VERSION@@
Release: @@RELEASE@@
License: MIT or ASL 2.0
Group: Applications/System
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
gzip -9 %{buildroot}%{_infodir}/%{name}.info

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
%{_exec_prefix}/local/bin/*
%config(noreplace) %{_exec_prefix}/local%{_sysconfdir}/%{name}/%{name}.conf
%doc %{_docdir}/%{name}/COPYRIGHT
%license %{_docdir}/%{name}/LICENSE
%{_infodir}/%{name}.info.gz
