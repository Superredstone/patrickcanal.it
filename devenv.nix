{
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
    ruff.enable = true;
    djlint = {
      enable = true;
      name = "djlint";
      entry = "djlint --check .";
      types = [ "html" ];
    };
  };
}
