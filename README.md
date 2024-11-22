# Chargerwallet firmware

## 🚀 Getting Onboard

1. Install [nix](https://nixos.org/download.html)
2. Pulling the latest code via the git command line tool,  setting up the development environment

```
  git clone --recurse-submodules https://github.com/chargerwallet/chargerwallet-firmware.git
  cd chargerwallet-firmware
  nix-shell
  poetry install
```

3. Run the build with:

```
   cd core && poetry run make build_unix
```

4. Now you can start the emulator

```
   poetry run ./emu.py
```

5. You can now install the command line client utility to interact with the emulator

```
   cd python && poetry run python3 -m pip install .
```

## ✏ Contribute

- Adding a small feature or a fix

  If your change is somewhat subtle, feel free to file a PR in one of the appropriate repositories directly. See the PR requirements noted at [CONTRIBUTING.md](docs/misc/contributing.md)

- Add new coin/token/network to the official chargerwallet firmware

  See [COINS.md](docs/misc/COINS.md)

Also please have a look at the [docs](docs/SUMMARY.md) before contributing. The misc chapter should be read in particular because it contains some useful assorted knowledge.

## 🔒 Security

- Please report suspected security vulnerabilities in private to dev@chargerwallet.com
- Please do NOT create publicly viewable issues for suspected security vulnerabilities.