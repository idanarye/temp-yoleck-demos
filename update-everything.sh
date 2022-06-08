wasm-bindgen ../bevy-yoleck/target/wasm32-unknown-unknown/release/examples/example2d.wasm --out-dir . --target web
wasm-bindgen ../bevy-yoleck/target/wasm32-unknown-unknown/release/examples/example3d.wasm --out-dir . --target web

cp ../bevy-yoleck/assets/levels2d/example.yol assets/levels2d/
cp ../bevy-yoleck/assets/levels3d/example.yol assets/levels3d/
