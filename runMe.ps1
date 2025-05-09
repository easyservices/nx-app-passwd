# PowerShell script to run Streamlit application with PowerShell 7.1
# This script ensures the application runs with the correct PowerShell version
# and activates the Python virtual environment if one exists

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
        ".env",
        "..\venv",
        "..\env"
    )
    
    foreach ($venvPath in $venvLocations) {
        # Check for Windows activation script
        $activateScript = Join-Path $venvPath "Scripts\Activate.ps1"
        if (Test-Path $activateScript) {
            Write-Host "Found virtual environment at: $venvPath"
            Write-Host "Activating virtual environment..."
            & $activateScript
            return $true
        }
        
        # Check for Unix/Linux/macOS activation script (in case of PowerShell on those platforms)
        $unixActivateScript = Join-Path $venvPath "bin/Activate.ps1"
        if (Test-Path $unixActivateScript) {
            Write-Host "Found virtual environment at: $venvPath"
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
            Write-Host "Installing Streamlit..."
            pip install streamlit
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
    Write-Host "Starting Streamlit application..."
    streamlit run streamlit_app.py
}

# Main execution
if ($psVersion -lt $requiredVersion) {
    Write-Host "Current PowerShell version is $($psVersion.ToString())"
    Write-Host "This script requires PowerShell 7.1 or higher. Attempting to launch with pwsh..."
    
    # Try to launch with pwsh (PowerShell 7)
    try {
        & pwsh -Command {
            # Source the script to get the functions
            . $PSScriptRoot\runMe.ps1
            
            $psVersion = $PSVersionTable.PSVersion
            Write-Host "Launched with PowerShell $($psVersion.ToString())"
            
            # Run Streamlit function
            Start-Streamlit
        }
    } catch {
        Write-Host "Failed to launch PowerShell 7. Please make sure it's installed."
        Write-Host "You can install it from: https://github.com/PowerShell/PowerShell/releases"
        exit 1
    }
} else {
    Write-Host "Running with PowerShell $($psVersion.ToString())"
    Start-Streamlit
}