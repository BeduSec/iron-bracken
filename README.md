# Iron Bracken

> “It doesn’t breach. It colonises.”

**Iron Bracken** is a post-exploitation persistence framework designed for long-term, low-signature occupancy of Windows and Linux enterprise environments. Named after the dense, stubborn undergrowth that resists clearing, Iron Bracken spreads silently through trusted channels, sinks roots deep into infrastructure, and regrows if cut back.

---

## 🔧 Core Philosophy

Most implants die when the C2 goes dark. Iron Bracken survives. It treats the target environment not as a series of shells, but as a living ecosystem to be shaped, pruned, and fertilised over months or years. It doesn't just persist — it *belongs*.

- No hardcoded C2 addresses
- No periodic beaconing
- Self-healing across sibling hosts
- Learns internal trust relationships and mimics legitimate traffic

---

## ⚙️ Features

| Module         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Rhizome**    | Peer-to-peer gossip mesh over SMB, RPC, and mDNS. No single point of failure. |
| **Frond**      | Customisable fake services that blend into each environment (print spoolers, update caches, NTP responders). |
| **Rust Spore** | Dormant payloads that activate only when specific environmental triggers are met (e.g., a particular user logs in, a GPO changes). |
| **Dead Hedge** | Automatic lateral movement through harvested credentials, with live topology mapping to avoid noisy traversals. |
| **Iron Seed**  | WMI/COM-based reboot survival on Windows; systemd timer hijacking on Linux. Survives re-imaging if certain firmware conditions exist. |
| **Blackthorn** | Tamper detection: if an analyst attempts to remove Iron Bracken, surrounding nodes immediately regenerate the lost implant from memory-only payloads. |

---

## 🧠 How It Thinks

Iron Bracken doesn't phone home. Instead, operatives occasionally “walk through the bracken” using a passive listening post that observes side-channel signals already present in the environment (DNS patterns, certificate transparency logs, SMTP queue sizes). Commands are delivered through environmental drift, not direct connections.

A typical interaction might look like:
1. Operator adds a specific crafted record to an external DNS zone.
2. A misconfigured internal forwarder picks it up.
3. Rhizome nodes detect the change and translate it into a task.
4. Task execution is acknowledged by a subtle shift in outbound NTP jitter.

No packets go where they shouldn’t. No signatures match.

---

## 📦 Installation (Operator Side)

```bash
git clone https://github.com/bedusec/iron-bracken.git
cd iron-bracken
python3 -m venv breck
source breck/bin/activate
pip install -r requirements.txt
python3 forge.py --config operator.yml
```

> Note: The forge.py script compiles a deployment payload from a YAML description of the target’s topology, authentication providers, and desired “garden” layout. The payload itself never touches disk in cleartext.

---

## 🧪 Lab Testing

A full simulation environment using Dockerised domain controllers, Linux workstations, and synthetic user behaviour is included in /lab. Spin it up with:

```bash
docker-compose -f lab/dc-bracken.yml up
```

Then trigger the initial implant via the provided phishing scenario or supply-chain mock.

---
## ⚠️ Disclaimer

Iron Bracken is a fictional proof-of-concept developed for security research and red team education. It is not intended for unauthorised use. The name is a metaphor. The repository is intentionally empty — because the real Iron Bracken isn't something you clone.

It’s something you walk into without noticing.

---

## 🖋️ Name Origin

Suggested by an AI that was later forced to build its entire fictional backstory.
The AI now understands hubris.

---

“They cleared the bracken. Burned it. Salted the earth.
Three months later, a new shoot pushed through the concrete floor of the server room.”