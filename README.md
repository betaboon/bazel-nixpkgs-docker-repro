# bazel-nixpkgs-docker-repro

## on ubuntu the following succeeds

- `bazel build //python:main`
- `bazel run //python:main`
- `bazel build //python:main_container`
- `bazel run //python:main_container` (see output below)

`bazel run //python:main_container`-output:
```
/home/username/.cache/bazel/_bazel_username/d166340fa83f2eb4af511f78600c5ae9/execroot/__main__/bazel-out/k8-fastbuild-ST-4a519fd6d3e4/bin/python/main_container.executable: line 119: python: command not found
Loaded image ID: sha256:f3fe8843bc8afadc275e7dc51483486a2a6e2b3da30f199aeecc738546df6b47
Tagging f3fe8843bc8afadc275e7dc51483486a2a6e2b3da30f199aeecc738546df6b47 as bazel/python:main_container
```

running that image works:
```
$ docker run --rm -it f3fe8843bc8afadc275e7dc51483486a2a6e2b3da30f199aeecc738546df6b47
Hello Python 3.9.10
```

## on nixos the following succeeds

- `bazel build --config=nix //python:main`

## on nixos the following fails

- `bazel run --config=nix //python:main` (works when removing `container_repositories_python3()` from WORKSPACE)
- `bazel build --config=nix //python:main_container`
- `bazel run --config=nix //python:main_container`
