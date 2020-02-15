# rust-pkg-rpm primer

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
```
