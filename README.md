# YouTube Downloader Flask App

Aplicação web simples em Flask para baixar vídeos e áudios do YouTube utilizando a biblioteca `yt-dlp`.

---

## Funcionalidades

- Baixa vídeos em formato MP4 (qualidade padrão do YouTube).
- Baixa áudios em formato MP3 (extrai áudio dos vídeos).
- Organiza os downloads em pastas separadas (`video/` e `audio/`).
- Interface web responsiva para desktop e mobile.
- Página para listar os arquivos já baixados.
- Feedback visual durante o processo de download.

---

## Requisitos

- Python 3.7+
- [FFmpeg](https://ffmpeg.org/download.html) instalado e acessível no PATH (necessário para conversão de áudio).
- Bibliotecas Python:
  - Flask
  - yt-dlp

---
## Passos Futuros

O aplicativo já está funcional, mas existem várias melhorias e funcionalidades que podem ser adicionadas para torná-lo mais robusto, seguro e amigável para os usuários. Aqui estão algumas sugestões para os próximos passos no desenvolvimento:

1. **Separar arquivos por usuário (autenticação básica)**
   - Implementar sistema de login/logout para que cada usuário tenha seu próprio espaço.
   - Armazenar vídeos e áudios baixados em pastas separadas por usuário, garantindo privacidade.

2. **Melhorar a interface e experiência do usuário (UX)**
   - Adicionar barra de progresso real para o download usando WebSockets ou polling.
   - Tornar a interface totalmente responsiva e mobile-friendly.
   - Implementar notificações visuais e sonoras ao concluir o download.

3. **Suporte a múltiplos downloads simultâneos**
   - Permitir que vários usuários baixem vídeos ao mesmo tempo sem travar o servidor.
   - Utilizar filas e processamento assíncrono (ex: Celery com Redis) para gerenciar tarefas.

4. **Suporte a mais formatos e qualidades**
   - Oferecer opções de qualidade do vídeo (360p, 720p, 1080p, etc).
   - Suportar outros formatos além de MP3 e MP4.
   - Mostrar informações adicionais, como duração e tamanho do arquivo antes do download.

5. **Deploy em ambiente de produção**
   - Hospedar o app em servidores reais que suportem Python e FFmpeg (Heroku, DigitalOcean, AWS, Railway, etc).
   - Garantir que dependências essenciais estejam instaladas e configuradas.

6. **Melhorias de segurança**
   - Validar URLs para evitar downloads de conteúdos maliciosos.
   - Limitar tamanho e duração dos downloads para proteger o servidor.
   - Configurar HTTPS para comunicação segura.

7. **Logs e monitoramento**
   - Registrar logs detalhados das atividades e downloads para auditoria.
   - Monitorar erros e performance para manter a estabilidade do sistema.

Essas melhorias ajudarão a tornar o aplicativo mais completo, seguro e agradável para os usuários. Sinta-se à vontade para contribuir ou sugerir novas funcionalidades!

---

## Como usar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
