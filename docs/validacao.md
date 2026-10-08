# Validação do CineApp

Verificação realizada em 05/10/2026.

## Verificações aprovadas

- `npx tsc --noEmit`: sem erros de TypeScript.
- `npm run lint`: sem erros ou avisos de lint.
- `npx expo export --platform web`: exportação das quatro telas concluída.
- Teste de interação no Chrome, com janela de 390 x 844: início, catálogo, seis filmes e imagens locais.
- Favoritar e desfavoritar: alteração de texto, estrela e aparência, sem modificar os outros filmes.
- Detalhes de cada um dos seis filmes: título e status corretos.
- Retorno de Detalhes e Sobre: favorito preservado no catálogo.
- Retorno ao início e novo acesso ao catálogo: favoritos reiniciados, conforme o ciclo de vida do estado local.
- `useEffect`: mensagem de carregamento observada no console.
- Identificador inexistente: mensagem de filme não encontrado e retorno ao catálogo.
- Sem erros JavaScript ou mensagens de erro no console durante o teste.
- Sem transbordamento horizontal em 390 x 844 e 1280 x 900.
- Capturas de início, catálogo, favoritos, detalhes, sinopse e Sobre revisadas visualmente.

As verificações de interface foram realizadas na versão web. Não foi realizada execução em aparelho Android ou iOS.

## Capturas

- `capturas/01-inicio.png`
- `capturas/02-catalogo.png`
- `capturas/02b-catalogo-final.png`
- `capturas/03-favorito.png`
- `capturas/04-detalhes.png`
- `capturas/04b-detalhes-sinopse.png`
- `capturas/05-sobre.png`

## Itens pessoais para entrega

- Preencher nome completo e RA no README.
- Gravar o vídeo explicativo de até um minuto conforme o enunciado; roteiro de apoio em `roteiro-video.md`.
