import type { ImageSourcePropType } from 'react-native';

export type Filme = {
  id: string; titulo: string; genero: string; ano: number;
  imagem: ImageSourcePropType; duracao: string; sinopse: string;
};

// Catálogo fictício cadastrado no código. As imagens são locais e autorais.
export const filmes: Filme[] = [
  { id: 'orbita', titulo: 'Além da Órbita', genero: 'Ficção científica', ano: 2024,
    imagem: require('../assets/images/filmes/orbita.png'), duracao: '2h 08min',
    sinopse: 'Uma astronauta recebe um sinal vindo de um planeta esquecido. Ao atravessar os limites conhecidos do espaço, ela descobre que a maior distância a vencer é aquela que a separa de casa.' },
  { id: 'cidade', titulo: 'Última Luz', genero: 'Suspense', ano: 2023,
    imagem: require('../assets/images/filmes/cidade.png'), duracao: '1h 46min',
    sinopse: 'Quando as luzes de uma cidade se apagam, uma fotógrafa encontra uma única janela iluminada. A busca por seu morador revela um mistério que ninguém queria trazer à luz.' },
  { id: 'mar', titulo: 'Mar de Memórias', genero: 'Drama', ano: 2022,
    imagem: require('../assets/images/filmes/mar.png'), duracao: '1h 52min',
    sinopse: 'De volta à vila onde cresceu, um músico reencontra cartas guardadas por sua avó. Entre lembranças e encontros à beira-mar, ele aprende a dar um novo significado ao passado.' },
  { id: 'floresta', titulo: 'O Vale Secreto', genero: 'Aventura', ano: 2025,
    imagem: require('../assets/images/filmes/floresta.png'), duracao: '1h 58min',
    sinopse: 'Dois irmãos seguem um mapa antigo até um vale escondido. Para proteger o lugar, precisam enfrentar uma jornada que transforma a rivalidade em uma inesperada parceria.' },
  { id: 'encontro', titulo: 'Um Café em Paris', genero: 'Romance', ano: 2024,
    imagem: require('../assets/images/filmes/encontro.png'), duracao: '1h 38min',
    sinopse: 'Uma ilustradora e um cozinheiro dividem por acaso a última mesa de um café. Uma conversa muda os planos dos dois e dá início a uma história sobre encontros e recomeços.' },
  { id: 'viagem', titulo: 'Próxima Parada', genero: 'Comédia', ano: 2023,
    imagem: require('../assets/images/filmes/viagem.png'), duracao: '1h 34min',
    sinopse: 'Três amigos pegam o ônibus errado na viagem de férias. Sem roteiro e com pouca bagagem, descobrem que os melhores destinos nem sempre aparecem no planejamento.' },
];
