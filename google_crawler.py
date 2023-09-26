import pickle
from multiprocessing import Pool as ProcessPool

from Spider import Spider

def main():
    ### The start page's URL
    start_url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C44&as_ylo=2019&q=%22computer+Networks%22%22bandwidth%22%22intranet%22%22TCP%22%22protocol%22&btnG='

    #p_key = ['regression', 'supervise', 'unsupervised', 'speech',
    #         'vision', 'noise recognition', 'cost',
    #         'sound', 'nlp' , 'python']
    #n_key = ['imagery', 'visual', 'segmentation', 'reflect', 'quantum',
    #         'photon']

    p_key = ['computer Networks', 'bandwidth', 'intranet', 'TCP',
             'Protocol', 'Since 2019']
    n_key = ['patents', 'voice', 'persian', 'farsi', 'signal']


    ### Google Scholar Crawler, Class Spider
    myCrawler = Spider(start_url, p_key, n_key, page=80)

    results = myCrawler.crawl()

    with open('result.pickle', 'wb') as f:
        pickle.dump(results, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()
