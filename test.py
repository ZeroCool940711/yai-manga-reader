import pickle, os, requests, logging, json
from mlscraper.html import Page
from mlscraper.samples import Sample, TrainingSet
from mlscraper.training import train_scraper

# fetch the page to train
extension = 'reddit'

with open(f'extensions/{extension}/config.json', encoding='utf-8') as f:
    config = json.load(f)

url = config['url']
resp = requests.get(url)
assert resp.status_code == 200

training_set = TrainingSet()

def create_sample(resp, sample_data):
    page = Page(resp.content)
    sample = Sample(page, sample_data)
    training_set.add_sample(sample)
    #return sample

def save_model(scraper, filename):
    file = open(filename, 'wb')
    pickle.dump(scraper, file)
    file.close()

def load_model(filename):
    file = open(filename, 'rb')
    scraper = pickle.load(file)
    file.close()
    return scraper
    
for sample in config['samples']:
    create_sample(resp, sample)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    # train the scraper with the created training set
    scraper = train_scraper(training_set, complexity=100)

    print('Training finished. Saving model')
    # save the trained models
    save_model(scraper, f'extensions/{extension}/{extension}.pkl')

    # load the trained model
    scraper = load_model(f'extensions/{extension}/{extension}.pkl')

    print('Scraping a page with the previously trained model')
    # scrape another page
    resp = requests.get('https://www.reddit.com/r/ImaginaryArchers/')
    result = scraper.get(Page(resp.content))

    print(result)# returns {'name': 'J.K. Rowling', 'born': 'July 31, 1965'}