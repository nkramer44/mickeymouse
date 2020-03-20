# mickeymouse
For all my BankerBros working from home this fine pandemic

## Instructions
These instructions are for macOS users. If you need instructions for a Windows computer, hit me up

### Setup
Open up the `Terminal` application.

Run the following commands:
```shell
# This will install the code on your Desktop.  If you want it somewhere else, 
# substitute ~/Desktop for the current path
cd ~/Desktop

git clone https://github.com/nkramer44/mickeymouse.git
cd mickeymouse

# This will install a bunch of stuff.  Might take a while...
chmod a+x install.sh
./install.sh
```

### Run
The first time you run this, you'll have to make `run.sh` executable, so run
```
chmod a+x run.sh
``` 

Every time after that, whenever you want to don't feel like doing your 
work for the day, run these
```shell 
# Replace this path with where you cloned the repo
cd ~/Desktop/mickeymouse

./run.sh
```

Then sit back, relax, and enjoy the view.  The world only ends once!

When you want to get back to work, go to your `Terminal` application, and hit
`control + c`
