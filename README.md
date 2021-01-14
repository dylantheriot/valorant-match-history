## If you downloaded this project BEFORE 1/12/2021, you will need to redownload the code/zip and rerun installation for it to work again.

# VALORANT ELO TRACKER

Track and view your VALORANT elo with this web application. As of 12/26, the original site has been taken down.

# DISCLAIMER
Please note that **ANY** currently online websites utilizing this code with the original functionality are not endorsed by me and I **CANNOT** guarantee that your username/password are safe when using them. Currently the only safe method I can endorse is downloading this project from my GitHub and running it locally on your computer by following this video tutorial.

Please **DO NOT** input your username/password into any other URL links that are running the same code as your information may be stolen. Even if the website links to me, it does not mean I endorse it or that I am the person running it.

Riot Games, if you would like me to take this application down please let me know. I can be contacted via [Twitter](https://twitter.com/_dylantheriot) or [Email](mailto:dylantheriot@tamu.edu).

## Installation
Pick one of the two following methods to install and run this project:
### Regular Installation (Recommended)
You can follow along with the **VIDEO TUTORIAL** [here](https://youtu.be/56D9lH0O5hU).

1. Ensure you have Python 3.X and pip on your computer. You can download it on Windows [here](https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7?activetab=pivot:overviewtab), and most Macbooks should already have Python pre-installed.
2. Clone the code/repo (download the zip, utilize `git clone`, or any other method)
3. In the root directory (the valorant-match-history folder), run `python3 -m pip install -r requirements.txt`
4. Run `python3 ./wsgi.py`
5. If no errors occur, visit the site `http://127.0.0.1:5000/` in your browser of choice. Only the computer you ran step 4 on will have access to this site.

### Docker Installation
1. Clone the code/repo (download the zip, utilize `git clone`, or any other method)
2. In the root directory, run `docker build -t valorantelo:1.0 .`
3. Run `docker images` and identify the *IMAGE ID* associated with the valorantelo repository and 1.0 tag. In the following screenshot, the IMAGE ID is fbce9febcaa8.

![image](https://user-images.githubusercontent.com/43360378/103196926-ada76100-48aa-11eb-97bc-ca475d9c7696.png)

4. Run `docker run -p 5000:5000 <YOUR_IMAGE_ID>`. In the example, the commmand would be `docker run -p 5000:5000 fbce9febcaa8`.
5. Visit `http://0.0.0.0:5000/` in your web browser from the same device that ran step 4.

### Login
Login using your Riot Games account
If you currently login with google, you will have to disconnect that and create a standard Riot login
To do so:
1. Go to https://account.riotgames.com/account
2. Select the "connected accounts" tab
3. Press disconnect onto google/facebook/whatever you are using to login in
4. It will tell you to create a new riot login, create it
5. Press submit, and you should be able to use the new login you made for this, but remember it/write it down because you may need to re-login into any riot games you have and will need to use this new login


## Notes
Inspired from https://github.com/RumbleMike/ValorantRankedPoints and https://gist.github.com/Luc1412/1f93257a2a808679ff014f258db6c35b

Hosted at https://valorantelo.gg

## Alternatives
If you are looking for an alternative, please checkout RumbleMikee's version (we are not affiliated, but this site was based off of his project). You can learn more about his project [here](https://twitter.com/RumbleMikee/status/1341427684145033217?s=20)
