# Open Source Search Engine
The project implements a inverted index search for a query in a set of documents.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

There are no prerequisites for running the project besides Python3.

### Installing

All the libraries used are part of the Python standard, so you only need to
install Python3.
For installing Python3 on Ubuntu 18.04(although it should already be installed), run:
```
apt-get install python3
```
## Running the tests

The tests are not yet implemented, but a general expected case would be:
python3 testUnit.py <projectMainFile> which will run a number of different tests
that will try to cover as many corner cases as possible, afterwards displaying
which tests have failed, if any.
### Break down into end to end tests

The tests will try to cover more and more complex cases, in order to cover most
possible uses cases.
The first tests will deal with basic functions, like finding a word that is in every
file, a word that isn't in any file, finding two words etc.
Following tests will try to cover small corner cases like word && !(word), ending with
large  20 terms queries to check the full functionality.
Examples:
```
Raspberry
Raspberry && !(Raspberry)
Raspberry || Python || ancient
```

## Deployment

There should be no aditional steps for deployment since the project is a
pretty standard Python file.

## Authors

* **Datcu Gabriel** - *Initial work* - [thoughtitwasadrought](https://github.com/thoughtitwasadrought)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Various Stack Overflow users for small Python functionalities I forgot.
