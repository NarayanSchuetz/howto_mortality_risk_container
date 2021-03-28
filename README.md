## howto_mortality_risk_container

### 1. Load Docker Image:
Let `nsappslim.tar` be the docker image.
To load the local image from the file run the following command:

    docker load --input nsappslim.tar
    
### 2. Run the Docker Image:
To run the docker image, first check whether it loaded correctly by issueing the following command: `docker images`.
This should show a listing of all locally available docker images.
The entry `flask-app-slim` (or something similar, at the end of the listing), should correspond the the previously loaded image.
To run the image, execute the following command:

    docker run --name mortality -it -p 8123:1234 7398fefe04a7
   
NOTE: `8123` corresponds to the IP that will be forwarded on your host machine, so make sure it is open and not already bound by some other service (it shouldn't), otherwise pick another port.

### 3. Install Jupyter Notebook inside the running container:
First you have to enter the local shell of the running container, to do this execute: 

    docker exec -it mortality bash
    
Now that you entered the shell, install jupyter notebook inside the container:

    pip install jupyter notebook
    
### 4. Start a Notebook inside the container:
Now that `jupyter notebook` is installed, run the following command inside the container's shell:

    jupyter notebook --allow-root --port=1234 --ip=0.0.0.0
    
As a result, a local jupyter notebook instance should be spun up, look for the message in the terminal, something along the lines of 

    Or copy and paste one of these URLs:
        http://5bbd63b07445:1234/?token=94171b2fd82815a370f137f5b47af7bfdaadfab107d3033b

At this point, copy the URL (the one you got, not the one here) and enter it in an open browser window on your host machine.
Then change the port the `1234` part into the port you forward to, if you didn't manually change, this should be `8123`. It should now look something like this:

    http://5bbd63b07445:8123/?token=94171b2fd82815a370f137f5b47af7bfdaadfab107d3033b
    
By pasting the new URL into the browser and pressing enter, a `jupyter notebook` window should open, where you can now start a new notebook inside the container and also upload files to it (alternatively you could also mount a local directory on your host machine, to directly access the data - google should help here).

### 5. Do whatever you want in the local environment:
An example of how to use the models inside the container is given in [`example.py`](https://github.com/NarayanSchuetz/howto_mortality_risk_container/blob/main/example.py)
