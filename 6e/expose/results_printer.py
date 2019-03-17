import csv

input = "expose_6.csv"
output = "details.tex"

with open(input, 'r') as csv_file :
    csv_reader = csv.reader(csv_file, delimiter=";")
    
    headers = next(csv_reader)
    
    with open(output, 'w') as tex_file :
        
        for line in csv_reader :
    
            print("\t\\LARGE{\\texttt{Expos\\'e $6^e$ - L'espace}}", file = tex_file)
            print("\t\\vspace*{1cm}", file=tex_file)
            
            name = "\n\t\\textbf{" + line[2] + " " +  line[1] + "\\ ("+line[0]  +")}\n"
            print (name, file=tex_file)
            print("\t\\vspace*{2cm}", file=tex_file)
            
            print("\t\\begin{tabular}{|l|c|}", file=tex_file)
            
            print("\t\t\\hline", file=tex_file)
            
        
            
            for i in range(3,13):
                tab_line = "\t\t" + headers[i] + " & "  + line[i] + "/2 \\\\"
                print(tab_line, file=tex_file)
                print("\t\t\\hline", file=tex_file)
                
                
            total_line = "\t\t\\textbf{TOTAL}  & \\textbf{"  + line[13] + "/20} \\\\"
            print(total_line, file=tex_file)
            print("\t\t\\hline", file=tex_file)
            print("\t\\end{tabular}", file=tex_file)
            
            print("\t\\newline", file=tex_file)