# PowerShell script to run Streamlit HTTP Bearer Auth application with PowerShell 7.1
# This script ensures the application runs with the correct PowerShell version
# and activates the Python virtual environment if one exists

# Set the working directory to the script's location
$scriptPath = $MyInvocation.MyCommand.Path
$scriptDir = Split-Path -Parent $scriptPath
Set-Location -Path $scriptDir
Write-Host "Working directory set to: $scriptDir"

# Check if running in PowerShell 7.1 or higher
$psVersion = $PSVersionTable.PSVersion
$requiredVersion = [Version]"7.1"

# Function to find and activate virtual environment
function Find-And-Activate-Venv {
    # Common virtual environment locations to check
    $venvLocations = @(
        "venv",
        ".venv",
        "env",
        ".env"
    )
    
    foreach ($venvPath in $venvLocations) {
        # Use absolute paths based on script directory
        $fullVenvPath = Join-Path $scriptDir $venvPath
        # Check for Windows activation script
        $activateScript = Join-Path $fullVenvPath "Scripts\Activate.ps1"
        if (Test-Path $activateScript) {
            Write-Host "Found virtual environment at: $venvPath"
            Write-Host "Activating virtual environment..."
            & $activateScript
            return $true
        }
        
        # Check for Unix/Linux/macOS activation script (in case of PowerShell on those platforms)
        $unixActivateScript = Join-Path $fullVenvPath "bin/Activate.ps1"
        if (Test-Path $unixActivateScript) {
            Write-Host "Found virtual environment at: $fullVenvPath"
            Write-Host "Activating virtual environment..."
            & $unixActivateScript
            return $true
        }
    }
    
    Write-Host "No virtual environment found in common locations."
    return $false
}

# Function to run Streamlit
function Start-Streamlit {
    # Try to activate virtual environment
    $venvActivated = Find-And-Activate-Venv
    
    if ($venvActivated) {
        Write-Host "Using Python from virtual environment"
    } else {
        Write-Host "Using system Python"
    }
    
    # Display Python and pip information
    try {
        $pythonVersion = python --version
        Write-Host "Python version: $pythonVersion"
        
        $pipList = pip list | Select-String -Pattern "streamlit"
        if ($pipList) {
            Write-Host "Streamlit is installed: $pipList"
        } else {
            Write-Host "Streamlit is not installed in the current Python environment."
            Write-Host "Checking if requirements.txt exists..."
            
            $requirementsPath = Join-Path $scriptDir "requirements.txt"
            if (Test-Path $requirementsPath) {
                Write-Host "Installing dependencies from requirements.txt..."
                pip install -r $requirementsPath
            } else {
                Write-Host "Installing Streamlit..."
                pip install streamlit
            }
        }
    } catch {
        Write-Host "Error checking Python environment: $_"
        exit 1
    }
    
    # Check if Streamlit is installed
    try {
        $streamlitVersion = (streamlit --version) 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Streamlit version: $streamlitVersion"
        } else {
            throw "Streamlit not found"
        }
    } catch {
        Write-Host "Streamlit is not installed or not in PATH. Please install it with: pip install streamlit"
        exit 1
    }
    
    # Run the Streamlit application
    Write-Host "Starting Streamlit HTTP Bearer Basic Auth Token Generator application..."
    streamlit run streamlit_http_bearer_gen.py
}

# Main execution
if ($psVersion -lt $requiredVersion) {
    Write-Host "Current PowerShell version is $($psVersion.ToString())"
    Write-Host "This script requires PowerShell 7.1 or higher. Attempting to launch with pwsh..."
    
    # Try to launch with pwsh (PowerShell 7)
    try {
        & pwsh -NoExit -Command {
            # Get the script path from the parent scope
            $scriptPath = $args[0]
            $scriptDir = Split-Path -Parent $scriptPath
            
            # Change to the script directory
            Set-Location -Path $scriptDir
            Write-Host "Working directory set to: $scriptDir"
            
            # Source the script to get the functions
            . $scriptPath
            
            $psVersion = $PSVersionTable.PSVersion
            Write-Host "Launched with PowerShell $($psVersion.ToString())"
            
            # Run Streamlit function
            Start-Streamlit
        } -Args $MyInvocation.MyCommand.Path
    } catch {
        Write-Host "Failed to launch PowerShell 7. Please make sure it's installed."
        Write-Host "You can install it from: https://github.com/PowerShell/PowerShell/releases"
        exit 1
    }
} else {
    Write-Host "Running with PowerShell $($psVersion.ToString())"
    Start-Streamlit
}