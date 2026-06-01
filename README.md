![header](https://capsule-render.vercel.app/api?type=waving&color=0,0d1117,0d1117&height=120&section=header&bg_color=0d1117)

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=13&duration=1&pause=999999&color=00FF33&center=true&vCenter=true&multiline=true&repeat=false&width=750&height=110&lines=++++_++_+++___+++_++_+++_++_++++_++++++___++___++___+++___++++_++++___+++_++_+++___+;++++|+%5C|+|+%2F+_+%5C+|+|+|+|+|+|+|++%2F_%5C++++%2F+__||+__||+++%5C+|+_+%5C++%2F_%5C++%2F+_+%5C+|+|+|+|+|_+_|;++++|+.%60+||+(_)+||+|_|+|+|+__+|%2F+_+%5C+++%5C__+%5C|+_|+|+|)+||+++%2F+_+%5C|+(_)+||+|_|+|++|+|+;++++|_%7C%5C_|+%5C___%2F++%5C___%2F++|_||_||_%2F+%5C_%5C+|___%2F|___||___%2F+|_%7C_%5C%2F_+%5C_%5C___%2F++%5C___%2F++|___|" alt="NOUHA SEDRAOUI ASCII" />

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=15&pause=1000&color=2358A6&center=true&vCenter=true&width=600&lines=%E2%9A%A1+SECURITY+OPERATIONS+CENTER+%2F%2F+CORE+OPERATOR+NODE+%E2%9A%A1" alt="subtitle" />

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-sedraoui--nouha-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/sedraoui-nouha)
[![Medium](https://img.shields.io/badge/Medium-%40ryxocrypt-000000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@ryxocrypt)
[![GitHub](https://img.shields.io/badge/GitHub-nouhasedraoui-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nouhasedraoui)
[![Email](https://img.shields.io/badge/Email-Nouha.Sedraoui%40esprit.tn-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:Nouha.Sedraoui@esprit.tn)
![Location](https://img.shields.io/badge/Tunisia-Ariana-20B2AA?style=for-the-badge&logo=google-maps&logoColor=white)

</div>

---

---

---

```bash
#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
#  SOC-OS v3.7.1  |  OPERATOR SESSION INIT  |  TLP:WHITE
#  Identity   : Nouha Sedraoui
#  Clearance  : SOC-ENGINEER // THREAT-HUNTER // WEB-APPSEC
#  Location   : Ariana, Tunisia  [TZ: Africa/Tunis]
# ─────────────────────────────────────────────────────────────────────────────

[BIOS]    POST check .................................................... 🟢 OK
[BOOT]    Loading SOC-OS kernel image .................................. 🟢 OK
[INIT]    Mounting encrypted volumes /sec /ops /intel .................. 🟢 OK
[INIT]    Starting entropy daemon (urandom) ............................ 🟢 OK

# ── THREAT DETECTION MODULES ─────────────────────────────────────────────────
[MOD]     Loading security stack...
          ├── wazuh-agent        SIEM + Active Response ............. 🟢 LOADED
          ├── elastic-stack      Log Aggregation / ELK .............. 🟢 LOADED
          ├── splunk-forwarder   Threat Hunting / BOTSv1 ............ 🟢 LOADED
          └── suricata-ids       Network IDS / Ruleset 42 ........... 🟢 LOADED

# ── THREAT INTELLIGENCE FEEDS ────────────────────────────────────────────────
[INTEL]   Pulling live feeds...
          ├── MISP sync .......................... 🟢  1,247 IOCs ingested
          ├── CVE database refresh ............... ⚠️   3 critical  |  0-day: 1
          ├── APT correlation rules .............. 🔵  91 TTPs mapped (MITRE)
          └── Dark web monitor ................... 🟢  no active mentions detected

# ── DFIR TOOLKIT ─────────────────────────────────────────────────────────────
[DFIR]    Initializing forensic suite...
          ├── Autopsy ................................................ 🟢 STANDBY
          ├── Volatility3 ............................................ 🟢 STANDBY
          ├── FTK Imager ............................................. 🟢 STANDBY
          └── Wireshark + Suricata PCAP engine ....................... 🟢 STANDBY

# ── OFFENSIVE RECON ──────────────────────────────────────────────────────────
[PENTEST] Loading offensive modules...
          ├── Burp Suite Pro (PortSwigger) ........................... 🟢 ACTIVE
          ├── Metasploit Framework 6.x ............................... 🟢 ACTIVE
          └── SQLMap / OWASP ZAP ..................................... 🟢 ACTIVE

# ── AUTH ─────────────────────────────────────────────────────────────────────
[AUTH]    Verifying operator credentials...
          ├── Identity     : Nouha Sedraoui
          ├── Clearance    : SOC-ENGINEER // THREAT-HUNTER // WEB-APPSEC
          ├── Session key  : 0xC8F3A2...E71D  [AES-256-GCM]
          └── Access       : 🟢 GRANTED

[SYS]     SOC-OS operational.  Threat posture: ⚠️ ELEVATED.
          Welcome back, Nouha. All systems green. Stay sharp. ▌
```

---

## ⚡ `[root@soc-ops ~]# cat who_am_i.log`

I'm a Cybersecurity Engineering graduate from ESPRIT Tunisia (specialization: Network Infrastructure and Data Security), working at the intersection of threat detection, SOC operations, and web application security.

I don't collect theory. I build things, break things, and document everything:

- Built a full SOC at Next Step IT using Wazuh + ELK Stack, with Active Response automation, APT correlation rules, and MISP threat intelligence integration
- Shipped CyberAudit Pro — an AI-driven audit platform unifying 14 scanning tools under a single Django interface, powered by a multi-model AI pipeline (DeepSeek, Grok, Llama, Qwen via OpenRouter + Mistral via Ollama), ISO 27001-aligned
- Investigated Splunk BOTSv1 — completed both scenarios, scored **16,193 with zero penalties**, traced the full Cerber v2 ransomware kill chain across Sysmon, Suricata, stream:dns, and stream:smb
- Published CVE analysis on Medium — in-depth breakdown of CVE-2026-34197, an Apache ActiveMQ RCE that sat hidden for 13 years and is now actively exploited
- Ranked **#1 in Bronze League** and climbed to **#1 in Silver League** on TryHackMe within consecutive weeks

---

## 🛡️ `[root@soc-ops ~]# ./thm_status.sh --operator rsd177`

```bash
[THM-API]  Querying TryHackMe operator profile: rsd177 ............. 🟢 200 OK
[THM-API]  Dashboard loaded — rendering operator telemetry...
```

<div align="center">

| Global Rank | Current Streak | Completed Rooms |
|:-----------:|:--------------:|:---------------:|
| 🌐 **Top 15%** | 🔥 **21 Days** | 🚪 **41 Rooms** |


### 🏅 EARNED SECURITY BADGES (8 OPERATIONAL)

| | | | |
|:-:|:-:|:-:|:-:|
| <img src="https://assets.tryhackme.com/img/badges/league-silver.png" width="80" alt="Silver League"/> | <img src="https://assets.tryhackme.com/img/badges/league-bronze.png" width="80" alt="Bronze League"/> | <img src="https://assets.tryhackme.com/img/badges/ai-odyssey-participation.svg" width="80" alt="AI Odyssey"/> | <img src="https://assets.tryhackme.com/img/badges/linux.png" width="80" alt="Linux"/> |
| **Silver League** | **Bronze League** | **AI Odyssey** | **cat linux.txt** |
| <img src="https://assets.tryhackme.com/img/badges/streak7.png" width="80" alt="7 Day Streak"/> | <img src="https://assets.tryhackme.com/img/badges/streak3.png" width="80" alt="3 Day Streak"/> | <img src="https://assets.tryhackme.com/img/badges/howthewebworks.png" width="80" alt="How The Web Works"/> | <img src="https://assets.tryhackme.com/img/badges/webbed.png" width="80" alt="Webbed"/> |
| **7 Day Streak** | **3 Day Streak** | **WWW** | **Webbed** |

</div>

---

## 📊 `[root@soc-ops ~]# ./render_dashboard.py --module highlights`

```bash
[DASHBOARD]  Compiling operational highlights ......................... 🟢 done
[DASHBOARD]  Rendering threat-hunting metrics and platform telemetry... 🟢 done
```

<div align="center">

| | Splunk BOTSv1 | CyberAudit Pro |
|---|---|---|
| **Type** | Threat Hunting Competition | AI-Driven Audit Platform (PFE) |
| **Score / Scale** | **16,193** — zero penalties | 14 scanning tools unified |
| **Scope** | Both scenarios completed | Multi-model AI pipeline |
| **Key Achievement** | Full Cerber v2 kill chain reconstructed | ISO 27001-aligned workflow |
| **Log Sources / Stack** | Sysmon · Suricata · stream:dns · stream:smb | DeepSeek · Grok · Llama · Qwen · Mistral |
| **Output** | Incident report + investigation notes | Certification-ready documentation |

</div>

---

## 💼 `[root@soc-ops ~]# cat /var/log/career/experience.log`

```bash
[EXP-LOG]  Parsing operator field deployments ......................... 🟢 done
[EXP-LOG]  3 engagements found — displaying chronological records.
```

**SmartSkills — Final Year Engineering Intern (PFE)** `Jan 2025 – Oct 2025`

Architected CyberAudit Pro, an AI-driven cybersecurity audit platform unifying 14 scanning tools (Nmap, OWASP ZAP, Nuclei, Nikto, SQLMap, Lynis) within a Django web application. Built a multi-model AI pipeline using OpenRouter (DeepSeek, Grok, Qwen, Llama) to automate vulnerability correlation and false-positive reduction across heterogeneous scan outputs. Designed an ISO 27001-aligned audit workflow with dual-stage AI analysis generating certification-ready documentation. Implemented offline, privacy-preserving analysis using Ollama-hosted Mistral and LangChain, with async scan orchestration via Python subprocess management and Paramiko SSH across a fully virtualized infrastructure.

**Next Step IT — SOC Engineering Intern** `Jun 2024 – Jul 2024`

Deployed Wazuh SIEM integrated with ELK Stack for centralized log management and advanced threat detection. Configured Active Response automation for real-time mitigation through IP blocking, process termination, and firewall rule updates. Deployed correlation rules to detect APT activity, brute-force attacks, and malware infections. Integrated MISP threat intelligence feeds to enrich security alerts with contextual vulnerability data.

**Tunisie Telecom — Network Monitoring Intern** `Jun 2023 – Jul 2023`

Deployed the EyesOfNetwork monitoring suite (Nagios, Cacti, NagVis, Weathermap) for real-time supervision of a large corporate infrastructure. Configured SNMP across Windows and Linux hosts and implemented customized Nagios checks for network devices with Cacti graphs for traffic analysis and capacity planning.

---

## 🔬 `[root@soc-ops ~]# ls -la /projects/academic/`

```bash
[FS]  Mounting project archive ........................................ 🟢 done
[FS]  4 entries found — access level: READ
```

**Healthcare SOC** `Dec 2023 – Jun 2024`
Designed and built a HIPAA-compliant SOC from scratch using SIEM and SOAR technologies. Developed threat hunting playbooks, alert triage workflows, and automated incident response procedures for a simulated healthcare environment.

**DevSecOps — Securing a Spring Boot CI/CD Pipeline** `Sep 2024 – Nov 2024`
Integrated SonarQube, OWASP Dependency-Check, and Trivy into a Jenkins and GitLab CI pipeline to automate security testing at every build stage. Reduced vulnerability exposure through policy-as-code deployment gates.

**Active Directory Identity and Access Management** `Mar 2024 – Jun 2024`
Deployed and hardened a Windows Active Directory environment. Used PingCastle for security posture scoring and Keycloak for federated identity and SSO management.

**Digital Forensics Investigation on Windows** `Sep 2024 – Nov 2024`
Performed a full forensic investigation on a compromised Windows machine using Autopsy, FTK Imager, SleuthKit, and memory analysis tools (PSList, ListDLL, PMDump, LogonSessions) to reconstruct the full attack timeline.

---

## ⚙️ `[root@soc-ops ~]# cat /etc/soc-os/arsenal.conf`

```bash
[ARSENAL]  Enumerating operator toolkit ................................ 🟢 done
[ARSENAL]  Cross-referencing MITRE ATT&CK tool mappings ............... 🟢 complete
```

### Languages

| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | ![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white) | ![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white) | ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) |
|---|---|---|---|

### SOC / SIEM

| ![Wazuh](https://img.shields.io/badge/Wazuh-005571?style=for-the-badge&logo=wazuh&logoColor=white) | ![Splunk](https://img.shields.io/badge/Splunk-000000?style=for-the-badge&logo=splunk&logoColor=white) | ![Elastic Stack](https://img.shields.io/badge/Elastic_Stack-005571?style=for-the-badge&logo=elastic&logoColor=white) | ![MISP](https://img.shields.io/badge/MISP-1A3C5E?style=for-the-badge&logoColor=white) | ![TheHive](https://img.shields.io/badge/TheHive-FFBE00?style=for-the-badge&logoColor=black) |
|---|---|---|---|---|

### Penetration Testing

| ![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=for-the-badge&logo=portswigger&logoColor=white) | ![Nmap](https://img.shields.io/badge/Nmap-0E83CD?style=for-the-badge&logo=nmap&logoColor=white) | ![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-00549E?style=for-the-badge&logo=owasp&logoColor=white) | ![Metasploit](https://img.shields.io/badge/Metasploit-2596CD?style=for-the-badge&logo=metasploit&logoColor=white) | ![SQLMap](https://img.shields.io/badge/SQLMap-CC0000?style=for-the-badge&logoColor=white) |
|---|---|---|---|---|

### DFIR / Network

| ![Autopsy](https://img.shields.io/badge/Autopsy_DFIR-2C3E50?style=for-the-badge&logoColor=white) | ![FTK Imager](https://img.shields.io/badge/FTK_Imager-4A4A4A?style=for-the-badge&logoColor=white) | ![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white) | ![Volatility](https://img.shields.io/badge/Volatility-4A90D9?style=for-the-badge&logoColor=white) | ![Suricata](https://img.shields.io/badge/Suricata-EF3B2D?style=for-the-badge&logoColor=white) |
|---|---|---|---|---|

### DevSecOps / Cloud

| ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) | ![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white) | ![GitLab CI](https://img.shields.io/badge/GitLab_CI-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white) | ![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=for-the-badge&logo=sonarqube&logoColor=white) | ![Trivy](https://img.shields.io/badge/Trivy-1904DA?style=for-the-badge&logo=aquasecurity&logoColor=white) |
|---|---|---|---|---|

---

## 🗂️ `[root@soc-ops ~]# tree ~/cybersecurity-portfolio --depth 3`

```bash
[FS]  Rendering portfolio directory structure ......................... 🟢 done
```

```
cybersecurity-portfolio/
│
├── web-application-security/
│     ├── sql-injection/
│     │     └── portswigger-sqli-notes.md          ← Full PortSwigger SQLi lab series
│     └── server-side-vulnerabilities/
│           └── portswigger-server-side-vulns-notes.md ← Path traversal, SSRF, file upload, cmdi
│
├── threat-intelligence/
│     ├── CVEs/
│     │     ├── cve-analysis-template.md
│     │     ├── cpanel-cve-may-2026.md             ← Code exec + privesc in cPanel/WHM
│     │     └── cve-2026-7482-bleeding-llama.md    ← OOB Read, 300k+ servers exposed
│     ├── Webinaires & Podcasts/
│     │     └── sans-moab-webcast-2026.md
│     └── attack-techniques/supply-chain/
│           └── typosquatting.md
│
├── soc-labs/
│     ├── THM/                                      ← TryHackMe room notes
│     └── splunk-bots/
│           ├── botsv1-investigation-notes.md       ← Full Cerber v2 investigation
│           └── botsv1_ransomware_investigation.pdf ← Final incident report (score: 16,193)
│
├── tools-and-scripts/
│     ├── Python-Scripts/
│     │     └── Own_ones/
│     │           └── PyGhost-MAC.py               ← Custom MAC spoofing tool
│     └── Bash-Scripts/
│
├── Certifications/
│     ├── Fortigate/
│     │     ├── fortigate-administrator-notes.md
│     │     └── fcf-notes.md
│
└── resources/
      ├── network_protocols_reference.md
      └── useful-links.md
```

---

## 🎯 `[root@soc-ops ~]# ./load_featured.sh --priority HIGH`

```bash
[FEATURED]  Indexing high-value operational artifacts ................. 🟢 done
[FEATURED]  7 entries flagged — rendering mission-critical work.
```

| Work | Category | What's Inside |
|------|----------|---------------|
| [BOTSv1 Ransomware Investigation](https://github.com/nouhasedraoui/cybersecurity-portfolio/blob/main/soc-labs/splunk-bots/botsv1-investigation-notes.md) | SOC / DFIR | Cerber v2 kill chain · Score 16,193 · Zero penalties |
| [BOTSv1 Final Report (PDF)](https://github.com/nouhasedraoui/cybersecurity-portfolio/blob/main/soc-labs/splunk-bots/botsv1_ransomware_investigation-2026-05-10%20(9).pdf) | SOC / DFIR | Full incident report with timeline and IOCs |
| [PortSwigger SQLi Series](https://github.com/nouhasedraoui/cybersecurity-portfolio/blob/main/web-application-security/sql-injection/portswigger-sqli-notes.md) | Web Security | Full PortSwigger SQLi lab series — every technique documented |
| [Bleeding Llama CVE-2026-7482](https://github.com/nouhasedraoui/cybersecurity-portfolio/blob/main/threat-intelligence/CVEs/cve-2026-7482-bleeding-llama.md) | Threat Intel | AI platform OOB Read — 300k+ servers exposed |
| [cPanel Triple CVE — May 2026](https://github.com/nouhasedraoui/cybersecurity-portfolio/blob/main/threat-intelligence/CVEs/cpanel-cve-may-2026.md) | Threat Intel | Code execution + privilege escalation in cPanel/WHM |
| [FortiGate Administrator Notes](https://github.com/nouhasedraoui/cybersecurity-portfolio/blob/main/Certifications/Fortigate/fortigate-administrator-notes.md) | Certification | Full FCA 15-module notes |
| [PyGhost-MAC](https://github.com/nouhasedraoui/cybersecurity-portfolio/blob/main/tools-and-scripts/Python-Scripts/Own_ones/PyGhost-MAC.py) | Tools | Custom Python MAC spoofing script |

---

## ✍️ `[root@soc-ops ~]# curl -s https://medium.com/@ryxocrypt/feed`

```bash
[RSS]   Fetching threat intelligence publications from @ryxocrypt .... 🟢 200 OK
[RSS]   1 article published — high-severity CVE coverage confirmed.
```

Published threat intelligence breakdowns for defenders:

**[CVE-2026-34197: A Bug That Hid Inside Apache ActiveMQ for 13 Years](https://medium.com/@ryxocrypt/cve-2026-34197-a-bug-that-hid-inside-apache-activemq-for-13-years-and-now-its-being-exploited-ae0e17996ddc)**
Root cause analysis, full attack chain walkthrough, and detection guidance for an actively exploited remote code execution vulnerability.

More articles in progress.

---

## 🏆 `[root@soc-ops ~]# cat /etc/soc-os/certifications.db`

```bash
[CERT-DB]  Querying operator credential store ......................... 🟢 done
[CERT-DB]  Verified issuers: Fortinet · Cisco · NVIDIA · Hedera
[CERT-DB]  Displaying active clearances...
```

| Certification | Issuer | Year |
|--------------|--------|------|
| Fortinet FCA — NSE 1 & NSE 2 Network Security Associate | Fortinet | 2026 |
| Cybersecurity Defense Analyst Career Path (Splunk & Cisco) | Cisco Netacad | 2026 |
| NVIDIA: Exploring Adversarial Machine Learning | NVIDIA | 2025 |
| Certified Cybersecurity Educator Professional (CCEP) | — | 2025 |
| Hedera Hashgraph Certified Developer | Hedera | 2024 |
| Cisco CyberOps Associate (SecFund & SecOps) | Cisco Netacad | 2023 |
| Cisco CCNA Security / Implementing Network Security | Cisco Netacad | 2023 |

```bash
[CERT-DB]  In-progress pipeline  ETA 2027:
           ├── CEH  (Certified Ethical Hacker) ..................... 🔵 IN PROGRESS
           ├── ISO/IEC 27001 Lead Auditor ......................... 🔵 IN PROGRESS
           └── Fortinet NSE 4 .................................... 🔵 IN PROGRESS
```

---

## 🧩 `[root@soc-ops ~]# ./thm_roomlog.sh --operator rsd177 --verbose`

```bash
[THM]   Operator rsd177: #1 Bronze League → #1 Silver League ......... 🟢 CONFIRMED
[THM]   Consecutive weekly leaderboard dominance confirmed.
[THM]   Loading room completion manifest...
```

**Ranked #1 in Bronze League · Promoted to Silver League · Ranked #1 in Silver League**
Consistent top performer across back-to-back weekly leaderboard cycles.

<details>
<summary><b>⚠️ [EXPAND] Web Application Security — Rooms Completed</b></summary>

| Room | Difficulty | Focus |
|------|-----------|-------|
| [How Websites Work](https://tryhackme.com/room/howwebsiteswork) | Easy | Web architecture fundamentals |
| [HTTP in Detail](https://tryhackme.com/room/httpindetail) | Easy | HTTP protocol, methods, status codes |
| [Putting it all Together](https://tryhackme.com/room/puttingitalltogether) | Easy | End-to-end web request lifecycle |
| [Web Application Basics](https://tryhackme.com/room/webapplicationbasics) | Easy | Core web app concepts |
| [Guided Pentest: Web](https://tryhackme.com/room/guidedpentestweb) | Easy | Web app pentesting — recon to full compromise |
| [CyberHeroes](https://tryhackme.com/room/cyberheroes) | Easy | CTF — authentication bypass |
| [W1seGuy](https://tryhackme.com/room/w1seguy) | Easy | CTF — plaintext cryptography |

</details>

<details>
<summary><b>⚠️ [EXPAND] SOC, DFIR & Forensics — Rooms Completed</b></summary>

| Room | Difficulty | Focus |
|------|-----------|-------|
| [DFIR: An Introduction](https://tryhackme.com/room/introductoryroomdfirmodule) | Easy | Digital forensics and incident response foundations |
| [Windows Forensics 1](https://tryhackme.com/room/windowsforensics1) | Medium | Windows Registry forensics |
| [KAPE](https://tryhackme.com/room/kape) | Medium | Kroll Artifact Parser & Extractor for DFIR collection |
| [Disk Analysis & Autopsy](https://tryhackme.com/room/autopsy2ze0) | Medium | Disk image forensics using Autopsy |
| [Memory Analysis Introduction](https://tryhackme.com/room/memoryanalysisintroduction) | Easy | Live memory forensics and threat detection |
| [Malware Classification](https://tryhackme.com/room/malwareclassification) | Easy | Identify and classify common malware types |
| [Dev Diaries](https://tryhackme.com/room/devdiaries) | Easy | OSINT — hunting development traces |

</details>

<details>
<summary><b>⚠️ [EXPAND] Defensive Security & SOC Concepts — Rooms Completed</b></summary>

| Room | Difficulty | Focus |
|------|-----------|-------|
| [Defensive Security Intro](https://tryhackme.com/room/defensivesecurityintroqW) | Easy | Threat intel, SOC, DFIR, SIEM |
| [Offensive Security Intro](https://tryhackme.com/room/offensivesecurityintrokK) | Easy | Ethical hacking fundamentals |
| [The CIA Triad](https://tryhackme.com/room/theciatriad) | Easy | Core security principles |
| [Cryptography Concepts](https://tryhackme.com/room/cryptographyconcepts) | Easy | Cryptography in digital environments |
| [Vectara](https://tryhackme.com/room/vectara) | Easy | CTF — 2026 AI Odyssey event |
| [AI Security Path Ticketing Event](https://tryhackme.com/room/aisecuritypathticketingevent) | Info | AI security fundamentals |

</details>

<details>
<summary><b>⚠️ [EXPAND] Systems & Networking Fundamentals — Rooms Completed</b></summary>

| Room | Difficulty | Focus |
|------|-----------|-------|
| [Linux Fundamentals 1](https://tryhackme.com/room/linuxfundamentalspart1) | Info | Linux CLI essentials |
| [Bash Scripting](https://tryhackme.com/room/bashscripting) | Easy | Bash automation |
| [Windows Fundamentals 1–3](https://tryhackme.com/room/windowsfundamentals1xbx) | Info | Windows desktop, registry, security, BitLocker |
| [What is Networking?](https://tryhackme.com/room/whatisnetworking) | Info | Computer networking fundamentals |
| [DNS in Detail](https://tryhackme.com/room/dnsindetail) | Easy | DNS protocol and resolution |
| [Nmap](https://tryhackme.com/room/furthernmap) | Easy | Advanced Nmap scanning techniques |
| [Nmap Basic Port Scans](https://tryhackme.com/room/nmap02) | Easy | TCP connect, SYN, and UDP scan internals |
| [Cloud Computing Fundamentals](https://tryhackme.com/room/cloudcomputingfundamentals) | Easy | Cloud scaling and service models |
| [DevSecOps Basics](https://tryhackme.com/room/devsecopsbasics) | Medium | Shift-left security, development models |

</details>

<details>
<summary><b>⚠️ [EXPAND] Scripting & Development — Rooms Completed</b></summary>

| Room | Difficulty | Focus |
|------|-----------|-------|
| [Python Basics](https://tryhackme.com/room/pythonbasics) | Easy | Python scripting fundamentals |
| [Bash Scripting](https://tryhackme.com/room/bashscripting) | Easy | Bash automation |

</details>

---

## 📡 `[root@soc-ops ~]# git log --oneline --graph --all`

<div align="center">

![Snake](https://raw.githubusercontent.com/nouhasedraoui/nouhasedraoui/output/github-contribution-grid-snake.svg)

</div>

---

## 📈 `[root@soc-ops ~]# ./sys_diagnostics.sh --module github-telemetry`

```bash
[TELEMETRY]  Querying GitHub API ..................................... 🟢 rate limit OK
[TELEMETRY]  Rendering operator commit statistics and language distribution.
```

<div align="center">
  <table border="0" cellspacing="0" cellpadding="0">
    <tr>
      <td align="center" valign="top">
        <img src="https://github-readme-stats-sigma-five.vercel.app/api?username=nouhasedraoui&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true" width="420px" alt="GitHub Stats" />
      </td>
      <td align="center" valign="top">
        <img src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=nouhasedraoui&layout=compact&theme=tokyonight&hide_border=true&langs_count=5" width="320px" alt="Top Languages" />
      </td>
    </tr>
  </table>
</div>

---

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--   FOOTER — INCIDENT REPORT INTEGRITY EXPORT                   -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,50:0a2540,100:0d1117&height=2" width="100%"/>

```bash
#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
#  SOC-OS :: INCIDENT REPORT INTEGRITY EXPORT
#  Session    : SOC-2026-NS-0x4F7A
#  Operator   : nouhasedraoui  [ESPRIT · Tunisia]
#  Class      : TLP:WHITE
# ─────────────────────────────────────────────────────────────────────────────

# ── SESSION SUMMARY ───────────────────────────────────────────────────────────
[REPORT]  Compiling final session metrics...
          ├── Threats hunted    : 3 CVEs analyzed · 1 kill chain reconstructed
          ├── IOCs processed    : 1,247 indicators ingested via MISP
          ├── Labs completed    : 41 TryHackMe rooms · BOTSv1 score 16,193
          └── Posture rating    : 🟢 HARDENED — no operator vulnerabilities found

# ── LOG SANITIZATION ──────────────────────────────────────────────────────────
[DFIR]    Executing forensic cleanup...
          ├── Flushing session artifacts from /tmp/soc-ops/ ......... 🟢 done
          ├── Zeroing swap partitions  (DoD 5220.22-M) .............. 🟢 done
          ├── Scrubbing volatile memory segments .................... 🟢 done
          └── Audit trail archived → /var/log/soc/session.enc ....... 🟢 done

# ── FEED TEARDOWN ─────────────────────────────────────────────────────────────
[NET]     Disconnecting threat intelligence feeds...
          ├── MISP feed ..................................... 🟢 SYNCED & CLOSED
          ├── CVE stream .................................... 🟢 FLUSHED
          ├── Suricata IDS .................................. 🟢 RULES SAVED · ENGINE HALTED
          └── C2 watchdog ................................... 🟢 0 beacons detected this session

# ── MODULE UNLOAD ─────────────────────────────────────────────────────────────
[KERNEL]  Unloading SOC-OS modules in reverse order...
          ├── suricata-ids.ko ............................... 🟢 UNLOADED
          ├── splunk-forwarder.ko ........................... 🟢 UNLOADED
          ├── elastic-stack.ko .............................. 🟢 UNLOADED
          └── wazuh-agent.ko ................................ 🟢 UNLOADED
```

```bash
# ── SHA-256 INTEGRITY MATRIX ──────────────────────────────────────────────────
[CRYPTO]  Running report integrity verification...

          Profile hash  (SHA-256):
          ┌──────────────────────────────────────────────────────────────────┐
          │  a9f3c8e2 b41d7056 f3c2e8a1 b94d0f7e                            │
          │  3c5a91e2 d80b64f7 a2e15c3d 90b87f2a                            │
          └──────────────────────────────────────────────────────────────────┘
          Signature   : 🟢 VALID   [ED25519 · nouhasedraoui.pub]
          Integrity   : 🟢 CONFIRMED — no tampering detected

[SYS]     SOC-OS session closed. Threat posture preserved.
          ▌ Until next engagement. — ryxocrypt
```

<div align="center">

![Visitors](https://komarev.com/ghpvc/?username=nouhasedraoui&style=flat-square&color=0a84ff&label=PROFILE+VIEWS)
&nbsp;
[![GitHub followers](https://img.shields.io/github/followers/nouhasedraoui?label=FOLLOWERS&style=flat-square&color=0a84ff)](https://github.com/nouhasedraoui)

> *"The best defenders think like attackers. Document everything. Trust nothing. Stay curious."*
> — **Nouha Sedraoui**, SOC-OS Operator

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,30:0f3460,60:0a2540,100:0d1117&height=120&section=footer&reversal=true" width="100%"/>
