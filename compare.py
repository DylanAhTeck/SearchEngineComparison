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
    #For single overlap special case
    same_rank = False
    for idx, google_link in enumerate(google_links):
        if google_link in personal_links:
            overlaps += 1
            personal_idx = personal_links.index(google_link)
            same_rank = idx == personal_idx
            d_squared = (idx - personal_idx) ** 2
            sum_d_squared += d_squared

    if overlaps == 0: return 0, 0, 0
    elif overlaps == 1:
        if same_rank: return 1, 10, 1
        else: return 1,10,0

    percent_overlap = overlaps/10 * 100
    spearman_coefficient = 1 - ((6 * sum_d_squared)/(overlaps * ((overlaps ** 2)-1)))

    return overlaps, percent_overlap, spearman_coefficient

def write_output(results):
    total_overlaps = 0
    total_percent = 0
    total_spearman_coeffficient = 0
    n = len(results)
    with open('output.csv', 'w+') as output:
        output.write("Queries, Number of Overlapping Results, Percent Overlap, Spearman Coefficient \n")
        for result in results:
            total_overlaps += result[1]
            total_percent += result[2]
            total_spearman_coeffficient += result[3]
            output.write(f'Query {result[0]}, {result[1]}, {result[2]}, {result[3]} \n')
        output.write(f"Averages, {total_overlaps/n}, {total_percent/n}, {total_spearman_coeffficient/n}")
        output.close()
 
#google_links = parse_json_file('Google_Result3.json')
#personal_links = parse_json_file('output.json')
#queries = read_queries('100QueriesSet3.txt')

google_links = parse_json_file('Google_Result3.json')
personal_links = parse_json_file('fast_output.json')
queries = read_queries('100QueriesSet3.txt')

results = []
#print(google_links['What are two properties or characteristics of cotton fibers'])
for idx, query in enumerate(queries):
    query = query.strip()
    overlaps, percent_overlap, spearman_coefficient = process_query(query, google_links[query], personal_links[query])
    results.append([idx+1, overlaps, percent_overlap, spearman_coefficient])

write_output(results)

#for query in queries:
