import re
import pandas as pd
import pdfplumber

pdf_path = ".venv/lista.pdf"
xml_output_path = ".venv/ranking_candidatos.xml"

def formatar_nota(nota):
    parte_inteira = int(nota)
    
    # Se a parte inteira tiver apenas um dígito, ajustamos a nota
    if parte_inteira < 10:
        nota = float(f"{parte_inteira}0{str(nota)[len(str(parte_inteira)):]}")
    
    return nota


def get_first_last_el(text):
    group = text.split()
    first = group[0]
    last = group[-1]
        
    return [first, last]
    

def extract_text_with_plumber(pdf_path):
    result_list = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            formated_text = page_text.split('\n')[11:-2]
            for t in formated_text:
                to_append = get_first_last_el(t)
                if len(to_append) == 2:  # Apenas adiciona se houver exatamente dois elementos
                    result_list.append(to_append)  
    return result_list

pdf_text = extract_text_with_plumber(pdf_path)
print(len(pdf_text))

# Filtrando a lista para remover as entradas com 'faltou' no segundo elemento
# pdf_text_filtrado = [item for item in pdf_text if len(item) == 2 and item.lower() != 'faltou']


# # Criar DataFrame do Pandas
df = pd.DataFrame(pdf_text, columns=["Inscrição", "Pontos"])

# # Ordenar por "Pontos" (ranking)
df = df.sort_values(by="Pontos", ascending=False)

# Resetar índice após ordenação para refletir a posição no ranking
df = df.reset_index(drop=True)

df.insert(0, "Posição", df.index + 1)

# Função para obeter a posição no ranking com base em uma inscrição
def obter_posicao(inscricao):
    resultado = df[df["Inscrição"] == inscricao]
    if not resultado.empty:
        return resultado["Posição"].values[0]
    return None  # Retorna None se a inscrição não for encontrada
inscricao_desejada = "9991009480"  # Substitua pelo número da inscrição desejada
posicao = obter_posicao(inscricao_desejada)

if posicao:
    print(f"A inscrição {inscricao_desejada} está na posição {posicao}.")
else:
    print("Inscrição não encontrada.")

# # Exportar para XML
# df.to_xml(xml_output_path, index=False, root_name="Ranking", row_name="Candidato")

# print(f"Arquivo XML salvo em: {xml_output_path}")