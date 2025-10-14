# 🌐 GUIA DE CONFIGURAÇÃO PARA IIS

## Problemas Resolvidos:
- ✅ Erro de JSON (Unexpected token '<')
- ✅ Erro 405 (Method Not Allowed)
- ✅ CORS configurado
- ✅ URLs absolutas implementadas

## 🚀 Configuração Passo a Passo:

### 1. Configuração do IIS
Adicione estas regras no seu arquivo `web.config` ou no IIS Manager:

```xml
<rule name="Youtube" stopProcessing="true">
  <match url="^youtube/(.*)" />
  <action type="Rewrite" url="http://localhost:6001/{R:1}" />
</rule>
<rule name="YoutubeStatic" stopProcessing="true">
  <match url="^youtube/static/(.*)" />
  <action type="Rewrite" url="http://localhost:6001/static/{R:1}" />
</rule>
<rule name="YoutubeAPI" stopProcessing="true">
  <match url="^youtube/(video_info|download|progress)" />
  <action type="Rewrite" url="http://localhost:6001/{R:1}" />
</rule>
```

### 2. Iniciar o Servidor Flask
Execute um destes comandos:

**Opção A - Script automático:**
```cmd
run_iis.bat
```

**Opção B - Manual:**
```cmd
set FLASK_CONFIG=production
set FLASK_HOST=127.0.0.1
set FLASK_PORT=6001
python app.py
```

### 3. Testar a Configuração

**Via IIS:**
- Acesse: `http://seudominio/youtube/`

**Direto (para teste):**
- Acesse: `http://localhost:6001`

**Teste da API:**
- `http://localhost:6001/video_info?url=https://www.youtube.com/watch?v=exemplo`

## 🔧 Troubleshooting:

### Se ainda der erro de JSON:
1. Abra o console do navegador (F12)
2. Veja os logs detalhados
3. Verifique se o Flask está rodando na porta 6001
4. Teste a URL direta: `http://localhost:6001/video_info?url=URL_DO_VIDEO`

### Se der erro 405:
1. Certifique-se que o formulário está usando POST
2. Verifique se a regra do IIS está correta
3. Teste diretamente: `http://localhost:6001/download`

### Verificar se o Flask está rodando:
```cmd
netstat -an | findstr :6001
```

## 📝 URLs de Teste:

- **Homepage:** `http://localhost:6001/`
- **API Video Info:** `http://localhost:6001/video_info?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- **Download:** `http://localhost:6001/download` (POST)

## ⚙️ Configurações Importantes:

- **Porta:** 6001 (configurável em config.py)
- **Host:** 127.0.0.1 (apenas local)
- **CORS:** Habilitado para todas as origens
- **Timeout:** 10 minutos para downloads grandes

## 🔄 Reiniciar Serviços:

Se algo não funcionar:
1. Pare o Flask (Ctrl+C)
2. Reinicie o IIS: `iisreset`
3. Execute novamente: `run_iis.bat`

## 📋 Checklist de Verificação:

- [ ] Flask rodando na porta 6001
- [ ] Regras do IIS configuradas
- [ ] CORS habilitado
- [ ] URLs absolutas no JavaScript
- [ ] Dependências instaladas (flask-cors)
- [ ] Firewall/antivírus não bloqueando a porta 6001