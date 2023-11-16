# https://github.com/snipem/gt7dashboard
# http://localhost:5006/gt7dashboard

.\env.ps1
echo $Env:GT7_PLAYSTATION_IP

cd ../clones/gt7dashboard
.\.venv\Scripts\Activate.ps1

python -m bokeh serve .
