import { router } from 'expo-router';
import { Image, ScrollView, StyleSheet, Text, View } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import Botao from '../components/Botao';
import Cabecalho from '../components/Cabecalho';
import { cores, estilos } from '../styles/tema';

export default function Inicio() {
  return (
    <SafeAreaView style={estilos.tela}>
      <ScrollView contentContainerStyle={[estilos.conteudo, estilos.centro]}>
        <Cabecalho legenda="Seu próximo filme começa aqui" />
        <View style={styles.hero}>
          <Image source={require('../assets/images/filmes/orbita.png')} style={styles.poster} resizeMode="cover" accessibilityLabel="Ilustração de um planeta e suas órbitas" />
          <View style={styles.selo}><Text style={styles.seloTexto}>UMA NOVA HISTÓRIA A CADA PLAY</Text></View>
        </View>
        <View style={styles.chamada}>
          <Text style={estilos.etiqueta}>LUZES. CÂMERA. DESCOBERTA.</Text>
          <Text style={styles.titulo}>Grandes histórias.{ '\n' }Na palma da mão.</Text>
          <Text style={estilos.texto}>Explore nosso catálogo, descubra os detalhes de cada filme e marque as histórias que merecem um lugar nos seus favoritos.</Text>
        </View>
        <Botao titulo="Explorar catálogo →" onPress={() => router.push('/catalogo')} />
        <Text style={estilos.rodape}>6 filmes · Histórias para todos os gostos</Text>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  hero: { height: 240, overflow: 'hidden', borderRadius: 22, backgroundColor: cores.painel },
  poster: { width: '100%', height: '100%' },
  selo: { position: 'absolute', bottom: 16, left: 16, right: 16, backgroundColor: '#101017E6', borderRadius: 8, padding: 12 },
  seloTexto: { color: cores.dourado, fontSize: 10, letterSpacing: 2, textAlign: 'center', fontWeight: '700' },
  chamada: { gap: 14 },
  titulo: { color: cores.texto, fontSize: 37, lineHeight: 44, fontWeight: '800' },
});
