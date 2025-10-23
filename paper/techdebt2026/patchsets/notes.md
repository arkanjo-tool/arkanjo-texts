# Takeaways

## _T2_: Meaningful code

## _T3_: Upstream Integration Overhead

## _T4_: Cognitive Load

## _T5_: Performance

## T?: Undefined

# Bianca e Júlia (Grupo 1)

- Thread v1: https://lore.kernel.org/linux-iio/20250426194135.244774-1-biancalvao@gmail.com/t/
- Thread v2 (1/2): https://lore.kernel.org/linux-iio/20250507182327.49068-1-biancalvao@gmail.com/t/
- Thread v2 (2/2): https://lore.kernel.org/linux-iio/20250526120340.16880-1-biancalvao@gmail.com/t/

## Status

Rejeitado ✗

## Contexto

1 patch para o IIO com uma deduplicação usando _extract method_. Duas funções
predicado faziam a mesma lógica, apenas retornando a negação uma da outra.
Assim, implementaram uma função que fazia esta lógica duplicada e chamaram ela
nas funções duplicadas.

## Motivos para aceitação/rejeição

### v1

Mantenedor principal disse que _"The patch is mostly fine"_, mas comentou que
**a nova função criada não tinha um nome que indicasse a sua funcionalidade**
(talvez vale incluir). Comentou que seria melhor (por questão de documentação
mesmo) só fazer uma das funções retornar a negação da outra, vendo até uma
vantagem de se fazer dessa forma _"will effectively document that all non
writeable registers are volatile"_.

### v2

Os mantenedores acabaram mudando de ideia em relação a se fazia sentido em
relação ao significado (a negação de writeable ser volatile). Porém, os "erros"
de newcomer parecem ter desestimulado o mantenedor principal, de forma que o
patch acabou sendo esquecido.

## Boas aspas

### v1

- _T2_: Jonathan Cameron sobre a legibilidade vir antes da deduplicação:
  _"The patch is mostly fine but I think the naming as
  _reg_check() is not helpful as it doesn't indicate anything specific
  is being checked."_

### v2

- _T3_: Marcelo Schmitt sobre o trade-off de aceitar um patch "não tão importante":
  _"[...] such patches might not worth it since the proposed improvement is very
  small (and questionable) while the upstreaming process still requires some
  effort."_


# Mikhael e Augusto (Grupo 2)

- Thread v1: https://lore.kernel.org/all/20250429093923.347370-1-mikhael_abdallah@usp.br/t/

## Status

Rejeitado ✗

## Contexto

1 patch para o IIO com uma deduplicação usando _parametize method_. Duas
funções faziam a mesma lógica complexa e os autores criaram uma função genérica
que aceitava um novo parâmetro, o qual definiria o comportamento específico
para cada função.

## Motivos para aceitação/rejeição

### v1

O mantenedor principal disse que a redução de código era pequena (-2 no total)
e que tornava o código mais complexo.

Aqui é algo legal de discutir (se houver espaço), já remover duplicações não é
só sobre reduzir linhas de código, mas também é interessante para "centralizar
partes iguais"; assim quando for mudar um código duplicado, não é necessário
lembrar de mudar nos outros lugares onde a duplicação aparece. O bacana é que
essa visão "clássica" não se traduz tão bem nesse contexto do kernel, em que
(nesse caso) duas funções fazem conceitualmente duas coisas um tanto
diferentes, mas de forma muito parecida e "centralizar a parte comum" causaria
um problema de legibilidade _mental overhead_.

## Boas aspas

### v1

- _T2_: Jonathan Cameron sobre a pequena redução de código não compensar o aumento na
  complexidade: _"In my view this isn't a significant enough reduction to justify
  the more complex code."_


# Beatriz e Gabriela (Grupo 3)

- Thread v1: https://lore.kernel.org/linux-iio/20250424002144.23260-1-beatrizvianacosta16@gmail.com/t/

## Status

Aceito ✓

## Contexto

1 patch para o IIO com uma deduplicação usando _parametize method_. Duas
funções faziam essencialmente a mesma lógica apenas divergindo sobre qual tipo
de `struct` operavam; as autoras então criaram uma `struct` genérica e uma
função geral que aceita esse nova `struct` como parâmetro.

