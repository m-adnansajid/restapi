import json
import os
import uvicorn
from fastapi import FastAPI

from restapi.python.hotelService.config.definitions import ROOT_DIR

app = FastAPI()

#This method is returning the default json data.
@app.get("/")
def index():
    return jsonData

#This method will return the list of all hotels.
@app.get("/hotels")
async def hotels():
    response = []
    for destination in jsonData:
        for key, value in destination.items():
            for hotel in value:
                result = {'name': hotel['name'], 'stars': hotel['stars'], 'destination': key}
                response.append(result)
    return response

#This method returns the filtered list of hotels based on the 'stars'.
@app.get("/hotels/")
async def filterHotels(stars:int):
    response = []
    for destination in jsonData:
        for key, value in destination.items():
            for hotel in value:
                if stars == hotel['stars']:
                    result = {'name': hotel['name'], 'stars': hotel['stars'], 'destination': key}
                    response.append(result)
                else:
                    response #returns an empty list for any int value outside the request filtering criteria.
    return response

#This method tries to fetch the json file in a given location
def loadjson(loc):
    try:
       with open(loc, 'r', encoding = 'utf-8') as file:
        # perform file operations
        data = json.load(file)
        return data
    except IOError as error:
        print ("I/O error({0}): {1}".format(error.errno, error.strerror))
    finally:
       file.close()


#Json data file location relative to the os path.
jsonData = loadjson(os.path.join(ROOT_DIR, 'data', 'data.json'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #uvicorn Config and Server instances.
    config = uvicorn.Config("main:app", port=3000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()






