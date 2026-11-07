<!-- KARUN H G | CYBERSECURITY PORTFOLIO -->

<div align="center">

<img src="./assets/cyber-banner.png" width="100%" alt="Karun H G Cybersecurity Banner"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=16&duration=3200&pause=1000&color=00FF9C&center=true&vCenter=true&width=700&height=38&lines=root%40karun-lab%3A~%24+whoami;Karun+H+G+%7C+MCA+Student;Cybersecurity+%7C+Software+Development+%7C+AI+Security;Observe.+Investigate.+Validate.+Secure." alt="Animated terminal"/>

<br/>

![Status](https://img.shields.io/badge/STATUS-LEARNING_%26_BUILDING-080D12?style=for-the-badge&labelColor=00ff9c)
![Focus](https://img.shields.io/badge/FOCUS-SOC_%7C_DFIR_%7C_AI_SECURITY-080D12?style=for-the-badge&labelColor=00ff9c)
![Location](https://img.shields.io/badge/BASE-BENGALURU%2C_INDIA-080D12?style=for-the-badge&labelColor=00ff9c)

<br/>

[**About**](#01--about) &nbsp;•&nbsp;
[**Security Operations**](#02--security-operations) &nbsp;•&nbsp;
[**Projects**](#03--featured-projects) &nbsp;•&nbsp;
[**Skills**](#04--technical-skills--tools) &nbsp;•&nbsp;
[**Roadmap**](#05--security-roadmap) &nbsp;•&nbsp;
[**Connect**](#06--connect)

</div>

---

## `01 // ABOUT`

```bash
root@karun-lab:~$ cat profile.json
```

```json
{
  "name": "Karun H G",
  "education": "MCA Student",
  "roles": ["Cybersecurity Learner", "Software Developer", "Aspiring AI Security Engineer"],
  "current_focus": ["SOC Operations", "Network Forensics (TShark / PCAP)", "DNS Recon", "AI Security"],
  "lab": "Kali Linux and isolated practice environments",
  "workflow": "Observe -> Investigate -> Validate -> Document -> Improve",
  "goal": "Security Engineering / SOC / AI Security roles",
  "open_to": ["Internships", "Collaboration", "Mentorship", "CTF teams"]
}
```

I'm an MCA student, cybersecurity learner and software developer interested in how systems work, how vulnerabilities emerge, and how technology can be made more secure. My interests span offensive security, defensive security, network forensics, applied cryptography, post-quantum cryptography and AI security.

**Current mission:** build practical projects, investigate security concepts, strengthen technical skills and document what I learn.

> **Ethical boundary:** All offensive security testing is performed only on systems I own or have explicit permission to test.

---

## `02 // SECURITY OPERATIONS`

<div align="center">

<img src="./assets/Neon Cybersecurity Tri-Panel Banner.png" width="100%" alt="Red Team, Blue Team and AI Security overview"/>

</div>

<table>
<tr>
<td width="33%" valign="top">

<h3 align="center">🔴 RED TEAM</h3>
<p align="center"><sub>OFFENSIVE SECURITY</sub></p>
<p align="center"><i>Understand the attack surface. Anticipate weaknesses.</i></p>

<ul>
<li>Reconnaissance and enumeration</li>
<li>DNS reconnaissance</li>
<li>Network scanning and service discovery</li>
<li>Web application security fundamentals</li>
<li>Vulnerability assessment</li>
<li>Adversarial AI testing</li>
</ul>

<p><strong>TOOLKIT</strong></p>

<p><code>Nmap</code> · <code>Burp Suite</code> · <code>OWASP ZAP</code> · <code>Metasploit</code> · <code>gobuster</code> · <code>ffuf</code> · <code>Kali Linux</code></p>

</td>
<td width="33%" valign="top">

<h3 align="center">🔵 BLUE TEAM</h3>
<p align="center"><sub>DEFENSIVE SECURITY</sub></p>
<p align="center"><i>Detect threats. Investigate incidents. Protect the network.</i></p>

<ul>
<li>SOC operations and alert triage</li>
<li>Network traffic analysis</li>
<li>PCAP investigation</li>
<li>TLS / SNI / QUIC inspection</li>
<li>Threat detection and log analysis</li>
<li>Incident investigation</li>
<li>Secure system design</li>
</ul>

<p><strong>TOOLKIT</strong></p>

<p><code>Wireshark</code> · <code>TShark</code> · <code>tcpdump</code> · <code>Linux CLI</code> · <code>grep</code> · <code>awk</code> · <code>jq</code> · <code>SIEM concepts</code></p>

</td>
<td width="33%" valign="top">

<h3 align="center">🟢 AI SECURITY</h3>
<p align="center"><sub>AI SAFETY & EVALUATION</sub></p>
<p align="center"><i>Evaluate intelligent systems. Build safer AI.</i></p>

<ul>
<li>AI red teaming and prompt-injection testing</li>
<li>Adversarial testing in controlled environments</li>
<li>Defensive evaluation and guardrails</li>
<li>Secure AI design and access control</li>
<li>AI safety and reliability testing</li>
</ul>

<p><strong>FOCUS</strong></p>

<p><code>AI Red Teaming</code> · <code>Evaluation</code> · <code>Python</code> · <code>AI Safety</code></p>

</td>
</tr>
</table>

<div align="center">

**RED TEAM → EVIDENCE → BLUE TEAM → HARDENING**

*Every ethical offensive experiment can become a defensive lesson.*

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

## `03 // FEATURED PROJECTS`

<div align="center">

<sub>SELECTED BUILDS • SECURITY RESEARCH • SOFTWARE DEVELOPMENT</sub>

</div>

### 🔐 Post-Quantum Secure File Vault

<sub>CRYPTOGRAPHY / SECURE STORAGE</sub>

Security-focused file storage exploring post-quantum cryptography concepts.

![Cryptography](https://img.shields.io/badge/CRYPTOGRAPHY-00C987?style=flat-square&labelColor=080D12)
![PQC](https://img.shields.io/badge/POST--QUANTUM-00C987?style=flat-square&labelColor=080D12)
![Security](https://img.shields.io/badge/SECURITY-00C987?style=flat-square&labelColor=080D12)

---

### 🛡️ Bayora — AI Safety Testing

<sub>AI SECURITY / RED TEAM × BLUE TEAM</sub>

Infrastructure for controlled AI security testing and defensive evaluation.

![AI Security](https://img.shields.io/badge/AI_SECURITY-00C987?style=flat-square&labelColor=080D12)
![Red Team](https://img.shields.io/badge/RED_TEAM-FF5252?style=flat-square&labelColor=080D12)
![Evaluation](https://img.shields.io/badge/EVALUATION-00C987?style=flat-square&labelColor=080D12)

[**↗ Explore repository**](https://github.com/Karunpoojari7/Bayora_Sec)

---

### 🔵 SOC Analyst Journey

<sub>NETWORK FORENSICS / DEFENSIVE SECURITY</sub>

Practical learning through packet analysis, command references and investigation reports.

![SOC](https://img.shields.io/badge/SOC-2389E8?style=flat-square&labelColor=080D12)
![PCAP](https://img.shields.io/badge/PCAP-2389E8?style=flat-square&labelColor=080D12)
![DFIR](https://img.shields.io/badge/DFIR-2389E8?style=flat-square&labelColor=080D12)

[**↗ Explore repository**](https://github.com/Karunpoojari7/Soc-Analyst-Journey)

---

### 📊 Insight AI

<sub>AI / DATA ANALYTICS</sub>

AI-powered analytics chatbot and dashboard concept for exploring data in natural language.

![AI](https://img.shields.io/badge/AI-00C987?style=flat-square&labelColor=080D12)
![Analytics](https://img.shields.io/badge/ANALYTICS-00C987?style=flat-square&labelColor=080D12)
![Dashboard](https://img.shields.io/badge/DASHBOARD-00C987?style=flat-square&labelColor=080D12)

---

### 🎓 GMU Connect 2.0

<sub>MOBILE DEVELOPMENT / STUDENT TECHNOLOGY</sub>

Student-focused mobile application initiative involving academic APIs, authentication and a React Native + TypeScript foundation.

> Project status varies: some projects are ongoing or exploratory. Visit each repository for details.

---

## `04 // TECHNICAL SKILLS & TOOLS`

<details open>
<summary><b>💻 Programming & Development</b></summary>
<br/>

<div align="center">

<a href="https://www.python.org/"><img src="https://skillicons.dev/icons?i=python" width="55" alt="Python"/></a>
<a href="https://www.java.com/"><img src="https://skillicons.dev/icons?i=java" width="55" alt="Java"/></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/HTML"><img src="https://skillicons.dev/icons?i=html" width="55" alt="HTML"/></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/CSS"><img src="https://skillicons.dev/icons?i=css" width="55" alt="CSS"/></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript"><img src="https://skillicons.dev/icons?i=js" width="55" alt="JavaScript"/></a>
<a href="https://www.typescriptlang.org/"><img src="https://skillicons.dev/icons?i=ts" width="55" alt="TypeScript"/></a>
<a href="https://react.dev/"><img src="https://skillicons.dev/icons?i=react" width="55" alt="React"/></a>
<a href="https://nextjs.org/"><img src="https://skillicons.dev/icons?i=nextjs" width="55" alt="Next.js"/></a>
<a href="https://spring.io/projects/spring-boot"><img src="https://skillicons.dev/icons?i=spring" width="55" alt="Spring Boot"/></a>
<a href="https://fastapi.tiangolo.com/"><img src="https://skillicons.dev/icons?i=fastapi" width="55" alt="FastAPI"/></a>
<a href="https://flask.palletsprojects.com/"><img src="https://skillicons.dev/icons?i=flask" width="55" alt="Flask"/></a>
<a href="https://tailwindcss.com/"><img src="https://skillicons.dev/icons?i=tailwind" width="55" alt="Tailwind CSS"/></a>

</div>

</details>

<details open>
<summary><b>🗄️ Databases & Development Tools</b></summary>
<br/>

<div align="center">

<a href="https://www.mysql.com/"><img src="https://skillicons.dev/icons?i=mysql" width="55" alt="MySQL"/></a>
<a href="https://www.postgresql.org/"><img src="https://skillicons.dev/icons?i=postgres" width="55" alt="PostgreSQL"/></a>
<a href="https://www.mongodb.com/"><img src="https://skillicons.dev/icons?i=mongodb" width="55" alt="MongoDB"/></a>
<a href="https://www.docker.com/"><img src="https://skillicons.dev/icons?i=docker" width="55" alt="Docker"/></a>
<a href="https://git-scm.com/"><img src="https://skillicons.dev/icons?i=git" width="55" alt="Git"/></a>
<a href="https://github.com/"><img src="https://skillicons.dev/icons?i=github" width="55" alt="GitHub"/></a>
<a href="https://code.visualstudio.com/"><img src="https://skillicons.dev/icons?i=vscode" width="55" alt="VS Code"/></a>

</div>

</details>

<details open>
<summary><b>🖥️ Systems & Environments</b></summary>
<br/>

<div align="center">

<a href="https://www.kali.org/"><img src="https://skillicons.dev/icons?i=kali" width="55" alt="Kali Linux"/></a>
<a href="https://www.linux.org/"><img src="https://skillicons.dev/icons?i=linux" width="55" alt="Linux"/></a>
<a href="https://www.gnu.org/software/bash/"><img src="https://skillicons.dev/icons?i=bash" width="55" alt="Bash"/></a>
<a href="https://www.microsoft.com/windows"><img src="https://skillicons.dev/icons?i=windows" width="55" alt="Windows"/></a>

</div>

</details>

<details open>
<summary><b>🔐 Cybersecurity Tools & Interests</b></summary>
<br/>

<div align="center">

<a href="https://www.wireshark.org/"><img src="https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white" alt="Wireshark"/></a>
<a href="https://nmap.org/"><img src="https://img.shields.io/badge/Nmap-4682B4?style=for-the-badge&logo=nmap&logoColor=white" alt="Nmap"/></a>
<a href="https://portswigger.net/burp"><img src="https://img.shields.io/badge/Burp_Suite-FF6633?style=for-the-badge&logo=burpsuite&logoColor=white" alt="Burp Suite"/></a>
<a href="https://www.zaproxy.org/"><img src="https://img.shields.io/badge/OWASP_ZAP-00549E?style=for-the-badge&logo=owasp&logoColor=white" alt="OWASP ZAP"/></a>
<a href="https://www.metasploit.com/"><img src="https://img.shields.io/badge/Metasploit-2596CD?style=for-the-badge&logo=metasploit&logoColor=white" alt="Metasploit"/></a>
<a href="https://www.tcpdump.org/"><img src="https://img.shields.io/badge/tcpdump-00A67D?style=for-the-badge&labelColor=080D12" alt="tcpdump"/></a>

<br/>

![Network Security](https://img.shields.io/badge/NETWORK_SECURITY-0969DA?style=for-the-badge&labelColor=0969DA)
![Web Application Security](https://img.shields.io/badge/WEB_APPLICATION_SECURITY-0969DA?style=for-the-badge&labelColor=0969DA)
![Incident Response](https://img.shields.io/badge/INCIDENT_RESPONSE-0784B8?style=for-the-badge&labelColor=0784B8)
![Applied Cryptography](https://img.shields.io/badge/APPLIED_CRYPTOGRAPHY-0784B8?style=for-the-badge&labelColor=0784B8)
![Post Quantum Cryptography](https://img.shields.io/badge/POST_QUANTUM_CRYPTOGRAPHY-0969DA?style=for-the-badge&labelColor=0969DA)
![AI Security](https://img.shields.io/badge/AI_SECURITY-0969DA?style=for-the-badge&labelColor=0969DA)

</div>

</details>

<sub>Technologies listed are tools I have worked with or am actively learning. They do not imply expert-level proficiency in every item.</sub>

---

## `05 // SECURITY ROADMAP`

<div align="center">

`RESEARCH → EXPERIMENT → DOCUMENT → IMPROVE`

</div>

<details open>
<summary><b>🟢 Phase 01 — Foundation (completed)</b></summary>
<br/>

- [x] Network traffic analysis
- [x] TShark and PCAP fundamentals
- [x] TLS / SNI / QUIC inspection
- [x] DNS reconnaissance
- [x] Linux fundamentals

</details>

<details open>
<summary><b>🔵 Phase 02 — Active Investigation (in progress)</b></summary>
<br/>

- [ ] SOC detection engineering
- [ ] SIEM lab practice
- [ ] OWASP Top 10
- [ ] Web application security
- [ ] CTF practice — TryHackMe / Hack The Box

</details>

<details>
<summary><b>🟣 Phase 03 — Next Targets (planned)</b></summary>
<br/>

- [ ] Security+ / BTL1 / eJPT preparation
- [ ] AI red teaming
- [ ] LLM security research
- [ ] Advanced incident response
- [ ] Applied cryptography research

</details>

---

## `06 // CONNECT`

<div align="center">

`root@karun-lab:~$ ./connect.sh`

**Open to learning, collaboration, mentorship and cybersecurity opportunities.**

<br/>

<a href="https://in.linkedin.com/in/karun-poojari-uiux">
<img src="https://img.shields.io/badge/LINKEDIN-CONNECT-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
</a>
<a href="https://github.com/Karunpoojari7">
<img src="https://img.shields.io/badge/GITHUB-FOLLOW-181717?style=for-the-badge&logo=github&logoColor=00ff9c" alt="GitHub"/>
</a>

<br/><br/>

**OBSERVE / INVESTIGATE / VALIDATE / SECURE**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:080D12,45:003B2A,100:00FF9C&height=150&section=footer&animation=fadeIn" width="100%" alt="Footer wave"/>

</div>
