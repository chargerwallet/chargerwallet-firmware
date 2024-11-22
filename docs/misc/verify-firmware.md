We want to invite the wider community to participate in the verification of the firmware built by Chargerwallet. 

We do daily builds via github action, chargerwallet to multi-sign the firmware, and release official firmware.

The fingerprints of the CI builds are compared with the fingerprints of the official firmware for verification.

## Chargerwallet Mini firmware 

1. Download the official firmware from [here](https://github.com/chargerwallet/firmware/releases)

```
   wget https://github.com/chargerwallet/firmware/releases/download/mini%2Fv2.3.0/mini.2.3.0-Stable-0810-2bcc073.bin --no-check-certificate
```

2. Download the [artifacts](https://github.com/chargerwallet/firmware/actions/runs/2829420581) for the corresponding ci build and unzip it

```
  unzip firmware-e132e608d09fff246ba36ef7737a5ca403a2af09.zip -d ci
```

3. Verify firmware, Those two hashes should be equal
```
  tail -c +1024 mini.2.3.0-Stable-0810-2bcc073.bin | shasum -a 256
  tail -c +1024 ci/mini.2.3.0-Stable-0810-2bcc073.bin | shasum -a 256
```

## Chargerwallet Classic firmware 

See Chargerwallet Mini firmware

## Chargerwallet Touch firmware 

See Chargerwallet Mini firmware
