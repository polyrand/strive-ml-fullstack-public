import argparse



def download_data(url, folder="data"):
    
    if "data.zip" not in os.listdir():
        r = requests.get(url)

        with open("data.zip", "wb") as f:
            f.write(r.content)
            
        with zipfile.ZipFile("data.zip", "r") as zip_ref:
            zip_ref.extractall(folder)
    
    



def main(args):
    
    
    # ...
    # ..
    
    
    if args.adam:
        optim = optim.Adam(...)
    elif args.sgd:
        optim = optim.SGD(...)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    
    
    # --download-data
    # --train --epochs INT (it should have a default)
    # --optimizer STRING
    # --load-weights STRING
    
    # extra otion
    # load the data URL from an environment variable

# python3 train.py --download-data --train --epochs 3 --optimizer sgd --load-weights my_weigths.pth