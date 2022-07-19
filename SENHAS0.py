 /\\\\\\\\\\\\\\\\\\\/////////////////////COGIGO AINDA NÃO ESTÁ PRONTO/////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
print('-=-'*10)
print(f'{"-= BEM VINDO =-":^30}')
print('-=-'*10)
op = 1
c = 0
nc=''
sc=''
tt = 0
n=''
s=''
while op != 3:
  /\\\\\\\\\\\\\\\\\\\/////////////////////COGIGO AINDA NÃO ESTÁ PRONTO/////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 
    op= int(input('''\n[1]-DESEJA EFETUAR LOGIN\n[2]-CADASTRO\n[3]-SAIR
DIGITE A OPÇÃO SELECIONADA: '''))
 /\\\\\\\\\\\\\\\\\\\/////////////////////COGIGO AINDA NÃO ESTÁ PRONTO/////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    print('')
   /\\\\\\\\\\\\\\\\\\\/////////////////////COGIGO AINDA NÃO ESTÁ PRONTO/////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\  
    if op == 1:
        n = input('DIGITE SEU NOME: ')
        s = input('DIGITE A SUA SENHA: ')
        if n == nc and s == sc:
           print('ACESSO PERMITIDO!!')
    elif op == 2:
            nc = input('DIGITE SEU NOME: ').strip
            sc = input('DIGITE SUA SENHA: ').strip
            print('CADASTRO REALIZADO COM SUCESSO!!!')
    elif op == 3:
            print('OBRIGADO FIM DA EXECUÇÃO!')

 /\\\\\\\\\\\\\\\\\\\/////////////////////COGIGO AINDA NÃO ESTÁ PRONTO/////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\