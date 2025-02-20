# Docker MySQL Setup Script

This script built by me automates the process of finding an available port, running a MySQL Docker container, retrieving the generated root password, and optionally stopping or removing the container.

## Features
- Finds the first available port between **8080** and **8999**.
- Runs a **MySQL Docker container** with a randomly generated root password.
- Extracts and displays the generated root password from the container logs.
- Prompts the user to **stop** or **remove** the container after execution.
- Displays all Docker containers (running and stopped) at the end.

## Requirements
- Python 3.12.3
- Docker installed and running

## Installation
1. Ensure **Docker** is installed on your system.
2. Clone this repository or copy the script to your local machine.
3. Install required Python modules (if not already available):
   ```sh
   pip install docker
   ```

## Usage
Run the script using Python:
```sh
python3 script.py
```

## How It Works
1. The script finds an **available port** (starting from 8080).
2. It runs a **MySQL container** using the found port.
3. It extracts the **generated MySQL root password** from the logs.
4. It prompts the user whether they want to **stop** or **remove** the container.
5. Finally, it displays all Docker containers (including stopped ones).

## Example Output
```
First available port starting from 8080: 8081

Docker Output: [Container ID]
Docker Errors: No errors!

Looking for your MySQL server's password...

Your MySQL server's password: xxxxxxxx

Do you want to stop your container? (Y/n)
Remember to stop your container later.

Do you want to delete your container? (Y/n)
Remember to delete your container later.

CONTAINER ID   IMAGE   ...
```

## Notes
- The MySQL container is started with the **MYSQL_RANDOM_ROOT_PASSWORD=yes** environment variable, which means the password is auto-generated.
- If no available port is found, the script **exits**.
- The container name is set to `db`. If a container with this name already exists, the script may fail.

