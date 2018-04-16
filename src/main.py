from scraper import MovieRatingScraper

output_file = "dataset.csv"

scraper = MovieRatingScraper();
scraper.scrape();
scraper.data2csv(output_file);