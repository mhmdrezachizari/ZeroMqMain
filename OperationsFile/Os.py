import subprocess
async def OsHandler(command_data):
    command_name = command_data.get("command_name")
    parameters = command_data.get("parameters", [])

    try:
        return await run_command(command_name, *parameters)

    except Exception as error:
        return {"error": f"Failed to execute {command_name} with parameters {parameters}. Error: {str(error)}"}

async def run_command(command_name, *parameters):
    try:
        cmd = f"{command_name} {' '.join(parameters)}"
        result = subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            return {"result": result.stdout.strip()}
        else:
            return {"error1": result.stderr.strip()}

    except Exception as error:
        return {"error2": str(error)}
