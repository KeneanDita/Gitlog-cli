
# Gitlog-cli

[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=flat-square)]()
[![Made with ♥ by Kenean Dita](https://img.shields.io/badge/Made%20with%20%E2%99%A5%20by-Kenean%20Dita-blueviolet?style=flat-square)]()

> **Gitlog-cli** is a terminal-based Python application that displays a user's GitHub activity in a clean and readable format. Ideal for developers who prefer staying in the command line.



## Screenshots

<p align="center">
  <img src="assets/screenshot1.png" alt="Gitlog-cli screenshot 1" width="700"/>
  <br/><br/>
  <img src="assets/screenshot2.png" alt="Gitlog-cli screenshot 2" width="700"/>
</p>

## Features

- View recent GitHub activity (commits, PRs, issues)
- Pretty terminal output using `rich`
- Lightweight and fast
- Cross-platform

## Installation

```bash
git clone https://github.com/keneandita/gitlog-cli.git
cd gitlog-cli
```

Install dependencies:

```bash
pip install -r requrements.txt
```

### Usage

```bash
python .\main.py --username
```

Or you can set up a global shortcut by editing your default profile.
For Windows:

```bash
notepad.exe $PROFILE
```

Add this to your script with the correct path of the cloned repo.

```notepad
function github_activity {
    python "C:\Users\..." $args
}
```

### Author

**Kenean Dita**
[GitHub](https://github.com/kenean-dita) | [LinkedIn](https://www.linkedin.com/in/keneandita/)

Show Your Support
If you find this project helpful, please consider giving it a ⭐

### License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
