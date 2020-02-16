%define __spec_install_post %{nil}
%define __os_install_post %{_dbpath}/brp-compress
%define debug_package %{nil}
%define _unitdir /usr/lib/systemd/system
 

Name: rust-rpm-daemon
Summary: Rust daemon, RPM packaged
Version: @@VERSION@@
Release: @@RELEASE@@
License: MIT or ASL 2.0
Group: System Environment/Daemons
Source0: %{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
#BuildRequires: systemd

#Requires(post): systemd
#Requires(preun): systemd
#Requires(postun): systemd

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
rm -rf %{buildroot}


#https://www.golinuxhub.com/2018/05/how-to-execute-script-at-pre-post-preun-postun-spec-file-rpm.html


%pre
echo "==> pre: $1 <=="

%post
echo "==> post: $1 <=="
systemctl enable %{name}.service
systemctl restart %{name}.service
echo "enabled/(re)started"

%preun
echo "==> preun: $1 <=="
if [ $1 == 0 ] ; then #removed
  systemctl disable %{name}.service
  systemctl stop %{name}.service
  echo "disabled/stoped"
fi

%postun
echo "==> postun: $1 <=="


%files
%defattr(-,root,root,-)
%{_exec_prefix}/local/bin/*
%config(noreplace) %{_exec_prefix}/local%{_sysconfdir}/%{name}/%{name}.conf
%doc %{_docdir}/%{name}/COPYRIGHT
%license %{_docdir}/%{name}/LICENSE
%{_infodir}/%{name}.info.gz
%{_unitdir}/%{name}.service
