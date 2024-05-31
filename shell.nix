{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  nativeBuildInputs = with pkgs; [
    # all packages go here
    feh
    python3
    python311Packages.pillow
  ];
}
