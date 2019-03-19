import csv

input = "C:\\Users\olivi\\Documents\\GitHub\\physics_projects2\\6e\\expose\\expose_6.csv"
input2 = "expose_6.csv"
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
            print("\t\\vspace*{1.5cm}", file=tex_file)
            
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
            
            
            print("\n\t\\vspace*{1cm}", file=tex_file)
            comm = "\t" + line[14].replace("é", "\\'e").replace("è", "\\`e").replace("à", "\\`a").replace("ê", "\^e")
            
            if comm != "" :
                print(comm, file=tex_file)
            
            print("\t\\newpage", file=tex_file)