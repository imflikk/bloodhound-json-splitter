# bloodhound-json-splitter
Python script to split very large JSON files generated by SharpHound into smaller files.

In my experience, running SharpHound in very large Active Directory environments can generate very large corresponding JSON files (1gb+) with the domain information.  The Bloodhound GUI will often run out of available memory, regardless of the resources available, and error out when trying to parse and upload these files.

This script currently takes three arguments: the input file, the number of JSON objects to include in each output file, and the Bloodhound data type.  It will parse through the input file and extract the provided number of objects, build a new collection of JSON objects matching the format Bloodhound expects, and write the information to a new file in the same directory in the format of output-1.json, output-2.json, etc.

Currently accepts the following data types, though I have only tested with users.

- users
- groups
- ous
- computers
- gpos
- domains

![image](https://user-images.githubusercontent.com/58894272/113531922-ed9f7380-957e-11eb-97c3-4849e58b12da.png)
