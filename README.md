# Django easy way to handle environments

This Django project demonstrates a simple way to manage both local and production environments. It is built upon Fly.io deployment and provides an easy method to switch between local development and production environments.

## Usage
To run the project, just type the following commands in the terminal:

**For development:**
```
    python3 environment.py -d
```
or
```
    python3 environment.py --development
```

**For production:**
```
    python3 environment.py -p
```
or
```
    python3 environment.py --production
```

## An easier and smarter way
Create an alias to make it easier and faster to handle environments.

On Linux / Ubuntu / Mac
```
    $ nano ~/.bashrc
```

Add the following to the bottom of the file:
```
    alias pe="python3 environment.py"
```
Now you can simply type **pe -p** or **pe --production** and **pe -d** or **pe --development.**
