About:


## Design
* [API design](docs/api.md)
* [Docs for Install](docs/install_docs.md)

## Tests:
Testing will be utilized with the unittest library.
Testing consists of, ensuring that the API is returning a 200 response,
dependencies have been installed, and 

To run the test file:
`python3 -m unittest tests/test_view.py`


## Functionality:
This program contains a CLI command to run a Python3 file that will take in an input CSV file as the first argument, and output a new CSV file that has been merged with an API to provide additional data for Account's. The new CSV file contains all original peices of data on the input file, with two additional headers from the API. 

We will primarily use the built in functions of Python3. We'll be importing CSV to read the files. JSON and Requests to read the data coming from the API. Followed by SYS to run command line arguments and pass them to the function. 


## Develop:
- Setting up this program only requires a few things to get running. 

1. Ensure that your .csv file is in the root of the project and not inside of a folder. 

2. A.) Python offers a built-in virtual environment so you can install dependencies just in the virtual environment, rather than to your local machine. 
This is recommended not only for efficency but security as well. 
This is best typed in your real terminal and not the Visual Studio Code terminal.

In your terminal inside of the folder where the application exists. 

Create the venv file:
Run `python -m venv .venv` 
Start the virtual environment file:

macOS:
`source ./.venv/bin/active`
Windows:
`.\.venv\Scripts\Activate.ps1`

To exit the venv:
run `deactivate`


3. Running the .sh file on a macOS or linux. 
    After your virtual environment is activated; you can run the entire install of dependent packages as well as set up path.
    run `./run.sh` 
    The terminal will ask you for a password to enable permissions for the pages; 
    You'll see the requirements being installed and a message will output saying 
    `Installation Complete`. 


4. Ensure that your path is set up correctly, if not previously completed in the run.sh file or a windows user. 

utilizing MAC/LINUX:
    run `pwd` to verify the hierarchy of your file on the local machine
    copy the output in the terminal 
    run `export PATH=$PATH:[path to directory]`
    run `echo $PATH` to verify it was added correctly 
utilizing WINDOWS:
    open in the file explorer;
    `edit system enviornment variables`
    once system properties is open, click on the `environment variables` button;
    inside of the system variables box, find `Path` and open it. 
    run `pwd` in your terminal to grab the exact path.  
    copy the output of the pwd from the terminal, and add it to
    the `Edit enviornment variable` box thats open by clicking the `new` 
    button. 
    One you see your path at the bottom, select the `okay` boxes to ensure the changes are stored. 

    See the associated link from the microsoft docs on how to set up PATH.
    * [Docs for Install](docs/install_docs.md)

<!-- windows registration of path is NOT successful. cli command is opening the page itself not running the .sh file -->


5. Once path is correctly configured, simply run this command in your terminal of choice. The first property is an .sh file that executes the program. The second property is an argument that needs to be the title of your .csv file. The third property is what you would like your new .csv file to be named, as an argument that gets passed in. 

` wpe_merge <inputfile.csv> <outputfile.csv> `

    When merge is successful; you should see the `outputfile.csv` file at the root level. You'll also see a `Merge Complete` message to let you know it was successful. 




