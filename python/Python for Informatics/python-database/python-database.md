

## Data Models and Relational SQL

### Designing a Data Model
### Representing a Data Model in Tables
### Inserting Relational Data

* Three Kinds of Keys
	* Primary key - generally an integer auto-increment field
	* Logical key - What the outside world uses for lookup
	* Foreign Key - generally an integer key pointing to a row in another table
	
### Reconstructing data with JOIN
	
* join
	* The `JOIN`	operation `links across several tables` as part of a select operation
	* You must tell the `JOIN` `how to use the keys` that make the connection between the tables using an `ON clause`.
	* `SELECT Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id`
		* `Album.title, Artist.name` : What we want to see
		* `from Album join Artist` : The table that hold the data
		* `Album.artist_id = Artist.id` : How the tables are linked

* Additional SQL Topics
	* `Indexes` improve access performance for things like string fields
	* `Constraints` on data - (cannot be NULL, etc..)
	* `Transactions` - allow SQL operations to be grouped and done as a unit
	* `See SI664` - Database Design ( All Semesters)
	
		
		
### Multi-Table Relational SQL





### Many-to-Many Relationships in SQL
> How to model situations like students enrolling in courses :
    * each course has many students
    * each student is enrolled in many courses
    
    




### Databases and Visualization
> In this section, we put it all together, retrieve and process some data and then use the Google Maps API to visualize our data.







