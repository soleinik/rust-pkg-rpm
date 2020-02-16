# rust-rpm-app primer

## host info
```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.4 LTS
Release:	18.04
Codename:	bionic
```
<br/>

## local cargo setup
![cargo-rpm](https://crates.io/crates/cargo-rpm)

<br/>

## steps
```
$ cargo install cargo-rpm
```

```
$ sudo apt install rpm
 ```
<br/>

## this is run once to init (this repo already initialized)
```
$ cargo rpm init
Created /home/soleinik/work/rust/rust-pkg-rpm/.rpm
Rendered /home/soleinik/work/rust/rust-pkg-rpm/.rpm/rust-rpm-daemon.spec
Updating /home/soleinik/work/rust/rust-pkg-rpm/Cargo.toml
Finished rust-rpm-daemon configured (type "cargo rpm build" to build)
```




## to build
```
$ cargo rpm build
   Compiling rust-rpm-daemon v0.1.0 (/home/soleinik/work/rust/rust-pkg-rpm)
   Finished release [optimized] target(s) in 0.21s
   Building rust-rpm-daemon-0.1.0-1.rpm (using rpmbuild 4.14.1)

$ tree target/release/rpmbuild/
    target/release/rpmbuild/
    ├── BUILD
    │   └── rust-rpm-daemon-0.1.0
    │       └── usr
    │           ├── bin
    │           │   └── rust-rpm-daemon
    │           └── share
    │               ├── doc
    │               │   └── rust-rpm-daemon
    │               │       ├── COPYRIGHT
    │               │       └── LICENSE
    │               ├── etc
    │               │   └── rust-rpm-daemon
    │               │       └── rust-rpm-daemon.conf
    │               └── info
    │                   └── rust-pkg-rpm.info
    ├── BUILDROOT
    │   └── rust-rpm-daemon-0.1.0-1.x86_64
    │       └── usr
    │           ├── bin
    │           │   └── rust-rpm-daemon
    │           ├── lib
    │           └── share
    │               ├── doc
    │               │   └── rust-rpm-daemon
    │               │       ├── COPYRIGHT
    │               │       └── LICENSE
    │               ├── etc
    │               │   └── rust-rpm-daemon
    │               │       └── rust-rpm-daemon.conf
    │               └── info
    │                   └── rust-pkg-rpm.info.gz
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

    27 directories, 14 files

```