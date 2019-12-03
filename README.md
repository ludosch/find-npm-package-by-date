# find-npm-version-by-date
Find most recent package by given date (work with package list)

## How it's work ?
Use npm view and a little of python

## How to run ?
Install npm and run with python 3 :
```
> python find-npm-version-by-date.py <YYYY-MM-DD> <packages...>
```

Exemple :
```
> python find-npm-version-by-date.py 2019-02-28 lodash chalk
lodash@4.17.11
chalk@2.4.2
```