## Motivos para aceitação/rejeição

### v1

Um mantenedor reclamou do uso de uma macro no geral, advocando em favor da
antiga duplicação. Outro achou a ideia boa, só requisitou uma mudança de nome.

## Boas aspas

Nenhuma


# Arthur, Bruno e André (Grupo 4)

- Thread v1: https://lore.kernel.org/linux-iio/20250419161347.28157-1-arthurpilone@usp.br/t/
- Thread v2: https://lore.kernel.org/linux-iio/20250420222512.173029-1-arthurpilone@usp.br/t/
- Thread v3: https://lore.kernel.org/linux-iio/20250421145534.91146-1-arthurpilone@usp.br/t/

## Status

Aceito ✓

## Contexto

1 patch para o IIO com uma deduplicação usando um método não definido. Duas
funções basicamente retornavam a negação uma da outra (i.e., quando uma
retornava `true` a outra retornava `false`); inicialmente, optaram por uma
macro, porém com os ciclos de revisões, terminaram fazendo uma das funções
apenas retornar a negação da outra adicionando um comentário explicando a
situação.

## Motivos para aceitação/rejeição

### v1

Um mantenedor reclamou do uso de uma macro no geral, advocando em favor da
antiga duplicação. Outro achou a ideia boa, só requisitou uma mudança de nome.
Nenhum dos mantenedores era o "principal".

A questão da legibilidade, mais uma vez veio a tona.

### v2

Mantenedor principal entrou na jogada e falou que preferia que não fosse usada
uma macro, mas que uma das função chamasse a negação da outra.

### v3

Com a sugestão do mantenedor principal incorporada, o patch foi aceito.

## Boas aspas

### v1

- _T2_: David Lechner, sobre trade-off deduplicação e legibilidade: _"I think the old
  code is more readable than hiding the values in a macro even if it is
  duplicating a few lines of code."_


# Gustavo e Francisco (Grupo 5)

- Thread v1: https://lore.kernel.org/linux-iio/20250423204631.16460-1-gustavo.vaz@usp.br/t/

## Status

Aceito ✓

## Contexto

1 patch para o IIO com uma deduplicação usando o _parametize method_. Duas
funções tinham uma lógica muito similar, então os autores criaram uma função
mais genérica que aceitava um parâmetro adicional.

## Motivos para aceitação/rejeição

### v1

Nenhum em particular, o mantenedor principal apenas disse _"Seems fine to me"_
e aceitou o patch.

## Boas aspas

Nenhuma


# Gabriel, Gabriel e Vitor (Grupo 6)

- Thread v1: https://lore.kernel.org/all/20250623201539.16148-1-gabriellimamoraes@gmail.com/t/

## Status

Rejeitado ✗

## Contexto

1 patch para o IIO com uma deduplicação usando o _parametize method_. Duas
funções inicializavam de forma muito similar o driver do sensor de luz, e então
criaram uma função que generaliza ambas através de parâmetros.

## Motivos para aceitação/rejeição

### v1

