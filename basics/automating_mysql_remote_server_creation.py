import subprocess
import socket
import re
import time

def find_available_ports(start=8080, end=8999):
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
    return None

# Find available ports
port = find_available_ports()

def user_input(msg: str) -> bool:
    ipt = input(msg).lower()
    possible_inputs = ["yes", "y", "no", "n"]

    while ipt not in possible_inputs:
        ipt = input("Invalid input. (Y/n)")

    if ipt[0] == "y":
        return True
    return False

def stop_or_rm(yes_or_no: bool, cmd: list[str], keyword: str) -> bool:
    if yes_or_no:
        subprocess.run(cmd)
        return True
    print(f"Remember to {keyword} your container later.")
    return False

if port:
    print(f"First available port starting from 8080: {port}")
    r = subprocess.run(["docker", "container", "run", "--publish", f"{port}:80", "--name", "db", "-e", "MYSQL_RANDOM_ROOT_PASSWORD=yes", "-d", "mysql"], capture_output=True, text=True)
    # Print the Docker output
    print("\nDocker Output:", r.stdout)

    docker_errors_output = r.stderr
    if(not r.stderr):
        docker_errors_output = "No errors!"
    print("Docker Errors:", docker_errors_output)

    time.sleep(8)

    dockerlogs = subprocess.run(["docker", "container", "logs", "db"], capture_output=True, text=True)

    match = re.search(r"GENERATED ROOT PASSWORD:\s*(\S+)", dockerlogs.stdout)

    print("\nLooking for your MySQL server's password...")
    
    time.sleep(2)

    if match:
        print(f"\nYour MySQL server's password: {match.group(1)}")
    else:
        print("\nNo password found")

    stop = user_input("\nDo you want to stop your container?(Y/n) ")
    stop_or_rm(stop, ["docker", "stop", "db"], "stop")
    stop = user_input("\nDo you want to delete your container?(Y/n) ")
    stop_or_rm(stop, ["docker", "rm", "-f", "db"], "delete")
else:
    print("No ports available")

docker_ps_all = subprocess.run(["docker", "container", "ls", "-a"], capture_output=True, text=True)
print(f"\n{docker_ps_all.stdout}")
