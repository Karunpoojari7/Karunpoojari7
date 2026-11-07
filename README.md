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

<div align="center">

<img src="./assets/about-card.svg" width="100%" alt="Karun H G terminal profile card"/>

</div>

<br/>

---

## `02 // Inside my security lab`

I organize my work around three connected areas: attack the surface, collect evidence, then harden what I find.

<div align="center">

<img src="./assets/lab-overview.svg" width="100%" alt="Red Team, Blue Team and AI Security overview"/>

<br/>

*Every ethical offensive experiment can become a defensive lesson.*

</div>

<details>
<summary><b>📡&nbsp; Sample investigation workflow (TShark)</b> &nbsp;·&nbsp; <sub>tap to expand</sub></summary>
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

<p><i>Selected work across cybersecurity, AI and software engineering. Select a card to open its repository, or expand the details below it.</i></p>

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/Karunpoojari7/Bayora_Sec"><img src="./assets/project-cards/bayora.svg" width="100%" alt="BAYORA project card"/></a>
<details>
<summary><b>Technical details</b> · BAYORA</summary>

Isolated Red Team, Target LLM and Blue Team environments, with an evidence-focused security evaluation workflow.

<a href="https://github.com/Karunpoojari7/Bayora_Sec">Open repository ↗</a>
</details>
</td>
<td width="50%" valign="top">
<a href="https://github.com/Karunpoojari7/NETWATCH"><img src="./assets/project-cards/netwatch.svg" width="100%" alt="NETWATCH.AI project card"/></a>
<details>
<summary><b>Technical details</b> · NETWATCH.AI</summary>

Full-stack monitoring platform with a real-time dashboard, traffic visibility and anomaly detection components.

<a href="https://github.com/Karunpoojari7/NETWATCH">Open repository ↗</a>
</details>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/Karunpoojari7/Soc-Analyst-Journey"><img src="./assets/project-cards/soc-analyst-journey.svg" width="100%" alt="SOC ANALYST JOURNEY project card"/></a>
<details>
<summary><b>Technical details</b> · SOC ANALYST JOURNEY</summary>

Documented learning labs covering packet inspection, DNS and TLS analysis, SIEM practice and sanitized evidence.

<a href="https://github.com/Karunpoojari7/Soc-Analyst-Journey">Open repository ↗</a>
</details>
</td>
<td width="50%" valign="top">
<a href="https://github.com/Karunpoojari7/QuantumValut"><img src="./assets/project-cards/claudevault.svg" width="100%" alt="CLAUDEVAULT project card"/></a>
<details>
<summary><b>Technical details</b> · CLAUDEVAULT</summary>

The repository README identifies the application as ClaudeVault. The repository name is QuantumValut; the README does not currently substantiate a post-quantum cryptography claim.

<a href="https://github.com/Karunpoojari7/QuantumValut">Open repository ↗</a>
</details>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/Karunpoojari7/Resume_Gap_AI"><img src="./assets/project-cards/resume-gap-ai.svg" width="100%" alt="RESUME GAP AI project card"/></a>
<details>
<summary><b>Technical details</b> · RESUME GAP AI</summary>

An AI-powered SkillForge application designed to analyze resume gaps and produce professional optimization reports.

<a href="https://github.com/Karunpoojari7/Resume_Gap_AI">Open repository ↗</a>
</details>
</td>
<td width="50%" valign="top">
<a href="https://github.com/Karunpoojari7/GMU-CONNECT-APP"><img src="./assets/project-cards/gmu-connect.svg" width="100%" alt="GMU CONNECT 2.0 project card"/></a>
<details>
<summary><b>Technical details</b> · GMU CONNECT 2.0</summary>

A student ERP prototype with a mobile application, admin portal and backend API architecture. It is a demonstration project, not a live university ERP integration.

<a href="https://github.com/Karunpoojari7/GMU-CONNECT-APP">Open repository ↗</a>
</details>
</td>
</tr>
</table>

<sub>Project descriptions reflect the current repository documentation. The card artwork is static; repository links and expandable details are native GitHub README interactions.</sub>


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

## `05 // Learning roadmap`

Where I am and what comes next, grouped by progress.

<table>
<tr>
<th width="33%">✅ Completed</th>
<th width="33%">🔄 In progress</th>
<th width="33%">🎯 Planned</th>
</tr>
<tr>
<td valign="top">
<ul>
<li>Network traffic analysis</li>
<li>TShark and PCAP fundamentals</li>
<li>TLS / SNI / QUIC inspection</li>
<li>DNS reconnaissance</li>
<li>Linux fundamentals</li>
</ul>
</td>
<td valign="top">
<ul>
<li>SOC detection engineering</li>
<li>SIEM lab practice</li>
<li>OWASP Top 10</li>
<li>Web application security</li>
<li>CTF practice (TryHackMe / Hack The Box)</li>
</ul>
</td>
<td valign="top">
<ul>
<li>Advanced incident response</li>
<li>AI red teaming and LLM security research</li>
<li>Applied cryptography research</li>
<li>Security+ / BTL1 / eJPT preparation</li>
</ul>
</td>
</tr>
</table>

---

## `06 // GitHub activity`

<div align="center">

<img src="./assets/stats-dashboard.svg" width="100%" alt="Live GitHub activity dashboard"/>

<sub>Auto-refreshed every 6 hours by GitHub Actions directly from the GitHub API. No third-party stat services.</sub>

</div>
<br/>

---

## `07 // Let's connect`

<div align="center">

Open to learning, collaboration, mentorship and cybersecurity opportunities.

<br/>

<a href="https://in.linkedin.com/in/karun-poojari-uiux"><img src="./assets/btn-linkedin.svg" width="320" alt="Connect with me on LinkedIn"/></a>
&nbsp;&nbsp;
<a href="https://github.com/Karunpoojari7?tab=repositories"><img src="./assets/btn-github.svg" width="320" alt="Explore my GitHub repositories"/></a>

<br/>

<img src="./assets/footer-pulse.svg" width="100%" alt="Observe, Investigate, Validate, Secure"/>

</div>
