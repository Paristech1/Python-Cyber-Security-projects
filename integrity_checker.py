import hashlib
import os
import json
from datetime import datetime

# This is my "Digital Fingerprint" tool. It uses SHA-256 to scramble file data.
def hash_file(filepath):
    """Calculate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        # "rb" means read binary—perfect for any file type
        with open(filepath, "rb") as f:
            # Read in 8192-byte chunks so big files don't crash my RAM!
            for chunk in iter(lambda: f.read(8192), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except (PermissionError, FileNotFoundError) as e:
        return f"ERROR:{e}"      

# This takes a "Security Photo" of the folders I'm worried about.
def create_baseline(directories, output_file="baseline.json"):
    """Create a hash baseline for files in specified directories."""
    baseline = {}
    file_count = 0

    for directory in directories:
        # os.walk is the "Spider" that crawls through every sub-folder for me!
        for root, dirs, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_hash = hash_file(filepath)
                if not file_hash.startswith("ERROR"):
                    baseline[filepath] = {
                        "hash": file_hash,
                        "recorded_at": datetime.now().isoformat()
                    }
                    file_count += 1

    # Save the results in JSON format so it's easy for me to read later.
    with open(output_file, "w") as f:
        json.dump(baseline, f, indent=2)

    print(f"Baseline created: {file_count} files recorded.")
    return baseline

# The "Tripwire" part—compare the live files to my "Security Photo."
def check_integrity(baseline_file="baseline.json"):
    """Compare current file hashes against the baseline."""
    with open(baseline_file, "r") as f:
        baseline = json.load(f)

    modified = []
    missing = []

    for filepath, record in baseline.items():
        if not os.path.exists(filepath):
            missing.append(filepath)
            continue

        # If the fingerprint changed, a hacker might have been here! (Avalanche Effect)
        current_hash = hash_file(filepath)
        if current_hash != record["hash"]:
            modified.append({
                "file": filepath,
                "expected": record["hash"][:16] + "...",
                "actual": current_hash[:16] + "..."
            })

    print(f"\nIntegrity Check Results")
    print(f"Files checked: {len(baseline)}")
    print(f"Modified: {len(modified)}")
    print(f"Missing: {len(missing)}")

    return modified, missing

# The "Ignition" block that starts the whole thing up!
if __name__ == "__main__":
    import sys

    # If I type "check" in the terminal, run the tripwire.
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        check_integrity()
    else:
        # Otherwise, create a new baseline for the test folder.
        dirs_to_monitor = ["./test_folder"]
        
        if not os.path.exists("./test_folder"):
            os.makedirs("./test_folder")
            with open("./test_folder/secret.txt", "w") as f:
                f.write("This is a secret file.")
        
        create_baseline(dirs_to_monitor)
        print("Run with 'check' argument to verify integrity.")
