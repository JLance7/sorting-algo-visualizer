# PowerShell

$VENV_PATH = ".venv"

if (-not (Test-Path -Path $VENV_PATH -PathType Container)) {
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
} else {
    .\.venv\Scripts\Activate.ps1
}

pytest
echo 'running...'
python main.py