# CineApp - ATV1 de PDM

- **Aluno:** Rogerio Pupo Toledo 
- **Aplicativo:** CineApp.
- **Versão:** 1.0.0.
- **Disciplina:** Programação para Dispositivos Móveis I - Fatec Registro.
- **Professor:** Maylon H. Oliveira.

Aplicação React Native com Expo para explorar um catálogo de seis filmes fictícios, visualizar suas informações e marcar favoritos. Criada a partir da estrutura do TaskFlow fornecida, conforme o enunciado da ATV1.

## Executar

Pré-requisitos: Node.js compatível com Expo SDK 54 (20.19 ou superior), npm e um dispositivo ou navegador para testar.

```bash
npm install
npx expo start
```

Leia o QR Code com uma versão do Expo Go compatível com SDK 54, na mesma rede do computador. No terminal, pressione `a` para abrir um emulador Android configurado ou `w` para executar no navegador. Também é possível usar `npm run web`.

## Funcionalidades

1. Início: logotipo, nome, descrição e botão para explorar o catálogo.
2. Catálogo: seis filmes com título, cartaz local, gênero, ano e botão de favorito.
3. Favoritos: `☆ Favoritar` alterna para `★ Favorito`, com mudança de cor e estrela.
4. Detalhes: cartaz, título, gênero, ano, duração, sinopse e status de favorito ao selecionar o filme.
5. Sobre: finalidade, versão, instituição e identificação da disciplina.
6. Navegação: início → catálogo → detalhes/sobre → voltar.

Os favoritos permanecem ao abrir Detalhes ou Sobre e voltar usando os botões do aplicativo, pois o catálogo continua montado na pilha. São estados em memória: ao sair do catálogo para o início, recarregar ou fechar a aplicação, voltam ao valor inicial. O enunciado não exige armazenamento permanente. A alteração de favoritos é realizada no catálogo.

Os filmes, as sinopses e os cartazes são fictícios e autorais, para demonstração acadêmica. Todas as imagens são locais; não há API, login ou dependência de internet para carregar o catálogo.

## Organização

```text
app/
  _layout.tsx       Pilha de navegação
  index.tsx         Início
  catalogo.tsx      Catálogo e useEffect
  detalhes.tsx      Informações do filme selecionado
  sobre.tsx         Informações do aplicativo
components/
  FilmeCard.tsx     Card reutilizável e useState de favorito
  Botao.tsx         Pressable com texto, ação e feedback visual
  Cabecalho.tsx     Logotipo e legenda recebida por Props
data/filmes.ts      Seis filmes cadastrados diretamente no código
styles/tema.ts      Cores e estilos compartilhados
assets/images/     Logotipo, ícone e cartazes locais
docs/capturas/     Capturas das funcionalidades
docs/roteiro-video.md  Apoio para o vídeo explicativo
```

Os componentes e hooks remanescentes do template Expo não são usados nas telas do CineApp.

## Conceitos aplicados

| Conteúdo | Aplicação |
| --- | --- |
| View, Text, Image, SafeAreaView e ScrollView | Organização, textos, imagens, área segura e rolagem das telas |
| StyleSheet e Flexbox | Tema, cabeçalhos em linha, cards com flexWrap e tamanhos adaptáveis |
| Pressable e eventos | Todos os botões e seleção de filmes; opacidade e escala durante o toque |
| useState | Booleano independente de favorito em cada FilmeCard |
| useEffect | Registro de carregamento após montar o catálogo |
| Expo Router | Stack, rotas por arquivo, push e back |
| Componentes e Props | FilmeCard, Botao e Cabecalho reutilizados |

`FilmeCard` recebe `titulo`, `genero`, `ano`, `imagem` e `onDetalhes`. A função `onDetalhes` envia o estado atual do favorito à tela de detalhes por parâmetros de rota. As Props informam o card; o estado guarda a informação que muda durante a interação.

O `useEffect` em `app/catalogo.tsx` registra `Catálogo carregado: 6 filmes disponíveis.` no console após a montagem. O array vazio `[]` evita executar esse registro a cada atualização de favorito. Isso separa o registro no console da renderização visual, conforme a situação sugerida na atividade.

## Verificação

```bash
npx tsc --noEmit
npm run lint
npx expo export --platform web
```

Para conferir manualmente: entre no catálogo, percorra os seis filmes, favorite e desfavorite um deles, abra seus detalhes e volte. Abra Sobre e volte ao catálogo. Os demais filmes não devem mudar quando um único favorito for alterado.

TypeScript, lint, exportação web e testes de interação no navegador foram aprovados. O registro detalhado está em [docs/validacao.md](docs/validacao.md).
