# rust-rpm-daemon primer


## host info
```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.4 LTS
Release:	18.04
Codename:	bionic
```

## local cargo setup
![cargo-rpm](https://crates.io/crates/cargo-rpm)


### steps
```
$ cargo install cargo-rpm
```
```
$sudo apt install rpm
```

## this is run once (this repo already initialized)

```
cargo rpm init \
 --service ./etc/systemd/rust-rpm-daemon.service \
 --systemd
```


## to build
```
$ cargo rpm build
   Compiling rust-rpm-daemon v0.1.0 (/home/soleinik/work/rust/rust-pkg-rpm)
    Finished release [optimized] target(s) in 0.20s
    Building rust-rpm-daemon-0.1.0-1.rpm (using rpmbuild 4.14.1)
    Finished rust-rpm-daemon-0.1.0-1.rpm: built in 0 secs

$ tree target/release/rpmbuild/
target/release/rpmbuild/
├── BUILD
│   └── rust-rpm-daemon-0.1.0
│       └── usr
│           ├── lib
│           │   └── systemd
│           │       └── system
│           │           └── rust-rpm-daemon.service
│           ├── local
│           │   ├── bin
│           │   │   └── rust-rpm-daemon
│           │   └── etc
│           │       └── rust-rpm-daemon
│           │           └── rust-rpm-daemon.conf
│           └── share
│               ├── doc
│               │   └── rust-rpm-daemon
│               │       ├── COPYRIGHT
│               │       └── LICENSE
│               └── info
│                   └── rust-rpm-daemon.info
├── BUILDROOT
├── RPMS
│   └── x86_64
│       └── rust-rpm-daemon-0.1.0-1.x86_64.rpm
├── SOURCES
│   └── rust-rpm-daemon-0.1.0.tar.gz
├── SPECS
│   └── rust-rpm-daemon.spec
├── SRPMS
│   └── rust-rpm-daemon-0.1.0-1.src.rpm
└── tmp

21 directories, 10 files

```
