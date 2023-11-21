Step 1: Install Python
Go to the official Python website.
Download the latest version of Python for your operating system.
Run the Python installer and ensure the "Add Python to PATH" option is selected.

Step 2: Create a Virtual Environment (venv)
Open a terminal (command prompt) and navigate to your project directory.
# Create a virtual environment in the project directory
python -m venv venv

Step 3: Activate the Virtual Environment
For Windows:
venv\Scripts\activate

Step 4: Install Dependencies
Then, install the dependencies:

pip install -r requirements.txt

Step 6: Run the Script
Activate the virtual environment if it's not already activated and run the script:

python main.py
Note:
Ensure you have an internet connection, as the script makes requests to websites.
It is assumed that the sites.xlsx file exists in the same directory as your script and contains a column named urls.