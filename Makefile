default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200 > ygainers.html

ygainers.csv: ygainers.html
	. env/bin/activate; python -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"

wjsgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox https://www.wsj.com/market-data/stocks/us/movers > wjsgainers.html

wjsgainers.csv: wjsgainers.html
	. env/bin/activate; python -c "import pandas as pd; raw = pd.read_html('wjsgainers.html'); raw[0].to_csv('wjsgainers.csv')"

test: ygainers.csv wjsgainers.csv
	@echo "Checking if CSV files were generated successfully..."
# awesome that you added a more intricate test here in the makefile. I suppose that could be farmed off to a script, however
# it does give you insight into how to better use makefiles!
	@if [ -s ygainers.csv ] && [ -s wjsgainers.csv ]; then \
		echo "Test passed: Both CSV files were created and are not empty"; \
	else \
		echo "Test failed: One or both CSV files are empty or were not created"; \
		exit 1; \
	fi

# I'm not seeing pytest being called here, nor pylint


clean:
	rm -f *.html *.csv
	rm -rf env/
