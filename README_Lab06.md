# LAB 06: Object orienting, and applying Design Patterns to your code.

This week we'll go hands on with **refactoring** by object orienting your code and setting up a couple of design patterns around it.

This lab should be done **AFTER** we have merged your current branch so code review can be done separately from the base setup.

After review and merge, create a new branch `LAB-06_oop_design_patterns` for this lab.

## Overview:
* Review the class lecture video where I will describe the sample file.
* You should find the sample file `base_gainers.py` in our scripts directory.
* Fill in more detail, i.e. migrate your existing code to fill out the classes.
* You should have in the end
    - A bin/gainers/ directory for three files, your base class, and the two gainers
    - Also in this bin/gainers directory you should have a gainers_factory.py file for that class
    - In your root directory, a new script which will have your template class and a 'main' section to run the file directly
* The last bullet point should account for all the new code, you will also need to:
    - refactor your tests to adapt to the new architecture
    - add a `make gainers SRC=<which>` job to your makefile.

## You know you will be done when:
Your directory structure looks like:

