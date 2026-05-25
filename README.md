<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1A3C5E,100:0d1117&height=120&section=header" width="100%"/>

# Nouha Sedraoui
### Cybersecurity Engineer · SOC · Threat Intelligence · Web Application Security

*Engineering graduate. Real labs. Real investigations. Zero fluff.*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nouha_Sedraoui-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nouha-sedraoui)
[![Medium](https://img.shields.io/badge/Medium-@ryxocrypt-000000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@ryxocrypt)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:Nouha.Sedraoui@esprit.tn)
[![Location](https://img.shields.io/badge/🇹🇳_Tunisia-Ariana-1DB954?style=for-the-badge)](.)

</div>

---

## Who I Am

I'm a Cybersecurity Engineering graduate from ESPRIT Tunisia (specialization: Network Infrastructure & Data Security), and I work at the intersection of **threat detection**, **web application security**, and **SOC operations**.

I don't collect theory. I build things, break things, and document everything:

- 🔵 **Built a full SOC** at Next Step IT using Wazuh + ELK, with Active Response automation, APT correlation rules, and MISP threat intelligence integration
- 🔵 **Shipped CyberAudit Pro** — an AI-driven audit platform unifying 14 scanning tools, powered by a multi-model AI pipeline (DeepSeek, Grok, Llama, Mistral via Ollama), ISO 27001-aligned
- 🔵 **Investigated Splunk BOTSv1** — completed both scenarios, scored **16,193 with zero penalties**, traced the full Cerber v2 ransomware kill chain across Sysmon, Suricata, stream:dns, and stream:smb
- 🔵 **Published CVE analysis** on Medium (@ryxocrypt) — in-depth breakdown of CVE-2026-34197, an Apache ActiveMQ RCE that sat hidden for 13 years and is now actively exploited

```
Active on:    PortSwigger Web Academy · TryHackMe · Splunk BOTS
Writing at:   medium.com/@ryxocrypt  (threat intel, CVE breakdowns)
Building:     cybersecurity-portfolio 
```

---

## 🏆 Highlight: Splunk BOTSv1 — Cerber v2 Ransomware Investigation

> *Boss of the SOC is Splunk's flagship threat hunting competition — real attack data, real questions, zero hints.*

| Metric | Result |
|--------|--------|
| Final Score | **16,193** |
| Penalties | **0** |
| Scenarios Completed | Both (APT + Ransomware) |
| Kill Chain Reconstructed | Cerber v2 — full chain |
| Log Sources Analyzed | Sysmon · Suricata · stream:dns · stream:smb |

📄 Full report → [`soc-labs/splunk-bots/botsv1-ransomware-report.pdf`](./soc-labs/splunk-bots/botsv1-ransomware-report.pdf)  
📝 Investigation notes → [`soc-labs/splunk-bots/botsv1-investigation-notes.md`](./soc-labs/splunk-bots/botsv1-investigation-notes.md)

---

## 🛠 Technical Stack

<details>
<summary><b>Security Operations & SIEM</b></summary>

Wazuh · ELK Stack · Splunk · Microsoft Sentinel · SecurityOnion · Kibana · Sguil · MISP · TheHive · Cortex

</details>

<details>
<summary><b>Vulnerability Assessment & Pentesting</b></summary>

Nmap · Burp Suite · OWASP ZAP · Nessus · Nuclei · SQLMap · Nikto · OpenVAS · Metasploit · Caldera · Kali Linux · Parrot OS

</details>

<details>
<summary><b>Network Security & Forensics</b></summary>

Suricata · Snort · Zeek · pfSense · OPNsense · Wireshark · Autopsy · FTK Imager · Volatility · SleuthKit

</details>

<details>
<summary><b>DevSecOps</b></summary>

Docker · Jenkins · GitLab CI · GitHub Actions · SonarQube · OWASP Dependency-Check · Trivy

</details>

<details>
<summary><b>AI for Security</b></summary>

OpenRouter API (DeepSeek · Grok · Llama · Qwen) · Ollama (Mistral) · LangChain · BERT · Prompt Engineering

</details>

<details>
<summary><b>Scripting & Development</b></summary>

Python · Bash · PowerShell · Django · REST APIs · Spring Boot (Java) · PostgreSQL

</details>

<details>
<summary><b>Compliance & Frameworks</b></summary>

ISO/IEC 27001 · NIST CSF · MITRE ATT&CK · CVSS · PCI DSS · HIPAA

</details>

---

## 📁 Repository Map

```
cybersecurity-portfolio/
│
├── 🌐 web-application-security/
│     ├── sql-injection/
│     │     └── portswigger-sqli-notes.md        ← All PortSwigger SQLi labs
│     └── server-side-vulnerabilities/
│           └── server-side-vulns-notes.md        ← Path traversal, SSRF, file upload, cmdi
│
├── 🕵️ threat-intelligence/
│     ├── cve-analysis-template.md
│     ├── cpanel-cve-may-2026.md                  ← Code exec + privesc in cPanel/WHM
│     ├── cve-2026-7482-bleeding-llama.md         ← OOB Read, 300k+ servers exposed
│     └── sans-moab-webcast-2026.md
│
├── 🔵 soc-labs/
│     └── splunk-bots/
│           ├── botsv1-investigation-notes.md     ← Full Cerber v2 investigation
│           └── botsv1-ransomware-report.pdf      ← Final incident report (score: 16,193)
│
├── 📜 certifications/
│     ├── fortinet-fcf-notes.md
│     └── fortigate-administrator-notes.md
│
└── 📚 resources/
      └── protocol-security-reference.md          ← 70+ protocols: attacks, tools, defenses
```

---

## 📌 Featured Work

| Work | Category | What's Inside |
|------|----------|---------------|
| [BOTSv1 Ransomware Report](./soc-labs/splunk-bots/botsv1-ransomware-report.pdf) | SOC / DFIR | Cerber v2 kill chain · Score 16,193 · Zero penalties |
| [SQL Injection Notes](./web-application-security/sql-injection/portswigger-sqli-notes.md) | Web Security | Full PortSwigger SQLi lab series — every technique |
| [Server-Side Vulnerabilities](./web-application-security/server-side-vulnerabilities/server-side-vulns-notes.md) | Web Security | Path traversal · SSRF · File upload · Command injection |
| [Bleeding Llama CVE-2026-7482](./threat-intelligence/cve-2026-7482-bleeding-llama.md) | Threat Intel | AI platform OOB Read — 300k+ servers exposed |
| [cPanel Triple CVE — May 2026](./threat-intelligence/cpanel-cve-may-2026.md) | Threat Intel | Code execution + privilege escalation in cPanel/WHM |
| [Protocol Security Reference](./resources/protocol-security-reference.md) | Reference | 70+ protocols with attack vectors, tools, and defenses |
| [FortiGate Administrator Notes](./certifications/fortigate-administrator-notes.md) | Certification | Full FCA 15-module notes |

---

## 🎓 Certifications

| Certification | Issuer | Year |
|--------------|--------|------|
| Fortinet FCA — FortiGate Administrator (NSE 1 & 2) | Fortinet | 2026 |
| Cybersecurity Defense Analyst Career Path (Splunk & Cisco) | Cisco Netacad | 2026 |
| NVIDIA: Adversarial Machine Learning | NVIDIA | 2025 |
| Certified Cybersecurity Educator Professional (CCEP) | — | 2025 |
| Hedera Hashgraph Certified Developer | Hedera | 2024 |
| Cisco CyberOps Associate | Cisco Netacad | 2023 |
| Cisco CCNA Security | Cisco Netacad | 2023 |

*In progress: CEH · ISO/IEC 27001 Lead Auditor · Fortinet NSE 4 (Expected 2027)*

---

## ✍️ Writing — Medium @ryxocrypt

Published threat intelligence breakdowns for defenders:

- **[CVE-2026-34197: A Bug That Hid Inside Apache ActiveMQ for 13 Years](https://medium.com/@ryxocrypt/cve-2026-34197-a-bug-that-hid-inside-apache-activemq-for-13-years-and-now-its-being-exploited-ae0e17996ddc)** — Root cause, full attack chain, and detection guidance for an actively exploited RCE

More articles in progress.

---

<div align="center">

*Everything here is real lab work and hands-on analysis — updated regularly*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1A3C5E,100:0d1117&height=80&section=footer" width="100%"/>

</div>
