#!/usr/bin/python3

from plumbum import local

for path in local.path('../bevy-yoleck/target/wasm32-unknown-unknown/release/examples/'):
    if '-' in path.name:
        continue
    path.copy('.')
