# Summary

This Python script employs Selenium to automate a sequence of steps for searching a bank branch and clicking on it on Banque Populaire's website (https://www.banquepopulaire.fr/).

### Installation

1.  Clone the repository to your local machine:

```sh
   git clone https://github.com/valentinc94/bpce_selenium_practice.git
```

2.  Change into the project directory:

```sh
   cd bpce
```

3.  Create a virtual environment (optional, but recommended):

```sh
   python -m venv venv
```

4.  Activate the virtual environment:

-   On Windows:

```sh
   venv\Scripts\activate
```

-   On macOS and Linux:

```sh
   source venv/bin/activate
```

5.  Install the required packages:

```sh
   pip install -r requirements/base.txt
```

### Running the Tests
To run the unit tests, make sure you are in the project directory and the virtual environment is activated.

```sh
   python -m unittest discover tests
```

### Running the Code

To run the code, make sure you are in the project directory and the virtual environment is activated.

```sh
   python client.py
```

### Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

Happy coding!
