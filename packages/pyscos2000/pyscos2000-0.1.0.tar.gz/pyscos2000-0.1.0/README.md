# pyscos2000

Parsing and checking SCOS-2000 databases with native python.

You can find the [documentation 
here](https://irf.developer.irf.se/pyscos2000/).


## Installation

To install `pyscos2000` you will have to clone the repository and install 
it like this:

    git clone https://gitlab.irf.se/irf/pyscos2000.git
    pip install ./pyscos2000

In case you want to actually modify this library be sure to clone the 
repository through ssh and install it in a way that’ll allow you to build 
the documentation, too:

    git clone git@gitlab.irf.se:irf/pyscos2000.git
    pip install -e ./pyscos2000[docs]


## Usage

To load a SCOS-2000 database from the `.dat` files in your
`ASCII` directory, run this:

    import pyscos2000

    scos = pyscos2000.SCOS('./ASCII')

The various tables will then be available as (for example) `scos.plf`.

Each table has the rows available as the `rows` property, e.g.
`scos.plf.rows`.


## License

[MIT](LICENSE)
