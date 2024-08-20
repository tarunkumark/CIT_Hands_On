# Local Setup Steps
## Clone the repo
```bash
git clone https://github.com/tarunkumark/CIT_Hands_On
```
## Create a virtual environment

```bash
cd CIT_Hands_On
python3 -m venv env
```

## Activate your environment

### Windows
```powershell
./env/Scripts/activate
```

### Linux/Mac
```bash
source env/bin/activate
```

## Install the requirements
```bash
pip install -r requirements.txt
```

## Run the server
```bash
uvicorn app.main:app --reload
```