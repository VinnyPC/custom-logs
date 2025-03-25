# custom-logs
Sistema de logs que adiciona funcionalidades dinâmicas como timestamp, cor, ou salvar em arquivo a qualquer função usando decorators

# Decorators
O Decorator é um padrão de projeto que permite estender a funcionalidade de objetos sem modificar seu código original.

Nele, a classe base é encapsulada por outra classe, que adiciona novas funcionalidades dinamicamente, mantendo a estrutura original intacta. Assim é evitado alterações diretas no código em produção, reduzindo o risco de introduzir bugs.

Benefícios:
- Extensão sem modificação – Novos comportamentos são adicionados sem alterar a classe original.
- Flexibilidade – Combina funcionalidades em tempo de execução.
- Menos riscos – Preserva o código já testado e em produção.

É ideal para cenários onde herança não é viável ou quando se precisa de comportamentos customizáveis em tempo de execução. 🚀

# Exemplo de onde pode ser usando
Um ótimo exemplo de onde esse padrão pode ser usado é o exemplo citado no site [CodeGuru](https://refactoring.guru/design-patterns/decorator):

Uma biblioteca de notificações começou com uma classe simples Notificador que enviava alertas apenas por e-mail. Com o tempo, surgiram demandas para novos canais como SMS, Facebook e Slack.
- Usar herança para cada novo canal (ex: NotificadorSMS, NotificadorSlack) criaria uma explosão de classes.
- Combinações como "E-mail + SMS + Slack" exigiriam subclasses específicas (NotificadorEmailSMS), tornando o código complexo e difícil de manter.
Nesse caso, a solução é ter uma classe base (ex.: `notificator`) onde teria a lógica de enviar as notificações, e conforme novas demandas vão aparecendo, são criadas outras classes Decorators que encapsulam um a `notificator` e adicionam funcionalidades.

