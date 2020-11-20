#environment: conda minimal_ds
#thanks: PyAltmetric, laurenrevere, wearp

from pyaltmetricmod import Altmetric, Citation, HTTPException, AltmetricException 
import csv 
import time 

a = Altmetric ()

with open('dois.list', 'r') as infile:
    with open('Free_API.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        
        for item in infile:
            time.sleep(1.01)
            item = item.rstrip()
            article = a.doi(item)
            if article:
                citation = Citation(article)
                api_data = citation.get_fields('doi', 'journal', 'cited_by_posts_count', 'cited_by_tweeters_count', 'cited_by_msm_count', 'cited_by_videos_count', 
                'cited_by_fbwalls_count', 'cited_by_gplus_count', 'cited_by_rdts_count', 'cited_by_feeds_count', 'score', 'url')
            else:
                api_data = [item, 'none']
            writer.writerow(api_data)






