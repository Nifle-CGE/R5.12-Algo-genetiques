{
  pkgs ? import <nixpkgs> { },
}:

let
  pythonEnv = pkgs.python3.withPackages (ps: [
    ps.matplotlib
    ps.numpy
  ]);

in
pkgs.mkShell {
  packages = [
    pythonEnv
    pkgs.python3Packages.pip
  ];
  shellHook = ''
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
  '';
}
