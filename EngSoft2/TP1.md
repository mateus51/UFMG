# Boostnote

###  Descrição do sistema, incluindo principais features, objetivo, linguagem de programação.
	https://boostnote.io/
https://github.com/BoostIO/Boostnote

Autores:

 - Luiz Otávio Caldonazo
 - Mateus Lopes
 - Paulo Vandeveld
<p align="center">
  <img src="https://image.prntscr.com/image/d984d5c0cee047aaa1cf72a2d77f2860.png"/>
</p>

O **Boostnote** é uma aplicativo open source de criação de notas com foco em desenvolvedores de software mantido sobre a licença GNU GPL v3 e entregue de forma gratuita para os usuários interessados. 

Seu objetivo principal é permitir que profissionais da área de TI escrevam notas rapidamente para auxiliar em sua produtividade. O Boostnote se diferencia de outros aplicativos de notas pois permite que seja escrito snippets de código em suas notas, algo rotineiro para programadores, pois tem a capacidade de reconhecimento de mais de 100 linguagens de programação, além de HTML e Latex. Com a funcionalidade de *syntax highlight*, é muito mais simples ler e entender códigos. 

O aplicativo consegue identificar a sintaxe de diversas linguagens e salvar as notas com identação e coloração na sintaxe, facilitando a leitura de códigos que o usuário queira anotar rapidamente. Além disso, é possível criar várias subnotas, para melhorar a organização das anotações.

O Boostnote é desenvolvido com programadores em mente, e por isso conta com features essenciais no workflow de um programador moderno, como: 

 - suporte a Markdown, uma linguagem simples de marcação que converte qualquer texto em XHTML válido, facilitando a criação de documentos no formato utilizado pelo Github;

 - suporte ao LateX, o conjunto de macros para o software de diagramação de textos TeX, muito utilizado na comunidade científica da computação, pois fornece um conjunto de comandos de alto nível; 
 - não é necessário conexão com a Internet: o usuário pode criar notas a qualquer momento em seu laptop;
 
 - Finder Pop Up (Mac OS X e Linux): é possível procurar notas mesmo que outro software esteja sendo utilizado utilizando a função Spotlight do Mac OS X, que é um sistema amplo de busca no desktop.


----------

O Boostnote é desenvolvido primariamente em Javascript, uma das principais linguagens de programação interpretada. Com o crescente uso de Javascript no mercado e a constante otimização de códigos, como por exemplo a engine V8 desenvolvida pela equipe do Google Chrome, que é um interpretador da linguagem Javascript para o browser e acelera o desempenho da aplicação garantem que o Boostnote seja leve, eficiente e consuma pouca bateria em laptops. 

Como o Boostnote é open source, aliado à popularidade do Javascript, é possível que os próprios usuários baixem o código fonte, e a modifiquem à seu critério.


## Equipe de desenvolvedores e mantenedores:

 - Kazu Yokomizo: Criador do Boostnote
 - Rokt33r 
 - sota1235   
 - Kohei 
 - TAKATA   
 - asmsuechan  

Gráfico de contribuições para a plataforma **Boostnote** através do GitHub:
<p align="center">
  <img src="https://image.prntscr.com/image/d33e2e1137d449969f0035276bf543e1.png"/>
</p>

## Breve descrição da evolução do sistema: principais releases e novidades de cada uma.

A primeira versão do aplicativo Boostnote foi a versão 0.4.1-beta. Ela foi lançada em 16 de novembro de 2015, nesta versão o aplicativo já era capaz de fazer o conferimento de novas atualizações de forma automática, e tinha também a possibilidade de edição da ordenação e cores para as pastas que estavam disponíveis, além disso havia já uma ferramenta que impossibilitaria o usuário trocar de artigo no momento em que um artigo estava sendo editado. Os ícones de notificação no aparelho foram corrigidos de forma apropriada e além disso também adicionaram a ferramenta de sugestão de tag’s que funciona quando o usuário está editando as suas tags.

Em 21 de novembro de 2015, quando foi lançada a versão 0.4.1-beta.2, foi decidido pela equipe de desenvolvimento da ferramenta Boostnote que o código seria escondido.

