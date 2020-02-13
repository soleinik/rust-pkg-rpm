use std::thread;
use std::time::Duration;

//https://docs.fedoraproject.org/en-US/packaging-guidelines/Rust/

//https://pagure.io/fedora-rust/rust2rpm

fn main() {

    loop{
        println!("Hello, world!");
        thread::sleep(Duration::from_secs(5));
    }
}
