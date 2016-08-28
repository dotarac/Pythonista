'''

Copyright 2016 David-Olivier Tarac
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

'''
This script is meant to import python files stored in a specific dropbox folder.
It uses Workflow iOS app as middleware to access dropbox folder files list. 
User can select multiple files to import all or some of them. 
Content of .py files is then imported back to pythonista using ios clipboard functionality. 
Url scheme is used to switch between pythonista and Workflow and loop through the selected files list.

The workflow is described here: https://github.com/dotarac/Pythonista/blob/master/README.md

original script from Paul Snydel was modified as follows
- bug corrected on encoding content of clipboard
- import is made in a specific pythonista folder which is created in case it does not exists
- script checks for already existing filenames to avoid overwriting and numerical suffix is added to filename if necessary
- pythonista invokes url callback to return in workflow and finish looping in the list of files selected for import

'''
# coding: utf-8
import sys
import clipboard
import webbrowser
import os

importpath= "ImportedScripts/"
if not os.path.exists(importpath):
	os.mkdir(importpath)
newscriptname =importpath+sys.argv[1] + ".py"
while os.path.exists(newscriptname):
	newscriptname=newscriptname[:-3]+"_1"+".py"
cbcontent = clipboard.get()
newscriptfile = open(newscriptname, "w",encoding='utf-8')
newscriptfile.write(cbcontent)
newscriptfile.close()
webbrowser.open('workflow://')