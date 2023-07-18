# Code coverage report with selenium

More info here https://opensrc.mx/posts/getting-a-code-coverage-report-with-selenium/

## Get it working


### For getting working the frontend 

```
cd react/
npm install
npm run dev
```

### Run the e2e


```
python -m env .venv
source .venv/bin/activate
pip install -r requirements.txt
python test_todo.py
```

### Analyze the coverage

```
mkdir -p react/.nyc_output
cp coverage1.json react/.nyc_output
cd react
npx -y nyc report 
npx -y nyc report  -r html
firefox coverage/index.html
```


