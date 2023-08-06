""" 
A mapping tool for Dataweave developers

Use Case : It generates dataweave mapping

Considerations :
1. Use a comma-separated file
2. The file should have the 3 mandatory columns : ['Source','Logic','Canonical']
3. Please use the following to denote the different levels:
    ~ {field-name} - A field at root level
    ~ object:{name} - An object at root level
    ~ array:{name} - An array at root level
    ~ <<{field-name} - A field belonging to an array/object
    ~ <<object:{name} - An object inside an array
    ~ ++{field-name} - A field at root level that is mapped to an element in an array/object
    ~ <<<<{field-name} - A field belonging to an object inside an array
    ~ <<<<payload>{field-name} - Reference to a field at root-level inside an object in an array
    ~ <<<<root>{field-name} - Reference to a field belonging to the array inside an object in that array
4. The last line on the file should not belong to any collection
5. Map an array to an array; object to an object
    ~ Incase of mapping some fields at root level to some fields in an object, the cell corresponding to the object name on 'Source' column should be blank
6. The first row should be a mapping at root level & should not be null
7. There should not be an empty collection
8. A logic can have more than 1 "if" statements but only 1 "else" statements
    ~ Please break the logic into mutiple lines as per the number of "if" & "else" statements. One line can have only one "if"/"else" statement
    ~ To write an "if" statement based on 
        - whether the field is null, use syntax - "if {field}=null"
        - whether the field is not null, use syntax - "if {field}=not_null"
9. In case there is a default value for any field, use syntax - "use {value}"
10. Use '__header_script' to get the proper syntax for using the 'map' function

** There might be unhandled cases. Please use the mapping generated carefully after due inspection.
** Array within objects are not handled as of now.

"""

from dwscripter import bridge
import click, logging, pandas as pd, warnings, pkg_resources
from tabulate import tabulate
warnings.filterwarnings("ignore")

@click.group()
def main():
    click.echo("A CLI tool to generate DW Scripts based on a CSV file")
    pass 

@main.command()
@click.argument('guide', required=False)
def guide(**kwargs):
    """User Manual - Information/Instruction"""
    click.echo(__doc__)

@main.command()
@click.argument('mapper', required=False)
def mapper(**kwargs):
    """DW Script Generator - An input file is needed (Please use command 'try' for example)"""
    bridge.bridgeClass().map_gen()
    click.echo("Process completed.")

@main.command()
@click.argument('try', required=False)
def trial(**kwargs):
    """A sample CSV File is displayed which can be used as a reference"""
    try:
        read = pkg_resources.resource_stream(__name__, 'sample/sample.csv')
        sample = pd.read_csv(read, delimiter = ",")
        click.echo("\nSample File: \n")
        click.echo(tabulate(sample, headers='keys', tablefmt='psql'))
        sample_mapping = bridge.bridgeClass().performMapping(data = sample)
        click.echo(f'Mapping Output: \n\n{sample_mapping}\n')
    except:
        logging.error("Problem occured while reading the internal file.")
        exit()
        
if __name__ == '__main__':
        main()