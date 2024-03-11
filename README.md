# MultiCat CLI Tool

The MultiCat CLI tool is a command-line utility designed to concatenate and display the contents of text files within a specified directory and its subdirectories. It also offers an option to copy the concatenated output to the clipboard, making it easier to paste into other applications. Particularly helpful when you need to provide context from multiple files in a chatbot conversation.

## Features

- Recursively search and read text files in a specified directory or the current working directory.
- Display the concatenated contents of all found text files, with each file's path included for clarity.
- Optionally copy the concatenated contents to the clipboard.
- Skip over specified directories (e.g., `.git`, `node_modules`) to avoid reading unnecessary files.
- Cross-platform compatibility (Unix-based systems, macOS, and Windows).

## Installation

Before installing the MultiCat CLI tool, ensure you have Python 3.6 or later installed on your system.

1. **Clone the Repository**

   ```bash
   git clone https://SuperMuel/multicat.git
   cd multicat
   ```

2. **Create and Activate a Virtual Environment (Optional but Recommended)**

   - On Unix/macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the MultiCat CLI tool, navigate to the directory where you've installed the tool and run one of the following commands:

- Display the contents of all text files in the current directory and its subdirectories:

  ```bash
  python multicat.py .
  ```

- Display the contents of all text files within a specific directory and its subdirectories, and another text file:

  ```bash
  python multicat.py /path/to/directory textfile.txt
  ```

- Display the contents of all files in the current directory and its subdirectories, and copy the output to the clipboard:

  ```bash
  python multicat.py --copy
  ```

- Display the contents of all files in the specified directory and its subdirectories, and copy the output to the clipboard:

  ```bash
  python multicat.py /path/to/directory --copy
  ```

## Calling multicat from anywhere

To use the MultiCat CLI tool from anywhere on your system, you'll want to make it executable and add its location to your system's PATH environment variable. This will allow you to call the tool using a simple command like `multicat` instead of needing to specify the full path to the Python script or navigate to its directory. Here are instructions for Unix-based systems (like Linux and macOS) and Windows.

### For Unix-based Systems (Linux/macOS)

1. **Make the Script Executable**: First, you need to make your `multicat.py` script executable. Navigate to the directory containing `multicat.py` and run:

   ```bash
   chmod +x multicat.py
   ```

2. **Rename the Script (Optional)**: For convenience, you might want to rename `multicat.py` to `multicat` (removing the `.py` extension).

   ```bash
   mv multicat.py multicat
   ```

3. **Add the Script to Your PATH**:

   - **Temporary Addition**: For a temporary solution that works only in your current terminal session, you can add the script's directory to your PATH using the export command. Replace `/path/to` with the actual path to the directory containing the `multicat` script.

     ```bash
     export PATH=$PATH:/path/to
     ```

   - **Permanent Addition**: For a more permanent solution, you'll want to add the script to your PATH by editing your shell's profile script (e.g., `~/.bash_profile`, `~/.bashrc`, `~/.zshrc`, etc.). Add the following line to the end of the file:

     ```bash
     export PATH=$PATH:/path/to
     ```

     Replace `/path/to` with the full path to the script's directory. After editing, save the file, and restart your terminal or source the profile script (e.g., `source ~/.bash_profile`).

### For Windows

1. **Add the Script to Your PATH**:

   - **Via System Properties**:

     1. Right-click on 'This PC' or 'My Computer' and select 'Properties'.
     2. Click on 'Advanced system settings' and then the 'Environment Variables' button.
     3. Under 'System Variables', scroll down and find the 'Path' variable, then click on 'Edit'.
     4. In the 'Edit Environment Variable' window, click 'New' and add the path to the directory containing `multicat.py`.
     5. Click 'OK' on all open windows to apply the changes.

   - **Via Command Line**:

     - Open Command Prompt as Administrator and run the following command, replacing `C:\path\to` with the actual path to the directory containing `multicat.py`:

       ```cmd
       setx PATH "%PATH%;C:\path\to"
       ```

2. **Create a Batch File (Optional)**: To simplify calling the script, you can create a batch file named `multicat.bat` in the same directory as your Python script (or another directory that's already in your PATH). The batch file should contain the following command:

   ```bat
   @echo off
   python C:\path\to\multicat.py %*
   ```

   Replace `C:\path\to\multicat.py` with the actual path to your `multicat.py` script. This batch file allows you to invoke the script simply by typing `multicat` followed by any arguments.

After completing these steps, you should be able to run the MultiCat CLI tool from anywhere in your terminal or command prompt by typing `multicat` (or just `multicat.py` if you skipped the renaming and batch file steps on Windows).

## Contributing

Contributions to the MultiCat CLI tool are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes.
4. Submit a pull request with a clear description of your changes.

## Support

If you encounter any issues or have questions about the MultiCat CLI tool, please file an issue on the GitHub repository.

## License

The MultiCat CLI tool is released under the [MIT License](LICENSE). Please see the LICENSE file for more details.
