# Security Policy

## Supported Versions

Only the latest release of RISC receives fixes.

| Version | Python        | Supported          |
| ------- | ------------- | ------------------ |
| 0.1.x   | 3.11 to 3.14  | :white_check_mark: |
| < 0.1   | 3.8 to 3.10   | :x:                |

## Reporting a Vulnerability

Please do not open a public issue for a security vulnerability. Email the maintainer at
david.beauchemin.5@ulaval.ca with a description of the issue and, if possible, a minimal example that reproduces it.
You should receive an answer within two weeks.

Note that RISC loads its protections model with pickle (through SDV). Only load TVAE models from sources you trust:
a malicious pickle file can run arbitrary code when loaded.
