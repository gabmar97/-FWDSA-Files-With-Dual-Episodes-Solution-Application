# Rename TV Episodes: A Script for the Incompetent

Welcome to the pinnacle of your inadequacy: **Rename TV Episodes**, a script so basic and straightforward that one might assume even a brainless hamster could figure it out. But alas, here you are, reading this README. How tragic.

## 🤔 What Does This Script Do?

This script renames your TV show episode files based on **accurate episode titles** fetched from the TVDB API for double episode files. Why? Because clearly, you couldn’t manage to name them properly yourself. And yes, it includes pop-up dialogs because even typing file paths is evidently beyond you.

## 🛠 Requirements (But You Should Know This Already, Right?)

Before you embarrass yourself further by running this, make sure you have:

- **Python 3.6+**: Hopefully, you've heard of Python before. If not, I suggest starting with "What is a computer?" tutorials.
- **Internet Connection**: Because API calls don’t work offline. Shocker, right?
- **TVDB API Key**: This is a thing you'll need to set up. Head over to [TVDB](https://thetvdb.com/) and figure it out. Or is copy-pasting links too much to handle?

## 📦 Installation (For the Hopelessly Clueless)

Let’s install the only dependency you'll need, assuming your Python setup isn’t as disorganized as your episode library:

```bash
pip install request
```
### Tkinter Installation Instructions:
If you somehow don’t have tkinter installed, follow these steps based on your operating system:

- **Linux (Debian/Ubuntu)**: Open your terminal and run:
    ```bash
    sudo apt-get install python3-tk
    ```
- **macOS**: If you’re using Homebrew Python, you need to reinstall Python with tkinter support:
    ```bash
    brew reinstall python-tk
    ```
- **Windows**: Ensure you downloaded Python from python.org. If tkinter is missing, reinstall Python and ensure the tkinter option is checked during installation.
Ensure you downloaded Python from python.org. If tkinter is missing, reinstall Python and ensure the tkinter option is checked during installation.

## 🚀 Usage (Because You Clearly Need Instructions)

### Run the Script:
Execute it in the terminal or double-click the script (whichever you can manage). Here’s the terminal command:
```bash
python rename_tv_episodes.py
```
Select the Series Directory:
A file dialog will pop up (you’re welcome). Select the folder containing your series.
Example:

bash
Copy
Edit
/path/to/TVShows/The Amazing World of Gumball
Select the Season Directory:
Another dialog will appear. Select the specific season’s directory you want to process.
Example:

bash
Copy
Edit
/path/to/TVShows/The Amazing World of Gumball/Season 1
Let the Script Work Its Magic:
The script will fetch proper episode titles using TVDB and rename your files into something civilized, like this:

scss
Copy
Edit
Season 1 - Episode 1 (The Responsible) and Episode 2 (The DVD).mkv
## 😬 Troubleshooting (Because You’ll Still Fail)
### Authentication Errors:

```vbnet
Failed to authenticate with TVDB
```
Cause: You messed up your API key.
Fix: Get a valid key. It’s not rocket science.
### File Parsing Issues:
```bash
Could not parse season/episode from {filename}
```
Cause: Your file names are a mess. Fix them. Use the SxxEyy format, for crying out loud.
### Missing Episode Data:
```kotlin
Not enough episode data found
```
Cause: TVDB couldn’t find information for your bad input. Or maybe you picked the wrong season. Who knows? 
### tkinter Module Not Found:
```vbnet
ModuleNotFoundError: No module named 'tkinter'
```
Cause: tkinter isn’t installed in your Python environment.
Fix: Follow the installation instructions above for your operating system.
## 🙄 Contributing
Don’t bother. If you’re reading this, it’s unlikely you have the skills to contribute. But hey, if you want to prove me wrong, fork the repo, make some changes, and submit a pull request. I won’t hold my breath.

## 📜 License
Do whatever you want with this script. Just don’t come crying to me when you break something. And for the love of all that is holy, stop renaming files manually.










