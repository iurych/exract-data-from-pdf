import pdfplumber

# pdf_path = ".venv/lista.pdf"  # Confirme se o caminho está correto

def get_first_last_el(text):
    group = text.split()
    first = group[0]
    last = group[-1]
    
    return [first, last] 
    
def extract_text_with_plumber(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        result_list = []  # Inicializa a lista para armazenar os resultados
        for page in pdf.pages:  # Itera sobre todas as páginas do PDF
            text = page.extract_text()
            formated_text = text.split('\n')[11:-2]
            for t in formated_text:
                to_append = get_first_last_el(t)
                result_list.extend(to_append)  # Adiciona os elementos à lista principal
        return result_list

#         # fazer loop np textv - ok
#         # pegar o primeiro elemento e o último - ok
#         # armazenar em uma list [] - ok
#         # fazer para toda lista principal
#         # usar pandas pra ciar o data frame
#         # Ordenar por "Total de Pontos"
#         # Exportar para XML  
#         # test_function = get_first_last_el(text)
        
#     return text

# # Executar o teste
# pdf_text = extract_text_with_plumber(pdf_path)
# print(len(pdf_text))

nota = 63.45

score = 70

print(score > nota)