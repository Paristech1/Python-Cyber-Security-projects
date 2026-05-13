# Python Cybersecurity Learning Recap

This document tracks the core concepts and lessons learned during the creation of the **Port Scanner** and **Log Analyzer** projects.

## 🛡️ Project 1: TCP Port Scanner
**Goal**: Identify open ports on a target IP using the `socket` module.

### Key Lessons:
*   **The socket Toolkit**: Using `socket.socket()` to create a connection and `connect_ex()` to check for open ports.
*   **Range and Exclusivity**: `range(1, 100)` stops at 99. To include 100, you must use `range(1, 101)`.
*   **The "Main" Switch**: Using `if __name__ == "__main__":` to ensure the script only runs when executed directly.

---

## 🔍 Project 2: SSH Log Analyzer
**Goal**: Use Regex to find failed login attempts and flag high-risk IP addresses.

### Key Lessons:
*   **The "Octet Rule" (Regex)**: `\d` is a special code for a digit. Without the backslash, it's just the letter 'd'. Every "Octet" and "Period" in an IP address needs an escape backslash (`\d+\.\d+\.\d+\.\d+`).
*   **The Bouncer (Sets)**: A `set()` only stores unique items. If an attacker tries the same username 100 times, the set will only show it once.
*   **Indentation (The Tornado)**: Python uses indentation to define blocks. If your code doesn't line up vertically, it won't run.
*   **Scope (The Las Vegas Rule)**: Variables created inside a function stay inside that function.

---

## 🛡️ Project 3: File Integrity Checker
**Goal**: Use SHA-256 cryptographic hashes to detect if files have been tampered with or deleted.

### Key Lessons:
*   **Cryptographic Hashes**: A fixed-length "fingerprint" of a file's data.
*   **The Avalanche Effect**: Changing one bit of data results in a completely different hash.
*   **Efficiency (Chunking)**: Reading large files in small pieces (`8192` bytes) so the computer's memory doesn't get overwhelmed.
*   **JSON Baselines**: Storing "Known Good" states in a structured format for easy comparison.
*   **sys.argv**: Using command-line arguments to make one script perform multiple tasks (like `check` vs `create`).

---

*Follow along at: https://github.com/Paristech1/Python-Cyber-Security-projects*
