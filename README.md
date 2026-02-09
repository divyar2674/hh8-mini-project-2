# KeyLogger detection tool
## Description
- This project is a behavior-based keylogger detetction tool built using python.
- It monitors running processes and detects suspicious programs that may behave like key loggers by analyzing:
  - Keyboard hook activity(Windows mechanism that allows process to intercept keyboard events using windows apis)
  - Abnormal process behavior
  - Suspicious execution paths
  - CPU usage patterns

# Goals
- Understand how keyloggers operate at behavioral level
- learn behavior-based malware detection techniques
- Monitor running processes using system-level APIs
- Identify suspicious processes using heuristic risk scoring 

# Tools Used
- Python
- psutil library
- windows api (pywin32)

# Environment Setup
- The project is developeed and executed on windows system.Python is used as the primary programming language.
- The psutil library in python is used to monitor running processes.
- No real user data or keystroke are collected to ensure rntical use.

# Methodology

## 1-Process Monitoring
- All running processes are retrieved using psutil library.Each process is represented as psutil.Process object.

## 2-Suspicious Path Detection
- Processes running from suspicious location such ass temp,AppData,Downloads are considered risky.
- Trusted system directories like Windows,Program Files are excluded from suspicion.

## 3-Behavior based risk scoring
- Processes are evaluated using behavioral parameters such as Execution path,Process name pattern,CPU usage each parameter contributes to risk score used to classify the process.

## 4-Threshold based detetction
A predefined risk threshold is applied.Processes exceeding the threshold are flagged as suspicious and recorded.

# What I learned
- Keylogger behavior and detection technique.
- difference between signature based and behavior based security technique.
- Process monitoring using python.
- Risk-based detection methods.
- Ethical use of Cybersecurity tools.

# Ethical Considerations
- No Keystrokes are captured
- No sensitive data is accessed

# Conclusion
- This project successfully demonstrated behavior based detection of suspicious processes.By analyzing how processes behave rather than relying on known signature, the system highlights the imporatnce of proactive monitoring and strong defensive security practices.