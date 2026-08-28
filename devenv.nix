{
  pkgs,
  ...
}:

{
  languages.python = {
    enable = true;
    version = "3.14";
    venv = {
      enable = true;
      requirements = ./requirements.txt;
    };

  };

  git-hooks.hooks = {
    ruff = {
      enable = true;
      package = pkgs.ruff;
      excludes = [ "migrations/" ];
    };
    djlint = {
      enable = true;
      name = "djlint";
      entry = "djlint --check .";
      types = [ "html" ];
    };
  };
}
