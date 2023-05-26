# :toolbox: Tecnologias usadas:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# :open_book: Objetivo do projeto inventory report

<details>
  <summary>:speech_balloon: Objetivos</summary>

  ```
  1. Desenvolver um gerador de relatórios que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.
  2. Esses dados de estoque poderão ser obtidos de diversas fontes:
    2.1 Através da importação de um arquivo CSV,JSON ou XML
  3. O relatório final possui duas versões: simples e completa.
  4. Habilidades desenvolvidas:
    4.1 Aplicar conceitos de Orientação a Objetos em Python;
    4.2 Aplicar padrões de projeto;
    4.3 Leitura de arquivos (XML, CSV, JSON).
  ```
</details>

<details>
  <summary>:speech_balloon: Exemplo de funcionamento</summary>
 
![Captura de tela de 2023-05-26 12-00-30](https://github.com/Lucas-Israel/project-inventory-report/assets/104790267/ff05dace-398d-4404-b626-d5a85e5635f1)
![Captura de tela de 2023-05-26 13-25-21](https://github.com/Lucas-Israel/project-inventory-report/assets/104790267/8ff3bb1b-e5e9-4199-a342-cd6a050c6709)

</details>

# :heavy_exclamation_mark: Arquivos desenvolvidos nesse projeto:

<details>
  <summary>:speech_balloon: Arquivos</summary>

  ```
  inventory_report/
    main.py

    importer/
        csv_importer.py
        importer.py
        son_importer.py
        xml_importer.py
        
    inventory/
        inventory.py
        inventory_iterator.py
        inventory_refactor.py
    
    reports/
        complete_report.py
        simple_report.py
    
    
  tests/
    product/
        test_product.py
    
    product_report/
        test_product_report.py
    
    report_decorator/
        test_report_decorator.py
  ```
</details

#### :warning: todos os outros arquivos foram desenvolvidos pela [Trybe](https://www.betrybe.com).

# :thinking: Como checar o projeto

```
git clone git@github.com:Lucas-Israel/project-inventory-report.git
python3 -m venv .venv && source .venv/bin/activate
python3 -m pip install -r dev-requirements.txt
inventory_report <caminho_do_arquivo_input> <tipo_de_relatório>
exemplo: 
    inventory_report inventory_report/data/inventory.json completo
    inventory_report inventory_report/data/inventory.csv simples
```

# :calendar: Datas para desenvolvimento

```
início: 04/04/23 às 14h09
término: 05/04/23 às 17h17
prazo: 7 dias
dias específicos para o desenvolvimento do projéto: 2
```

# :trophy: Percentual de conclusão do projeto

![Captura de tela de 2023-05-26 13-33-51](https://github.com/Lucas-Israel/project-inventory-report/assets/104790267/97a32a66-8d82-4884-b588-02b809e52b5d)

<details>
  <summary>:warning: Metodo de avaliação da Trybe</summary>
  
##### A escola de programação [Trybe](https://www.betrybe.com) utiliza um sistema de avaliação baseado na conclusão de requisitos em cada projeto, considerando a porcentagem de conclusão, com um mínimo de 80% dos requisitos obrigatórios, em um prazo regular de no máximo 7 dias, tendo dias específicos para o desenvolvimento do projeto que variam de acordo com a complexidade dele.

##### Não alcançando esse patamar mímino, o aluno entra em recuperação, tendo que entregar 90% dos requisitos obrigatórios mais os bonús, em outros 7 dias, caso o aluno falhe novamente ele é mudado de turma para refazer o conteúdo e projeto, caso falhe após mudar de turma, no mesmo conteúdo/projeto, o aluno é removido do curso.
  
</details>
