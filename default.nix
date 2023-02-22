{ pkgs ? import <nixpkgs> {} }:

pkgs.stdenv.mkDerivation {
    Artifactors = pkgs.python3Packages.buildPythonPackage {
        name = "Artifactors";
        src = ./.;
    };
}