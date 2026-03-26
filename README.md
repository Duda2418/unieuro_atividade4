# unieuro-concorrente-202601-atividade4
Aplicador de filtro em imagem de forma paralela.


## Passo-a-passo

A atividade será realizada em grupo de 4 alunos.

1) Apenas 1 aluno deverá realizar o fork desse repositório para poder trabalhar na solução.
2) Adicionar os demais alunos do grupo como membro do repositório.
3) Execute o programa python de geração da imagem apenas uma vez. Ele vai criar uma imagem de 16gb.
```
python .\geradorimagem.py
```
4) Executar o programa que converte a imagem gerada em uma nova imagem em escala em cinza na versão serial.
```
python .\conversoremescalacinza.py
```
✅ Processamento concluído!  
⏱️ Tempo total: 171.11 segundos

5) Se reunam e decidam uma forma de paralelizar a execução dessa atividade sem alterar o programa original de conversão (conversoremescalacinza.py). Vocês devem tratar esse programa como uma caixa-preta que não pode ser modificada. A solução de paralelização deve ser externa ao programa.

6) Implementem a solução planejada e execute o experimento para 2, 4, 8 e 12 threads.

7) Crie o relatório no modelo que estámos trabalhando nas atividades e preenchar o questionário no AVA.
