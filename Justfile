css:
    npx @tailwindcss/cli -i ./src/input.css -o ./dist/tailwind.css

css-nix:
    nix run nixpkgs#tailwindcss -- -i ./static/css/input.css -o ./static/css/style.css -c tailwind.config.js 

