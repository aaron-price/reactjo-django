# Installation

Start with this if you haven't already

```bash
python3 -m venv env         # Or python -m venv env (windows)
source env/bin/activate     # Or just env/Scripts/activate (window)
pip install reactjo
reactjo init
```

2. In reactjorc/config.json, add this to the extensions array:

```
{
    "uri": "https://github.com/aaron-price/reactjo_django.git",
    "rc_home": "reactjo_django",
    "branch": "master"
}
```
Note that branch is optional and defaults to master.

3. Back in your terminal, run:
```
reactjo update
```
This clones the extension into reactjorc/extensions/django_trial
It will be listening for the commands listed below, in Usage.

# Usage

```bash
reactjo new # prints "hello world"
```