Em 13 de dezembro de 2015, o aplicativo foi relançado na versão 0.4.7 e a versão antiga foi considerada obsoleta, além disso o aplicativo para o sistema operacional Windows foi lançado para o público em geral fazerem o download em seus computadores.
Já a versão 0.6.0 foi lançada em 23 de julho de 2016 e contou com uma grande renovação visual, nela foram adicionados novos temas, e durante este tempo foram adicionadas ferramentas como, por exemplo, a não diferenciação de letras minúsculas e maiúsculas na ferramenta de busca do aplicativo (insensitive case), as fontes disponíveis foram alteradas, houve uma melhora no funcionamento com imagens, a introdução da configuração do zoom dentro da aplicação, informações sobre OSS, modificação dos links de contato com a equipe, além disso a aplicação passou a fechar automaticamente quando a janela principal era fechada e houveram também inúmeras correções de bugs e de falhas dentro da aplicação.

A versão 0.7.0 foi lançada três meses depois da versão 0.6.0 em 17 de outubro de 2016 com a principal mudança na alteração do editor, na ocasião o Ace Editor foi substituído pelo Codemirror, um componente Javascript que fornece um editor de código no navegador, além disso a interface de usuário também foi melhorada. Durante o período, também houve a edição de dicas para utilizar as ferramentas da aplicação, a barra lateral foi expandida, melhora na ferramenta de seleção das pastas, adição da barra de rolar infinita, refatoração para o dataApi, além de correções de bugs no dataApi e segfaults na versão para o Ubuntu da aplicação Boostnote.

O número de versões diminui bastante a partir daí, foram apenas 4 versões lançadas entre a  versão 0.7.0 e a versão 0.8.0, que veio com a intenção principal de redefinir o design da aplicação, inclusive foi feita a renovação do logo do programa. A versão 0.8.0 foi lançada em 3 de janeiro de 2017 e antes dela houveram algumas correções de bugs, pequenas melhoras de performance na versão do aplicativo para a plataforma Mac e também no serviço de mensagens de erro do sistema.

A última versão lançada foi a 0.8.9 no dia 29 de abril de 2017 que contou com algumas correções de erros e melhoramentos na experiência do usuário com o sistema.

	

## Principais frameworks, ferramentas e linguagens usadas no desenvolvimento. 

### Principais linguagens de programação utilizadas

