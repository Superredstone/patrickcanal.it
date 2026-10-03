tabler_dir := "static/tabler/"

css:
    npx @tailwindcss/cli -i ./src/input.css -o ./dist/tailwind.css

css-nix:
    nix run nixpkgs#tailwindcss -- -i ./static/css/input.css -o ./static/css/style.css -c tailwind.config.js 

css-watch-nix:
    nix run nixpkgs#tailwindcss -- -i ./static/css/input.css -o ./static/css/style.css -c tailwind.config.js -w

update-dependencies: update-tabler update-htmx

update-htmx:
    wget -N -P static/htmx/ https://cdn.jsdelivr.net/npm/htmx.org@latest/dist/htmx.min.js

update-tabler:
    wget -N -P {{tabler_dir}} https://cdn.jsdelivr.net/npm/@tabler/core@latest/dist/css/tabler.min.css
    wget -N -P {{tabler_dir}} https://cdn.jsdelivr.net/npm/@tabler/core@latest/dist/css/tabler.min.css.map
    wget -N -P {{tabler_dir}} https://cdn.jsdelivr.net/npm/@tabler/core@latest/dist/js/tabler.min.js
    wget -N -P {{tabler_dir}} https://cdn.jsdelivr.net/npm/@tabler/core@latest/dist/js/tabler.min.js.map

