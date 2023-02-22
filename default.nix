{ pkgs ? import <nixpkgs> {} }:

pkgs.stdenv.mkDerivation {
    Artifactors = pkgs.python3Packages.buildPythonPackage {
        name = "Artifactors";
        src = ./.;
        nativeBuildInputs = with pkgs; [
            python310
            python310Packages.numpy
            python310Packages.scipy
            python310Packages.matplotlib
        ];
    };

}