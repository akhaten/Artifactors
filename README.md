# Artifactors
Python module to add artefacts into image

Artifacts are abberations into an image. They can be provide by several ways.
You can find two examples in
[examples](https://github.com/akhaten/Artifactors/tree/main/examples).


# Installation

## Nix

### Build from source (fetch from github)

Fetch from github will build package from [default.nix](https://github.com/akhaten/Artifactors/blob/main/default.nix) 

In `shell.nix` file :
```nix
{ pkgs ? import <nixpkgs> {} }:

let

    Artifactors = pkgs.fetchgit {
        url = "https://github.com/akhaten/Artifactors.git";
        sha256 = "sha256-oL9JUVu/hDgcW8tpQ2gx12StAw6+/Mg4Q9mybSiaQ+o=";
        #sha256 = "sha256-0000000000000000000000000000000000000000000=";
    };

in pkgs.mkShell {

    buildInputs = with pkgs; [
        python310
        (callPackage Artifactors {})
    ];

}
```

then in your terminal:

```bash
nix-shell shell.nix
```

### Build from source (clone from github)

```bash
git clone https://github.com/akhaten/Artifactors.git
or git clone git@github.com:akhaten/Artifactors.git
```

then in shell.nix file:

```nix
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {

    buildInputs = with pkgs; [
        python310
        (callPackage path/of/Artifactors {})
    ];

}
```

then in your terminal:
```bash
nix-shell shell.nix
```

## Pip

```bash
pip -m venv venv
cd venv
source ./bin/activate
pip install -U git+https://github.com/akhaten/Artifactors.git
```