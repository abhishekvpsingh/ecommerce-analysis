import subprocess

def run_python_script(script_path):
    print(f"Running script: {script_path}")
    try:
        subprocess.run(["python", script_path], check=True)
        print(f"Script '{script_path}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing script '{script_path}': {e}")
    except FileNotFoundError:
        print(f"Error: Script not found at '{script_path}'")

def run_dbt_command(command):
    print(f"Running dbt command: {command}")
    try:
        subprocess.run(["dbt", command], check=True, cwd="../dbt_ecommerce_analysis")
        print(f"dbt command '{command}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing dbt command '{command}': {e}")

if __name__ == "__main__":
    run_python_script("./extract_data.py")
    run_python_script("./load_data.py")
    run_dbt_command("run")
    # run_dbt_command("test") # Optional: Run dbt tests
    print("Data pipeline execution complete.")