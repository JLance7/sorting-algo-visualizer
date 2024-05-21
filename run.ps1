# PowerShell

$VENV_PATH = ".venv"
$TEST = $args[0]


if (-not (Test-Path -Path $VENV_PATH -PathType Container)) {
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
} else {
    .\.venv\Scripts\Activate.ps1
}

mypy src/
if ($null -ne $TEST) {
    pytest
}
echo 'running...'
python main.py

# python versoin 3.8.2
# pip version 24.0