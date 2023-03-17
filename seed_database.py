import os
import json
import model
import server



if __name__ == "__main__":

        #Delete DB
        os.system("dropdb -U postgres GMBL")

        #Create DB
        os.system("createdb -U postgres GMBL")

        #Connect to DB
        model.connect_to_db(server.app)
        model.db.create_all()