| Linguagem de Programação | Porcentagem do código |
|--------------------------|-----------------------|
| Javascript               | 75%                   |
| CSS                      | 23.7%                 |
| HTML                     | 1.3%                  |


	
### Principais frameworks utilizados: 
- [Electron](https://electron.atom.io/)  
- [React + Redux](http://redux.js.org/) 
- [Webpack](https://webpack.github.io/) 
- [CSS Modules](https://github.com/css-modules/css-modules) 



# ** Framework s**

## Electron
*Electron* é um *framework open-source* que permite ao usuário o desenvolvimento de aplicações desktop com GUIs através da utilização de componentes que são originalmente desenvolvidos para aplicações web. Node.js é utilizado para o desenvolvimento backend, enquanto o Chromium é utilizado para o desenvolvimento frontend. 
O Electron permite aos desenvolvedores web conseguir fazer aplicações para desktop sem a necessidade do aprendizado de novas linguagens de programação, e o mais importante: uma vez que suas tecnologias são crossplatform, é possível compilar o mesmo código para gerar arquivos executáveis em plataformas Windows (.exe), Mac OS X (.app) e Linux (./executavel). 
Ao desenvolver para a aplicação Boostnote, basta utilizar a ferramente Electron para compilar o código para a sua plataforma preferida. Como o Boostnote está disponível tanto para Windows, quanto para Mac OS X e Linux, a equipe de desenvolvimento sempre lança versões para os três sistemas operacionais a cada *release*.

---
## React + Redux
React é uma biblioteca Javascript para criação de interfaces de usuário. O React é baseado em componentes: abstrações que fazem o encapsulamento de lógica, estados e dados. Seguindo as boas práticas de programação, é fácil criar interfaces ricas utilizando somente componentes simples. É possível também codificar toda a lógica e as regras de negócio utilizando apenas a linguagem Javascript, e o React fica a cargo da troca de dados entre os componentes, o que facilita o desenvolvimento e a manutenção dos componentes e de todo o sistema.
O React não manipula diretamente o DOM, e sim uma virtualização dele que é chamada de Virtual DOM, é isso que permite que, junto ao eficiente compilador de códigos .jsx, apenas as partes modificadas do código sejam renderizadas ao invés de requerer uma renderização da tela inteira. A partir disso é gerado um código mais eficiente e softwares mais rápidos para os usuários, além de possibilitar uma maior agilidade no desenvolvimento, pois como o código é compilado, mensagens de erros são exibidas em tempo de compilação, isso permite que bugs, que antes poderiam passar despercebidos, agora sejam encontrados e tratados antes mesmo do código entrar em produção.
Para adicionar novas funcionalidades ao Boostnote é muito simples, basta criar novos componentes React no caminho *Boostnote/browser/components*. Em caso de haver alguma nova dependência criada por esse novo componente, o Webpack tem a capacidade de adicionar esse novo módulo ao *bundle* de dependências da aplicação. É recomendado experiência com desenvolvimento em React para adicionar novas funcionalidades ao Boostnote.
Redux é um framework utilizado para facilitar a manipulação de estados de componentes. Apesar de ser usado frequentemente em junção com a ferramenta React, Redux trabalha independente de frameworks e funciona como um "oráculo", pois é capaz de adivinhar qual o estado futuro do componente, além de facilitar a implementação do tratamento dessas mudanças de estado.

*Exemplo simples da utilização do React: componente responsável por renderizar o avatar do usuário*

*/Boostnote/browser/components/ProfileImage.js*

```javascript
import React, { PropTypes } from 'react'
import md5 from 'md5'

export default class ProfileImage extends React.Component {
  render () {
    let className = this.props.className == null ? 'ProfileImage' : 'ProfileImage ' + this.props.className
    let email = this.props.email != null ? this.props.email : ''
    let src = 'http://www.gravatar.com/avatar/' + md5(email.trim().toLowerCase()) + '?s=' + this.props.size

    return (
      <img
        className={className}
        width={this.props.size}
        height={this.props.size}
        src={src} />
    )
  }
}

ProfileImage.propTypes = {
  email: PropTypes.string,
  size: PropTypes.string,
  className: PropTypes.string
}
```

### Webpack
Webpack é um *module bundler* utilizado em aplicações na linguagem Javascript. Essa ferramenta é utilizada a fim de criar um grafo de dependências da aplicação, em que cada nó é considerado um módulo necessário para a execução da aplicação. Assim que é criado o grafo, o Webpack gera *bundles* (usualmente apenas um é gerado) que posteriormente serão então carregados pelo navegador. Isso atua na melhora do desempenho da aplicação, principalmente em navegadores que utilizam HTTP/1.1, pois conseguem reduzir o tempo em que o navegador se mantém ocioso enquanto espera outra requisição fazer o download das dependências.

*Exemplo resumido, demonstrando a utilização do Webpack para configurar as dependências do Boostnote*

*webpack.config.js*

```javascript
const skeleton = require('./webpack-skeleton')
const path = require('path')

var config = Object.assign({}, skeleton, {
  module: {
    loaders: [
      {
        test: /\.js?$/,
        exclude: /node_modules/,
        loader: 'babel?cacheDirectory'
      },
  output: {
    path: path.join(__dirname, 'compiled'),
    filename: '[name].js',
    sourceMapFilename: '[name].map',
    libraryTarget: 'commonjs2',
    publicPath: 'http://localhost:8080/assets/'
  },
  debug: true,
  devtool: 'cheap-module-eval-source-map'
})
```

---
# Frontend
## Front-end: HTML + CSS (CSS Modules)
O *Boostnote* utiliza as ferramentas HTML e CSS para o desenvolvimento frontend, em junção com as ferramentas React e Redux citadas anteriormente. Para a organização do código CSS, é utilizado o CSS Modules, que é um arquivo CSS onde todos os nomes de classes são referenciados localmente, para que não haja a necessidade de especificar o caminho inteiro do arquivo para a classe. Ao utilizá-lo dentro de um módulo da linguagem Javascript, é possível exportar um objeto com o mapeamento de todos os nomes de escopo local para nomes de escopo global.

<p align="center">
  <img src="https://image.prntscr.com/image/cd275e9caf7940c2b47fd18495c16568.png"/>
</p>

---
# ** Arquitetura **

A arquitetura do Boostnote está dividida em módulos segundo este diagrama:
<p align="center">
  <img src="https://image.prntscr.com/image/f54beefff9904a09a39d5713b88006fb.png"/>
</p>

Nesta seção iremos descrever cada um destes módulos, será falado sobre suas funcionalidades, e mostraremos detalhes de implementação e as principais classes. 

---
## ** Text Editor **

Existem duas formas de tomar notas com Boostnote, a primeira é através do uso de Markdown e a segunda se dá através do uso de tags em HTML, aqui será demonstrado como foram implementados os módulos referentes a essas duas funcionalidades.

---
### Markdown Editor

O módulo Markdown Editor é a ferramenta que possibilita aos usuários tomar notas na linguagem simples de marcação Markdown, que converte qualquer texto em XHTML válido. Há, na aplicação, um serviço de visualização prévia em tempo real da conversão para acompanhamento do usuário aumentando assim a qualidade de uso da ferramenta.

#### Diagrama de classes:

<p align="center">
  <img src="https://image.prntscr.com/image/e60cb59e1d2b4fe49c65ec497737496b.png"/>
</p>

* Markdown editor*: Essa classe é responsável por implementar o editor de Markdown da ferramenta Boostnote. Ela é a responsável por toda a renderização do editor na tela, e também pela manipulação de todos os eventos Javascript, como o *onBlur*, listeners para os cliques de botões, além das mudanças de estados.

* MarkdownPreview *: Essa classe faz a implementação de métodos de controle de eventos, aqueles que são iniciados por handle, ela possibilita a visualização prévia do texto na linguagem markdown em tempo real.

* MarkdownNoteDetail *: Essa classe é a responsável pela implementação do menu de contexto que é utilizado para comunicar o usuário de informações sobre a atual nota já convertido em Markdown. Assim como as outras classes deste módulo, ela também implementa listeners e ações para os diversos eventos Javascript dentro de seu escopo.


---
### Tag Editor

O Tag Editor é o módulo que possibilita ao usuário tomar notas utilizando tags no formato HTML.

#### Diagrama de classes:

<p align="center">
  <img src="https://image.prntscr.com/image/168f561e3f83409b99a32003aa93af09.png"/>
</p>


*CodeEditor*: este componente React declara o editor de texto, incluindo seu comportamento e seu estilo.

*SnippetTab*: este componente faz a declaração de um pequeno menu para manipular notas, como abrir ou deletar uma.

*SnippetNoteDetail*: implementação de cada item mostrado no menu declarado em *SnippetTab*, mostrando informações sobre as notas.



---
### Finder

O módulo Finder, como o próprio nome diz, é um buscador que possibilita ao usuário encontrar referências dentro das anotações e no armazenamento, atuando basicamente como um Ctrl+F que tem como referência para a busca todo o sistema. Sua funcionalidade é baseada no Finder dos sistemas operacionais Mac OS X e Linux, permitindo aos usuários assim fazer buscas em todo o SO. A ferramenta Boostnote permite que as notas do usuário sejam indexadas para permitir tal busca.

#### Diagrama de classes:

<p align="center">
  <img src="https://image.prntscr.com/image/d3001b7e10bd47fc9aa7e4897fe3870c.png"/>
</p>

* NoteDetail:* Classe responsável por criar uma popup com as notificações de detalhes das notas, implementa função para salvar, e avançar ou retroceder nas notas, assim como a função que renderiza a estilização dessa classe.

*Notelist*: Essa classe implementa uma lista simples que contém as notas armazenadas com algumas poucas informações extras.
```javascript
  render () {
    let { notes, index } = this.props

    let notesList = notes
      .slice(0, 10 + 10 * this.state.range)
      .map((note, _index) => {
        const isActive = (index === _index)
        const key = `${note.storage}-${note.key}`
        const dateDisplay = moment(note.updatedAt).fromNow()

        return (
          <NoteItem
            isActive={isActive}
            note={note}
            dateDisplay={dateDisplay}
            key={key}
            handleNoteClick={(e) => this.props.handleNoteClick(e, _index)}
            handleNoteContextMenu={() => ''}
          />
        )
      })

```

*index*: Essa classe é responsável pela implementação em React da janela principal do Finder. Também há a manipulação de estados e listeners.

*ipcClient*: Essa classe é uma implementação em Node.js que tem como objetivo recuperar as notas do usuário em memória, além disso, ela é a responsável pela implementação da funcionalidade do módulo Finder.
```javascript
nodeIpc.connectTo(
  'node',
  path.join(app.getPath('userData'), 'boostnote.service'),
  function () {
    nodeIpc.of.node.on('error', function (err) {
      console.log(err)
    })
    nodeIpc.of.node.on('connect', function () {
      console.log('Conncted successfully')
    })
    nodeIpc.of.node.on('disconnect', function () {
      console.log('disconnected')
    })
```
---
## ** User Interface **

A interface de usuário é composta por um layout que foi desenvolvido em HTML e CSS, utilizando a biblioteca React para a renderização dos componentes, além de um buscador (finder) que tem a capacidade de encontrar referências dentro de notas e storages e, por último pela aba de configuração, por onde são controladas as preferências do usuário em relação ao design do programa, hotkeys e storages.


---
### Layout

O layout do software é o responsável pela sua aparência, ele também foi feito em HTML e CSS e foi dividido em vários arquivos, abaixo se encontra um lista de todos os arquivos utilizados pelo programa para tratar a sua estilização.

#### Lista de arquivos de estilização:

<p align="center">
  <img src="https://image.prntscr.com/image/80a689b9c45b46e5980389218d459548.png"/>
</p>

---
### Configuration

Este módulo do Boostnote é utilizado para inicializar e verificar as configurações estéticas do editor de texto.
#### Diagrama de classes:

<p align="center">
  <img src="https://image.prntscr.com/image/e99af693f92642498ca414ca6b55f816.png"/>
</p>

*configManager*: Esse arquivo da linguagem Javascript possui a declaração de diversas variáveis e métodos do Electron utilizados pela ferramenta Boostnote, entre elas estão as configurações específicas para certos sistemas operacionais, a validação de configurações, o tratamento de exceções para as mesmas, além de configurações default para o editor de texto do programa.

*zoomManager*: Essa classe possui a implementação da função de zoom, e utiliza funcionalidades do framework *Electron* para tal. Ela permite que o nível de zoom na nota possa ser definido pelo próprio usuário, e além disso permite que o frontend use essas mesmas informações para renderizar na tela o nível correto de zoom.

---
## ** Files Management **

A ferramenta Boostnote implementa recursos para lidar com arquivos, possibilitando assim a fácil criação e remoção de pastas, a criação e remoção de notas e a organização de suas notas em uma seção que fica dentro do programa chamada storage, isso permite que os usuários possam armazenar suas notas sem a necessidade de haver conexão com a Internet para salvá-las. Abaixo falaremos mais sobre seu sistema de files management. 

---
### Storage

#### Diagrama de classes:

<p align="center">
  <img src="https://image.prntscr.com/image/eaaa028db34441febc239c65fff1270e.png"/>
</p>


*StorageSection*: Essa classe faz a implementação do componente que tem como responsabilidade mostrar ao usuário as notas que estão armazenadas em memória, além de tratar os cliques de input.

*resolveStorageData:* Classe responsável por atribuir os valores relacionado a descrição do arquivo, como nome, tipo, caminho, etc...

*addStorage*: Essa classe utiliza a linguagem Javascript para obter acesso à memória local do computador a fim de armazenar e recuperar notas que estão salvas. 

*renameStorage*: Essa classe faz a declaração de uma função Javascript que é responsável por renomear algum armazenamento local que o usuário já tenha criado. 

*removeStorage*: Assim como na classe acima, esse arquivo tem a declaração de uma função que remove algum armazenamento local que o usuário já tenha criado.

*StorageItem*: Essa classe faz a declaração do estilo com o qual os armazenamentos serão exibidos na tela para o usuário.

*StorageTab*: Essa classe faz a declaração do componente do menu lateral (sidebar) que exibe os armazenamentos. Além disso, é também o responsável por tratar todos os eventos Javascript dele.

---
### Folders

#### Diagrama de classes:

<p align="center">
  <img src="https://image.prntscr.com/image/191a20b9f710413da57ecd58e92cf627.png"/>
</p>


*folderSelect*: Esse módulo é o responsável pela obtenção de quais são as pastas disponíveis no armazenamento local e pela exibição delas ao usuário da aplicação.

*createFolder:* Essa é uma função auxiliar e tem a responsabilidade de criar pastas no armazenamento.

*updateFolder:* Outra função auxiliar, tem a responsabilidade de atualizar os conteúdos da pasta, para que possam ser renderizados por *folderSelect*.

*deleteFolder:* Outra função auxiliar, é utilizada para fazer a remoção de uma pasta e de seus conteúdos.

*RenameFolder:* Outra função auxiliar que tem a responsabilidade de renomear um diretório já existente.

*CreateFolderModal:* Esste é um componente que é utilizado para a criação do menu de exibição das pastas no armazenamento.

---
### Notes

#### Diagrama de classes:

<p align="center">
  <img src="https://image.prntscr.com/image/2eaf09f6c6194e9491224d2783ccd4ba.png"/>
</p>


*NewNoteModal:* Esta classe é a responsável pela renderização da janela de criação de notas e também pela chamada do método de criação de notas (createNote()).

*createNote: *É a classe que possui métodos responsáveis pela criação de notas e pela validação de input.

*deleteNote:* É a classe que possui métodos responsáveis pela remoção de notas e pela validação de input.

*updateNote:* É a classe que possui métodos responsáveis pela atualização das notas e pela validação de input.


 
 
 
