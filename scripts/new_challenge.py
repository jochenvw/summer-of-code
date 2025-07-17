import os
import sys

template = """# {title}

## 🧩 Goal
...

## 🛠️ How It Works
...

## 💡 Key Learnings
...

## ✅ Status
- [ ] Not started
"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python new_challenge.py 'Challenge Title'")
        exit(1)
    title = sys.argv[1]
    folder_name = title.lower().replace(" ", "-")
    os.makedirs(f"challenges/{folder_name}", exist_ok=True)
    with open(f"challenges/{folder_name}/README.md", "w") as f:
        f.write(template.format(title=title))
    print(f"Created challenge folder: challenges/{folder_name}")
