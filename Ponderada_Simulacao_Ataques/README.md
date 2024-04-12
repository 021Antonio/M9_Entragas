# Simulação de Vulnerabilidades em MQTT Segundo a Triade CIA

Este README descreve as vulnerabilidades identificadas em um ambiente MQTT utilizando os princípios da Triade CIA - Confiabilidade, Integridade e Disponibilidade. Detalhamos as simulações realizadas, os impactos identificados e as soluções propostas para cada tipo de vulnerabilidade.

## Confiabilidade

**Problema Identificado:** Configuração inadequada de autenticação no broker MQTT, permitindo acessos não autorizados.

**Simulação:** Utilização de um cliente MQTT para conectar ao broker com credenciais básicas e acessar informações de tópicos sensíveis.

**Impacto:** Vazamento potencial de informações sensíveis, comprometendo a confidencialidade do sistema.

**Solução Proposta:** Implementação de um sistema robusto de autenticação e autorização, como OAuth ou LDAP/Active Directory.

## Integridade

Problema Identificado: Comunicação não criptografada e sem validação, permitindo ataques de interceptação e modificação de mensagens.

**Simulação:** Execução de um ataque de Man-in-the-Middle, alterando o conteúdo das mensagens MQTT.

**Impacto:** Alterações maliciosas no comportamento dos dispositivos conectados ao broker MQTT.

**Solução Proposta:** Implementação de [TLS para criptografia](https://www.cloudflare.com/pt-br/learning/ssl/transport-layer-security-tls/) e uso de assinaturas digitais para verificação de integridade.

## Disponibilidade

**Problema Identificado:** Broker MQTT suscetível a ataques de negação de serviço (DoS - Denial Of Service).

**Simulação:** Realização de um ataque DoS, sobrecarregando o broker com múltiplas requisições simultâneas.

**Impacto:** Queda do serviço, impedindo que usuários legítimos acessem o broker MQTT.

**Solução Proposta:** Limitação de rate para conexões e requisições, e implementação de [sistemas de IDS/IPS](https://www.spiceworks.com/it-security/network-security/articles/ids-vs-ips/) para prevenção de ataques.


## Conclusão

Através de simulações práticas, identificamos e achamos possiveis soluções para as principais vulnerabilidades em um ambiente MQTT. A implementação das medidas sugeridas contribuirá significativamente para a segurança do sistema, assegurando a confiabilidade, integridade e disponibilidade das comunicações.