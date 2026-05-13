import re
from collections import Counter




def analyze_auth_log(filepath, threshold=10):
    """Parse auth.log for failed SSH attempts and flag suspicious IPs."""
    failed_pattern = re.compile( 
        r"Failed password for (?:invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)"
    )

    attempts = []
    usernames_targeted = {}

    with open(filepath, "r") as log_file:
        for line in log_file:
            match = failed_pattern.search(line)
            if match:
                username = match.group(1)
                ip_address = match.group(2)

                attempts.append(ip_address)

                if ip_address not in usernames_targeted:
                    usernames_targeted[ip_address] = set()
                usernames_targeted[ip_address].add(username)


    ip_counts = Counter(attempts)

    print(f"Total failed attempts: {len(attempts)})")
    print(f"Unique source IPs: {len(ip_counts)}")
    print(f"\nIPs exceeding {threshold} failed attempts:)")
    print("-" * 55)

    flagged = []

    for ip, count in ip_counts.most_common():
        if count >= threshold:
            users = usernames_targeted.get(ip, set())
            print(f"  {ip:18s} {count:4d} attempts {len(users)} usernames")
            flagged.append(ip)


    return flagged 

if __name__ == "__main__":

    flagged_ips = analyze_auth_log("test_auth.log", threshold=2)