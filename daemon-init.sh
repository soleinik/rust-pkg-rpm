#!/bin/bash

cargo rpm init \
 --service ./etc/systemd/rust-rpm-daemon.service \
 --systemd
