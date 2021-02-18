import arxiv
import csv
import datetime

csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = ("arxiv_paper" + csv_date + ".csv")
f = open(csv_file_name, "w", encoding="cp932", errors="ignore")

QUERY = "cat:'cs.AI'"
result_list = arxiv.query(query = QUERY,max_results=5,sort_by='submittedDate')

writer = csv.writer(f, lineterminator="\n") 
csv_header = ["著者","タイトル","要約","URL"]
writer.writerow(csv_header)

for res in result_list:
    csvlist = []
    csvlist.append( res.author)
    csvlist.append( res.title)
    csvlist.append( res.summary)
    csvlist.append( res.pdf_url)
    writer.writerow(csvlist)