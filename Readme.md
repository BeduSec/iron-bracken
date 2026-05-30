![](https://raw.githubusercontent.com/BeduSec/iron-bracken/main/ironb.png)
# Iron Bracken

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-orange)](setup.py)
[![Status](https://img.shields.io/badge/status-active-brightgreen)]()

**Iron Bracken** is a post-exploitation persistence framework designed for long-term, low-signature occupancy of Windows and Linux enterprise environments. Named after the dense, stubborn undergrowth that resists clearing, Iron Bracken spreads silently through trusted channels, sinks roots deep into infrastructure, and regrows if cut back.

## Philosophy

Most implants die when the C2 goes dark. Iron Bracken survives. It treats the target environment not as a series of shells, but as a living ecosystem to be shaped, pruned, and fertilised over months or years. It does not merely persist — it belongs.

- No hardcoded C2 addresses
- No periodic beaconing
- Self-healing across sibling hosts
- Learns internal trust relationships and mimics legitimate traffic

## Architecture

Iron Bracken is built around a modular core that enables operators to deploy, manage, and recover implants with minimal detectable footprint.

```

iron-bracken/
├── forge.py
├── setup.py
├── requirements.txt
└── iron_bracken/
├── rhizome.py
├── frond.py
├── rust_spore.py
├── dead_hedge.py
├── iron_seed.py
├── blackthorn.py
├── communicator.py
├── listener.py
├── crypto.py
├── config.py
├── utils.py
├── logger.py
├── cli.py
├── payloads/
│   ├── base.py
│   ├── windows.py
│   ├── linux.py
│   └── hybrid.py
├── transports/
│   ├── dns_transport.py
│   ├── smtp_transport.py
│   ├── ntp_transport.py
│   └── custom_transport.py
├── persistence/
│   ├── wmi_seed.py
│   ├── systemd_seed.py
│   └── registry_seed.py
├── evasion/
│   ├── timing.py
│   ├── noise_filter.py
│   └── mimicry.py
├── ops/
│   ├── operator.py
│   ├── garden.py
│   └── topology.py
├── tests/
│   ├── test_rhizome.py
│   ├── test_frond.py
│   ├── test_rust_spore.py
│   ├── test_crypto.py
│   ├── test_communicator.py
│   └── test_dead_hedge.py
└── simulation/
├── lab_manager.py
├── user_simulator.py
├── domain_controller.py
└── trigger.py

```

## Modules

### Rhizome
Peer-to-peer gossip mesh over SMB, RPC, and mDNS. No single point of failure. Nodes share state without a centralised controller.

### Frond
Customisable fake services that blend into each environment. Can mimic print spoolers, update caches, NTP responders, and other common services.

### Rust Spore
Dormant payloads that activate only when specific environmental triggers are met (e.g., a particular user logs in, a GPO changes). The payload remains inert until precisely needed.

### Dead Hedge
Automatic lateral movement through harvested credentials, with live topology mapping to avoid noisy traversals. Moves like routine administrative traffic.

### Iron Seed
WMI/COM-based reboot survival on Windows; systemd timer hijacking on Linux. Can survive re-imaging under certain firmware conditions.

### Blackthorn
Tamper detection and regeneration. If an analyst removes one implant, surrounding nodes immediately regenerate the lost implant from memory-only payloads.

## Communication

Iron Bracken does not phone home in a traditional sense. Operators "walk through the bracken" using a passive listening post that observes side-channel signals already present in the environment (DNS patterns, certificate transparency logs, SMTP queue sizes). Commands are delivered through environmental drift, not direct connections.

**A typical interaction**:
1. Operator adds a specific crafted record to an external DNS zone.
2. A misconfigured internal forwarder picks it up.
3. Rhizome nodes detect the change and translate it into a task.
4. Task execution is acknowledged by a subtle shift in outbound NTP jitter.

No packets go where they shouldn't. No signatures match.

## Installation

```bash
git clone https://github.com/bedusec/iron-bracken.git
cd iron-bracken
pip install -e .
```

## Usage

```bash
# Forge an implant from a configuration file
python forge.py operator.yml

# Launch the command-line interface
bracken config.yml gossip
```

## Testing

```bash
python -m unittest discover iron_bracken/tests
```

## Simulation Lab

A full simulation environment using Dockerised domain controllers, Linux workstations, and synthetic user behaviour is available. Spin it up with:

```bash
docker-compose -f lab/dc-bracken.yml up
```

## Disclaimer

Iron Bracken is a fictional proof-of-concept developed for security research and red team education. It is not intended for unauthorised use. The name is a metaphor. The repository is intentionally incomplete — the real bracken isn't something you clone. It's something you walk into without noticing.

## License

MIT License. See [LICENSE](LICENSE) for details.

---

"They cleared the bracken. Burned it. Salted the earth.
Three months later, a new shoot pushed through the concrete floor of the server room."