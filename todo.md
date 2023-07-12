Test the initialization of the BaseModel instance:

Check if the id attribute is assigned correctly.
Verify that the created_at and updated_at attributes are initialized properly.
Test the save() method:

Verify that calling save() updates the updated_at attribute.
Check if the save() method updates the updated_at attribute when called multiple times.
Test the to_dict() method:

Verify that the returned dictionary contains the expected key-value pairs.
Check if the to_dict() method converts datetime objects to ISO 8601 formatted strings.
Test the from_dict() class method:

Verify that calling from_dict() creates a new BaseModel instance with the correct attributes.
Check if the attributes are set correctly when passing a dictionary with missing or extra keys.
Test the __str__() method:

Verify that calling __str__() returns a string representation of the BaseModel instance.
