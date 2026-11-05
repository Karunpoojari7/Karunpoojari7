 <!-- ═══════════════════════════════════════════════════════════════
     KARUN H G | CYBERSECURITY PROFILE
     Dark Cyber Operations | Red Team × Blue Team × AI Security
     ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<img src="./assets/cyber-banner.png" width="100%" alt="Karun H G Cybersecurity Banner" />

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&duration=3500&pause=1000&color=00FF9C&center=true&vCenter=true&width=750&height=45&lines=%24+whoami+%E2%86%92+Karun+H+G;%24+mission+%E2%86%92+Secure.+Investigate.+Build.;%24+mode+%E2%86%92+Red+Team+%E2%87%84+Blue+Team;%24+focus+%E2%86%92+Cybersecurity+%7C+AI+Security" alt="Terminal typing animation" />

<br/>

![Status](https://img.shields.io/badge/STATUS-LEARNING_%26_BUILDING-00ff9c?style=for-the-badge&labelColor=080D12)
![Focus](https://img.shields.io/badge/FOCUS-SOC_%7C_DFIR_%7C_AI_SECURITY-00ff9c?style=for-the-badge&labelColor=080D12)
![Location](https://img.shields.io/badge/BASE-BENGALURU%2C_INDIA-00ff9c?style=for-the-badge&labelColor=080D12)

<br/>

`[ RED TEAM ]` &nbsp; × &nbsp; `[ BLUE TEAM ]` &nbsp; × &nbsp; `[ AI SECURITY ]`

<br/>

[ABOUT](#-system-identity) &nbsp; • &nbsp;
[RED TEAM](#-red-team--offensive-security) &nbsp; • &nbsp;
[BLUE TEAM](#-blue-team--defensive-security) &nbsp; • &nbsp;
[AI SECURITY](#-ai-security) &nbsp; • &nbsp;
[PROJECTS](#-featured-projects) &nbsp; • &nbsp;
[CONTACT](#-connect)

</div>

---

## `01 // SYSTEM IDENTITY`

<div align="center">

### `root@karun-lab:~$ whoami`

</div>

<table>
<tr>
<td width="55%" valign="top">

**Karun H G**

MCA Student | Cybersecurity Learner | Software Developer | Aspiring AI Security Engineer

I build software, explore security vulnerabilities in controlled environments, and study how systems can be protected against real-world threats.

My interests span offensive security, defensive security, network forensics, cryptography and AI security.

**Current mission:** Learn through practical experimentation, build meaningful security projects, and document every discovery.

</td>
<td width="45%" valign="top">

### `system.info`

```yaml
name: Karun H G
education: MCA Student

environment:
  - Kali Linux
  - Isolated Lab Environments

currently_learning:
  - SOC Operations
  - Network Forensics
  - DNS Reconnaissance
  - AI Red Teaming

currently_building:
  - Post-Quantum Secure File Vault
  - Bayora

workflow:
  - Observe
  - Investigate
  - Validate
  - Document
  - Improve

open_to:
  - Internships
  - Collaboration
  - Mentorship
  - CTF Teams
```

</td>
</tr>
</table>

> **Operating principle:** Understand how systems fail. Learn how attacks work. Build better defenses. All offensive testing is performed only on systems I own or have explicit permission to test.

---

## `02 // RED TEAM — OFFENSIVE SECURITY`

<text></text>

<div align="center">

<kbd> RECONNAISSANCE </kbd> &nbsp; <kbd> ENUMERATION </kbd> &nbsp; <kbd> VULNERABILITY ANALYSIS </kbd>

</div>

*Understanding the attacker's mindset to build stronger defenses.*

<table>
<tr>
<td width="50%" valign="top">

### 🔴 Attack Surface Exploration

- Reconnaissance and enumeration
- DNS reconnaissance
- Network scanning and service discovery
- Web application security fundamentals
- Vulnerability assessment
- Adversarial AI testing

</td>
<td width="50%" valign="top">

### 🧰 Security Toolkit

- `Nmap`
- `Burp Suite`
- `OWASP ZAP`
- `Metasploit` — lab use
- `gobuster` / `ffuf`
- `dig` / `nslookup`
- `Kali Linux`

</td>
</tr>
</table>

<details>
<summary><b>🔓 Explore my ethical hacking methodology</b></summary>

| Phase | Activity |
|:--|:--|
| 01 — Recon | Information gathering and DNS discovery |
| 02 — Scanning | Port and service enumeration |
| 03 — Analysis | Identifying potential security weaknesses |
| 04 — Validation | Safely verifying findings in a lab |
| 05 — Reporting | Evidence, impact and remediation |

**Ground rules:** Authorized targets only · Controlled environments · Responsible disclosure · Evidence-based reporting.

</details>

---

## `03 // BLUE TEAM — DEFENSIVE SECURITY`

<div align="center">

<kbd> MONITOR </kbd> &nbsp; <kbd> DETECT </kbd> &nbsp; <kbd> INVESTIGATE </kbd> &nbsp; <kbd> RESPOND </kbd>

</div>

*Detect. Investigate. Respond. Harden.*

<table>
<tr>
<td width="50%" valign="top">

### 🔵 Defensive Focus

- SOC operations and alert triage
- Network traffic analysis
- PCAP investigation
- TLS / SNI / QUIC inspection
- Threat detection and log analysis
- Incident investigation
- Secure system design

</td>
<td width="50%" valign="top">

### 🧰 Defensive Toolkit

- `Wireshark`
- `TShark`
- `tcpdump`
- Linux CLI
- `grep` / `awk` / `jq`
- Log analysis workflows
- SIEM concepts

</td>
</tr>
</table>

<details>
<summary><b>📡 Explore a sample network investigation workflow</b></summary>

```bash
# 01 - Protocol overview
tshark -r capture.pcap -q -z io,phs

# 02 - Extract TLS Server Name Indication
tshark -r capture.pcap \
-Y "tls.handshake.type == 1" \
-T fields -e ip.src \
-e tls.handshake.extensions_server_name

# 03 - Review DNS queries
tshark -r capture.pcap \
-Y "dns.flags.response == 0" \
-T fields -e frame.time -e ip.src -e dns.qry.name

# 04 - Identify QUIC traffic
tshark -r capture.pcap -Y "quic"
```

**Investigation workflow:** Observe → Investigate → Validate → Document → Improve.

</details>

<details>
<summary><b>🔁 Red Team ⇄ Blue Team security cycle</b></summary>

```mermaid
flowchart LR
    A["🔴 Attack Simulation"] --> B["📝 Evidence Collection"]
    B --> C["🔵 Detection & Analysis"]
    C --> D["🛡️ Hardening & Response"]
    D --> A
```

Every offensive experiment can become a defensive lesson.

</details>

---

## `04 // AI SECURITY`

<div align="center">

### 🤖 Exploring the security of intelligent systems

`AI RED TEAMING` &nbsp; × &nbsp; `AI DEFENSE` &nbsp; × &nbsp; `SECURE AI DESIGN`

</div>

| Research Area | Exploration |
|:--|:--|
| 🔴 Adversarial Testing | Prompt injection, jailbreak-style probing and robustness testing in controlled settings |
| 🔵 Defensive Evaluation | Guardrails, evaluation pipelines and safety scoring |
| 🛡️ Secure AI Design | Separation of attack and defense layers, least privilege for AI tools |
| 🧪 AI Safety | Understanding failure modes and improving system reliability |

---

## `05 // FEATURED PROJECTS`

*Building practical solutions through software development and security research.*

<table>
<tr>
<td width="50%" valign="top">

### 🔐 Post-Quantum Secure File Vault

Security-focused file storage exploring post-quantum cryptography concepts.

![Cryptography](https://img.shields.io/badge/CRYPTOGRAPHY-00ff9c?style=flat-square&labelColor=080D12)
![PQC](https://img.shields.io/badge/POST--QUANTUM-00ff9c?style=flat-square&labelColor=080D12)

</td>
<td width="50%" valign="top">

### 🛡️ Bayora — AI Safety Testing

Red Team / Blue Team infrastructure that separates attack attempts from defensive evaluation of AI systems.

[![Repository](https://img.shields.io/badge/VIEW_REPOSITORY-Bayora__Sec-00ff9c?style=flat-square&logo=github&logoColor=white&labelColor=080D12)](https://github.com/Karunpoojari7/Bayora_Sec)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🌐 SOC Analyst Journey

A practical learning journey covering packet analysis, command references, observations and evidence-based reports.

[![Repository](https://img.shields.io/badge/VIEW_REPOSITORY-SOC--Analyst--Journey-00ff9c?style=flat-square&logo=github&logoColor=white&labelColor=080D12)](https://github.com/Karunpoojari7/Soc-Analyst-Journey)

</td>
<td width="50%" valign="top">

### 📊 Insight AI

AI-powered analytics chatbot and dashboard concept for exploring data in plain language.

![AI Analytics](https://img.shields.io/badge/AI_ANALYTICS-00ff9c?style=flat-square&labelColor=080D12)

</td>
</tr>
<tr>
<td colspan="2" valign="top">

### 🎓 GMU Connect 2.0

Student-focused mobile app initiative with academic APIs, authentication, and a React Native + TypeScript foundation.

</td>
</tr>
</table>

> Project status varies: some projects are ongoing or exploratory. Visit their repositories for implementation details.

---

## `06 // TECHNOLOGY STACK`

<details open>
<summary><b>💻 Programming Languages</b></summary>
<br/>

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)

</details>

<details open>
<summary><b>🌐 Web Development & Backend</b></summary>
<br/>

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)

</details>

<details open>
<summary><b>🗄️ Databases, DevOps & Platforms</b></summary>
<br/>

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</details>

<details open>
<summary><b>🔐 Cybersecurity Toolkit</b></summary>
<br/>

![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)
![Nmap](https://img.shields.io/badge/Nmap-4682B4?style=for-the-badge&logo=nmap&logoColor=white)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=for-the-badge&logo=burpsuite&logoColor=white)
![OWASP](https://img.shields.io/badge/OWASP-000000?style=for-the-badge&logo=owasp&logoColor=white)

</details>

<sub>A selected list of technologies I have worked with or am actively learning, not a claim of expert-level proficiency in every tool.</sub>

---

## `07 // SECURITY RESEARCH ROADMAP`

*Learning through practical exploration and continuous improvement.*

| Status | Research / Learning Area |
|:--:|:--|
| ✅ | Network traffic analysis with TShark & PCAP |
| ✅ | TLS / SNI / QUIC inspection basics |
| ✅ | DNS reconnaissance & Linux fundamentals |
| 🔄 | SOC detection engineering & SIEM labs |
| 🔄 | Web application security — OWASP Top 10 |
| 🔄 | CTF practice — TryHackMe / Hack The Box |
| 🔄 | Security certifications — Security+, BTL1, eJPT |
| 🔄 | AI red-teaming & LLM security research |

---

## `08 // GITHUB ACTIVITY`

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=Karunpoojari7&show_icons=true&theme=dark&bg_color=080D12&title_color=00ff9c&icon_color=00ff9c&text_color=c9d1d9&border_color=164B3C&hide_border=false" alt="GitHub statistics" />

<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Karunpoojari7&layout=compact&theme=dark&bg_color=080D12&title_color=00ff9c&text_color=c9d1d9&border_color=164B3C&hide_border=false" alt="Top programming languages" />

<br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=Karunpoojari7&theme=dark&background=080D12&ring=00ff9c&fire=ff4b4b&currStreakLabel=00ff9c&border=164B3C" alt="GitHub contribution streak" />

</div>

---

## `09 // CONNECT`

<div align="center">

### `root@karun-lab:~$ ./connect.sh`

Open to learning, collaboration, mentorship and cybersecurity opportunities.

<br/>

[![LinkedIn](https://img.shields.io/badge/LINKEDIN-CONNECT-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://in.linkedin.com/in/karun-poojari-uiux)
[![GitHub](https://img.shields.io/badge/GITHUB-FOLLOW-181717?style=for-the-badge&logo=github&logoColor=00ff9c)](https://github.com/Karunpoojari7)

<br/>

```bash
karun@kali-lab:~$ echo "Building with curiosity."
karun@kali-lab:~$ echo "Learning through practice."
karun@kali-lab:~$ echo "Designing with security in mind."
```

**OBSERVE. INVESTIGATE. VALIDATE. SECURE.**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:080D12,50:003b2a,100:00ff9c&height=110&section=footer" width="100%" alt="Cyber green footer" />

</div>
