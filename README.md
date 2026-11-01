<!-- ═══════════════════════════════════════════════════════════════
     Karun H G — GitHub Profile README
     Theme: Hacker terminal (green on dark) | Red Team + Blue Team
     ═══════════════════════════════════════════════════════════════ -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:003b2a,100:00ff9c&height=220&section=header&text=Karun%20H%20G&fontSize=56&fontColor=00ff9c&fontAlignY=38&desc=Cybersecurity%20%7C%20Software%20Developer%20%7C%20Aspiring%20AI%20Security%20Engineer&descSize=16&descColor=c9d1d9&descAlignY=60&animation=fadeIn" alt="Karun H G banner" width="100%" />

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=3500&pause=900&color=00FF9C&center=true&vCenter=true&width=720&height=45&lines=%24+whoami+%E2%86%92+Karun+H+G;%24+role+%E2%86%92+MCA+Student+%7C+SOC+Analyst+in+Training;%24+mode+%E2%86%92+Red+Team+%E2%87%84+Blue+Team;%24+focus+%E2%86%92+Network+Forensics+%7C+AI+Security;%24+motto+%E2%86%92+Observe.+Investigate.+Validate.+Document." alt="Typing animation" />
</a>

<br/>

![Status](https://img.shields.io/badge/STATUS-LEARNING_%26_BUILDING-00ff9c?style=for-the-badge&labelColor=0d1117)
![Focus](https://img.shields.io/badge/FOCUS-SOC_%7C_DFIR_%7C_AI_SEC-00ff9c?style=for-the-badge&labelColor=0d1117)
![Location](https://img.shields.io/badge/BASE-BENGALURU,_IN-00ff9c?style=for-the-badge&labelColor=0d1117)

<br/>

[**▸ About**](#-about) &nbsp;•&nbsp;
[**▸ Red Team**](#-offensive-security-red-team) &nbsp;•&nbsp;
[**▸ Blue Team**](#-defensive-security-blue-team) &nbsp;•&nbsp;
[**▸ AI Security**](#-ai-security) &nbsp;•&nbsp;
[**▸ Projects**](#-featured-projects) &nbsp;•&nbsp;
[**▸ Stack**](#-tech-stack) &nbsp;•&nbsp;
[**▸ Contact**](#-contact)

</div>

---

## 🖥️ About

```bash
karun@kali-lab:~$ cat profile.json
```

```json
{
  "name": "Karun H G",
  "education": "MCA Student",
  "roles": ["Cybersecurity Learner", "Software Developer", "Aspiring AI Security Engineer"],
  "currently_learning": ["SOC Operations", "Network Forensics (TShark/PCAP)", "DNS Recon", "AI Red-Teaming"],
  "currently_building": ["Post-Quantum Secure File Vault", "Bayora (AI Safety Testing)"],
  "lab": "Kali Linux + isolated practice environments",
  "workflow": "Observe -> Investigate -> Validate -> Document -> Improve",
  "goal": "Security Engineering / SOC / AI Security roles",
  "open_to": ["Internships", "Collaboration", "Mentorship", "CTF teams"]
}
```

> 💡 I build software, break it **ethically** in controlled labs, and then learn how to defend it. All offensive work is performed only on systems I own or have explicit permission to test.

---

## ⚔️ Offensive Security (Red Team)

*Understanding the attacker's mindset to build better defenses.*

<table>
<tr>
<td width="50%" valign="top">

### 🎯 Focus Areas
- Reconnaissance & enumeration
- DNS reconnaissance
- Web application security basics
- Network scanning & service discovery
- Vulnerability assessment fundamentals
- Adversarial testing of AI systems

</td>
<td width="50%" valign="top">

### 🧰 Tooling (Lab Use)
- `nmap` &nbsp;•&nbsp; `dig` / `nslookup`
- `Burp Suite` &nbsp;•&nbsp; `OWASP ZAP`
- `Metasploit` (lab only)
- `gobuster` / `ffuf`
- `Kali Linux` toolchain

</td>
</tr>
</table>

<details>
<summary><b>🔓 Click to expand — My ethical hacking approach</b></summary>
<br/>

| Phase | What I practice |
|:--|:--|
| **1. Recon** | Passive/active information gathering, DNS records, subdomain discovery |
| **2. Scanning** | Port/service enumeration, version detection |
| **3. Analysis** | Mapping findings to known weakness classes (OWASP Top 10) |
| **4. Validation** | Confirming issues safely in lab environments |
| **5. Reporting** | Evidence, impact, remediation guidance |

**Ground rules:** authorized targets only • isolated labs • responsible disclosure • documentation over destruction.

</details>

---

## 🛡️ Defensive Security (Blue Team)

*Detect. Investigate. Respond. Harden.*

<table>
<tr>
<td width="50%" valign="top">

### 🔎 Focus Areas
- SOC operations & alert triage
- Network traffic analysis (PCAP)
- TLS / SNI / QUIC traffic inspection
- Threat detection & log analysis
- Incident analysis & evidence handling
- Secure system design

</td>
<td width="50%" valign="top">

### 🧰 Tooling
- `TShark` / `Wireshark`
- `tcpdump`
- Linux CLI (`grep`, `awk`, `jq`)
- Log analysis workflows
- SIEM concepts (detection, correlation)

</td>
</tr>
</table>

<details>
<summary><b>📡 Click to expand — Sample investigation workflow</b></summary>
<br/>

```bash
# 1. Overview of protocols in a capture
tshark -r capture.pcap -q -z io,phs

# 2. Extract TLS Server Name Indication (SNI)
tshark -r capture.pcap -Y "tls.handshake.type == 1" \
       -T fields -e ip.src -e tls.handshake.extensions_server_name

# 3. Review DNS queries
tshark -r capture.pcap -Y "dns.flags.response == 0" \
       -T fields -e frame.time -e ip.src -e dns.qry.name

# 4. Identify QUIC traffic
tshark -r capture.pcap -Y "quic"
```

**Method:** Observe → Investigate → Validate → Document → Improve.

</details>

<details>
<summary><b>🔁 Click to expand — Red Team ⇄ Blue Team loop</b></summary>
<br/>

```mermaid
flowchart LR
    A[🔴 Attack Simulation<br/>Recon · Scan · Test] --> B[📝 Evidence<br/>Logs · PCAPs · Notes]
    B --> C[🔵 Detection<br/>Analyze · Correlate]
    C --> D[🧱 Hardening<br/>Fix · Monitor · Document]
    D --> A
```

Every offensive experiment becomes a defensive lesson.

</details>

---

## 🤖 AI Security

Exploring how AI systems fail, and how to make them safer.

| Area | Description |
|:--|:--|
| 🔴 **Adversarial Testing** | Prompt injection, jailbreak-style probing, robustness checks (in controlled settings) |
| 🔵 **Defensive Evaluation** | Guardrails, evaluation pipelines, safety scoring |
| 🧱 **Secure AI Design** | Separation of attack and defense layers, least privilege for AI tools |

---

## 🚀 Featured Projects

<table>
<tr>
<td width="50%" valign="top">

### 🔐 Post-Quantum Secure File Vault
Security-focused file storage exploring post-quantum cryptography concepts.

![Crypto](https://img.shields.io/badge/-Cryptography-00ff9c?style=flat-square&labelColor=0d1117)
![PQC](https://img.shields.io/badge/-Post--Quantum-00ff9c?style=flat-square&labelColor=0d1117)

</td>
<td width="50%" valign="top">

### 🛡️ Bayora — AI Safety Testing
Red-team / blue-team infrastructure that separates attack attempts from defensive evaluation of AI systems.

[![Repo](https://img.shields.io/badge/View_Repo-Bayora__Sec-0d1117?style=flat-square&logo=github&logoColor=00ff9c)](https://github.com/Karunpoojari7/Bayora_Sec)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🌐 SOC Analyst Journey
Packet analysis, command references, observations, and evidence-based reports.

[![Repo](https://img.shields.io/badge/View_Repo-soc--analyst--journey-0d1117?style=flat-square&logo=github&logoColor=00ff9c)](https://github.com/Karunpoojari7/soc-analyst-journey)

</td>
<td width="50%" valign="top">

### 📊 Insight AI
AI-powered analytics chatbot and dashboard concept for exploring data in plain language.

![AI](https://img.shields.io/badge/-AI_Analytics-00ff9c?style=flat-square&labelColor=0d1117)

</td>
</tr>
<tr>
<td colspan="2" valign="top">

### 🎓 GMU Connect 2.0
Student-focused mobile app initiative with academic APIs, authentication, and a React Native + TypeScript foundation.

</td>
</tr>
</table>

> *Project status varies: some are ongoing or exploratory. Check each repository for details.*

---

## 🧰 Tech Stack

<details open>
<summary><b>💻 Languages</b></summary>
<br/>

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)

</details>

<details open>
<summary><b>🌐 Web & Backend</b></summary>
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
<summary><b>🔐 Security Toolkit</b></summary>
<br/>

![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)
![Nmap](https://img.shields.io/badge/Nmap-4682B4?style=for-the-badge&logo=nmap&logoColor=white)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=for-the-badge&logo=burpsuite&logoColor=white)
![OWASP](https://img.shields.io/badge/OWASP-000000?style=for-the-badge&logo=owasp&logoColor=white)

</details>

*A selected list of technologies I have worked with or am actively learning, not a claim of expert-level proficiency in every tool.*

---

## 🗺️ Roadmap

- [x] Network traffic analysis with TShark & PCAP
- [x] TLS / SNI / QUIC inspection basics
- [x] DNS reconnaissance & Linux fundamentals
- [ ] SOC detection engineering & SIEM labs
- [ ] Web app penetration testing (OWASP Top 10)
- [ ] CTF participation (TryHackMe / Hack The Box)
- [ ] Security certifications (e.g. Security+, BTL1, eJPT)
- [ ] AI red-teaming & LLM security research

---

## 📈 GitHub Activity

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=Karunpoojari7&show_icons=true&theme=dark&bg_color=0d1117&title_color=00ff9c&icon_color=00ff9c&text_color=c9d1d9&border_color=00ff9c&hide_border=false" alt="GitHub stats" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Karunpoojari7&layout=compact&theme=dark&bg_color=0d1117&title_color=00ff9c&text_color=c9d1d9&border_color=00ff9c&hide_border=false" alt="Top languages" />

<img src="https://github-readme-streak-stats.herokuapp.com/?user=Karunpoojari7&theme=dark&background=0d1117&ring=00ff9c&fire=00ff9c&currStreakLabel=00ff9c&border=00ff9c" alt="Streak" />

</div>

---

## 📫 Contact

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://in.linkedin.com/in/karun-poojari-uiux)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=00ff9c)](https://github.com/Karunpoojari7)

```bash
karun@kali-lab:~$ echo "Building with curiosity. Learning through practice. Designing with security in mind."
```

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:003b2a,100:00ff9c&height=120&section=footer" width="100%" alt="footer" />

</div>