Foi mencionado a deduplicação adicionava mais código que removia (+95/-92). Em
relação a isso, deduplicar código muitas vezes resulta em remoção do número
total de linhas código, porém [não é um requisito](#checar-se-existe-ref), de
forma que o mantenedor não evidencia isso como a única razão para rejeitar (ele
revisa o código e tudo mais). Por outro lado, é bem notado pelo mantenedor que
os autores adicionaram uma declaração de protótipo de função desnecessária (a
definição da função ocorre antes das chamadas), o que resultaria em -11 linhas
de código ao patch.

Por outro lado, o mantenedor também aponta que, apesar de se deduplicar código,
havia aumento de [esforço cognitivo/carga cognitiva](#checar-se-existe-ref),
pois o leitor (incluindo ele mesmo ao revisar) teria que ficar pulando no
código para ver os argumentos passados pelas funções (i.e., antes: `soma(1,
2)`, com o patch: `soma(x, y)`).

## Boas aspas

### v1

- _T?_: Jonathan Cameron sobre a deduplicação estar adicionando mais código no total:
  _"When a patch removing duplication ends up adding code it might not be such a
  good idea..."_

- _T?_: Jonathan Cameron sobre não ver algo em favor de aceitar o patch: _"[...] in
  general there isn't a convincing argument that I can see for this code
  unification."_

- _T4_: Jonathan Cameron sobre a deduplicação criando uma nova função que generaliza
  as duas adiciona carga cognitiva ao obrigar o leitor (e o revisor) ao navegar
  pelo código: _"Wrapping this up doesn't provide any real advantage, requiring
  as it does the reviewer to look at this function AND where the value is set
  rather than seeing them in one place."_


# Isabella e Rodrigo (Grupo 7)

- thread v1: https://lore.kernel.org/linux-iio/20250428132551.176788-1-bellacaselli20@gmail.com/t/
- thread v2: https://lore.kernel.org/linux-iio/20250507181854.49025-1-bellacaselli20@gmail.com/t/
- thread v3: https://lore.kernel.org/linux-iio/20250507184539.54658-1-bellacaselli20@gmail.com/t/

## Status

Aceito ✓

## Contexto

1 patch para o IIO com uma deduplicação usando o _extract method_. Duas funções
tinham lógicas em comum e os autores criaram um helper pra elas, inicialmente,
e moveram a parte em comum para dentro de um helper que já estava sendo chamado
em ambas as funções, depois.

## Motivos para aceitação/rejeição

### v1

Um mantenedor apontou que este par de funções não fazia sentido adicionar este
helper, pois já existia um helper que criava uma abstração em comum que tinha
significado no contexto de desenvolvimento. Apesar de haver redução de linhas
de código (bem pouco; -1), isto não era justificável.

### v2

Os autores perceberam que tinham enviado a v2 em cima da v1 ao invés de fazer o
amend do patch. Devido a isto, enviaram a v3 antes de obterem o feedback dos
mantenedores.

### v3

Um outro mantenedor (nem o principal, nem o que comentou na v1) disse que
poderia ser adicionado um outro parâmetro para a função helper que eles
expandiram, mas que estava ok com o estado atual, se os seus pares
concordassem. Após o primeiro revisor dar o Ack dele, o mantenedor principal
fez o merge da mudança.


## Boas aspas

### v1

- _T?_: Jean-Baptiste Maneyrol sobre, apesar de como já existe uma função helper e
  que adicionar mais uma apenas redução de linhas, não fazia sentido para ele:
  _"We already have a common function inv_mpu_i2c_master_xfer() for handling
  master I2C transfer, and there is no need to create a new external function
  inv_mpu_aux_exec_xfer() that is never called outside the inv_mpu_aux.c file."_


# Nattan e Lucas (Grupo 8)

- thread v1: https://lore.kernel.org/linux-iio/20250419232128.35759-1-nattanferreira58@gmail.com/t/
- thread v2: https://lore.kernel.org/linux-iio/20250422171503.26532-1-nattanferreira58@gmail.com/t/
- thread v3: https://lore.kernel.org/linux-iio/20250526235906.6598-1-nattanferreira58@gmail.com/t/
- thread v4: https://lore.kernel.org/linux-iio/20250611174253.16578-1-nattanferreira58@gmail.com/t/

## Status

Aceito ✓

## Contexto

1 patch para o IIO com uma deduplicação usando o _extract method_. Duas funções
tinham lógicas em comum e os autores criaram um helper pra elas.

## Motivos para aceitação/rejeição

### v1

Mantenedores apenas explicaram um pouco das convenções do projeto e demandaram
alterações que fossem mais no estilo coding style.

### v2

Como na v1, o mantenedor principal apenas reforçou erros de estilo de código.

### v3

Na mesma linha de coisas não relacionadas a implementação em si, mas sobre a
mensagem de commit (número de linhas máximo e changelog).

Ainda assim, um ponto contra o patch que foi levantado, apesar de ter sido
trazido como "geralmente fazemos assim...", foi como a deduplicação resultaria
em mais comparações (mesmo que poucas), e que isso impacto na execução é
relevante nesse de recursos limitados do IIO.

### v4

Após as correções mencionadas sobre estilo de código e "nitpickings", o
mantenedor principal aceitou a contribuição.

## Boas aspas

### v1

- _T5_: Marcelo sobre a deduplicação adicionar uma comparação a mais ao código:
  _"Even though there is less code repetition, we now have an extra comparison to
  handle get_thresh_reg() return."_

### v3

- _T5_: Subhajit Ghosh falando sobre o trade-off de modularidade (não duplicação,
  nesse caso) e velocidade de execução: _"There is always a balance/trade-off
  between modularity and execution speed. I agree with Marcelo's reply in the
  first patch and I also think that separate function for this does not add much
  value."_


# Andrew e Gustavo (Grupo 9)

- thread v1: https://lore.kernel.org/linux-iio/20250423170526.15143-1-andrew.lopes@alumni.usp.br/t/
- thread v2: https://lore.kernel.org/linux-iio/20250425235130.56122-1-andrew.lopes@alumni.usp.br/t/
- thread v3: https://lore.kernel.org/linux-iio/20250509013931.47524-1-andrew.lopes@alumni.usp.br/t/
- thread v4: https://lore.kernel.org/linux-iio/20250510190759.23921-1-andrew.lopes@alumni.usp.br/t/
- thread v5: https://lore.kernel.org/linux-iio/20250611194648.18133-1-andrew.lopes@alumni.usp.br/t/
- thread v6: https://lore.kernel.org/linux-iio/20250618031638.26477-1-andrew.lopes@alumni.usp.br/t/

## Status

Aceito ✓

## Contexto

1 patch (inicialmente) para o IIO usando o _function generalization method_ e
(ao final) usando o _inline method_. Duas funções eram muito parecidas em
implementação e propósito e os autores propuseram remover uma delas,
centralizando o comportamento duplicado na outra. Com a evolução do patch, a
série evoluiu e a deduplicação acabou sendo resolvida com um _inline method_
usando funções helper.

## Motivos para aceitação/rejeição

### v1

De início, o mantenedor apenas comentou sobre a mensagem de commit, e que um
trecho de código poderia ser escrito de forma mais sucinta (sem mudar a lógica
por trás).

### v2

O mantenedor principal entrou na revisão e trouxe a ideia que o driver era bem
antigo e não utilizava todo o potencial da nova infraestrutura, de forma que a
deduplicação poderia ser feita usando funções helper que já existiam (aqui
passou a ser _inline method_). Isso teria potencial de remover ambas as funções
duplicadas, ao invés de juntar as duas em uma mais geral, porém, o mantenedor
trouxe que poderia haver casos (e tinha um) em que manter uma das funções
usando a infraestrutura antiga ainda valeria a pena por questão de performance.

### v3

Vários feedbacks não relacionados a deduplicação e sim em coding style,
convenções e código limpo.

### v4

Aparentemente os autores não responderam/atacaram todos os comentários de um
dos mantenedores. Além disso, surgiram outras melhorias oportunas, de forma que
o mantenedor principal sugeriu expandir o patch para um série com 3 patches,
sendo um deles tratando especificamente da deduplicação.

### v5

A partir desta versão, apenas um patch da série atacava a dedupliação e iremos
nos focar apenas nele. Neste caso, foi notado por um novo mantenedor que havia
uma parte do patch que violava a questão de atomicidade, de forma que foi
sugerido separar este em dois (um só tratando diretamente da deduplicação). O
outro mantenedor (que não o principal) que estava revisando o patchset, trouxe
mais comentários de coding style e afins.

### v6

Apesar de algumas pequenas mudanças possíveis apontadas, o mantenedor principal
as aplicou e aceitou o patch que tratava da deduplicação.

## Boas aspas

### v2

- _T5_: Jonathan Cameron sobre motivos de não se aplicar o _inline method_ em alguns
  casos devido a possíveis problemas com performance: _"Note that is not an
  appropriate change for the large reads though as spi_write_then_read() bounces
  all buffers and so would add a copy to those high(ish) performance paths."_

- _T5_: Jonathan Cameron sobre ainda manter uma única chamada da função que restou
  após a deduplicação por motivos de performance: _"This is the one case were
  spi_write_then_read() is probably not appropriate due to the large buffers that
  are potentially involved. I think this will be the only remaining case to use
  the old infrastructure."_


# Gabriel e Nicolas (Grupo 10)

- thread v1: https://lore.kernel.org/linux-iio/20250428034222.318898-1-gabrielgeraldinosouza@gmail.com/t/

## Status

Rejeitado ✗

## Contexto

1 patch para o IIO com uma deduplicação usando o _extract method_. Em uma função, havia uma lógica de inicialiazação de alguns dispositivos que era duplicada, então os autores propuseram extrair esta parte duplicada em uma `struct`.

## Motivos para aceitação/rejeição

### v1

O mantenedor principal comentou que, apesar da deduplicação reduzir LOCs (e
talvez melhorar a performance), neste contexto legibilidade é prioridade e, na
visão dele, o patch piorava o código neste quesito.

## Boas aspas

### v1

- _T2_: Jonathan Cameron, comentando sobre a deduplicação, apesar de reduzir LOCs,
  reduzia a legibilidade: _" A few comments inline, but overall I'm not sure the
  code reduction is sufficiently to cover the resulting loss of readability.
  Sometimes a switch is simply clear than a partial look up table."_

- _T2/T5_: Jonathan Cameron, falando sobre como o patch até poderia trazer ganho de
  performance, mas que nesse contexto, legibilidade é mais prioridade: _"I'd be
  slightly interested to see the optimized output of the two approaches, but this
  is far from a high performance path so we care a lot more about readability
  here."_


# Sebastian IIO (Grupo 11)

- thread v1: https://lore.kernel.org/all/20250429165604.67984-1-saguileran@ime.usp.br/t

## Status

Rejeitado ✗

## Contexto

1 patch para o IIO com uma deduplicação usando o _inline method_. Duas funções,
literalmente, retornavam `false`, então o autor substituiu as chamadas desta
funções (cada uma era chamada uma única vez) pelos booleanos _inline_. De
acordo com o autor do patch, o fato de ambas as funções terem argumentos
(struct para dispositivo e número de registrador), mas que eles eram _dead
code_, somado ao fato de no datasheet não haver nenhuma menção (de acordo com o
autor) sobre o esses parâmetros definirem algo sobre os registradores.

## Motivos para aceitação/rejeição

### v1

O mantenedor principal foi bem vago em sua resposta, então apenas resta
especular sobre o que ele quis dizer. No meu entendimento, ele se refere ao
fato da deduplicação estar incorreta, pois o tipo esperado pelos campos da
`struct` que ele substitui por `false` eram funções que devolviam um `bool` e
tinham os parâmetros exatos como definidos. Ou seja, mesmo que a compilação
funcionasse (houvesse um cast automático ou algo do tipo), esta não era a forma
correta de se proceder.

## Boas aspas

Nenhuma


# Sebastian AMD (Grupo 11)

- thread v1: https://lore.kernel.org/amd-gfx/20250501225343.76300-1-saguileran@ime.usp.br/t/
- thread v2: https://lore.kernel.org/amd-gfx/20250503035949.11132-1-saguileran@ime.usp.br/t/

## Status

Aceito ✓

## Contexto

1 patch para o AMD display que remove 1 família de funções duplicadas usando um
método não definido. Nos drivers para as diferentes gerações das GPUs, na parte
do display, a função `hpd_ack()` era duplicada em praticamente todos, com
mínima mudança, de forma que o autor propôs duas funções de biblioteca que
cobriam todos os casos.

## Motivos para aceitação/rejeição

### v1

O patch só não foi aceito de cara, pois havia um número de erros de coding
style, os quais o mantenedor apontou que, ao serem resolvidos, ele iria
integrar o patch.

### v2

O patch foi aceito, apesar de ainda haver um pequeníssimo erro de coding style
(que foi corrigido) pelo próprio mantenedor.

## Boas aspas

Nenhuma









# checar se existe ref
