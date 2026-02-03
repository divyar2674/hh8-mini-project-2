# KeyLogger detection tool
## Description
- This project is a behavior-based keylogger detetction tool built using python.
- It monitord running processes and detects suspicious programs that may behave like key loggers by analyzing:
  - Keyboard hook activity(Windows mechanism that allows process to intercept keyboard events using windows apis)
  - Abnormal process behavior
  - Suspicious execution paths
  - CPU usage patterns
