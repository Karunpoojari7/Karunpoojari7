<div align="center">

<img src="./assets/cyber-banner.png" width="100%" alt="Karun H G Cybersecurity Banner"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=16&duration=3200&pause=1000&color=00FF9C&center=true&vCenter=true&width=700&height=38&lines=root%40karun-lab%3A~%24+whoami;Karun+H+G+%7C+MCA+Student;Cybersecurity+%7C+SOC+%7C+AI+Security;Observe.+Investigate.+Validate.+Secure." alt="Animated terminal"/>

<br/>

![Status](https://img.shields.io/badge/STATUS-LEARNING_%26_BUILDING-080D12?style=for-the-badge&labelColor=00ff9c)
![Focus](https://img.shields.io/badge/FOCUS-SOC_%7C_DFIR_%7C_AI_SECURITY-080D12?style=for-the-badge&labelColor=00ff9c)
![Base](https://img.shields.io/badge/BASE-BENGALURU%2C_INDIA-080D12?style=for-the-badge&labelColor=00ff9c)

<br/>

[![GitHub](https://img.shields.io/badge/GITHUB-Karunpoojari7-181717?style=flat-square&logo=github&logoColor=00ff9c)](https://github.com/Karunpoojari7)
[![LinkedIn](https://img.shields.io/badge/LINKEDIN-CONNECT-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://in.linkedin.com/in/karun-poojari-uiux)
[![Projects](https://img.shields.io/badge/VIEW-PROJECTS-00C987?style=flat-square&labelColor=080D12)](#03--featured-projects)
[![Connect](https://img.shields.io/badge/LET'S-CONNECT-00C987?style=flat-square&labelColor=080D12)](#07--lets-connect)

</div>

<br/>

> **I want to understand how systems break, so I can build ones that don't.**
> MCA student focused on cybersecurity, network forensics and AI security. I learn by building, investigating and documenting.

---

## `01 // The person behind the code`

Hi, I'm **Karun H G**, an MCA student and cybersecurity learner from Bengaluru. I like knowing how systems work, how vulnerabilities appear, and how to detect and fix them. I split my time between **defensive security (SOC, PCAP forensics)**, **offensive fundamentals (recon, web security)** and **AI security**.

| | |
|---|---|
| 🎓 **Education** | MCA (Master of Computer Applications) |
| 🎯 **Focus** | SOC Operations, Network Forensics, DNS Recon, AI Security |
| 🧪 **Lab** | Kali Linux and isolated practice environments |
| 🔁 **Workflow** | Observe → Investigate → Validate → Document → Improve |
| 🚀 **Career goal** | Security Engineer / SOC Analyst / AI Security roles |
| 🤝 **Open to** | Internships · Collaboration · Mentorship · CTF teams |

> **Ethical boundary:** all offensive testing is done only on systems I own or have explicit permission to test.

```bash
root@karun-lab:~$ cat mindset.txt
Every ethical offensive experiment becomes a defensive lesson.
```

---

## `02 // Inside my security lab`

I organize my work around three connected areas.

<table>
<tr>
<td width="33%" valign="top">

### 🔴 Red Team
<sub>OFFENSIVE SECURITY</sub>

- Reconnaissance and enumeration
- DNS reconnaissance
- Network scanning
- Web app security basics
- Vulnerability assessment

`Nmap` `Burp Suite` `OWASP ZAP` `Metasploit` `ffuf` `gobuster`

</td>
<td width="33%" valign="top">

### 🔵 Blue Team
<sub>DEFENSIVE SECURITY</sub>

- SOC alert triage
- PCAP investigation
- TLS / SNI / QUIC inspection
- Log analysis and detection
- Incident investigation

`Wireshark` `TShark` `tcpdump` `grep` `awk` `jq`

</td>
<td width="33%" valign="top">

### 🟢 AI Security
<sub>AI SAFETY & EVALUATION</sub>

- Prompt-injection testing
- AI red teaming (controlled)
- Guardrails and evaluation
- Secure AI design
- Reliability testing

`Python` `AI Red Teaming` `Evaluation`

</td>
</tr>
</table>

<div align="center">

**RED TEAM → EVIDENCE → BLUE TEAM → HARDENING**

</div>

<details>
<summary><b>📡 Sample investigation workflow (TShark)</b></summary>
<br/>

```bash
# Protocol hierarchy of a capture
tshark -r capture.pcap -q -z io,phs

# Extract TLS Server Name Indication (SNI)
tshark -r capture.pcap -Y "tls.handshake.type == 1" \
       -T fields -e ip.src -e tls.handshake.extensions_server_name

# Review DNS queries
tshark -r capture.pcap -Y "dns.flags.response == 0" \
       -T fields -e frame.time -e ip.src -e dns.qry.name

# Identify QUIC traffic
tshark -r capture.pcap -Y "quic"
```

</details>

---

## `03 // Featured projects`

Selected builds that show how I practice security and software development. Some are ongoing, so check each repo for status.

<table>
<tr>
<td width="50%" valign="top">

#### 🔐 01. Post-Quantum Secure File Vault
Security-focused file storage exploring post-quantum cryptography concepts.

![Crypto](https://img.shields.io/badge/CRYPTOGRAPHY-00C987?style=flat-square&labelColor=080D12)
![PQC](https://img.shields.io/badge/POST--QUANTUM-00C987?style=flat-square&labelColor=080D12)
![Security](https://img.shields.io/badge/SECURITY-00C987?style=flat-square&labelColor=080D12)

</td>
<td width="50%" valign="top">

#### 🛡️ 02. Bayora: AI Safety Testing
Infrastructure for controlled AI security testing and defensive evaluation.

![AI Security](https://img.shields.io/badge/AI_SECURITY-00C987?style=flat-square&labelColor=080D12)
![Red Team](https://img.shields.io/badge/RED_TEAM-FF5252?style=flat-square&labelColor=080D12)
![Evaluation](https://img.shields.io/badge/EVALUATION-00C987?style=flat-square&labelColor=080D12)

[↗ Repository](https://github.com/Karunpoojari7/Bayora_Sec)

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### 🔵 03. SOC Analyst Journey
Packet analysis, command references and investigation reports from hands-on practice.

![SOC](https://img.shields.io/badge/SOC-2389E8?style=flat-square&labelColor=080D12)
![PCAP](https://img.shields.io/badge/PCAP-2389E8?style=flat-square&labelColor=080D12)
![DFIR](https://img.shields.io/badge/DFIR-2389E8?style=flat-square&labelColor=080D12)

[↗ Repository](https://github.com/Karunpoojari7/Soc-Analyst-Journey)

</td>
<td width="50%" valign="top">

#### 📊 04. Insight AI
AI-powered analytics chatbot and dashboard concept for exploring data in natural language.

![AI](https://img.shields.io/badge/AI-00C987?style=flat-square&labelColor=080D12)
![Analytics](https://img.shields.io/badge/ANALYTICS-00C987?style=flat-square&labelColor=080D12)
![Dashboard](https://img.shields.io/badge/DASHBOARD-00C987?style=flat-square&labelColor=080D12)

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### 🎓 05. GMU Connect 2.0
Student-focused mobile app with academic APIs, authentication and a React Native + TypeScript foundation.

![React Native](https://img.shields.io/badge/REACT_NATIVE-00C987?style=flat-square&labelColor=080D12)
![TypeScript](https://img.shields.io/badge/TYPESCRIPT-00C987?style=flat-square&labelColor=080D12)

</td>
<td width="50%" valign="top">

#### ➕ More on GitHub
Experiments, notes and projects in progress. New work is added as I ship it.

[↗ View all repositories](https://github.com/Karunpoojari7?tab=repositories)

</td>
</tr>
</table>

---

## `04 // My technology toolkit`

<div align="center">

**Languages & Development**<br/>
<img src="https://skillicons.dev/icons?i=python,java,js,ts,html,css" alt="Languages"/>

**Frameworks**<br/>
<img src="https://skillicons.dev/icons?i=react,nextjs,spring,fastapi,flask,tailwind" alt="Frameworks"/>

**Databases & Tools**<br/>
<img src="https://skillicons.dev/icons?i=mysql,postgres,mongodb,docker,git,github,vscode" alt="Databases and tools"/>

**Systems**<br/>
<img src="https://skillicons.dev/icons?i=kali,linux,bash,windows" alt="Systems"/>

**Security Tools**<br/>
<img src="https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white" alt="Wireshark"/>
<img src="https://img.shields.io/badge/Nmap-4682B4?style=for-the-badge&logo=nmap&logoColor=white" alt="Nmap"/>
<img src="https://img.shields.io/badge/Burp_Suite-FF6633?style=for-the-badge&logo=burpsuite&logoColor=white" alt="Burp Suite"/>
<img src="https://img.shields.io/badge/OWASP_ZAP-00549E?style=for-the-badge&logo=owasp&logoColor=white" alt="OWASP ZAP"/>
<img src="https://img.shields.io/badge/Metasploit-2596CD?style=for-the-badge&logo=metasploit&logoColor=white" alt="Metasploit"/>

</div>

<sub>Tools listed are ones I have used or am actively learning. They do not imply expert-level proficiency in every item.</sub>

---

## `05 // What I'm learning next`

<table>
<tr>
<td width="50%" valign="top">

### 🔵 Defensive Track
- [x] Network traffic analysis
- [x] TShark and PCAP fundamentals
- [x] TLS / SNI / QUIC inspection
- [x] DNS reconnaissance
- [ ] SOC detection engineering
- [ ] SIEM lab practice
- [ ] Advanced incident response

</td>
<td width="50%" valign="top">

### 🔴 Offensive & AI Track
- [x] Linux fundamentals
- [ ] OWASP Top 10
- [ ] Web application security
- [ ] CTF practice (TryHackMe / Hack The Box)
- [ ] AI red teaming and LLM security research
- [ ] Applied cryptography research
- [ ] Security+ / BTL1 / eJPT preparation

</td>
</tr>
</table>

---

## `06 // GitHub activity`

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=Karunpoojari7&show_icons=true&theme=dark&bg_color=080D12&title_color=00FF9C&icon_color=00FF9C&text_color=c9d1d9&border_color=003B2A&hide_border=false" alt="GitHub stats"/>
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Karunpoojari7&layout=compact&theme=dark&bg_color=080D12&title_color=00FF9C&text_color=c9d1d9&border_color=003B2A" alt="Top languages"/>

<br/>

<img src="https://streak-stats.demolab.com?user=Karunpoojari7&theme=dark&background=080D12&ring=00FF9C&fire=00FF9C&currStreakLabel=00FF9C&border=003B2A" alt="GitHub streak"/>

</div>

---

## `07 // Let's connect`

<div align="center">

`root@karun-lab:~$ ./connect.sh`

I'm happy to talk about security, SOC work, CTFs, AI safety, internships or collaboration.

<br/>

<a href="https://in.linkedin.com/in/karun-poojari-uiux">
<img src="https://img.shields.io/badge/LINKEDIN-CONNECT-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
</a>
<a href="https://github.com/Karunpoojari7?tab=repositories">
<img src="https://img.shields.io/badge/EXPLORE-REPOSITORIES-181717?style=for-the-badge&logo=github&logoColor=00ff9c" alt="Repositories"/>
</a>

<br/><br/>

*Curiosity starts the experiment. Security turns it into something useful.*

**OBSERVE / INVESTIGATE / VALIDATE / SECURE**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:080D12,45:003B2A,100:00FF9C&height=120&section=footer" width="100%" alt="Footer wave"/>

</div>
