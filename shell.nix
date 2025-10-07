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
  ];
}
