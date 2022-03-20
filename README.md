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

### `bazel run --config=nix //python:main`

(works when removing `container_repositories_python3()` from WORKSPACE)

output:
```
INFO: Analyzed target //python:main (0 packages loaded, 0 targets configured).
INFO: Found 1 target...
Target //python:main up-to-date:
  bazel-bin/python/main
INFO: Elapsed time: 0.242s, Critical Path: 0.00s
INFO: 1 process: 1 internal.
INFO: Build completed successfully, 1 total action
INFO: Build completed successfully, 1 total action
Traceback (most recent call last):
  File "/home/betaboon/.cache/bazel/_bazel_betaboon/5c788199deb6914fac7d17e54410c820/execroot/__main__/bazel-out/k8-fastbuild/bin/python/main", line 392, in <module>
    Main()
  File "/home/betaboon/.cache/bazel/_bazel_betaboon/5c788199deb6914fac7d17e54410c820/execroot/__main__/bazel-out/k8-fastbuild/bin/python/main", line 382, in Main
    os.execv(args[0], args)
FileNotFoundError: [Errno 2] No such file or directory: '/home/betaboon/.cache/bazel/_bazel_betaboon/5c788199deb6914fac7d17e54410c820/execroot/__main__/bazel-out/k8-fastbuild/bin/python/main.runfiles/python3_9_x86_64-unknown-linux-gnu/bin/python3'
```

### `bazel build --config=nix //python:main_container`

output:
```
INFO: Repository bazel_gazelle_go_repository_tools instantiated at:
  /home/betaboon/src/bazel/bazel-nixpkgs-docker-repro/WORKSPACE.bazel:122:21: in <toplevel>
  /home/betaboon/.cache/bazel/_bazel_betaboon/5c788199deb6914fac7d17e54410c820/external/bazel_gazelle/deps.bzl:75:24: in gazelle_dependencies
Repository rule go_repository_tools defined at:
  /home/betaboon/.cache/bazel/_bazel_betaboon/5c788199deb6914fac7d17e54410c820/external/bazel_gazelle/internal/go_repository_tools.bzl:117:38: in <toplevel>
ERROR: An error occurred during the fetch of repository 'bazel_gazelle_go_repository_tools':
   Traceback (most recent call last):
	File "/home/betaboon/.cache/bazel/_bazel_betaboon/5c788199deb6914fac7d17e54410c820/external/bazel_gazelle/internal/go_repository_tools.bzl", line 85, column 17, in _go_repository_tools_impl
		fail("list_repository_tools_srcs: " + result.stderr)
Error in fail: list_repository_tools_srcs: env: ‘/home/betaboon/.cache/bazel/_bazel_betaboon/5c788199deb6914fac7d17e54410c820/external/go_sdk/bin/go’: No such file or directory
ERROR: /home/betaboon/src/bazel/bazel-nixpkgs-docker-repro/WORKSPACE.bazel:122:21: fetching go_repository_tools rule //external:bazel_gazelle_go_repository_tools: Traceback (most recent call last):
	File "/home/betaboon/.cache/bazel/_bazel_betaboon/5c788199deb6914fac7d17e54410c820/external/bazel_gazelle/internal/go_repository_tools.bzl", line 85, column 17, in _go_repository_tools_impl
		fail("list_repository_tools_srcs: " + result.stderr)
Error in fail: list_repository_tools_srcs: env: ‘/home/betaboon/.cache/bazel/_bazel_betaboon/5c788199deb6914fac7d17e54410c820/external/go_sdk/bin/go’: No such file or directory
ERROR: /home/betaboon/.cache/bazel/_bazel_betaboon/5c788199deb6914fac7d17e54410c820/external/io_bazel_rules_docker/container/go/cmd/join_layers/BUILD:3:11: no such package '@com_github_pkg_errors//': no such package '@bazel_gazelle_go_repository_config//': no such package '@bazel_gazelle_go_repository_tools//': list_repository_tools_srcs: env: ‘/home/betaboon/.cache/bazel/_bazel_betaboon/5c788199deb6914fac7d17e54410c820/external/go_sdk/bin/go’: No such file or directory
 and referenced by '@io_bazel_rules_docker//container/go/cmd/join_layers:go_default_library'
ERROR: Analysis of target '//python:main_container' failed; build aborted:
INFO: Elapsed time: 0.289s
INFO: 0 processes.
FAILED: Build did NOT complete successfully (1 packages loaded, 45 targets configured)
    Fetching @com_github_google_go_containerregistry; Restarting.
    Fetching @com_github_pkg_errors; Restarting.
    Fetching @bazel_gazelle_go_repository_config; Restarting.
```

### `bazel run --config=nix //python:main_container`
