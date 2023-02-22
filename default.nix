{ system ? builtins.currentSystem } :

let pkgs = import <nixpkgs> { inherit system; };

in pkgs.python310Packages.buildPythonPackage {
	name = "Artifactors";
	src = ./.;
	propagatedBuildInputs = with pkgs; [
		python310
        python310Packages.numpy
        python310Packages.scipy
        python310Packages.matplotlib
	];
	doCheck = false;
}