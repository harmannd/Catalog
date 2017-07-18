# Catalog: A catalog of categorized items allowing registered users to post, edit, and delete their own items.

This catelog app is a RESTful web app developed using the Python framework Flask. This app features third-party OAuth2 authentication and various HTTP methods to perform CRUD(create, read, update, and delete) operations. The backend is created with SQLAlchemy.

### Usage
* Install VM VirtualBox and Vagrant.
* Download this repository.
* Extract the contents of the zip file.
* Open git bash and navigate to location of this folder.
* Type "vagrant up" in git bash to create the virtual environment to run the app.
* Type "vagrant ssh" in git bash to login into the virtual environment.
* Type "cd /vagrant" in the prompt to open the shared folder.
* Type "python database_setup.py" to create the database for the app.
* Type "python project.py" to start the app on localhost:5000 in your browser.

### Files
* /static
  * bootstrap.min.css - Bootstrap css.
  * styles.css - Custom css.
* /templates
  * Various html templates for the app.
* catalogwithusers.db - Database file for the app.
* database_setup.py - Creates the database for the app.
* fill_database.py - Optional file to fill the database.
* project.py - Main project.
* Vagrantfile - File that tells the virtual environment what to install.

2017 Derek Harmann
