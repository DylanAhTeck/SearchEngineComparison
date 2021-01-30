import json

def parse_json_file(input_file): 
    with open(input_file) as json_file:
        data = json.load(json_file)
        return data

def read_queries(input_file):
    queries = []
    f = open(input_file, "r")
    for query in f:
        queries.append(query)
    return queries

def process_query(query, google_links, personal_links):
    sum_d_squared = 0
    overlaps = 0

    for idx, google_link in enumerate(google_links):
        if google_link in personal_links:
            overlaps += 1
            personal_idx = personal_links.index(google_link)
            d_squared = (idx - personal_idx) ** 2
            sum_d_squared += d_squared


google_res = parse_json_file('Google_Result3.json')
queries = read_queries('100QueriesSet3.txt')

#for query in queries:
