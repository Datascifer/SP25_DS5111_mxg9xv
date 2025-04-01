# LAB 07 - Collecting Data
In this lab you will set up a cron job to automatically collect data over spring break.
You'll use a standard tool in linux, the cronjob, which will call your code three times a day for a week.
The data you collect (around 15 csv files) will be the RAW data for your project.

In the following labs, you will load this data to Snowflake and process them with SQL.
You'll also be able to use python to process the RAW data to generate intermediate tables to store in Snowflake.
Finally, you'll process the intermediate data for final results.
We'll talk some more about these steps later on, for now we will focus on a simple task of setting up recurring data collection.

## What you'll need
* At the very least you need your code to be able to download the Yahoo and WSJ gainers **with a datestamp** in the filename.

## How to do it
Crontab is/should already be installed on your linux box.
At it's most basic, you can think of the feature as an always on app running in the background.
This app checks a special file `crontab` and reads entries in it every minute.
You start a line in the crontab with special notation to indicate a recurring time.
Then the app will execute the command following the time notation.

The time set up has 5 fields:
```
*    *    *    *    *
┬    ┬    ┬    ┬    ┬
│    │    │    │    └─  Weekday  (0=Sun .. 6=Sat)
│    │    │    └──────  Month    (1..12)
│    │    └───────────  Day      (1..31)
│    └────────────────  Hour     (0..23)
└─────────────────────  Minute   (0..59)
```

In place of the `*` we can also use
| operator | meaning                    |
| --       | --                         |
| *	       | all values                 |
| ,	       | separate individual values |
| -	       | a range of values          |
| /        | divide a value into steps  |

You'll notice the smallest sized field, (left most), is minutes.  So the highest frequency you can get is "every minute".
This would be `* * * * *`.  I.e. Every minute of every hour of every day of every month...
Here are some examples I picked up off the web:
```
0 * * * *	      # every hour
*/15 * * * *	  # every 15 mins
0 */2 * * *	    # every 2 hours
0 18 * * 0-6	  # every week Mon-Sat at 6pm
10 2 * * 6,7	  # every Sat and Sun on 2:10am
0 0 * * 0	      # every Sunday midnight
```

You can find more about the notation in the linux reading resources.

The thing to note here is you can select specific days.  So your first task is to find the cron notation to run:

* Every weekday, i.e. Monday thru Friday (stock markets are not open on weekdays, at least regular hours).
* Three times a day, at 9:31am EST, at 12:30pm EST and at 4:01 EST

The notation with a job would look like:
```
*/15 * * * * python /home/ubuntu/my_script.py
```
That would run `python /home/ubuntu/my_script.py` every 15 minutes.  The command just follows the time notation.

## Add a cron job for each of your gainers
So now you should have the notation to run your ygainers or wsjgainers commands from crontab.
The timestamp part is important because that way the csv generated won't overwrite.
Also, you will need to clear the html and csv generated after data collection since you want to make sure your jobs execute.
In other words, if you delegate to make, and make sees files exist for the jobs it won't run.

Set this up over spring break and you should have 15 files at the end of the week.  Some jobs may fail, that's ok, you should get most.

## How to edit the crontab
* `crontab -e` edits the crontab
* `crontab -l` lists the jobs

## What you'll turn in
* A link to a short file in your repository with the cron notation and commands you used
* A link to a folder with the successfully collected data, (hopefully around 10 to 15 so we have something to use for next lab).
* Points 10, (5 for the crontab commands, 5 for the data)
Points 10 points

## NB:
The crontab file works similarly than the makefile, in the sense that one sigle line is it's own 'shell'.
In other words, your full command has to fit in one line.

The crontab will not start in the location of your repository, so you will need to `cd` to where you want to execute from first.

Since the crontab starts from it's own location and does not enter your virtual environment, you'll have to add that.
You can either do it in the crontab, OR have your makefile do it.
