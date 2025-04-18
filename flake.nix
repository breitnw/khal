{
  inputs = { nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable"; };
  outputs = { self, nixpkgs }:
    let pkgs = nixpkgs.legacyPackages.aarch64-linux;
    in {
      # replace 'joes-desktop' with your hostname here.
      packages.aarch64-linux.default = pkgs.callPackage ./khal.nix { };
    };
}
