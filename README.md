# Github API access and visualisation

CSU-33012 Software Engineering project of Github API access and visualisation of data.

Started with Professor Stephen Barret's Python walkthrough lectures.

I aim to visualise data concerned with user locations and see how GitHub has allowed software developers to connect over vast distances. This tool will look at the location of a logged in user and the locations of all of their followers and followees. I hope to visualise the resulting data in a way that shows how physically ditant developers are closely connected on GitHub by timezones.

This is useful for softare developers to see which timezones to worry about if they're considering working with followers or followees on Github, as it is likely that future or past collaborators are either followed or followers, or both. Likewise, it can be used to see if a developer is in the same time zone as the majority of their followers or followees. Planning and working around international time zones is an important step in the software engineering process, and this tool help provide insight on this, especially in the light of the current era of remote work becoming ever more popular.

Because this tool is not intended to process a very large amount of data, I have opted to not use a database such as MongoDB. Instead, I have used a CSV file.

API access scripts: Written in Python 3.8.10 with PyGithub.
Data storage: CSV file.
Visualisation: D3.js.

## Pre-Requisites

- [Python 3.6 or higher](https://www.python.org/downloads/) installed
- Valid GitHub token set as an environment variable `GITHUB_TOKEN` (this can be done via [Control Panel or System Settings](https://imgur.com/a/CQjLpfk) if you are on Windows. You may need to restart your computer)
- The following Python packages installed (see installed packages with `pip list`):
  - pip (`python3 get-pip.py`)
  - PyGithub (`pip install PyGithub`)

If you don't have pip, run setup.sh to install it along with PyGithub.

## Instructions

Run start.sh to run the python script and start the http server.
Navigate to the webpage at <http://localhost:8080/> in your browser to view the visualisation.
